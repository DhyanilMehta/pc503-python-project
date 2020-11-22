"""
    Authors: Dhyanil Mehta, Prahar Pandya, Kishan Vaishnani
    Last Modified: 22-11-2020
"""

import os
import test_data_util as tdu
import re
from datetime import datetime
from matplotlib import pyplot as plt

baseip = "main_data_output/"
baseop = "test_data/"


# TODO: 9. Print the email Ids whose files do not have any “wave” information.
#   In the current exercise, there is only one such entry.

def print_not_wave(listFiles):
    non_wave_emails = []
    for each_file in listFiles:
        with open(os.path.join(baseip, each_file), "r") as fp:
            data = fp.read()
            email_regex = re.compile(r'\S+@[0-9a-z._]+')
            wave_regex = re.compile(r'(first|second|third|fourth)\s(wave)')
            wave_search = wave_regex.search(data)
            if not wave_search:
                # print(wave_search.groups())
                # print("yes")
                find_email = email_regex.findall(data)
                non_wave_emails.append(find_email[0])

    print("Print the email Ids whose files do not have any “wave” information: ")
    print(*non_wave_emails)


# TODO: 10. The users not having daiict email Id or without any “wave” information must be spammed.
#   Rename the corresponding files as spam1.txt, spam2.txt, … and update their contents by
#   adding a line at the beginning: “This email has been categorized as spam”.

def check_spam(listFiles):
    count = 0
    for each_file in listFiles:
        is_spam = False
        with open(os.path.join(baseip, each_file), "r+") as fp:
            data = fp.read()
            find_email = re.search("@daiict.ac.in", data)
            find_wave = re.search(r".* wave", data)
            if not find_email or not find_wave:
                fp.seek(0)
                fp.write("This email has been categorized as spam\n")
                fp.write(data)
                print("Spam file detected: " + each_file)
                count += 1
                is_spam = True
        if is_spam:
            spam_file = "spam" + str(count) + ".txt"
            os.rename(os.path.join(baseip, each_file), os.path.join(baseip, spam_file))
    print("Total spam files: ", count)


# TODO: 11. Create ordered_names.txt containing the user names (non-spam type) in the descending
#   order of date-time etc., i.e. most recent first. One name in each line. Keep duplicate names.
def Task11(nonSpamFiles):
    fileName = "ordered_names.txt"
    dateName = tdu.extractDateName(nonSpamFiles)
    descDateTime = sorted(dateName, key=lambda date: datetime.strptime(date, "%H:%M hrs on %B %d, %Y"), reverse=True)

    with open(os.path.join(baseop, fileName), "w") as fp:
        for i in descDateTime:
            fp.write(dateName[i] + "\n")


# TODO: 12. Create ordered_names_wave1.txt containing the user names (non-spam type) belonging to
#   the “first wave” group in the descending order of date-time etc., i.e. most recent first. No
#   duplicate names and one name in each line. Similarly create files for the “second wave”,
#   “third wave”, “fourth wave” groups.
def Task12(nonSpamFiles):
    # List to store all the filename who is containing relative information
    listWaves = {1: [], 2: [], 3: [], 4: []}

    for file in nonSpamFiles:
        wave = tdu.findWave(file)
        listWaves[wave].append(file)

    for n in range(1, 5):
        with open(os.path.join(baseop, f"ordered_names_wave{n}.txt"), "w") as fp:
            orderedWave = tdu.extractDateName(listWaves[n])
            descDateTime = sorted(orderedWave, key=lambda date: datetime.strptime(date, "%H:%M hrs on %B %d, %Y"),
                                  reverse=True)

            uniqueSortedNames = []
            for i in descDateTime:
                if orderedWave[i] not in uniqueSortedNames:
                    uniqueSortedNames.append(orderedWave[i])

            for name in uniqueSortedNames:
                fp.write(name + "\n")


# TODO: 13. Plot the number of users in each group and number of spam emails using a bar chart.
def Task13():
    data = dict()
    for n in range(1, 5):
        fp = open(os.path.join(baseop, f"ordered_names_wave{n}.txt"), "r")
        data[f"Wave{n}"] = len(fp.readlines())
        fp.close()

    # for spam file
    spamRegex = re.compile("spam.*")
    tmpList = list(filter(spamRegex.match, os.listdir("main_data_output/")))
    data["Spam"] = len(tmpList)

    plt.figure(figsize=(7, 5)).canvas.set_window_title("Output")
    graph = plt.bar(data.keys(), data.values(), color="maroon", width=0.3)
    graph[4].set_color("blue")
    plt.xlabel("Wave category")
    plt.ylabel("Frequency")
    plt.title("Frequency of wave statements")
    plt.show()


if __name__ == "__main__":
    emailFiles = tdu.findEmailFiles()

    print_not_wave(emailFiles)
    check_spam(emailFiles)

    nonSpamFileList = tdu.findEmailFiles()  # Since spam files are now named differently

    Task11(nonSpamFileList)
    Task12(nonSpamFileList)
    Task13()
