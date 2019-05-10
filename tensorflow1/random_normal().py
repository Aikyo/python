import tensorflow as tf

a = tf.random_normal(mean=5,shape=[3,2],stddev=1)
with tf.Session() as sess:
    result = sess.run(a)
    print(result)