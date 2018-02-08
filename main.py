# -*- coding: utf-8 -*-

import Reader
import hashlib


reader=Reader.reader()
ret, data=reader.prepare("openthesaurus.txt")
print("\n"+"\n")
#print(data)
reader.clean_up(data,["#","+","[",".","(",";",")","-","à","é"])
reader.remove_spaces("new_openthesaurus.txt")
reader.remove_doubble("new_openthesaurus.txt")


"""Hash werte stimmen nicht?!"""

def main():
    print("[i]: Setting up hashing function..")
    hash_file=open("hashes.txt","w",encoding="utf-8")
    data=open("new_openthesaurus.txt","r")
    lines=data.readlines()
    print("[*]: Start hashing with hashlib...")
    for _ in lines:
        Hash=hashlib.sha256(str.encode(_)).hexdigest()
        hash_file.write(Hash+"\n")
    print("[*]: Done")
main()
