import uuid
import json
import random

d = {}
filename = "data.json"

# them 1 song vao dict
def add(dic, path='',name='',author='',singer=''):
    dic[str(uuid.uuid4())] = {
    "path": path,
    "name": name,
    "author": author,
    "singer": singer,
    "views": 0,
    "dailymix": False,
    "shuffleorder": -1
}

# update json
# qua trinh: load json -> dict, edit dict, dump dict -> json
def write(dic):
    with open(filename,"w") as f:
        json.dump(dic,f,indent=4)

# luu json content vao 1 dict
def get():
    with open(filename,"r") as f:
        return json.load(f)

#tron bai
def shuff(dic,le):
    l = [int(i) for i in range(le)]
    random.shuffle(l)
    # print("l=",l)
    k = 0
    for i in dic:
        dic[i]["shuffleorder"]=l[k]
        k+=1

# tim kiem     
def find(dic,name):
    for i in dic:
        if name == dic[i]["name"]:
            print("found ",name,": ",i)
    
# daily mix
# voi so luong song nho co the ko dat toi num        
def dmix(dic,num=3):
    for i in range(num):
        dic[random.choice([k for k in dic])]["dailymix"] = True

# dump cho file
# dumps cho print
# load cho txt file
# loads cho str, byte, bytearr

# print(json.dumps(d,indent=4))
# json.dump(d,open(filename,"w"),indent=4)


# vi du mau dung cac ham:

# tao 5 song
for i in range(5):
    add (d,
        "abcd",
        "darude - sandstorm" + str(i),
        "darude",
        str(i)
    )

# ghi vao tempformat.json
write(d)

# e = noi dung lay tu tempformat.json
e = get()

# them 1 song nua
add(e)

# tron bai
shuff(e,len(e))

# tim ten 
# find(e,"darude - sandstorm2")

# daily mix, mac dinh 3
dmix(e)

# ghi e da thay doi vao tempformat.json
write(e)







# print(json.dumps(d,indent=4))

# json.dump(d,open(filename,"w"),indent=4)

# e = json.load(open(filename,"r"))
# print("e =\n",json.dumps(e,indent=4))
