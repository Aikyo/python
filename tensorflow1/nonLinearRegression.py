import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt



x_data = np.linspace(-1,1,200)
noise = np.random.normal(0,0.3,x_data.shape)
y_data = np.square(x_data) + noise

# plt.scatter(x_data,y_data)
# plt.show()





x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])

# define 1-20-1 feedforward neural network

w1 = tf.Variale(tf.random_normal([1, 30], mean=0, stddev=0.4))
biase1 = tf.Variable(tf.zeros([30]))
w2 = tf.Variable(tf.random_normal([30, 1], mean=0, stddev=0.4))
biase2 = tf.Variable(tf.zeros(1))

h1 = tf.nn.tanh(tf.matmul(x, w1) + biase1)
h2 = tf.nn.tanh(tf.matmul(h1, w2) + biase2)

# define loss function
loss = tf.losses.mean_squred_error(y, h2)

train = tf.train.GradientDescent(0.3).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2001):
        sess.run(train, feed_dict={x: x_data, y: y_data})
        if i % 50 == 0:
            result = sess.run(loss, feed_dict={x: x_data, y: y_data})
            print("After %d iteration loss is %s" % (i, result))



