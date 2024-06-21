'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = tf.keras.datasets.fashion_mnist # The MNIST is the dataset of a bunch of clothes in 28 by 28 pixels. It is what the ai is training off

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() # The images are 28 by 28 Numpy arrays, with pixel values ranging from 0 to 255. The labels are an array of integers, ranging from 0 to 9. These correspond to the different kinds of clothing.

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=30) 

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

model.save('fashion_mnist_model.keras')
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import Tk
from PIL import Image

model = tf.keras.models.load_model('fashion_mnist_model.keras')

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # Convert image to grayscale
    img = img.resize((28, 28))  # Resize image to 28x28
    img_array = np.array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def predict_image(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)
    predicted_label = np.argmax(predictions[0])
    return class_names[predicted_label]

def open_file_dialog():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

def main():
    image_path = open_file_dialog()
    if image_path:
        predicted_class = predict_image(image_path)
        print(f"Predicted Class: {predicted_class}")
        
        # Display the image and predicted label
        img = Image.open(image_path)
        plt.imshow(img, cmap='gray')
        plt.title(f"Predicted: {predicted_class}")
        plt.show()

if __name__ == "__main__":
    main()