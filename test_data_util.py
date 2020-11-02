import os
import re

baseip="main_data_output/"
#Find number of files in folder with that name email-*.txt and generate list of that
def find_file():
    listAll=os.listdir("main_data_output/")
    r=re.compile("email.*")
    listMail=list(filter(r.match,listAll))

    return listMail

#i/p: List of files o/p:Will get dictonary, key:Time Value: Username
def extractDateName(listMail):
    dateName=dict()
    for file in listMail:
        path=os.path.join(baseip,file)
        with open(path,"r") as Efile:
            str=Efile.readline()
            data=re.findall("[0-9].*",str)
               
            for i in range(len(data)):
                x=data[i].split(" from ")
                x[1]=x[1].rstrip("@daiict.ac.in")
                dateName[x[0]]=x[1]
    return dateName

def findWave(fname):
    with open(os.path.join(baseip,fname),"r") as fp:
        data=fp.readlines()
        r=re.compile(".* wave")
        listMail=list(filter(r.match,data))
        x=listMail[0].split("wave")
        tmp=x[0].strip()
        tmplist=tmp.split(" ")
        if(tmplist[-1] == "first")
            waveType="1"
        #Last word extraction is remaining
    # return waveType

findWave("email-10.txt")