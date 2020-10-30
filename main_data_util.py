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


# Extract lines from Accreditation.txt file
def __extractAccreditationLines():
    accreditation = open("main_data_output/Accreditation.txt", "r")
    acc_lines = []
    for line in accreditation.readlines():
        if line == "\n":
            continue
        acc_lines.append(line.strip())
    accreditation.close()
    return acc_lines


# Extract lines from Recognition.txt file
def __extractRecognitionLines():
    recognition = open("main_data_output/Recognition.txt", "r")
    recog_lines = []
    for line in recognition.readlines():
        if line == "\n":
            continue
        recog_lines.append(line.strip())
    recognition.close()
    return recog_lines


# Extract lines from Environment.txt file
def __extractEnvironmentLines():
    environment = open("main_data_output/Environment.txt", "r")
    env_lines = []
    for line in environment.readlines():
        if line == "\n":
            continue
        env_lines.append(line.strip())
    environment.close()
    return env_lines


# Extract and return list of wave lines from the History.txt file
def __extractWaveNonWaveLines():
    history = open("main_data_output/History.txt", "r")
    data = history.readlines()
    extracted_waves = []
    for i in range(len(data)):
        if data[i].startswith('Dhirubhai') or data[i].startswith('\n'):
            continue
        extracted_waves.append(data[i].strip())

    waves = []
    i = 0
    while i < len(extracted_waves) - 1:
        if extracted_waves[i].startswith("The second wave"):
            waves.append(extracted_waves[i])
            i += 1
            continue
        waves.append(extracted_waves[i])
        i += 2

    not_waves = [data[0].strip()]  # Initializing with the first line of History.txt
    for line in extracted_waves:
        if line not in waves:
            not_waves.append(line)

    split_fourth_wave = waves[len(waves) - 1].split(". ")  # Since there are two sentences in one line
    waves.pop()
    waves.append(split_fourth_wave[0] + ".")
    not_waves.append(split_fourth_wave[1])
    history.close()
    return waves, not_waves


# Extract lines from Accreditation, Environment, Recognition text files
# Make a large list of lines from all files except wave lines and another list of wave lines
# and return a random choice of 8 lines - 1 from wave lines and 7 from the other lines
def random8LinesGenerator(has_wave=True):
    wave_lines, non_wave_lines = __extractWaveNonWaveLines()
    env_lines = __extractEnvironmentLines()
    acc_lines = __extractAccreditationLines()
    recog_lines = __extractRecognitionLines()

    eight_lines = []
    # Selecting random 8 lines from the corresponding file lists
    # and ensuring there is at least one line from each file list
    if has_wave:
        combined_lines = acc_lines + env_lines + recog_lines

        eight_lines.append(random.choice(wave_lines))

        eight_lines.append(random.choice(env_lines))
        eight_lines.append(random.choice(acc_lines))
        eight_lines.append(random.choice(recog_lines))

        eight_lines.extend(random.sample(combined_lines, 4))
    else:
        combined_lines = non_wave_lines + acc_lines + env_lines + recog_lines

        eight_lines.append(random.choice(non_wave_lines))
        eight_lines.append(random.choice(env_lines))
        eight_lines.append(random.choice(acc_lines))
        eight_lines.append(random.choice(recog_lines))

        eight_lines.extend(random.sample(combined_lines, 4))

    random.shuffle(eight_lines)
    # Some post-processing
    for i in range(len(eight_lines) - 1):
        eight_lines[i] = eight_lines[i] + "\n"

    assert len(eight_lines) == 8

    # for line in eight_lines:
    #     print(line)
    return eight_lines
