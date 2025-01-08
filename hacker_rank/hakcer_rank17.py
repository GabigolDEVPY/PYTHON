import textwrap
def wrap(string, max_width):
    stringsep = textwrap.fill(string, max_width)
    return stringsep

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)