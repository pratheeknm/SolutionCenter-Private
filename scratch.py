import os
import sys

f=open("manifest.txt",'r',encoding = 'utf-8')
a = f.read().split("\n")
for x in a:
    if x.split(":")[0]=="Public":
        print(x.split(":")[1])
        if x.split(":")[1]=="YES":
            os.system("sh script.sh")