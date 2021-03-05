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
        char = " ".join(format(ord(letter), 'b') for letter in array[word])
        char = char.replace('1', "\t")
        char = char.replace('0', " ")
        array[word] = char


#file = open("hello.txt", 'r+')
#arrText = list(file.readlines())
text = "hey there\nhow are you\nhope you are doing well"
arrText = list(text.split('\n'))

string = "Hey this is the best test to practice fucked things"
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
                for x in range(n):
                    var += arrSec[x] + chr(160)
                    i += 1
                sentence = f"{chr(160)}{var}\n"
            arrTex[line] += sentence
        else:
            var = ""
            sentence = ""
            if (i < len(arrSec)):
                while (i != len(arrSec)):
                    var += arrSec[i] + chr(160)
                    i += 1
                sentence = f"{chr(160)}{var}"
            arrTex[line] += sentence

    file = open("output.txt", "w+")
    for line in arrTex:
        file.write(line)

    file.close()


hideText(arrText, arrSecret)
print(arrText)
