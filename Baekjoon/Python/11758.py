import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 'a' is semi-major axis : constant
# 'b' is semi-minor axis : constant
# 'x' is time value : variable
def ellipsePosition(a, b, t, interval):
    angle = t * np.pi / interval
    x = a * np.cos(angle)
    y = b * np.sin(angle)

    return x, y

max_range = 50

majorAxis = 3
minorAxis = 2

x_train = []
y_train = []

x_test = []
y_test = []

for i in range(0, max_range):
    x, y = ellipsePosition(majorAxis, minorAxis, i, max_range)
    x_train.append(x)
    y_train.append(y)
    x_t, y_t = ellipsePosition(majorAxis, minorAxis, i + max_range, max_range)
    x_test.append(x_t)
    y_test.append(y_t)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

x_train = np.array(x_train[:, np.newaxis])
y_train = np.array(y_train[:, np.newaxis])
x_test = np.array(x_test[:, np.newaxis])
y_test = np.array(y_test[:, np.newaxis])

plt.scatter(x_train, y_train, c='blue')
plt.scatter(x_test, y_test, c='red')
plt.show()


table = np.hstack([x_train, y_train])

trainData = pd.DataFrame(table)
trainData.columns = ['x', 'y']

print(trainData)
print("====")
print(x_test)

# print(trainData[trainData.columns[0]])
# print(trainData[trainData.columns[1:3]])

steps = 50
epochs = 10

batch_size = len(x_test)

trainBatchData = tf.data.Dataset.from_tensor_slices([x_train, y_train])
trainBatchData = trainBatchData.batch(batch_size)

trainXData = tf.data.Dataset.from_tensor_slices(x_train)
trainXData = trainXData.batch(batch_size)

trainYData = tf.data.Dataset.from_tensor_slices(y_train)
trainYData = trainYData.batch(batch_size)

testXBatchData = tf.data.Dataset.from_tensor_slices(x_test)
testXBatchData = testXBatchData.batch(batch_size)

print(trainBatchData)
# print(len(list(trainBatchData)))
print(trainBatchData.element_spec.shape)

model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(32, input_shape=(50, 1)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mae')

model.fit(trainXData, trainYData, epochs=epochs, steps_per_epoch=steps)

