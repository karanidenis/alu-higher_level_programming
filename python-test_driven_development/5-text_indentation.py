#!/usr/bin/python3
""" module that  prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    :param text: text to be split where (.?:) are
    :return: print a text and a new line where there are (.?:)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    char = ".?:"
    aux = 0
    for i in text:
        if aux == 0:
            if i == ' ':
                continue
            else:
                print("{}".format(i), end="")
                aux = 1
        else:
            if i in char:
                print("{}".format(i), end="\n\n")
                aux = 0
            else:
                print("{}".format(i), end="")


if __name__ == '__main__':
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")