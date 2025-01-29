from sys import argv

readFile = open(argv[1], "r")
writeFile = open(argv[2], "w")
opcodeFile = open("opcodes.txt", "r")
lineNumber = 0

opcodeDict = {}
tagDict = {}

# get opcodes and machine code
for line in opcodeFile:
    line = line.strip("\n").upper().split(" ")
    opcodeDict.update({line[0]: line[1]})

writeFile.write("v3.0 hex words plain\n\n") # specify type for logisim

# main assembling function, reads word by word
def assembleLine(line):
    translatedLine = []

    for word in line:
        if word in opcodeDict:  # check if opcode
            translatedLine.append(opcodeDict[word])

        elif word in tagDict:   # check if tag
            word = format(tagDict[word], "04x")     # translate tag linenumber to hex
            translatedLine.append(word)

        elif word[0] == "$":    # check if marked as hex
            word = word.strip("$")
            translatedLine.append(word)
        
        elif word[0] == "#":    # check if marked as dec
            word = word.strip("#")
            word = format(int(word), "04x")         # translate dec number to hex
            translatedLine.append(word)

    if len(translatedLine) == 1:        # fill out control word for operations without an operand
        translatedLine.append("0000")

    assembled = translatedLine[0] + translatedLine[1]
    writeFile.write(assembled + "\n")   # write assembled line to output file

codeLines = []

# main loop, reads line by line
for line in readFile:
    line = line.strip("\n").upper().split(" ")      # remove newlines and split lines into lists
    if line == [""]:            # skip empty lines
        continue

    if line[0] == "":           # if line is indented
        line = [x for x in line if x.strip()]       # remove empty strings from line list
        codeLines.append(line)
        lineNumber += 1
        continue

    elif line[0] == "/":        # skip comments
        continue

    else:
        tagDict.update({line[0].strip(":"): lineNumber})
        continue                # mark tag and line number, then skip

for line in codeLines:
    assembleLine(line)

print(f"done! lines assembled: {lineNumber}")