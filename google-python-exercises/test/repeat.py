import sys
import ast
def main():
    print repeat(sys.argv[1],ast.literal_eval(sys.argv[2]))

def repeat(s,exclaim):
    """
    Is this a doc block?
    """

    result = s * 3
    if exclaim:
        result = result + '!!!'
    return result

if __name__ == '__main__':
    main()
