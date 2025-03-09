count = 0
transcript = ""
with open('random.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line != "" and line[-1].isdigit() and line[-3] == ":":
            if len(line) == 4:
                minutes = int(line[-4:-3])
            elif len(line) >= 5:
                minutes = int(line[-5:-3])
            if minutes == count or count == 60:
                count += 1
                if count == 61:
                    count = 0
                if count % 2 == 1:
                    transcript += str(line) + "\n"
        else:
            if " um " in line:
                line = line.replace(" um ", " ")
            if " uh " in line:
                line = line.replace(" uh ", " ")
            transcript += line + "\n"
with open('random.txt', 'w') as file:
    file.write(transcript)
