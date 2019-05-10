import numpy as np

import tensorflow as tf
batch_size = 8
x_data = np.random.random_sample((100,2))
y_data = [int((x1 + x2)>1) for (x1,x2) in x_data]

#定义网络结构
w1 = tf.Variable(tf.random_normal([2,3],stddev=2,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev = 2,seed = 1))

x = tf.placeholder(tf.float32,shape=(None,2),name='features')
y = tf.placeholder(tf.float32,shape=(None,1),name = 'output')

h1 = tf.matmul(x,w1)
o1 = tf.matmul(h1,w2)

#定义loss function and backpropagation
o1 = tf.sigmoid(o1)
cross_entropy = -tf.reduce_mean(y*tf.log(tf.clip_by_value(o1,1e-10,1.0))
                               + (1-y)*tf.log(tf.clip_by_value(1-o1,1e-10,1.0))
                               )
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

with tf.Session() as sess:
    init1 = tf.global_variables_initializer()
    sess.run(init1)
    print("initial w1 : ", sess.run(w1))
    print("initial w2 : ", sess.run(w2))
    Steps = 10000
    for i in range(Steps):
        start = (batch_size * i) % len(x_data)
        end = min(start + batch_size, len(x_data))

        sess.run(train_step, feed_dict={x: x_data[start:end], y: y_data[start:end]})

        if i % 500 == 0:
            error = sess.run(cross_entropy, feed_dict={x: x_data, y: y_data})

            print(" After %d iteration ,cross entropy on all data is %g" % (i, error))
    print("trained w1 : ", sess.run(w1))
    print("trained w2 : ", sess.run(w2))