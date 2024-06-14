vowels = ['a', 'e', 'i', 'o', 'u','y']
text1 = open('data/text1.txt', 'r+')
text2 = open('data/text2.txt', 'r+')
text1.write("Suppose end get boy warrant general natural. Delightful met sufficient projection ask.\nDecisively everything principles if preference do impression of. Preserved oh so difficult\ndalsi text")
text2.write("Suppose end get boy warrant general natural. Delightful met sufficient projection ask.\nrepulsive on in household. In what do miss time be. Valley as be appear cannot so by.")
text1.close()
text2.close()

def task1(path1="data/text1.txt", path2="data/text1.txt"):
    with open(path1, 'r') as text1:
        with open(path2, 'r') as text2:
            text1, text2 = text1.read(), text2.read()
            text1 = list(text1.split('\n'))
            text2 = list(text2.split('\n'))
            for line in range(min(len(text1),len(text2))):
                if text1[line] != text2[line]:
                    print(f"{text1[line]} MM {text2[line]}")

def task2(path="data/text1.txt"):
    text = open(path, 'r').read()
    book = open('data/text1_info.txt', 'w')
    book.write(f"number of charackters: {number_of_charackters(text)}\n")
    book.write(f"number of lines: {len(list(open(path,'r').readlines()))}\n")
    book.write(f"number of vowels: {number_of_vowels(text)}\n")
    book.write(f"number of constant: {number_of_constants(text)}\n")
    book.write(f"number of digits: {number_of_digits(text)}\n")
    book.close()


def number_of_charackters(text):
    return len(text)

def number_of_vowels(text):
    return len(list(filter(lambda char: char in vowels, text)))

def number_of_constants(text):
    return len(list(filter(lambda char: char not in vowels, text)))

def number_of_digits(text):
    return len(list(filter(lambda char: char.isdigit(), text)))

def task3(path="data/text1.txt"):
    text = open(path, 'r').read()
    text = text[:text.rfind('\n')]
    file = open("data/mtext1.txt", 'w')
    file.write(text)
    file.close()

def task4(path="data/text1.txt"):
    with open(path, 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        longest = max([len(line) for line in text])
        return longest

def task5(path="data/text1.txt",word = "word"):
    text = open(path, 'r').read()
    return text.count(word)

def task6(path="data/text1.txt",word = "",replace= "change"):
    text = open(path, 'r').read()
    text.replace(word, replace)
    #open(path, 'w').close()
    open(path, 'w').write(text)

task6("data/text1.txt","end","F")

