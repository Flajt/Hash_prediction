import sys

"""
__author__:Flajt
"""

class reader():
    def __init__(self, set_default_file=None):
        self.default=set_default_file

    def prepare(self,book,search_args=[None]):
        """Read the file/book and decode it so you can use it for the next steps"""
        if self.default!=None: #check if a default File exists so you don`t have to enter the same file in every function
            book=set_default_file
        self.book=book
        data=open(self.book,"rb")
        data=data.read().decode() #use the "rb" feature and the .decode function to prevent problems with ä,ü etc.
        return True, data

    def clean_up(self, data, search_args=[None]): #add more than one search_args and experiment with the order
        """Uses a list of search arguments to remove them from the file. You may test the order of removing words. Need an upgrade"""
        if None in search_args: #if you don`t provide args the function errors
            return TypeError("Need args!")
        else:
            print("[*]: Start cleaning phase one")
            a=open(data)
            x=0
            while x!=len(search_args)-1: #because a computer starts counting by 0
                self.new=open("new_"+str(self.book),"w+",encoding="utf-8")#use utf-8 for propper encoding and less text problemss
                split_1=data.split(search_args[x])
                for item in split_1:
                    self.new.write(item+"\n")
                self.new.close()#close it so you can reopen it in the next step
                x=x+1#set count up to move to the next argument
                if x==1:
                    self.new=open("new_"+str(self.book))#reopen the file
                    data=self.new.read()# and use it to find all unwanted words, if you do it in an other way you will get some problems
                else:
                    pass
        print("[*]: Done with clean up phase 1!\n[i]: You can now run Phase two!")

    def remove_spaces(self,File):
        if self.default!=None:
            File=self.default
        """Remove spaces in a File """
        print("[*]: Starting clean up phase two!")
        data=open(File,"rb",)
        data_read=data.read().decode()
        data.close()#close data so you can open it for writing purposes
        data=open(File,"w",encoding="utf-8")
        spliter=data_read.rsplit() #spilt it in single words without space
        #print(spliter)
        for i in spliter:
            data.write(i+"\n")#write it in the old file #recycling
        data.close()
        print("[*]: Done")
        return True

    def word_split(self, File,output_file=None):# maybe useless maybe not the scripts obove will do it aswell
        """Split the words in sigle words and write them in the same file or an choosen output file """
        print("[*]: Starting formatter...")
        if output_file!=None:
            File=output_file
        print("[*]: Prepareing formatter...")
        data=open(File,"r",encoding="utf-8")
        new_data=data.read()
        data.close()
        d=new_data.rsplit()
        data=open(File,"w",encoding="utf-8")
        print("[*]: Running formatter...")
        for i in d:
            data.write(i+"\n")
        print("[*]: Done!")

    def remove_doubble(self,File):#remove the same words in a file
        """ This script will remove the same words in a file\n Stack link in source code"""
        print("[*]: Starting remover...")
        data=open(File,"r",encoding="utf-8")
        new_data=data.read().split()#read it and split it in one command (looks more professionell ^^)
        #print(new_data)
        data.close()
        print("[*]: Running remover...")
        print("[i]: This could take some time.")
        out=" ".join(sorted(set(new_data), key=new_data.index)) #visit: https://stackoverflow.com/questions/7794208/how-can-i-remove-duplicate-words-in-a-string-with-python for infomation
        #print(out)
        out=out.split() #split it to create a list
        #print(out)
        data=open(File,"w",encoding="utf-8")#reopen older file
        for output in out:
            data.write(output+"\n")# write everything inside
        data.close()
        print("[*]: Done!")
