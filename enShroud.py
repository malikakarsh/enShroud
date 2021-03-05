import argparse


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

    file = open(args.output, "w+")
    for line in arrTex:
        file.write(line)

    file.close()


def unHideText(arrTex):
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encode", help="encode", action="store_true")
    parser.add_argument("-d", "--decode", help="decode", action="store_true")
    parser.add_argument("-p", "--path", help="path to text file")
    parser.add_argument("-o", "--output", help="path to output")
    parser.add_argument("-s", "--secret", help="secret text")
    args = parser.parse_args()

    if args.encode:
        try:
            file = open(args.path, 'r')
            arrText = list(file.readlines())
            arrSecret = list(args.secret.split())
            for line in range(len(arrText)):
                if '\n' in arrText[line]:
                    arrText[line] = arrText[line].replace('\n', "")
            hideText(arrText, arrSecret)
            file.close()
        except:
            print("Bad file path!")

    elif args.decode:
        try:
            file = open(args.path, 'r')
            lines = list(file.readlines())
            file.close()
            unHideText(lines)

        except:
            print("Invalid file path!")

    else:
        print("Invalid arguments!")
        print("To encode:")
        print(
            "\tpython3 enShroud.py -e -p PATH_TO_FILE  -o PATH_TO_OUTPUT -s SECRET_MESSAGE")
        print("Tp decode:")
        print("\tpython3 enShroud.py -d -p PATH_TO_FILE")
