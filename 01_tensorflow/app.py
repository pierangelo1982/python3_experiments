import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# Importa il set di dati Fashion MNIST
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images,
                               test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# (60000, 28, 28) = (numero immagini, 28x28px di dimensione)
print(train_images.shape)

# 60000 numero di labels/etichette
print(len(train_labels))

# array([9, 0, 0, ..., 3, 0, 5], dtype=uint8)
# Ogni etichetta è un numero intero compreso tra 0 e 9:
print(train_labels)

# (10000, 28, 28) =  (numero immagini test, 28x28px di dimensione)
print(test_images.shape)

# numero labels test
print(len(test_labels))

# =================================================================
# Preelabora i dati
# =================================================================
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
plt.savefig(os.path.join('./pre.png'))


'''
I dati devono essere preelaborati prima dell'addestramento della rete. 
Se esamini la prima immagine nel set di addestramento, 
vedrai che i valori dei pixel rientrano nell'intervallo da 0 a 255:

Ridimensiona questi valori in un intervallo da 0 a 1 prima di inviarli al modello di rete neurale. 
Per fare ciò, dividere i valori da 255. 
E 'importante che il training set e il set di testing essere pre-elaborati nello stesso modo:
'''
train_images = train_images/255.0
test_images = test_images/255.0

'''
Per verificare che i dati sono nel formato corretto e che si è pronti a costruire e formare la rete, 
consentono di visualizzare le prime 25 immagini dal set di formazione 
e di visualizzare il nome della classe sotto ogni immagine.
'''
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

plt.show()
plt.savefig(os.path.join('./test.png'))

'''
Build the model
Building the neural network requires configuring the layers of the model, then compiling the model.
'''

# Set up the layers
# The basic building block of a neural network is the layer.
# Layers extract representations from the data fed into them.
# Hopefully, these representations are meaningful for the problem at hand.
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Compile the model
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Train the model

# Feed the model
model.fit(train_images, train_labels, epochs=10)

# Evaluate accuracy
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

""" 
Make predictions
With the model trained, you can use it to make predictions about some images. 
The model's linear outputs, logits. 
Attach a softmax layer to convert the logits to probabilities, which are easier to interpret.
 """
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)
print(predictions[0])
'''
A prediction is an array of 10 numbers. 
They represent the model's "confidence" that the image corresponds 
to each of the 10 different articles of clothing. 
You can see which label has the highest confidence value:
'''
np.argmax(predictions[0])
'''
So, the model is most confident that this image is an ankle boot, or class_names[9]. 
Examining the test label shows that this classification is correct:
'''
print(np.argmax(predictions[0]))
print(test_labels[0])

# Graph this to look at the full set of 10 class predictions.


def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100*np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


# Verify predictions
i = 0
plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1, 2, 2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()
plt.savefig(os.path.join('./test1.png'))

i = 12
plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1, 2, 2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()
plt.savefig(os.path.join('./test2.png'))

# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()
plt.savefig(os.path.join('./test3.png'))

################################################################
# Use the trained model
# Grab an image from the test dataset.
img = test_images[80]
print(img.shape)
# Add the image to a batch where it's the only member.
img = (np.expand_dims(img, 0))
print(img.shape)
# prrdict
predictions_single = probability_model.predict(img)
print(predictions_single)
###################
plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
plt.savefig(os.path.join('./predict.png'))
np.argmax(predictions_single[0])
print(np.argmax(predictions_single[0]))


#### mia immagine

