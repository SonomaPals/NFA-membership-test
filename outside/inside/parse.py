# function that parse a string and put every char in a list.
def parse(s):
    parseList = []

    for i in s:
        parseList.append(i.split())

    return parseList
