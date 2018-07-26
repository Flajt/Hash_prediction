# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
class train():
    def __init__(self):
        """An easy function to use for the pandas.get_dummies method"""
        pass

    def _train_from_file(self, train_data, item_count=1000):
        data=open(train_data,"r")
        data=data.read().split("\n")
        data_converted=pd.Series(data)
        done=pd.get_dummies(data_converted[:item_count])
        return done

    def _train_to_list(self, train_data,data_length=1000, advanced=False):
        if advanced==False:
            errors=[]
            data_list=[]
            count=0
            data=open(train_data,"r")
            data=data.read().split("\n")
            for i in data:
                if count>=data_length:
                    break
                try:
                    d=pd.Series(list(i))
                    da=pd.get_dummies(d)
                    data_list.append(da)
                    count+=1
                except Exception as e:
                    error.append(e)
                    count+=1
                    pass
            return data_list,errors

        elif advanced==True:
            data_list=[]
            errors=[]
            data=train_data
            count=0

            for i in data:
                if count>=data_length:
                    break
                try:
                    d=pd.Series(list(i))
                    da=pd.get_dummies(d)
                    data_list.append(da)
                    count+=1
                except Exception as e:
                    error.append(e)
                    count+=1
                    pass
            return data_list,errors


    def _word_generaliser(self, training_data, advanced=False, filler="0"):
        """Takes a training file as input and return a list were everything got the same length (default: filled up with zeros)"""
        if advanced==False:
            data=open(training_data,"r")
            data=data.read().split("\n")
            words_length_list=[]
            words_list=[]
            words_generalised=[]
            x=0
            for i in data:
                words_length_list.append(len(i))
                words_list.append(i)
            max_value=max(words_length_list)
            for i in words_length_list:
                for _ in words_list:
                    if x>=len(words_list):
                        break
                    else:
                        if i<max_value:
                            #print("so it should be")
                            stuff_to_append=max_value-i
                            words_generalised.append(_+stuff_to_append*filler)
                            x+=1
                        elif i==max_value:
                            x+=1
                            words_generalised.append(_)
                            pass
                        elif i>max_value:
                            print("Index word is bigger than biggest word in the list, something went wrong ^^")
                            x+=1
                            pass

            return words_generalised

        elif advanced==True:
            data=training_data
            words_length_list=[]
            words_list=[]
            words_generalised=[]
            x=0
            for i in data:
                words_length_list.append(len(i))
                words_list.append(i)
            max_value=max(words_length_list)
            for i in words_length_list:
                for _ in words_list:
                    if x>=len(words_list):
                        break
                    else:
                        if i<max_value:
                            #print("so it should be")
                            stuff_to_append=max_value-i
                            words_generalised.append(_+stuff_to_append*filler)
                            x+=1
                        elif i==max_value:
                            x+=1
                            words_generalised.append(_)
                            pass
                        elif i>max_value:
                            print("Index word is bigger than biggest word in the list, something went wrong ^^")
                            x+=1
                            pass
            return words_generalised

    def _train_from_list(self, liste, item_count=10000,use_last_items=False):
        if use_last_items!=False:
            series=pd.Series(liste[:item_count])
            dummies=pd.get_dummies(series)
            return dummies
        else:
            series=pd.Series(liste[-item_count:])
            dummies=pd.get_dummies(series)
            return dummies
"""
    def _test(self,train_data, optionl_split_arg="\n", numpy_datatype=object,reshape_size=20000,ndimension=2,length=20000):
        data=open(train_data,"r")
        data=data.read().split(optionl_split_arg)
        store_data=[]
        counter=0
        for i in data:
            if counter>=length:
                break
            store_data.append(i)
            counter+=1
        array=np.array(store_data,dtype=object,ndmin=ndimension)
        array=array.reshape(20000)
        array=[float(i) for i in array]
        return array
"""
#Problem is that i cant convert a string to a float character
