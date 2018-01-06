import tensorflow as tf

# x1 = tf.constant([5,6], shape = [1,2])
# x2 = tf.constant([6,7], shape = [2,1])

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1,x2)

print(result)

sess = tf.Session()
print(sess.run(result))

# print(tf.multiply(x1,x2))

# a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
# b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
# c = tf.matmul(a,b)
# print(c)