import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = tf.keras.datasets.fashion_mnist # The MNIST is the dataset of a bunch of clothes in 28 by 28 pixels. It is what the ai is training off

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() # The images are 28 by 28 Numpy arrays, with pixel values ranging from 0 to 255. The labels are an array of integers, ranging from 0 to 9. These correspond to the different kinds of clothing.

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

len(train_labels)

