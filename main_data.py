import random
import datetime


# Random date-time generator helper function
def dateTimeGenerator():
    datetime_list = []
    for i in range(20):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        datetime_list.append(datetime.datetime(2020, month, day, hours, minutes).strftime("%H:%M hrs on %B %d, %Y"))

    return datetime_list


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


# Generating email text files as specified in todos 5, 6, 7
def generateEmailFiles(student_name_list):
    # Generate email text file numbers and shuffle them for randomness
    emailNums = [i for i in range(1, 21)]
    random.shuffle(emailNums)
    print(emailNums)

    # Creating datetime list for randomising date-time in file
    datetime_list = dateTimeGenerator()

    # Task 5
    # Creating a new list by extending the original list by randomly chosen 5 names from the same list
    # and shuffling it for more randomness
    student_list_extended = student_name_list + random.choices(student_name_list, k=5)
    random.shuffle(student_list_extended)
    print(student_list_extended)
    # Looping and generating files
    for i in range(len(emailNums) - 5):
        emailTxt = open(f"email-{emailNums[i]}.txt", "w")
        # Create email id
        split_student_name = student_list_extended[i].split(" ")
        assert len(split_student_name) == 2
        email_id = f"{split_student_name[0].lower()}_{split_student_name[1].lower()}@daiict.ac.in"

        # Write to newly generated file
        emailTxt.write(f"Received at {datetime_list[i]} from {email_id}\n")  # 5.(a)
        emailTxt.write("\n")    # 5.(b)
        emailTxt.write("Wave information")
        # Some Tasks are still left
        emailTxt.close()


if __name__ == "__main__":
    generateHERAFiles()
    generateEmailFiles(createStudentNameList())


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
