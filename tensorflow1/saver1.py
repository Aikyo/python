import tensorflow as tf

a = tf.Variable(tf.random_normal([1,3]))
b = tf.Variable(tf.random_normal([1,3]))
result = a + b
init = tf.global_variables_initializer()

saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    sess.run(result)
    saver.save(sess,'D:/a_train/herman.ckpt')
