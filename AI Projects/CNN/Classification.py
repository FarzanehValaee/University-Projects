import os
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
import numpy as np
import random

DATADIR = "E:/Dataset"
CATEGORIES = ["Butterfly", "Cat", "Dog", "Elephant", "Gallina", "Horse", "Mucca", "Pecora", "Ragno", "Scoiattolo"]

training_data = []

IMG_SIZE = 50
train_percent = 80
evaluate_percent = 10


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)  # path to animals dir => E:/Dataset/Butterfly
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                new_array = new_array / 255.0
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()

random.shuffle(training_data)
random.shuffle(training_data)

length = len(training_data)
p1 = int((train_percent * length) / 100)
p2 = (evaluate_percent * length) / 100
p2 = int(p1) + int(p2)
length = int(length) - 1

train = []
evaluate = []
test = []
for i in range(p1):
    train.append(training_data[i])
for i in range(p1, p2):
    evaluate.append(training_data[i])
for i in range(p2, length):
    test.append(training_data[i])

X_train = []
y_train = []
X_evaluate = []
y_evaluate = []
X_test = []
y_test = []

for features, label in train:
    X_train.append(features)
    y_train.append(label)

for features, label in evaluate:
    X_evaluate.append(features)
    y_evaluate.append(label)

X_train = np.array(X_train).reshape((-1, IMG_SIZE, IMG_SIZE, 3))
y_train = np.array(y_train)

X_evaluate = np.array(X_evaluate).reshape((-1, IMG_SIZE, IMG_SIZE, 3))
y_evaluate = np.array(y_evaluate)

model = Sequential()

model.add(Conv2D(256, (4, 4), input_shape=X_train.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (4, 4)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())
model.add(Dense(128))
model.add(Activation("relu"))

model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True

model.fit(X_train, y_train, epochs=30)

val_loss, val_acc = model.evaluate(X_evaluate, y_evaluate)
print(val_acc)
print(val_loss)

model.save('final_image_classification.model')

for features, label in test:
    X_test.append(features)
    y_test.append(label)

X_test = np.array(X_test).reshape((-1, IMG_SIZE, IMG_SIZE, 3))

new_model = tf.keras.models.load_model('final_image_classification.model')

prediction = new_model.predict(X_test)

print(len(prediction))

correct = 0
for i in range(len(y_test)):
    if y_test[i] == np.argmax(prediction[i]):
        correct = correct + 1

i = 0
for predict in prediction:
    if np.argmax(predict) == 0:
        print("prediction["+str(i)+"] : "+"Butterfly")
    elif np.argmax(predict) == 1:
        print("prediction["+str(i)+"] : "+"Cat")
    elif np.argmax(predict) == 2:
        print("prediction["+str(i)+"] : "+"Dog")
    elif np.argmax(predict) == 3:
        print("prediction["+str(i)+"] : "+"Elephant")
    elif np.argmax(predict) == 4:
        print("prediction["+str(i)+"] : "+"Gallina")
    elif np.argmax(predict) == 5:
        print("prediction["+str(i)+"] : "+"Horse")
    elif np.argmax(predict) == 6:
        print("prediction["+str(i)+"] : "+"Mucca")
    elif np.argmax(predict) == 7:
        print("prediction["+str(i)+"] : "+"Pecora")
    elif np.argmax(predict) == 8:
        print("prediction["+str(i)+"] : "+"Ragno")
    elif np.argmax(predict) == 9:
        print("prediction["+str(i)+"] : "+"Scoiattolo")
    i = i + 1


print(correct)