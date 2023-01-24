# run under the conda environment

import tensorflow as tf
from tensorflow import keras

n_layer = 4
img_size = 128

detection_model = keras.models.load_model("dice-detection-model-dr03-0.729.h5")

xception_classifier = keras.models.load_model("xception-classifier-prepr-dr075-0.980.h5")

# inputs = keras.Input(shape=(img_size, img_size, 3))

# viz_model = keras.Model(inputs=detection_model.inputs, outputs=detection_model.layers[n_layer].output)

# converter = tf.lite.TFLiteConverter.from_keras_model(detection_model)
# tf_lite_model = converter.convert()


# with open('detection-model-dr03-0729.tflite', 'wb') as f_out:
#     f_out.write(tf_lite_model)


# converter = tf.lite.TFLiteConverter.from_keras_model(viz_model)
# tf_lite_model = converter.convert()

# with open('viz-model-dr03-0729.tflite', 'wb') as f_out:
#     f_out.write(tf_lite_model)

xception_converter = tf.lite.TFLiteConverter.from_keras_model(xception_classifier)
tf_lite_model = xception_converter.convert()

with open('xception-classifier-prepr-dr075-0.980.tflite', 'wb') as f_out:
    f_out.write(tf_lite_model)