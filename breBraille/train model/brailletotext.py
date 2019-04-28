# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:54:40 2019

@author: RAJVIR
"""
import pandas as pd
import numpy as np
import cv2
import urllib.request
import matplotlib.pyplot as plt
import string
import random

import keras
from keras.models import Sequential,load_model
from keras.layers import Dense,Dropout,Flatten
from keras.layers import MaxPooling2D,Conv2D
from keras.layers.advanced_activations import LeakyReLU



df = pd.read_csv('braille_data.csv')

alphabet = list(string.ascii_lowercase)
cur_pos = 0
target = {}
for letter in alphabet:
    target[letter] = [0] * 27
    target[letter][cur_pos] = 1
    cur_pos += 1
target[' '] = [0] * 27
target[' '][26] = 1
    
data = []
for i, row in df.iterrows():
    picture = []
    url = row['Labeled Data']
    label = row['Label']
    cur_target = target[label[11]]
    x = urllib.request.urlopen(url)
    resp = x.read()
    image = np.array(bytearray(resp), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (28,28))
    image = image.astype(np.float32)/255.0
    picture.append(image)
    picture.append(cur_target)
    data.append(picture)
    
    
#------------------------------------------------------------------------
#to change from 26 to 27
length = len(data)
for i in range(length):
    if(data[i][1][0] == 1):
        data[i][1] = [0] * 27
        data[i][1][0] = 1
    elif(data[i][1][1] ==1):
        data[i][1] =[0] * 27
        data[i][1][1] =1
    elif(data[i][1][2] ==1):
        data[i][1] =[0] * 27
        data[i][1][2] =1
    elif(data[i][1][3] ==1):
        data[i][1] =[0] * 27
        data[i][1][3] =1
    elif(data[i][1][4] ==1):
        data[i][1] =[0] * 27
        data[i][1][4] =1
    elif(data[i][1][5] ==1):
        data[i][1] =[0] * 27
        data[i][1][5] =1
    elif(data[i][1][6] ==1):
        data[i][1] =[0] * 27
        data[i][1][6] =1
    elif(data[i][1][7] ==1):
        data[i][1] =[0] * 27
        data[i][1][7] =1
    elif(data[i][1][8] ==1):
        data[i][1] =[0] * 27
        data[i][1][8] =1
    elif(data[i][1][9] ==1):
        data[i][1] =[0] * 27
        data[i][1][9] =1
    elif(data[i][1][10] ==1):
        data[i][1] =[0] * 27
        data[i][1][10] =1
    elif(data[i][1][11] ==1):
        data[i][1] =[0] * 27
        data[i][1][11] =1
    elif(data[i][1][12] ==1):
        data[i][1] =[0] * 27
        data[i][1][12] =1
    elif(data[i][1][13] ==1):
        data[i][1] =[0] * 27
        data[i][1][13] =1
    elif(data[i][1][14] ==1):
        data[i][1] =[0] * 27
        data[i][1][14] =1
    elif(data[i][1][15] ==1):
        data[i][1] =[0] * 27
        data[i][1][15] =1
    elif(data[i][1][16] ==1):
        data[i][1] =[0] * 27
        data[i][1][16] =1
    elif(data[i][1][17] ==1):
        data[i][1] =[0] * 27
        data[i][1][17] =1
    elif(data[i][1][18] ==1):
        data[i][1] =[0] * 27
        data[i][1][18] =1
    elif(data[i][1][19] ==1):
        data[i][1] =[0] * 27
        data[i][1][19] =1
    elif(data[i][1][20] ==1):
        data[i][1] =[0] * 27
        data[i][1][20] =1
    elif(data[i][1][21] ==1):
        data[i][1] =[0] * 27
        data[i][1][21] =1
    elif(data[i][1][22] ==1):
        data[i][1] =[0] * 27
        data[i][1][22] =1
    elif(data[i][1][23] ==1):
        data[i][1] =[0] * 27
        data[i][1][23] =1
    elif(data[i][1][24] ==1):
        data[i][1] =[0] * 27
        data[i][1][24] =1
    elif(data[i][1][25] ==1):
        data[i][1] =[0] * 27
        data[i][1][25] =1
    elif(data[i][1][26] ==1):
        data[i][1] =[0] * 27
        data[i][1][26] =1
 #------------------------------------------------------------------ 
 
 
random.shuffle(data)

data = np.asarray(data)
train_dataset = data[:1124]
test_dataset = data[1124:1264]
valid_dataset = data[1264:1404]

train_dataset_img = np.array(train_dataset[:,0])
train_dataset_label = np.array(train_dataset[:,1])
test_dataset_img = np.array(test_dataset[:,0])
test_dataset_label = np.array(test_dataset[:,1])
valid_dataset_img = np.array(valid_dataset[:,0])
valid_dataset_label = np.array(valid_dataset[:,1])


#------------------------------------------------------------
#to make dataset 4 dimension

a=np.expand_dims(train_dataset_img[0],axis=0)
b=np.expand_dims(train_dataset_img[1],axis=0)
tr_ds_img=np.append(a,b,axis=0)
for i in range(2,1124):
    x=np.expand_dims(train_dataset_img[i],axis=0)
    tr_ds_img=np.append(tr_ds_img,x,axis=0)
    
a1=np.expand_dims(test_dataset_img[0],axis=0)
b1=np.expand_dims(test_dataset_img[1],axis=0)
ts_ds_img=np.append(a1,b1,axis=0)
for i in range(2,140):
    x1=np.expand_dims(test_dataset_img[i],axis=0)
    ts_ds_img=np.append(ts_ds_img,x1,axis=0)

a2=np.expand_dims(valid_dataset_img[0],axis=0)
b2=np.expand_dims(valid_dataset_img[1],axis=0)
va_ds_img=np.append(a2,b2,axis=0)
for i in range(2,140):
    x=np.expand_dims(valid_dataset_img[i],axis=0)
    va_ds_img=np.append(va_ds_img,x,axis=0)

tr_ds_lb = np.expand_dims(train_dataset_label[0],axis=0)
for i in range(1,1124):
    x3 = np.expand_dims(train_dataset_label[i],axis=0)
    tr_ds_lb = np.append(tr_ds_lb,x3,axis=0)

ts_ds_lb = np.expand_dims(test_dataset_label[0],axis=0)
for i in range(1,140):
    x4 = np.expand_dims(test_dataset_label[i],axis=0)
    ts_ds_lb = np.append(ts_ds_lb,x4,axis=0)
    
va_ds_lb = np.expand_dims(valid_dataset_label[0],axis=0)
for i in range(1,140):
    x5 = np.expand_dims(valid_dataset_label[i],axis=0)
    va_ds_lb = np.append(va_ds_lb,x5,axis=0)


#--------------------------------------------------------------------------

batch_size = 40
num_classes = 27
epochs = 20

braille_model = Sequential()
braille_model.add(Conv2D(16, kernel_size=(5,5), activation='linear', input_shape=(28,28,3), padding='same', strides=1))
braille_model.add(LeakyReLU(alpha = 0.1))
braille_model.add(MaxPooling2D((2,2)))
braille_model.add(Conv2D(32, kernel_size=(5,5), activation ='linear', padding='same', strides=1))
braille_model.add(LeakyReLU(alpha = 0.1))
braille_model.add(MaxPooling2D(pool_size=(2,2)))
braille_model.add(Conv2D(64, kernel_size=(5,5), activation='linear', padding='same',strides=1))
braille_model.add(LeakyReLU(alpha=0.1))
braille_model.add(MaxPooling2D(pool_size=(2,2)))
braille_model.add(Conv2D(128, kernel_size=(5,5), activation='linear', padding='same',strides=1))
braille_model.add(LeakyReLU(alpha=0.1))
braille_model.add(MaxPooling2D(pool_size=(2,2)))
braille_model.add(Flatten())
braille_model.add(Dense(256,activation='linear'))
braille_model.add(LeakyReLU(alpha=0.1))
braille_model.add(Dense(num_classes,activation='softmax'))

braille_model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

braille_model.summary()

braille_train = braille_model.fit(tr_ds_img,tr_ds_lb,batch_size=batch_size,epochs=epochs, verbose=1, validation_data=(va_ds_img, va_ds_lb))

test_eval = braille_model.evaluate(ts_ds_img,ts_ds_lb,verbose=1)

braille_model.save('braille_train.h5')

#-------------------------------------------
braille_model_drop = Sequential()
braille_model_drop.add(Conv2D(32, kernel_size=(3,3), activation='linear', input_shape=(28,28,3), padding='same', strides=1))
braille_model_drop.add(LeakyReLU(alpha = 0.1))
braille_model_drop.add(MaxPooling2D((2,2)))
braille_model_drop.add(Dropout(0.25))
braille_model_drop.add(Conv2D(64, kernel_size=(3,3), activation ='linear', padding='same', strides=1))
braille_model_drop.add(LeakyReLU(alpha = 0.1))
braille_model_drop.add(MaxPooling2D(pool_size=(2,2)))
braille_model_drop.add(Dropout(0.25))
braille_model_drop.add(Conv2D(128, kernel_size=(3,3), activation='linear', padding='same',strides=1))
braille_model_drop.add(LeakyReLU(alpha=0.1))
braille_model_drop.add(MaxPooling2D(pool_size=(2,2)))
braille_model_drop.add(Dropout(0.4))
braille_model_drop.add(Flatten())
braille_model_drop.add(Dense(256,activation='linear'))
braille_model_drop.add(LeakyReLU(alpha=0.1))
braille_model_drop.add(Dropout(0.3))
braille_model_drop.add(Dense(num_classes,activation='softmax'))



braille_model_drop.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

braille_model_drop.summary()

braille_train_drop = braille_model_drop.fit(tr_ds_img,tr_ds_lb,batch_size=batch_size,epochs=epochs, verbose=1, validation_data=(va_ds_img, va_ds_lb))

test_eval_drop = braille_model_drop.evaluate(ts_ds_img,ts_ds_lb,verbose=1)

#---------------------------------------------------------------------


accuracy = braille_train.history['acc']
val_accuracy = braille_train.history['val_acc']
loss = braille_train.history['loss']
val_loss = braille_train.history['val_loss']
epochs = range(len(accuracy))
plt.plot(epochs,accuracy,'bo',label='training accuracy')
plt.plot(epochs,val_accuracy,'b',label='validation accuracy')
plt.title('training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs,loss,'bo',label='training loss')
plt.plot(epochs,val_loss,'b',label='validation loss')
plt.title('training and validation loss')
plt.legend()
plt.show()

"""def find_data_file(filename):
    if getattr(sys, "frozen", False):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.dirname("__file__")

    return os.path.join(datadir, filename)"""

def predict_braille(path):
    model = load_model('braille_train.h5')
    pred_img = cv2.imread(path,cv2.IMREAD_COLOR)
    pred_img = cv2.resize(pred_img, (28,28))
    pred_img = pred_img.astype(np.float32)/255.0
    pred_img = np.expand_dims(pred_img,axis=0)
    pred_lb = model.predict(pred_img)
    for j in range(len(pred_lb[0])):
        if pred_lb[0][j] > 0.6:
            pred_lb[0][j] = 1.0
        else:
            pred_lb[0][j] = 0.0
    for key,value in target.items():
        if np.array_equal(np.asarray(pred_lb[0]),np.asarray(value)):
            print(key)
            return key
        
    
    








