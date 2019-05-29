def read_file():
    words = []
    n = 0
    number_of_words = 0
    for line in open("wchain.in"):
        new_line = line.strip("\n")
        print(new_line)
        words.append(new_line)
        print(n)
        print (len(words))
        for word in words:
            print(word+'\n')

    words.sort(key=lambda word: len(word))
    return words


def process_words_array(words):
    result = [words.pop(0)]

    for word in words:
        word_to_check = result[-1]

        if len(word) - len(word_to_check) == 1:
            previous_difference = compare_two_words(word, word_to_check)
            if previous_difference <= 1:
                result.append(word)

        if len(word) == len(word_to_check):
            previous_difference = compare_two_words(word, result[-2])
            if previous_difference <= 1:
                result.pop()
                result.append(word)

    return result


def compare_two_words(first_word, second_word):
    first_word_index = 0
    second_word_index = 0
    counter = 0

    while (first_word_index < len(first_word)) & (second_word_index < len(second_word)):
        if first_word[first_word_index] != second_word[second_word_index]:
            counter += 1
            second_word_index -= 1

        first_word_index += 1
        second_word_index += 1

    return counter


if __name__ == "__main__":
    words = read_file()
    print("-------------------------------")
    print (words)
    print(words.__len__())
    result = process_words_array(words)

    print("The longest chain of words: ")
    result.sort(key=lambda word: len(word),
                reverse=True)
    for word in result:
        print("%s ->" % word)
    print("Its length: ", result.__len__())



