"""
    Authors: Dhyanil Mehta, Prahar Pandya, Kishan Vaishnani
    Last Modified: 22-11-2020
"""

import os
import re

baseip = "main_data_output/"


# Find number of files in folder with that name email-*.txt and generate list of that
def findEmailFiles():
    listAll = os.listdir("main_data_output/")
    r = re.compile("email.*")
    listMail = list(filter(r.match, listAll))

    return listMail


# i/p: List of files o/p:Will get dictionary, key:Time Value: Username
def extractDateName(listMail):
    dateName = dict()
    for file in listMail:
        path = os.path.join(baseip, file)
        with open(path, "r") as Efile:
            line = Efile.readline()
            data = re.findall(r"[0-9].*", line)
            # x[0] = 16:42 hrs on February 20, 2020
            # x[1] = Kishan Vaishnani
            x = data[0].split(" from ")
            x[1] = x[1].replace("@daiict.ac.in", "")
            x[1] = " ".join(x[1].split("_")).title()
            dateName[x[0]] = x[1]
    return dateName


def findWave(fname):
    waveType = 0
    with open(os.path.join(baseip, fname), "r") as fp:
        data = fp.readlines()
        r = re.compile(".* wave")
        listData = list(filter(r.match, data))
        if len(listData) != 0:
            x = listData[0].split("wave")
            tmp = x[0].strip()
            tmplist = tmp.split(" ")

            if tmplist[-1] == "first":
                waveType = 1
            elif tmplist[-1] == "second":
                waveType = 2
            elif tmplist[-1] == "third":
                waveType = 3
            elif tmplist[-1] == "fourth":
                waveType = 4
    return waveType
