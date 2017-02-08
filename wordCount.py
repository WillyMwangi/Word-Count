"""
WORD COUND LAB
ANDELA
For example for the input "olly olly in come free"

"""


def words(input):
    """
      This function takes an input string
      inputseparates them from each other using the whitespaces between them.
    """
    resultingDict = {}  # dictionary to hold the results

    separated = input.split()  # split the string into independent words

    if len(separated) == 1:
        resultingDict[separated[0]] = 1
        return resultingDict
    else:
        for item in separated:
            if item.isdigit():
                item = int(item)
            resultingDict[item] = separated.count(str(item))
        return resultingDict