"""
    Authors: Dhyanil Mehta, Prahar Pandya, Kishan Vaishnani
    Last Modified: 22-11-2020
"""

import random
import main_data_util as mdu


# Creating 4 files from About-DAIICT.txt
def generateHERAFiles():
    with open("About-DAIICT.txt", "r") as aboutDaiict:
        data = aboutDaiict.readlines()

        # Create files
        history = open("main_data_output/History.txt", "w")
        environment = open("main_data_output/Environment.txt", "w")
        recognition = open("main_data_output/Recognition.txt", "w")
        accreditation = open("main_data_output/Accreditation.txt", "w")

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
    datetime_list = mdu.dateTimeGenerator()

    # Task 5
    # Creating a new list by extending the original list by randomly chosen 5 names from the same list
    # and shuffling it for more randomness
    student_list_extended = student_name_list + random.sample(student_name_list, 5)
    random.shuffle(student_list_extended)
    print(student_list_extended)

    # Looping and generating files
    for i in range(len(emailNums) - 5):
        emailTxt = open(f"main_data_output/email-{emailNums[i]}.txt", "w")
        # Create email id
        split_student_name = student_list_extended[i].split(" ")
        assert len(split_student_name) == 2
        email_id = f"{split_student_name[0].lower()}_{split_student_name[1].lower()}@daiict.ac.in"

        # Write to newly generated file
        emailTxt.write(f"Received at {datetime_list[i]} from {email_id}\n")  # 5.(a)
        emailTxt.write("\n")  # 5.(b)
        for line in mdu.random8LinesGenerator():  # 5.(c)
            emailTxt.write(line)

        emailTxt.close()

    # Task 6
    # Generating spam email id text files with the same content as above generated files
    spam_emails = ["name1@gmail.com", "A_X_y@yahoo.co.in", "nm123@rediff.com", "nam_4_e@160.com"]
    random.shuffle(spam_emails)

    # Generating files with the unused 4 numbers
    offset = 15  # Offset for indexing unused numbers in emailNums list
    for i in range(len(spam_emails)):
        emailTxt = open(f"main_data_output/email-{emailNums[i + offset]}.txt", "w")

        # Write to newly generated file
        emailTxt.write(f"Received at {datetime_list[i+offset]} from {spam_emails[i]}\n")
        emailTxt.write("\n")
        for line in mdu.random8LinesGenerator():
            emailTxt.write(line)

        emailTxt.close()

    # Task 7
    # Generating one last email text file using the last unused number and a given email id
    # and it will not have any wave lines
    last_email_num, last_date_time = emailNums[-1], datetime_list[-1]
    last_email_id = "pc_503@daiict.ac.in"

    emailTxt = open(f"main_data_output/email-{last_email_num}.txt", "w")
    emailTxt.write(f"Received at {last_date_time} from {last_email_id}\n")
    emailTxt.write("\n")
    for line in mdu.random8LinesGenerator(has_wave=False):  # Setting has_wave to False to not include any wave line
        emailTxt.write(line)

    emailTxt.close()


if __name__ == "__main__":
    generateHERAFiles()
    generateEmailFiles(createStudentNameList())
