import tensorflow as tf
a = tf.constant([1,2,3])
print(type(a))
b = tf.random_normal([2,3],stddev=1)
print(type(b))

with tf.Session() as sess:
    print(sess.run(b))