import argparse

def characterDivider(text):
    characterSet = ''.join(dict.fromkeys(text))
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
    return characterDict

def compressMethod(characterDictionary, text):
    lower = 0
    upper = 1

    for i in text:
        r = upper - lower
        tmp_lower = lower
        for x in characterDictionary:
            tmp_upper = tmp_lower + r * x['probability']
            if x['character'] == i:
                upper = tmp_upper
                lower = tmp_lower
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
    code['decode'] = tmpFile[1]
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
    file.close()
    print("done code")

def writeText(fileModel, hasil):
    filename = fileModel[:-4]
    file = open(f"{filename}.txt", 'w')
    hasil = hasil.replace('\\n', '\n')
    file.writelines(hasil)
    file.close()
    print("done text")


def compress(fileText, bit=16):
    text = readFileText(fileText)
    characterDict = characterDivider(text)
    result = compressMethod(characterDict, text)
    resultBin = floatToBin(result, bit)
    # writeCode(fileText, result, len(text))
    writeCode(fileText, resultBin, len(text))
    writeModel(fileText, characterDict)

def extract(fileCode, fileModel):
    code = readFileCode(fileCode)
    resultBin = binToFloat(code['decode'])
    characterDict = readFileModel(fileModel, code)
    # hasil = extractMethod(code['decode'], code['length'], characterDict)
    hasil = extractMethod(resultBin, code['length'], characterDict)
    writeText(fileModel, hasil)

def floatToBin(floatNum, sizeBit):
    if sizeBit == 8:
        expBit = 4
        mantissa = 3
    elif sizeBit == 16:
        expBit = 5
        mantissa = 10
    elif sizeBit == 32:
        expBit = 8
        mantissa = 23
    elif sizeBit == 64:
        expBit = 11
        mantissa = 52

    convBinary = ""
    for i in range(sizeBit):
        floatNum *= 2
        if floatNum >= 1 :
            floatNum -= 1
            convBinary += "1"
        else :
            convBinary += "0"

    countFloat = 0
    for i in range(sizeBit):
        countFloat+=1
        if convBinary[i] == "1":
            countFloat = i + 1
            break

    biasExp = int(pow(2, expBit-1)-1) - countFloat
    biasBin = bin(biasExp).replace("0b", "")

    leftover = 0
    if len(convBinary[countFloat:countFloat+mantissa]) < mantissa:
        leftover = mantissa - len(convBinary[countFloat:countFloat+mantissa])

    for i in range(expBit-len(biasBin)):
        biasBin = "0" + biasBin
    
    binResult = "0" + biasBin + convBinary[countFloat:countFloat+mantissa] + "0" * leftover
    return binResult

def binToFloat(binary):
    sizeBit = len(binary)
    if sizeBit == 8:
        expBit = 4
        mantissa = 3
    elif sizeBit == 16:
        expBit = 5
        mantissa = 10
    elif sizeBit == 32:
        expBit = 8
        mantissa = 23
    elif sizeBit == 64:
        expBit = 11
        mantissa = 52
    
    biasBin = binary[1:expBit+1]
    biasBin = biasBin[::-1]
    
    exp = 0
    for i in range (len(biasBin)):
        if biasBin[i] == "1" :
            exp += pow(2, i)


    biasExp = int(pow(2, expBit-1)-1)
    countFloat = biasExp - exp

    binaryFraction = "1"
    for i in range(countFloat-1):
        binaryFraction += "0"

    mantissa = binary[expBit+1::]

    binaryFraction = binaryFraction[::-1] + mantissa 

    number = 0
    for i in range(len(binaryFraction)):
        if binaryFraction[i] == "1":
            number += pow(0.5, i+1)
    return number



parser = argparse.ArgumentParser(description='The program for Encoding and Decoding')
parser.add_argument("-c", "--compress", help = "Compress a file")
parser.add_argument("-e", "--extract", help = "Extract a file")
parser.add_argument("-p", help = "Specify the bit size")
parser.add_argument("-d", help = "Specify The Model")
args = parser.parse_args()

if args.compress != None:
    if args.p != None:
        compress(args.compress, int(args.p))
    else:
        compress(args.compress)
elif args.extract != None:
    if args.d != None:
        extract(args.extract, args.d)
    else:
        raise ValueError('File Model Tidak Ditemukan')






