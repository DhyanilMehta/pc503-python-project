import os
import test_data_util as tdu
import re
from datetime import datetime

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
    fileName="ordered_names_wave1.txt"
    listMail=tdu.find_file()
    #List to store all the filename who is containing relative information
    listWave1=[]
    listWave2=[]
    listWave3=[]
    listWave4=[]

    for file in listMail:
        



    dateName=tdu.extractDateName(listWave1)

# TODO: 13. Plot the number of users in each group and number of spam emails using a bar chart.

Task11()