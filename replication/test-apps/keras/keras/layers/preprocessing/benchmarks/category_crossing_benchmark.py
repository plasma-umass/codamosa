# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Benchmark for Keras categorical_encoding preprocessing layer."""

import tensorflow.compat.v2 as tf

import itertools
import time

import numpy as np

import keras
from keras.layers.preprocessing import category_crossing

tf.compat.v1.enable_v2_behavior()


# word_gen creates random sequences of ASCII letters (both lowercase and upper).
# The number of unique strings is ~2,700.
def int_gen():
  for _ in itertools.count(1):
    yield (np.random.randint(0, 5, (1,)), np.random.randint(0, 7, (1,)))


class BenchmarkLayer(tf.test.Benchmark):
  """Benchmark the layer forward pass."""

  def run_dataset_implementation(self, batch_size):
    num_repeats = 5
    starts = []
    ends = []
    for _ in range(num_repeats):
      ds = tf.data.Dataset.from_generator(
          int_gen, (tf.int64, tf.int64),
          (tf.TensorShape([1]), tf.TensorShape([1])))
      ds = ds.shuffle(batch_size * 100)
      ds = ds.batch(batch_size)
      num_batches = 5
      ds = ds.take(num_batches)
      ds = ds.prefetch(num_batches)
      starts.append(time.time())
      # Benchmarked code begins here.
      for i in ds:
        _ = tf.sparse.cross([i[0], i[1]])
      # Benchmarked code ends here.
      ends.append(time.time())

    avg_time = np.mean(np.array(ends) - np.array(starts)) / num_batches
    return avg_time

  def bm_layer_implementation(self, batch_size):
    input_1 = keras.Input(shape=(1,), dtype=tf.int64, name="word")
    input_2 = keras.Input(shape=(1,), dtype=tf.int64, name="int")
    layer = category_crossing.CategoryCrossing()
    _ = layer([input_1, input_2])

    num_repeats = 5
    starts = []
    ends = []
    for _ in range(num_repeats):
      ds = tf.data.Dataset.from_generator(
          int_gen, (tf.int64, tf.int64),
          (tf.TensorShape([1]), tf.TensorShape([1])))
      ds = ds.shuffle(batch_size * 100)
      ds = ds.batch(batch_size)
      num_batches = 5
      ds = ds.take(num_batches)
      ds = ds.prefetch(num_batches)
      starts.append(time.time())
      # Benchmarked code begins here.
      for i in ds:
        _ = layer([i[0], i[1]])
      # Benchmarked code ends here.
      ends.append(time.time())

    avg_time = np.mean(np.array(ends) - np.array(starts)) / num_batches
    name = "category_crossing|batch_%s" % batch_size
    baseline = self.run_dataset_implementation(batch_size)
    extras = {
        "dataset implementation baseline": baseline,
        "delta seconds": (baseline - avg_time),
        "delta percent": ((baseline - avg_time) / baseline) * 100
    }
    self.report_benchmark(
        iters=num_repeats, wall_time=avg_time, extras=extras, name=name)

  def benchmark_vocab_size_by_batch(self):
    for batch in [32, 64, 256]:
      self.bm_layer_implementation(batch_size=batch)


if __name__ == "__main__":
  tf.test.main()
