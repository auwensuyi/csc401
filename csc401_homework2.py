
def buy_ticket(age, ticket_type):
    if age < 65 and ticket_type == "10-ride":
        return int(38)
    if age < 65 and ticket_type == "monthly":
        return float(159.5)
    if age >= 65 and ticket_type == "10-ride":
        return float(34.2)
    if age >= 65 and ticket_type == "monthly":
        return float(143.55)


def sequences():
    for i in range(9, 16):
        print(i, end=" ")
    print()
    for i in range(4, 30, 4):
        print(i, end=" ")
    print()
    for i in range(30, 10, -3):
        print(i, end=" ")


def shorten_text(word_list):
    for word in (word_list):
        if word_list == '':
            print("Input is empty")
        else:
            print(word[0] + "..." + word[-1])


def find_multiples(number_list, target):
    for i in number_list:
        if i % target == 0:
            print(i)
    if target == 0 or number_list == []:
        print("No numbers provided")


# --------------------------------------------
# STOP! Do not change anything below this line
# The code below makes this file 'self-testing'
# --------------------------------------------
if __name__ == "__main__":
    import doctest

    doctest.testfile('csc401_homework2_test.txt', verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
