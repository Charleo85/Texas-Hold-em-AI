import os
import tensorflow as tf
from Game import queen_data

# # Parameters
# learning_rate = 0.01
# training_epochs = 25
# batch_size = 100
# display_step = 1
#
# # tf Graph Input
# x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
# y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes
#
# # Set model weights
# W = tf.Variable(tf.zeros([784, 10]))
# b = tf.Variable(tf.zeros([10]))
#
# # Construct model
# pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax
#
# # Minimize error using cross entropy
# cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# # Gradient Descent
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
#
# # Initializing the variables
# init = tf.initialize_all_variables()
#
# # Launch the graph
# with tf.Session() as sess:
#     sess.run(init)
#
#     # Training cycle
#     for epoch in range(training_epochs):
#         avg_cost = 0.
#         total_batch = int(mnist.train.num_examples/batch_size)
#         # Loop over all batches
#         for i in range(total_batch):
#             batch_xs, batch_ys = mnist.train.next_batch(batch_size)
#             # Fit training using batch data
#             _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs,
#                                                           y: batch_ys})
#             # Compute average loss
#             avg_cost += c / total_batch
#         # Display logs per epoch step
#         if (epoch+1) % display_step == 0:
#             print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))
#
#     print("Optimization Finished!")
#
#     # Test model
#     correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
#     # Calculate accuracy for 3000 examples
#     accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#     print("Accuracy:", accuracy.eval({x: mnist.test.images[:3000], y: mnist.test.labels[:3000]}))

mean_value = 0
mean_index = 0
iteration = 1
for i in range(iteration):
    datasets = queen_data(10)
    x = tf.constant(datasets)
    x_max_index = tf.argmax(x, 0)
    x_max_value = tf.reduce_max(x, reduction_indices=[0])

    with tf.Session() as sess:
        # print(sess.run(x_max_index))
        # print(sess.run(x_max_value))
        mean_index+=sess.run(x_max_index)
        mean_value+=sess.run(x_max_value)

print(mean_index/iteration)
print(mean_value/iteration)
