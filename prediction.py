# -*- coding: utf-8 -*-

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Dropout
from termcolor import colored
import numpy as np
from array import array
import trainer
from keras import *
import pandas as pd
import hashlib
import os
from keras import backend as k
from keras.preprocessing import text
import word_encoder
#data=text.one_hot(open("new_openthesaurus.txt","r").read(),100)
#data_2=text.one_hot(open("hashes.txt","r").read(),100)

main_path="C:/Users/Flajt/Documents/GitHub/Hash_prediction"
os.chdir(main_path)
w=word_encoder.encoder({"#","@"})
w2=word_encoder.encoder()
#t=trainer.train()

words=open("new_openthesaurus.txt",encoding="utf-8").read().split("\n")
hashes=open("hashes.txt",encoding="utf-8").read().split("\n")
word_vectors=w.on_hot_all(words)
hash_vectors=w2.on_hot_all(hashes)

#train_words=t._word_generaliser(words, advanced=True)
#train_hashs=t._word_generaliser(hashes, advanced=True)

#train_words=t._train_to_list(train_words, advanced=True)
#train_hashs=t._train_to_list(train_hashs, advanced=True)

#print(len(train_hashs))
#print(len(train_words))
#test_words,error_l1=t._train_to_list("new_openthesaurus.txt",20000)
#test_hashs,error_l2=t._train_to_list("hashes.txt",20000)
#print(test_words)
#print(test_hashs)
#print(type(test_words))
#print(train_words)
#print(train_hashs)

#a=np.array(train_words,ndmin=2)
#b=np.array(train_hashs, ndmin=2)
#print(a)
#print(b)

#b=b.reshape(20000)
#a=a.reshape(20000)

#print(a)
#print("a: "+str(a))
#print("b: "+str(b))
#print(a.shape)
#print(b.shape)
#print(error_l1)
#print(error_l2)
#print(test_words)
#print(test_hashs)

"""
#try:
model=load_model(filepath="first_test")
train_y=input("Input a word that is not contained in the training data: ")
train_x=pd.Series(hashlib.sha256(str.encode(train_y)).hexdigest())
train_y=pd.Series(train_x)
test_y=pd.get_dummies(train_y)
#test_y=pd.get_dummies(train_y)
#model.load("first_test")
score=model.evaluate(test_y, batch_size=128)

prediction=model.predict(test_y)
for i in prediction:
    print(i)
    a=1+1

"""

#except Exception as e:
#    print(colored("Error: "+str(e)+"\n","red"))
print(colored("Prepearing Sequential modell with Keras","green"))
model = Sequential()
model.add(Dense(64, input_shape=(1,), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
#model.add(Dense(units=64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='rmsprop', metrics=['accuracy'])
print("Fitting data...")
for i in word_vectors:
    for _ in hash_vectors:
        model.fit(_,i ,epochs=5,batch_size=128, verbose=0)
train_y=input("Input a hash that is not contained in the training data: ")
train_y=pd.Series(hashlib.sha256(str.encode(train_y)).hexdigest())
train_y=pd.Series(list(train_y))
train_y=pd.get_dummies(train_y)

#train_y=pd.Series(train_y)
#test_x=text.one_hot(train_x,100)
#test_y=pd.get_dummies(train_y)
#test_y=text.one_hot(train_y,100)
model.save("first_test")
#print(model.evaluate(train_y))
#sore=model.evaluate(test_x, test_y, batch_size=128,)
#print("Score: "+score)
prediction=model.predict(test_y,verbose=1)
for i in prediction:
   print(i)
#print(score)
