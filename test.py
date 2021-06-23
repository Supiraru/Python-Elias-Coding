from typing import Counter


def characterDivider(text):
    characterSet = ''.join(dict.fromkeys(text))
    characterDictionary = []

    for x in characterSet:
        tmpdict = {}
        tmpdict['character'] = x
        tmpdict['probability'] = text.count(x)/len(text)
        tmpdict['frequence'] = text.count(x) 
        characterDictionary.append(tmpdict)

    return characterDictionary


def compress(characterDictionary, text):
    lower = 0
    upper = 1

    for i in text:
        r = upper - lower
        tmp_lower = lower
        for x in characterDictionary:
            tmp_upper = tmp_lower + r * x['probability']
            print("tabel pada huruf", i, "dengan per-huruf", x['character'], "batas bawah", lower, "batas atas", upper)
            if x['character'] == i:
                upper = tmp_upper
                lower = tmp_lower
                print("huruf", i, "batas bawah", lower, "batas atas", upper)
                break
            tmp_lower = tmp_upper
        upper = tmp_upper
        lower = tmp_lower

        print("")
    
    return (upper+lower)/2

def extract(code, length, characterDictionary):
    lower = 0
    upper = 1

    charList = []

    Counter = 0
    for i in range(length):
        print(Counter)
        Counter+=1
        r = upper - lower
        tmp_lower = lower
        for x in characterDictionary:
            tmp_upper = tmp_lower + r * x['probability']
            if tmp_lower < code and tmp_upper > code:
                print("batas bawah", lower, "batas atas", upper)
                charList.append(x['character'])
                break
            tmp_lower = tmp_upper
        upper = tmp_upper
        lower = tmp_lower
    
    hasil = ""

    hasil = hasil.join(charList)

    return hasil

# nama='test.txt'
# openFile = open(nama, "r+")
# filename = nama[:-4]

# text = openFile.read()
# decode = 0.03264119414908981

# openFile.close()

# characterDict = characterDivider(text)


# ini untuk compress komen salah satu

# ini untuk compress 
# print(compress(characterDict, text))
# hasil = compress(characterDict, text)

# ini untuk extract
# print(extract(decode, len(text), characterDict))
# hasil = extract(decode, len(text), characterDict)




# FILE SYSTEM COMPRESS
# file = open(f"{filename}.cod", 'w')
# file.write(str(hasil))
# file.close()

# file = open(f"{filename}.mod", 'w')
# line = ""

# for x in characterDict:
#     line = line + f"{x['character']},{x['frequence']}\n"
    
# file.writelines(line)
# file.close()



#FILE EXTRACT


# Code
file = open("test.cod", 'r')
tmpFile = file.read().split(",")
code = {}
code['length'] = int(tmpFile[0])
code['decode'] = float(tmpFile[1])
file.close()

# print(code)

# Model
file = open("test.mod", 'r')
line = file.readlines()

characterDict = []

for x in line:
    characterSet = {}
    x = x.split(',')
    x[1] = x[1][:-1]
    characterSet['character'] = x[0]
    characterSet['frequence'] = x[1]
    characterSet['probability'] = float(int(x[1])/code['length'])
    characterDict.append(characterSet)

file.close()


hasil = extract(code['decode'], code['length'], characterDict)

file = open('test.txt', 'w')
file.writelines(hasil)