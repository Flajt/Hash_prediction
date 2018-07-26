# -*- coding: utf-8 -*-
import word_encoder
import numpy as np
import tflearn as tfl
import trainer
import pandas as pd
import hashlib
import time
np.set_printoptions(threshold=np.nan)

class Hash_Prediction():
    def __init__(self):
        self.learning_rate=1e-4
        self.d=word_encoder.encoder({"Ã":70,"¼":71,"¶":72,"¤":73,"Ÿ":74,"„":75,"œ":76,"–":77,"?":78,"â":79,"‚":80,"¬":81,"€":82})

    def network(self,load=False):
        if not load:
            net=tfl.layers.core.input_data(shape=[None,1,83])
            net=tfl.layers.conv_1d(net,20,[8,8],activation="relu")
            net=tfl.layers.max_pool_1d(net,[2,2])
            net=tfl.layers.conv_1d(net,25,[4,4],activation="relu")
            net=tfl.layers.max_pool_1d(net,[2,2])
            net=tfl.layers.dropout(net,0.6)
            net=tfl.layers.flatten(net)
            #net=tfl.layers.conv_1d(net,20,[8,8])
            #net=tfl.layers.conv_1d(net,25,[4,4])
            #net=tfl.layers.flatten(net)
            #net=tfl.layers.core.fully_connected(net,150,activation="relu")
            net=tfl.layers.core.fully_connected(net,300,activation='relu')#hash 2 with 50,50,100
            net=tfl.layers.dropout(net,0.8)
            net=tfl.layers.core.fully_connected(net,200,activation="relu")
            net=tfl.layers.core.fully_connected(net,150,activation="relu")
            net=tfl.layers.core.fully_connected(net,83,activation="linear")
            net=tfl.layers.estimator.regression(net,learning_rate=self.learning_rate,loss="mean_square",optimizer="sgd")
            self.model=tfl.DNN(net,checkpoint_path="C:\\Users\\Flajt\\Documents\\GitHub\\Hash_prediction\\Models\\model_2.ckpt")
        else:
            net=tfl.layers.core.input_data(shape=[None,1,83])
            net=tfl.layers.conv_1d(net,20,[8,8],activation="relu")
            net=tfl.layers.max_pool_1d(net,[2,2])
            net=tfl.layers.conv_1d(net,25,[4,4],activation="relu")
            net=tfl.layers.max_pool_1d(net,[2,2])
            net=tfl.layers.flatten(net)
            #net=tfl.layers.core.fully_connected(net,150,activation="relu")
            net=tfl.layers.core.fully_connected(net,300,activation='relu')
            net=tfl.layers.core.fully_connected(net,200,activation="relu")
            net=tfl.layers.core.fully_connected(net,150,activation="relu")
            net=tfl.layers.core.fully_connected(net,83,activation="linear")
            net=tfl.layers.estimator.regression(net,learning_rate=self.learning_rate,loss="mean_square",optimizer="sgd")
            self.model=tfl.DNN(net,checkpoint_path="C:\\Users\\Flajt\\Documents\\GitHub\\Hash_prediction\\Models\\model_1.ckpt")
            self.model.load("C:\\Users\\Flajt\\Documents\\GitHub\\Hash_prediction\\Models\\hash_2.tfl",weights_only=True)#need function wich can output -1

    def train(self,x,y):
        count=0
        counter=1
        self.network(False)
        for a,b in zip(x,y):
            count+=1
            data=len(x)
            a=a.reshape((1,)+a.shape)
            b=b.reshape(1,83)
            print("Fitting Batch:{0} from {1}".format(counter, data))
            self.model.fit_batch(a,b)
            counter=counter+1
            if count==5:
                count=0
                self.model.save("C:\\Users\\Flajt\\Documents\\GitHub\Hash_prediction\\Models\\hash_2.tfl")
            else:
                pass
        print("Done")
        self.model.save("C:\\Users\\Flajt\\Documents\\GitHub\\Hash_prediction\\Models\\hash_2.tfl")

    def predict(self,x):
        self.network(True)
        x=self.d.split_words(data=[x])
        x=word_vectors=self.d.short_vector(x,83)# for each array take the first input and add it inside a new one
        x[0][0]=x[0][0].T
        print(type(x[0][0]))
        print(self.model.predict(x[0]))

    class LSTM():
        def __init__(self,learning_rate=1e-5,checkpoint_path="None",model_path=str()):
            self.model_path=model_path
            self.checkpoint_path=checkpoint_path
            self.learning_rate=learning_rate

        def model(self,load=False):
            lstm=tfl.layers.input_data([None,1,83])
            lstm=tfl.layers.lstm(lstm,n_units=10,return_seq=False)
            lstm=tfl.layers.lstm(lstm,n_units=50,return_seq=True)
            lstm=tfl.layers.lstm(lstm,n_units=100,return_seq=True)
            lstm=tfl.layers.lstm(lstm,n_units=50)
            lstm=tfl.layers.lstm(lstm,n_units=83)
            #lstm=tfl.layers.fully_connected(lstm,n_units=83)
            lstm=tfl.layers.estimator.regression(lstm,loss="mean_square",optimizer="adam",learning_rate=self.learning_rate)
            model=tfl.models.DNN(lstm,checkpoint_path=self.checkpoint_path)
            if load:
                model.load(self.model_path,weights_only=True)
                return model
            else:
                return model

        def train(self,x,y):
            model=self.model()
            batch=0
            max_b=len(x)
            for a,b in zip(x,y):
                print("Fitting batch {0} from {1}".format(batch,max_b))
                model.fit_batch(a.reshape((1,)+a.shape),b)
                batch+=1
            #model.fit(x,y,show_metric=True)
            model.save(self.model_path)

        def predict(self,x):
            model=self.model(load=True)
            return model.predict(x)

        def evaluate(self,testing_data=[]):
            """
            Evaluate the LSTM model.
            Parameters:
                test_data: A list were you input two lists( test_x and test_y )
                            each stores the testing arrays.
            """
            model=self.model(load=True)
            return model.evaluate(testing_data[0],testing_data[1])
