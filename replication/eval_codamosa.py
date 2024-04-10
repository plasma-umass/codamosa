# Measures CodaMosa coverage using SlipCover

import csv
from pathlib import Path
from collections import defaultdict
import subprocess
from datetime import datetime
import sys

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--codamosa-results', choices=['gpt4', 'codex'], default='gpt4',
                    help='codamosa results to use')
    ap.add_argument('--isolate-tests', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='run tests in isolation (to work around any state pollution) when measuring coverage')

    return ap.parse_args()

args = parse_args()

codamosa_tests = Path("gpt4-coda") if args.codamosa_results == 'gpt4' else \
                 Path("codamosa-dataset/final-exp/codamosa-0.8-uninterp")
output = Path(f"output-{args.codamosa_results}" + ("-isolated" if args.isolate_tests else ""))

modules_csv = Path("test-apps") / "good_modules.csv"


output.mkdir(exist_ok=True)

slipcover_args = '--isolate-tests' if args.isolate_tests else ''

with modules_csv.open() as f:
    reader = csv.reader(f)
    for p, module in reader:
        for coda_run in codamosa_tests.glob(f"{module}-*"):
            json = output / f"{coda_run.name}.json"

            if json.exists():
                continue

            pkg = module.split('.')[0]

            pytest_args = ''

            # Some of these 'failing' tests damage the system so much that it is not
            # possible to get a coverage measurement.  Disabling them turned out to be
            # unnecessary because some of the generations (samples) for flutils don't
            # have this issue.
#            if output.name == 'output-codex' and module == 'flutils.pathutils':
#                pytest_args += f'--ignore=/tests/test_{"_".join(module.split("."))}_failing.py'

            print(f"---- {datetime.now().isoformat()} {str(coda_run)} ----")

            cmd =  "docker run --rm " +\
                   "-v ./run_coda_tests.sh:/run_coda_tests.sh:ro " +\
                  f"-v {str(coda_run.absolute())}:/tests:ro " +\
                  f"-v {str(output.absolute())}:/output " +\
                  f"-v ./{p}:/package:ro " +\
                  f"-v {str((Path('.') / 'pip-cache').absolute())}:/root/.cache/pip " +\
                   "-t slipcover-runner " +\
                  f"bash /run_coda_tests.sh {pkg} {json.name} \"{slipcover_args}\" \"{pytest_args}\""
            print(cmd)
            subprocess.run(cmd, shell=True, check=False)
#            sys.exit(0)
