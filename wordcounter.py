import string


# initialize string
def word_counter(text, count=0):
    # using the sum(), strip(), split() methods

    for i in text.split():
        # check for numerical values in text
        a = i.strip(string.punctuation).isnumeric()
        if a is False:
            count += 1
            # count = "There are " + str(result) + " words."
    print(count)


text = "welcome to zuri's 00 internship"
word_counter(text)
