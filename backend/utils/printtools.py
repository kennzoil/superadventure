from time import sleep


def slowprint(text):
    """function for displaying text sequentially, to be used in place of print()"""
    text_list = list(text)
    for i in text_list:
        print(i, end="")
        sleep(15/1000)


def fastprint(text):
    """function for displaying text sequentially, to be used in place of print()"""
    text_list = list(text)
    for i in text_list:
        print(i, end="")
        sleep(1/1000)
