import numpy as np

class encoder():
    def __init__(self,special_characters_dic=None):
        """
        Possible setup:
        c=encoder(special_characters_dic={",":56,".":57})# only usefull for words with special_characters, if you don`t need it leave it empty
        words=c.split_words()#important
        out=c.on_hot_all(words)#encode all words with special_characters and upper and lower_case characters
        for i in out:
            print(i)
            print("")
        """
        self.word_dic={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
        self.upper_word_dic={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
        self.general_upper_word_list={"A":26,"B":27,"C":28,"D":29,"E":30,"F":31,"G":32,"H":33,"I":34,"J":35,"K":36,"L":37,"M":38,"N":39,"O":40,"P":41,"Q":42,"R":43,"S":44,"T":45,"U":46,"V":47,"W":48,"X":49,"Y":50,"Z":51}
        self.general_lower_word_list={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
        self.special_letters_dic={"ä":52,"ü":53,"ö":54,"ß":55}
        self.special_characters_dic=special_characters_dic
        self.general_numbers_dic={"1":56,"2":57,"3":58,"4":59,"5":60,"6":61,"7":62,"8":63,"9":64,"0":65}
        #self.lower_word_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","x","y","z"]# maybe useless
        #self.upper_word_list=map(str.upper,self.lower_word_list)# uses the map function to use a function on a list
        #self.sepecial_letters=["ä","ü","ö","ß"]
        #self.special_characters=["#",",","+","*","~","-","_",";",".",":","@","<","!","?",">","|","`"]
        self.coder=None

    def coder(self):
        """Return type of the encoder"""
        return self.coder

    def split_words(self,data=["auto","nice","Auto","Tim","Tomatensalat","gehen","auto,bahn"]):
        """Use a list of words as input and returns a list of a list containing the splitted words"""
        content=[]
        self.data=data
        for i in data:
            liste=list(i)
            content.append(liste)
        return content

    def return_values(self):
        return self.lower_word_list,self.upper_word_list,self.sepecial_letters,self.special_characters

    def create_new_array(self,shape=(26,26)):
        return np.zeros(shape)

    def on_hot_lower(self,splitted_words, description="basic on_hot method for lower_case characters"):
        """One hot encoder for lower_case characters, needs splitted_words as input list and returns a list of numpy matrices as output. Size(26,26)"""
        self.coder="on_hot_lower"
        array=self.create_new_array()
        array_storage=[]
        for i in splitted_words:#iterate through every list
            for letter in i:#iterate thorugh every letter in i
                #print(letter)
                position=self.word_dic[letter]
                #print(position)
                index=i.index(letter)
                    #print(i)
                array[index,position]=1
            array_storage.append(array)
            array=self.create_new_array()
        return array_storage

    def on_hot_upper(self,splitted_words):
        """One hot encoder for upper_case characters, needs splitted_words as input list and returns a list of numpy matrices as output. Size(26,26)"""
        self.coder="on_hot_upper"
        array=self.create_new_array()
        array_storage=[]
        for i in splitted_words:#iterate through every list
            for letter in i:#iterate thorugh every letter in i
                #print(letter)
                position=self.upper_word_dic[letter]
                #print(position)
                index=i.index(letter)
                    #print(i)
                array[index,position]=1
            array_storage.append(array)
            array=self.create_new_array()
        return array_storage

    def on_hot(self,splitted_words):
        """One hot encoder for lower_case and upper_case characters, needs splitted_words as input list and returns a list of numpy matrices as output. Size(26,52)"""
        self.coder="on_hot_without_special_characters"
        array=self.create_new_array(shape=(26,52))
        array_storage=[]
        for i in splitted_words:#iterate through every list
            for letter in i:#iterate thorugh every letter in i
                if str.isupper(letter)==True:
                    position=self.general_upper_word_list[letter]
                    index=i.index(letter)
                else:
                    position=self.general_lower_word_list[letter]
                    index=i.index(letter)

                array[index,position]=1
            array_storage.append(array)
            array=self.create_new_array(shape=(26,52))
        return array_storage

    def on_hot_all(self, splitted_words):
        """Generates a list of arrays of the size (26,56+length of sepecial_characters_dic)"""
        if self.special_characters_dic==True or None or False:
            raise ValueError("Please input a list of special characters to use this function. These list should start by: 66")
        else:
            pass
        self.coder="on_hot_encoder_with special_characters_maybe_memeory_intensiv_so_be_aware"
        array=self.create_new_array(shape=(26,56+len(self.special_characters_dic)))
        array_storage=[]
        for i in splitted_words:#iterate through every list
            for letter in i:#iterate thorugh every letter in i
                if str.isupper(letter)==True:
                    position=self.general_upper_word_list[letter]
                    index=i.index(letter)
                elif str.islower(letter)==True:
                    position=self.general_lower_word_list[letter]
                    index=i.index(letter)
                elif letter in self.special_characters_dic:
                    position=self.special_characters_dic[letter]
                    index=i.index(letter)
                elif letter in self.sepecial_letters_dic:
                    position=self.special_characters_dic[letter]
                    index=i.index(letter)
                elif letter in self.general_numbers_dic:
                    position=self.general_numbers_dic[letter]
                    index=i.index(letter)

                array[index,position]=1
            array_storage.append(array)
            array=self.create_new_array(shape=(26,56+len(self.special_characters_dic)))
        return array_storage
