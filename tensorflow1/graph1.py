import tensorflow as tf
b = tf.constant([1,2,3],name = 'a')
a = tf.constant([4,5,6],name= 'b')
product = a+b

session1 = tf.Session()
result1 = session1.run(product)
print(" add product : ",result1)


c = tf.constant([[3,3]])
d = tf.constant([[4],[4]])
product2 = tf.matmul(c,d)
result2 = session1.run(product2)

print(" multiple product : ",result2)

session1.close()

c = tf.constant([[3,3]])
d = tf.constant([[5],[5]])
product3 = tf.matmul(c,d)
with tf.Session() as session2:
    result = session2.run(product3)
    print(" with open  : ",result)

var1 = tf.Variable(0)


