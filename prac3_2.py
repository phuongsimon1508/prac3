def main():
    asciinum = get_number(50,100)
    print("The character with the ASCII value")
    get_name= input("please enter your name")
    method_name(get_name)


def method_name(get_name):
    print(get_name)


def get_number(minValue, maxValue):
    valid_input = False
    while not valid_input:
        try:
            num = int(input("please enter a number between {} and {}: " .format(min, max)))
            if  minValue <= num <= maxValue:
                valid_input = True
            else:
                print("please enter a number between {} and {}: " .format(min, max))
        except ValueError:
            print("please enter a valid interger")

    return num

main()

