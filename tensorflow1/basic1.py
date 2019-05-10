import tensorflow as tf
import numpy as np
a = np.array([0,0,0,1,0,0,0])
b = tf.argmax(a,1)
sess = tf.Session()
print(sess.run(b))
