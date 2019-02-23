from sys import argv
import json


def split(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]


def int2sc():
    bin_int = format(int(argv[1]),'b').zfill(60)
    s = split(bin_int, 6)
    table_json = open('base64_table.json', 'r')
    dictionary = json.loads(table_json.read())
    result = ''
    for i in s:
        result += dictionary[i]
    print(result)


def sc2int():
    shortcode = argv[1]
    s = split(shortcode, 1)
    table_json = open('base64_table.json', 'r')
    dict = json.loads(table_json.read())
    dict = {v:k for k, v in dict.items()}
    binary = ''
    for i in s:
        binary += dict[i]
    result = int(binary, 2)
    print(result)


if __name__ == '__main__':
    target = argv[1]
    if target.isdecimal():
        int2sc()
    else:
        sc2int()
