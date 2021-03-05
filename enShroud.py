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
        char += " ".join(format(ord(letter), 'b') for letter in array[word])
        char = char.replace('1', "\t")
        char = char.replace('0', " ")
        array[word] = char


file = open("hello.txt", 'r+')
arrText = list(file.readlines())
