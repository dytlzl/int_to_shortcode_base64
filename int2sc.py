from sys import argv
import json


def int2sc(decimal):
    bin_int = format(int(decimal),'b')
    bin_int = bin_int.zfill(((len(bin_int)+5)//6)*6)
    s = [bin_int[i:i+6] for i in range(0, len(bin_int), 6)]
    result = ''
    for i in s:
        if i == '111110':
            result += '-'
        elif i == '111111':
            result += '_'
        else:
            integer = int(i, 2)
            if integer > 51:
                result += chr(integer-4)
            elif integer > 25:
                result += chr(integer+71)
            else:
                result += chr(integer+65)
    print(result)


def sc2int(shortcode):
    binary = ''
    for i in shortcode:
        if i == '-':
            binary += '111110'
        elif i == '_':
            binary += '111111'
        else:
            asc = int(ord(i))
            if asc > 96:
                binary += format(asc-71, '06b')
            elif asc > 64:
                binary += format(asc-65, '06b')
            elif asc > 47:
                binary += format(asc+4, '06b')
    result = int(binary, 2)
    print(result)


if __name__ == '__main__':
    target = argv[1]
    if target.isdecimal():
        int2sc(target)
    else:
        sc2int(target)
