def characterDivider(text):
    characterSet = ''.join(dict.fromkeys(text))
    # print(characterSet)
    characterDict = []

    for x in characterSet:
        tmpdict = {}
        if x == '\n':
            tmpdict['character'] = '\\n'
            tmpdict['probability'] = text.count(x)/len(text)
            tmpdict['frequence'] = text.count(x) 

        else :
            tmpdict['character'] = x
            tmpdict['probability'] = text.count(x)/len(text)
            tmpdict['frequence'] = text.count(x) 
        characterDict.append(tmpdict)
    # print(characterDict)
    return characterDict

def compressMethod(characterDictionary, text):
    lower = 0
    upper = 1

    for i in text:
        r = upper - lower
        tmp_lower = lower
        for x in characterDictionary:
            tmp_upper = tmp_lower + r * x['probability']
            # print("tabel pada huruf", i, "dengan per-huruf", x['character'], "batas bawah", lower, "batas atas", upper)
            if x['character'] == i:
                upper = tmp_upper
                lower = tmp_lower
                # print("huruf", i, "batas bawah", lower, "batas atas", upper)
                break
            tmp_lower = tmp_upper
        upper = tmp_upper
        lower = tmp_lower
    
    return (upper+lower)/2


def extractMethod(code, length, characterDictionary):
    lower = 0
    upper = 1

    charList = []

    Counter = 0
    for i in range(length):
        Counter+=1
        r = upper - lower
        tmp_lower = lower
        for x in characterDictionary:
            tmp_upper = tmp_lower + r * x['probability']
            if tmp_lower < code and tmp_upper > code:
                charList.append(x['character'])
                break
            tmp_lower = tmp_upper
        upper = tmp_upper
        lower = tmp_lower
    
    hasil = ""

    hasil = hasil.join(charList)

    return hasil

def readFileText(fileText):
    openFile = open(fileText, "r+")
    lines = openFile.readlines()
    raw_text = ''
    for line in lines:
        raw_text+=line
    texts = raw_text.splitlines()
    text = ''
    counter = 0
    for x in texts:
        if(counter == len(texts)-1):
            text+=x
        else:
            text+=x + '\\n'
        counter+=1
    openFile.close()
    return text

def readFileCode(fileCode):
    file = open(fileCode, 'r')
    tmpFile = file.read().split(",")
    code = {}
    code['length'] = int(tmpFile[0])
    code['decode'] = float(tmpFile[1])
    file.close()
    return code

def readFileModel(fileModel, code):
    file = open(fileModel, 'r')
    line = file.readlines()

    characterDictionary = []

    for x in line:
        characterSet = {}
        x = x.split(',')
        x[1] = x[1][:-1]
        characterSet['character'] = x[0]
        characterSet['frequence'] = x[1]
        characterSet['probability'] = float(int(x[1])/code['length'])
        characterDictionary.append(characterSet)
    file.close()
    return characterDictionary

def writeCode(fileText, result, length):
    filename = fileText[:-4]
    file = open(f"{filename}.cod", 'w')
    file.write(str(length) + ',' +str(result))
    file.close()
    print("done model")

def writeModel(fileText, characterDictionary):
    filename = fileText[:-4]
    file = open(f"{filename}.mod", 'w')
    line = ""
    for x in characterDictionary:
        line = line + f"{x['character']},{x['frequence']}\n"
    file.writelines(line)
    print("done code")

def writeText(fileModel, hasil):
    filename = fileModel[:-4]
    file = open(f"{filename}.txt", 'w')
    hasil = hasil.replace('\\n', '\n')
    file.writelines(hasil)
    file.close()
    print("done text")


def compress(fileText):
    text = readFileText(fileText)
    characterDict = characterDivider(text)
    result = compressMethod(characterDict, text)
    writeCode(fileText, result, len(text))
    writeModel(fileText, characterDict)

def extract(fileModel, fileCode):
    code = readFileCode(fileCode)
    characterDict = readFileModel(fileModel, code)
    
    hasil = extractMethod(code['decode'], code['length'], characterDict)

    writeText(fileModel, hasil)


extract("test.mod", "test.cod")
# compress('test.txt')
# print(readFile("test.cod"))





