import tensorflow as tf

a = tf.random_normal([1],mean=2,stddev=0.1)
a1 = tf.random_normal([1],mean=1)
b = tf.nn.tanh(a)
c = tf.nn.sigmoid(a)
d = tf.nn.relu(a)
e = tf.nn.softmax(a)
with tf.Session() as sess:
    result = sess.run([a,b,c,d,e])
    result1 = sess.run(e)
    print(" softmax ",result1)
    print(result)
