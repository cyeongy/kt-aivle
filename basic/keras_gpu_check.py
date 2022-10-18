from tensorflow.python.client import device_lib
from tensorflow import keras
import tensorflow as tf
import keras

print(tf.config.list_physical_devices('CPU'))
print(tf.config.list_physical_devices('GPU'))
# print(device_lib.list_local_devices())
