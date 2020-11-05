import os
import test_data_util as tdu
import re
from datetime import datetime
from matplotlib import pyplot as plt

baseip="main_data_output/"
baseop="test_data/"

# TODO: 9. Print the email Ids whose files do not have any “wave” information.
#   In the current exercise, there is only one such entry.


# TODO: 10. The users not having daiict email Id or without any “wave” information must be spammed.
#   Rename the corresponding files as spam1.txt, spam2.txt, … and update their contents by
#   adding a line at the beginning: “This email has been categorized as spam”.


# TODO: 11. Create ordered_names.txt containing the user names (non-spam type) in the descending
#   order of date-time etc., i.e. most recent first. One name in each line. Keep duplicate names.
def Task11():
    fileName="ordered_names.txt"
    global baseip
    listMail=tdu.find_file()
    dateName=tdu.extractDateName(listMail)
    sorted(dateName,key=lambda date: datetime.strptime(date,"%H:%M hrs on %B %d, %Y"))

    with open(os.path.join(baseop,fileName),"w") as fp:
        for i in dateName:
            fp.write(dateName[i]+"\n")

# TODO: 12. Create ordered_names_wave1.txt containing the user names (non-spam type) belonging to
#   the “first wave” group in the descending order of date-time etc., i.e. most recent first. No
#   duplicate names and one name in each line. Similarly create files for the “second wave”,
#   “third wave”, “fourth wave” groups.
def Task12():
    listMail=tdu.find_file()
    #List to store all the filename who is containing relative information
    listWave1=[]
    listWave2=[]
    listWave3=[]
    listWave4=[]

    for file in listMail:
        wave=tdu.findWave(file) 
        if(wave=='1'):
            listWave1.append(file)
        elif(wave=='2'):
            listWave2.append(file)
        elif(wave=='3'):
            listWave3.append(file)
        elif(wave=='4'):
            listWave4.append(file)
    
    with open(os.path.join(baseop,"ordererd_names_wave1.txt"),"w") as fp1:
        orderedWave1=tdu.extractDateName(listWave1)
        for name in orderedWave1.values():
            fp1.writelines(name+"\n")
    
    with open(os.path.join(baseop,"ordererd_names_wave2.txt"),"w") as fp1:
        orderedWave2=tdu.extractDateName(listWave2)
        for name in orderedWave2.values():
            fp1.writelines(name+"\n")

    with open(os.path.join(baseop,"ordererd_names_wave3.txt"),"w") as fp1:
        orderedWave3=tdu.extractDateName(listWave3)
        for name in orderedWave3.values():
            fp1.writelines(name+"\n")

    with open(os.path.join(baseop,"ordererd_names_wave4.txt"),"w") as fp1:
        orderedWave4=tdu.extractDateName(listWave4)
        for name in orderedWave4.values():
            fp1.writelines(name+"\n")

# TODO: 13. Plot the number of users in each group and number of spam emails using a bar chart.
def Task13():
    data=dict()
    
    fp1=open(os.path.join(baseop,"ordererd_names_wave1.txt"),"r")
    tmpList=fp1.readlines()
    data["Wave1"]=len(tmpList)

    fp1=open(os.path.join(baseop,"ordererd_names_wave2.txt"),"r")
    tmpList=fp1.readlines()
    data["Wave2"]=len(tmpList)

    fp1=open(os.path.join(baseop,"ordererd_names_wave3.txt"),"r")
    tmpList=fp1.readlines()
    data["Wave3"]=len(tmpList)

    fp1=open(os.path.join(baseop,"ordererd_names_wave4.txt"),"r")
    tmpList=fp1.readlines()
    data["Wave4"]=len(tmpList)

    #for spam file
    tmpList=os.listdir("main_data_output/")
    r=re.compile("spam.*")
    tmpList=list(filter(r.match,tmpList))
    data["Spam"]=len(tmpList)

    fig=plt.figure(figsize=(7,5)).canvas.set_window_title("Output")
    graph=plt.bar(data.keys(),data.values(),color="maroon",width=0.3)
    graph[4].set_color("blue")
    plt.xlabel("Wave category")
    plt.ylabel("Frequency")
    plt.title("Frequency of wave statements")
    plt.show()

if __name__ == "__main__":
    Task13()