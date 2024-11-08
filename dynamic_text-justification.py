# TEXT JUSTIFICATION using dynamic programming
# 28.6.2024
# after https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-20-dynamic-programming-ii-text-justification-blackjack/
# (lecture on Dynamic Programming by Erik Demaine)

# 28.6.2024 -- 1525 -- taking a break for today.
# It does something, but the last line is wrong, very badly compressed whatever the width
# Checked "first words" list against output: correct, therefore, error is in the algorithm not in the display method
# Also: certain widths simply break the program. (45, in this case)


import sys

                            # set line length (width in characters) as a global, just for simplicity
width = 64

                            # main methjod
def justify(text):
    words = string_to_array(text)

                            # list to store indicdes of words which begin lines
    first_words = []

    j = len(words)

    badmin = sys.maxsize
    firstword_temp = len(words)-1

    while j > 1:
        for i in range(j):
            bad = badness(words[i:j])
            if bad < badmin:
                badmin = bad
                firstword_temp = i

        first_words.insert(0,firstword_temp)
        j = firstword_temp
        badmin = sys.maxsize


    return(array_to_output(words,first_words))


def array_to_output(words,first_words):
    print("\n\nFirst words should be:")
    print(first_words)
    print("\n")

    para = []
    line = -1

    for w in range(len(words)):
        if first_words and w == first_words[0]:
            line += 1
            para.append([])
            para[line].append(words[w])
            first_words.pop(0)
        else:
            para[line].append(words[w])
        #print(para)

    output = ""


    for line in range(len(para)):
        #print(para[line])
        output += pad(para[line]) + "\n"

    return output

def pad(words):

    lastword = len(words)-2

    chars = sum(len(w) for w in words)
    spaces = width-chars

    word = 0

    while spaces > -1:
        words[word] += " "
        spaces -= 1
        word += 1
        if word > lastword:
            word = 0

    return "".join(word for word in words)



                            # I coded this to split a string into an array using spaces
                            # then immediately realised there's probably a built-in function to do it
                            # Still, having done it:
def string_to_array(text):
    words = [""]
    index = 0

    while text:
        if text[0] == " ":
            words.append("")
            index += 1
        else:
            words[index] += text[0]

        text = text[1:]

    return words




                            # spaces are included!
                            # if the words+spaces > greater than the width, returns 'infinity'
                            # if not, returns the surplus space, cubed
def badness(words):

    tally = 0

    for word in words:
        tally += len(word)

    tally = tally + len(words)-1

    if tally > width:
        return sys.maxsize

    if tally <= width:
        return (width-tally) ** 3





if __name__ == "__main__":

    input = input("Text: ")

    print("Width is set to " + str(width))
    test = justify(input)

    print(test)