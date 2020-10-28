# import random


# Creating 4 files from About-DAIICT.txt
def generateHERAFiles():
    with open("About-DAIICT.txt", "r") as aboutDaiict:
        data = aboutDaiict.readlines()

        # Create files
        history = open("History.txt", "w")
        environment = open("Environment.txt", "w")
        recognition = open("Recognition.txt", "w")
        accreditation = open("Accreditation.txt", "w")

        # Update appropriate text to files by iterating over data
        hisIdx, envIdx = data.index("History\n"), data.index("Environment\n")
        recogIdx, accredIdx = data.index("Recognition\n"), data.index("Accreditation\n")
        for i in range(len(data)):
            if hisIdx + 1 < i < envIdx:
                history.write(data[i])
            if envIdx + 1 < i < recogIdx:
                environment.write(data[i])
            if recogIdx + 1 < i < accredIdx:
                recognition.write(data[i])
            if i > accredIdx + 1:
                accreditation.write(data[i])

        history.close()
        environment.close()
        recognition.close()
        accreditation.close()
        # print('data.index("History\\n"): ', data.index("History\n"))
        # print('data.index("Environment\\n"): ', data.index("Environment\n"))
        # print('data.index("Recognition\\n"): ', data.index("Recognition\n"))
        # print('data.index("Accreditation\\n"): ', data.index("Accreditation\n"))

# Create and return list of names of students
def createStudentNameList():
    with open("student_name_list.txt", "r") as stuNameFile:
        student_name_list = [name.rstrip() for name in stuNameFile.readlines()]
    return student_name_list

# TODO: 5. Randomly generate 15 files with file names: email-1.txt to email-20.txt.
#   So, the name of the 13th file need not be email-13.txt, it can also be email-19.txt or email-5.txt.
#   Content of each file (10 lines) should be as follows:
#   a) First line should have time, date, month, year, email Id in the following format:
#       Received at 17:23 hrs on October 7, 2018 from fname_lname@daiict.ac.in
#       All entries must be randomly inserted and email Ids can be created from random elements of
#       student_name_list. Obviously, there will be at least one or more files containing the same
#       email Id since the number of students is 10 (<15).
#   b) Second line should be blank.
#   c) Third line to the tenth line must be the lines from the four above mentioned text files
#       in random order such that (i) there is at least one line from each file and (ii) the lines
#       taken from History.txt can include only one of the four sentences containing “first wave”, “second wave”,
#       “third wave”, “fourth wave”. There is no restriction on other sentences in this text file.


# TODO: 6. Randomly generate 4 more files using the above mentioned logic with two modifications:
#       a) File name should be the unused numbers between 1 to 20.
#       b) Email Ids must be taken from the following list: email_ids =[ name1@gmail.com,
#       A_X_y@yahoo.co.in, nm123@rediff.com, nam_4_e@160.com].


# TODO: 7. Randomly generate 1 more file using the above mentioned logic with three modifications:
#       a) File name should be the unused number between 1 to 20.
#       b) Email Id is pc_503@daiict.ac.in
#       c) The lines taken from History.txt cannot include any one of the four sentences
#   containing “first wave”, “second wave”, “third wave”, “fourth wave”. There is no
#   restriction on other sentences in this text file.

if __name__ == "__main__":
    generateHERAFiles()
    print(createStudentNameList())
