import tensorflow as tf
c1 = tf.constant([1,2,3])
c2 = tf.constant([3,4,5])
r1 = c1 + c2
r2 = tf.multiply(c1,c2)
with tf.Session() as sess:
    result1,r2 = sess.run([r1,r2])
    result11 = sess.run(r1)
    print("second result :",result11)
    print(result1,r2)

x1 = tf.placeholder(tf.float32,[2,3])
x2 = tf.placeholder(tf.float32,[3,2])
r3 = tf.matmul(x1,x2)
with tf.Session() as sess:
    #r3 = sess.run(r3,{x1:[[1,2,3],[1,2,3]],x2:[[1,2],[1,2],[1,2,]]})#dictionary by sequence
    r3 = sess.run(r1)

    print(r3)

