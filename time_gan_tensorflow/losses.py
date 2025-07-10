import tensorflow as tf

@tf.function
def mean_squared_error(y_true, y_pred):
    """Mean squared error loss function."""
    # Instantiate the loss function
    mse = tf.keras.losses.MeanSquaredError()
    # Call the loss function with y_true and y_pred
    loss = mse(y_true, y_pred)
    return loss


@tf.function
def binary_crossentropy(y_true, y_pred):
    """Binary crossentropy loss function."""
    bce = tf.keras.losses.BinaryCrossentropy()
    loss = bce(y_true, y_pred)
    return loss

