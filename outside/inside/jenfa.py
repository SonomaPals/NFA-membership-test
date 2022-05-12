class Type:
    SYMBOL = 1
    CONCAT = 2
    UNION  = 3
    STAR = 4

class Exp_Tree:

    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.left = None
        self.right = None

def print_tree(et):
    if et.type == Type.SYMBOL:
        # evaluate symbol: it is going to create a nfa for the symbol. ex. if symbol is a, then it will create a nfa for a. 
        print(et.value)
    elif et.type == Type.CONCAT:
        print_tree(et.left)
        print(".")
        print_tree(et.right)
    elif et.type == Type.UNION:
        print_tree(et.left)
        print("+")
        print_tree(et.right)
    elif et.type == Type.STAR:
        print_tree(et.left)
        print("*")

def create_tree(regex_string):
    stack = []
    for char in regex_string:
        if char.isalnum():
            stack.append(Exp_Tree(Type.SYMBOL, char))
        else:
            if char == "+":
                node = Exp_Tree(Type.UNION)
                node.right = stack.pop()
                node.left = stack.pop()
            elif char == ".":
                node = Exp_Tree(Type.CONCAT)
                node.right = stack.pop()
                node.left = stack.pop()
            elif char == "*":
                node = Exp_Tree(Type.STAR)
                node.left = stack.pop()
            stack.append(node)
    return stack[0]

# The regular-expression operator star has the highest precedence and is left associative.
# The regular-expression operator concatenation has the next highest precedence and is left associative.
# The regular-expression operator + has the lowest precedence and is left associative.
def Precedence(a, b):
    p = ["+", ".", "*"]
    return p.index(a) > p.index(b)

def postfix(regex_list):
    stack = []
    string = ""

    for char in regex_list:
        if char.isalpha():
            string = string + char
            continue

        if char == ")":
            while len(stack) != 0 and stack[-1] != "(":
                string = string + stack.pop()
            stack.pop()
        elif char == "(":
            stack.append(char)
        elif char == "*":
            string = string + char
        elif len(stack) == 0 or stack[-1] == "(" or Precedence(char, stack[-1]):
            stack.append(char)
        else:
            while len(stack) != 0 and stack[-1] != "(" and not Precedence(char, stack[-1]):
                string = string + stack.pop()
            stack.append(char)

    while len(stack) != 0:
        string = string + stack.pop()
    return string

# return the string regex as a list (parse the regex into a list) 
# and add a dot "." between consecutive symbols for concatenation
def prepare_regex(regex_string):
    temp = []
    for i in range(len(regex_string)):
        if i != 0\
            and (regex_string[i-1].isalnum() or regex_string[i-1] == ")" or regex_string[i-1] == "*")\
            and (regex_string[i].isalnum() or regex_string[i] == "("):
            temp.append(".")
        temp.append(regex_string[i])
    regex_string = temp
    return postfix(regex_string)


#####################################################################
def main():
    input = "ab+c" 
    #input = "(a+b)(a+b)"
    regex = prepare_regex(input) # return a postfix string
    #print(regex)
    expression_Tree = create_tree(regex)
    print_tree(expression_Tree)
    return 0

main()

