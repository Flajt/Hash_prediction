import test as ann
import word_encoder
import hashlib
import numpy as np
#a=ann.Hash_Prediction()
a=ann.Hash_Prediction.LSTM(checkpoint_path="C:\\Users\\Flajt\\Documents\\GitHub\Hash_prediction\\Models\\hash_2stm.ckpt",
                            model_path="C:\\Users\\Flajt\\Documents\\GitHub\Hash_prediction\\Models\\hash_2stm1.tfl")
d=word_encoder.encoder({"Ã":70,"¼":71,"¶":72,"¤":73,"Ÿ":74,"„":75,"œ":76,"–":77,"?":78,"â":79,"‚":80,"¬":81,"€":82})
hashs=open("hashes.txt","r",encoding="utf-8").read().split("\n")
words=open("new_openthesaurus.txt","r",encoding="utf-8").read().split("\n")
data_1=d.split_words(hashs)
data_2=d.split_words(words)
word_vectors,n=d.short_vector(data_2,83)[:23189]
hash_vectors,n=d.short_vector(data_1,83)[:23189]
word_test=word_vectors[23189:26088]
hash_test=hash_vectors[23189:26088]
#word_vectors=[w.reshape(1,83,83) for w in word_vectors]
#hash_vectors=[h.reshape(1,83,83) for h in hash_vectors]
word_vectors=[w.T for w in word_vectors]
hash_vectors=[h.T for h in hash_vectors]
#del word_vectors[-1]
#del hash_vectors[-1]
#print(hash_vectors[-1])
a.train(hash_vectors,word_vectors)
#x=hashlib.sha256(str.encode("Autobahn")).hexdigest()
#x=d.split_words([x])
#x,n=d.short_vector(x,83)
#x=[x.reshape(1,83) for x in x]
#print(a.predict(x))
#print(x)
