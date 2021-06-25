
# from typing import Counter


# def characterDivider(text):
#     characterSet = ''.join(dict.fromkeys(text))
#     characterDictionary = []

#     for x in characterSet:
#         tmpdict = {}
#         tmpdict['character'] = x
#         tmpdict['probability'] = text.count(x)/len(text)
#         tmpdict['frequence'] = text.count(x) 
#         characterDictionary.append(tmpdict)

#     return characterDictionary


# def compress(characterDictionary, text):
#     lower = 0
#     upper = 1

#     for i in text:
#         r = upper - lower
#         tmp_lower = lower
#         for x in characterDictionary:
#             tmp_upper = tmp_lower + r * x['probability']
#             print("tabel pada huruf", i, "dengan per-huruf", x['character'], "batas bawah", lower, "batas atas", upper)
#             if x['character'] == i:
#                 upper = tmp_upper
#                 lower = tmp_lower
#                 print("huruf", i, "batas bawah", lower, "batas atas", upper)
#                 break
#             tmp_lower = tmp_upper
#         upper = tmp_upper
#         lower = tmp_lower

#         print("")
    
#     return (upper+lower)/2

# def extract(code, length, characterDictionary):
#     lower = 0
#     upper = 1

#     charList = []

#     Counter = 0
#     for i in range(length):
#         print(Counter)
#         Counter+=1
#         r = upper - lower
#         tmp_lower = lower
#         for x in characterDictionary:
#             tmp_upper = tmp_lower + r * x['probability']
#             if tmp_lower < code and tmp_upper > code:
#                 print("batas bawah", lower, "batas atas", upper)
#                 charList.append(x['character'])
#                 break
#             tmp_lower = tmp_upper
#         upper = tmp_upper
#         lower = tmp_lower
    
#     hasil = ""

#     hasil = hasil.join(charList)

#     return hasil

# # nama='test.txt'
# # openFile = open(nama, "r+")
# # filename = nama[:-4]

# # text = openFile.read()
# # decode = 0.03264119414908981

# # openFile.close()

# # characterDict = characterDivider(text)


# # ini untuk compress komen salah satu

# # ini untuk compress 
# # print(compress(characterDict, text))
# # hasil = compress(characterDict, text)

# # ini untuk extract
# # print(extract(decode, len(text), characterDict))
# # hasil = extract(decode, len(text), characterDict)




# # FILE SYSTEM COMPRESS
# # file = open(f"{filename}.cod", 'w')
# # file.write(str(hasil))
# # file.close()

# # file = open(f"{filename}.mod", 'w')
# # line = ""

# # for x in characterDict:
# #     line = line + f"{x['character']},{x['frequence']}\n"
    
# # file.writelines(line)
# # file.close()



# #FILE EXTRACT


# # Code
# file = open("test.cod", 'r')
# tmpFile = file.read().split(",")
# code = {}
# code['length'] = int(tmpFile[0])
# code['decode'] = float(tmpFile[1])
# file.close()

# # print(code)

# # Model
# file = open("test.mod", 'r')
# line = file.readlines()

# characterDict = []

# for x in line:
#     characterSet = {}
#     x = x.split(',')
#     x[1] = x[1][:-1]
#     characterSet['character'] = x[0]
#     characterSet['frequence'] = x[1]
#     characterSet['probability'] = float(int(x[1])/code['length'])
#     characterDict.append(characterSet)

# file.close()


# hasil = extract(code['decode'], code['length'], characterDict)

# file = open('test.txt', 'w')
# file.writelines(hasil)


# file = open('test.txt', 'r+')
# lines = file.readlines()
# stringSet = ''

# for line in lines :
#     stringSet += line

# print(len(stringSet))
# print(stringSet.splitlines())


def float_to_binfixpoint(number, limit = 16):

    #Menentukan wilayah kotak untuk eksponen dan mantissa
    mantissa = 0
    if limit == 8:
        eksbit = 4
        mantissa = 3
    elif limit == 16:
        eksbit = 5
        mantissa = 10
    elif limit == 32:
        eksbit = 8
        mantissa = 23
    elif limit == 64:
        eksbit = 11
        mantissa = 52
    # elif limit == 128:
    #     eksbit = 15
    #     mantissa = 112

    word = ""
    # print("input number : " , number)
    for i in range(limit):
        number *= 2
        if number >= 1 :
            number -= 1
            word += "1"
        else :
            word += "0"
    # print("binary number below one: " , word)

    count = 0
    for i in range(limit):
        if word[i] != "0":
            count = i + 1
            break
    # print(count)

    # Menentukan nilai bias eksponen lalu dikurang eksponen dari word
    bias_ex = int(pow(2, eksbit-1)-1) - count
    #Menentukan nilai biner di bagian eksponen
    exp_fragment = bin(bias_ex).replace("0b", "")
    exp_fragment = "0"*(eksbit - len(exp_fragment)) + exp_fragment
    print(exp_fragment)

    #Menentukan nilai Mantissa
    mantissa_fragment = word[count:count+mantissa]
    x = 0
    if len(mantissa_fragment) < mantissa:
        x = mantissa - len(mantissa_fragment)


    # print("binary exp : ", bias_ex)
    # print("exp fragment : " , exp_fragment)
    # # print(word[count:])
    # print("mantissa fragment : ", mantissa_fragment)
    
    # Menentukan fixed point binary-nya
    true_word = "0" + exp_fragment + mantissa_fragment + "0"*x
    # print("binary fixedpoint : ", true_word)
    print("punya japran:", true_word)

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
    print("punya japran:",binResult)
    return binResult

def binfixpoint_to_float(binary_fix):
    limit = len(binary_fix)
    mantissa = 0
    if limit == 8:
        eksbit = 4
        mantissa = 3
    elif limit == 16:
        eksbit = 5
        mantissa = 10
    elif limit == 32:
        eksbit = 8
        mantissa = 23
    elif limit == 64:
        eksbit = 11
        mantissa = 52
    # elif limit == 128:
    #     eksbit = 15
    #     mantissa = 112
    
    # Dipisah menjadi fragment yang bagian ekspnen
    bias_ex = int(pow(2, eksbit-1)-1)
    word_eks = binary_fix[1:eksbit+1]
    # print("exp fragment : ", word_eks)
    
    # Mencari nilai untuk binary exponent
    word_eks = word_eks[::-1]
    binary_exponent = 0
    for i in range (len(word_eks)):
        if word_eks[i] == "1" :
            binary_exponent += pow(2, i)

    # print("binary exp : ", binary_exponent)
    # print("bias exponent : ", bias_ex)
    count = bias_ex - binary_exponent

    binary = "1"
    for i in range(count-1):
        binary += "0"

    # Dipisah menjadi fragment yang bagian mantissa
    word_man = binary_fix[eksbit+1:]
    # print("mantissa fragment : " , word_man)

    binary = binary[::-1] + word_man 
    # print("binary number below one: ", binary)

    print("japran :", binary)
    number = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            number += pow(0.5, i+1)
    print("japran :", number)
    return number


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

# binfixpoint_to_float("00111100110011001100110011001100")
# binToFloat("00111100110011001100110011001100")

float_to_binfixpoint(0.010862529431967052, 16)
floatToBin(0.010862529431967052, 16)