import os
import shutil
import numpy as np
import random
import itertools

labels = os.listdir('./labels')
images = os.listdir('./dataset')

train_labels = []
test_labels = []

randomized = labels[:]
random.shuffle(labels)

quarter = len(labels)//4

train_labels = labels[quarter:]
test_labels = labels[:quarter]

train_images = []

for x in train_labels:
    image = x.replace('.txt', '.JPG')
    train_images.append(image)

test_images = []

for x in test_labels:
    image = x.replace('.txt', '.JPG')
    test_images.append(image)

for (x, y) in zip(train_images, train_labels):
    shutil.move('./dataset/' + x, './data/train/images/')
    shutil.move('./labels/' + y, './data/train/labels/' )
for (x, y) in zip(test_images, test_labels):
    shutil.move('./dataset/' + x, './data/test/images/')
    shutil.move('./labels/' + y, './data/test/labels/' )