# TEXT JUSTIFICATION using dynamic programming
# 28.6.2024
# after https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-20-dynamic-programming-ii-text-justification-blackjack/
# (lecture on Dynamic Programming by Erik Demaine)

import sys

                            # set line length (width in characters) as a global, just for simplicity
width = 57

                            # main methjod
def justify(text):
    words = string_to_array(text)

                            # list to store indicdes of words which begin lines
    first_words = []

    j = len(words)-1

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

    test = justify("Call me Ishmael. Some years ago -- never mind how long precisely -- having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off -- then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.")
    print(test)