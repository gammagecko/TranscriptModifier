count = 0
transcript = ""
with open('SampleTranscript.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line != "" and line[-1].isdigit() and line[-3] == ":":
            if len(line) == 4 or len(line) == 5:
                minutes = int(line[-4:-6:-1])

            if minutes == count:
                count += 1
                transcript += str(line) + "\n"
                if count == 61:
                    count = 0
        else:
            transcript += line + "\n"
print(transcript)
