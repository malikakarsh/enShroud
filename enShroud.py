# takes the count of the words in text and secret message and divides how many words would be there in each line
def perLine(n1, n2):  # n1 -> count of words in text, n2 -> count of words in secret
    global n
    if (n1 > n2):
        n = 1
    else:
        n = n2//n1


# convert each letter of secret to binary
def binConvert(array):
    for word in range(len(array)):
        char = chr(143).join(format(ord(letter), 'b')
                             for letter in array[word])
        char = char.replace('1', "\t")
        char = char.replace('0', " ")
        array[word] = char


# convert binary back to characters
def textConvert(array):
    for sentence in range(len(array)):
        array[sentence] = array[sentence].replace('\t', '1')
        array[sentence] = array[sentence].replace(' ', '0')


    #file = open("hello.txt", 'r+')
    #arrText = list(file.readlines())
text = "hey there\nhow are you\nhope you are doing well\nthis summer is quite well\nfor all of us"
arrText = list(text.split('\n'))

string = "this is my finest arrangements of all"
arrSecret = list(string.split())

for line in range(len(arrText)):
    if '\n' in arrText[line]:
        arrText[line] = arrText[line].replace('\n', "")


def hideText(arrTex, arrSec):
    perLine(len(arrTex), len(arrSec))
    binConvert(arrSec)
    i = 0
    for line in range(len(arrTex)):
        if (line != (len(arrTex) - 1)):
            var = ""
            sentence = "\n"
            if (i < len(arrSec)):
                for x in range(n):  # add words divided according to perLine function to each line
                    var += arrSec[i] + chr(144)
                    i += 1
                sentence = f"{chr(160)}{var}{chr(160)}\n"
            arrTex[line] += sentence
        else:  # The last line need not include a new line tab (\n) at its last
            var = ""
            sentence = ""
            if (i < len(arrSec)):
                # add all the remaining words of secret to the last line if exists
                while (i != len(arrSec)):
                    var += arrSec[i] + chr(144)
                    i += 1
                sentence = f"{chr(160)}{var}{chr(160)}"
            arrTex[line] += sentence

    file = open("output.txt", "w+")
    for line in arrTex:
        file.write(line)

    file.close()


#hideText(arrText, arrSecret)

file = open("output.txt", 'r+')
lines = list(file.readlines())
# print(lines)
file.close()


def unHideText(arrTex):
    newFile = open("decoded.txt", 'w+')
    textConvert(arrTex)
    sentence = ""
    for line in arrTex:
        lines = list(line.split(chr(160)))
        if (len(lines) > 1 and len(lines) != 2):
            words = list(lines[1].split(chr(144)))
            for word in words:
                letters = list(word.split(chr(143)))
                for letter in letters:
                    if (letter != ""):
                        sentence += chr(int(letter, 2))
                sentence += " "
    print(sentence)


unHideText(lines)
