import tensorflow as tf


class ResidualBlock(tf.keras.Model):

    def __init__(self):
        super(ResidualBlock, self).__init__()

    def call(self, inputs, training=True):
        x = tf.pad(inputs, [[0, 0], [1, 1], [1, 1], [0, 0]], "REFLECT")

        conv = tf.keras.layers.Conv2D(128, kernel_size=3, strides=1,
                                      kernel_initializer=tf.random_normal_initializer(stddev=0.02))
        x = conv(x)

        batch_norm = tf.keras.layers.BatchNormalization()
        x = batch_norm(x, training=training)

        x = tf.nn.relu(x)

        x = tf.pad(x, [[0, 0], [1, 1], [1, 1], [0, 0]], "REFLECT")

        conv = tf.keras.layers.Conv2D(128, kernel_size=3, strides=1,
                                      kernel_initializer=tf.random_normal_initializer(stddev=0.02))
        x = conv(x)

        batch_norm = tf.keras.layers.BatchNormalization()
        x = batch_norm(x, training=training)

        x = tf.add(x, inputs)

        return x