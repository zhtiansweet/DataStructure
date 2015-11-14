__author__ = 'tianzhang'


def reverse_string(s):
    temp = list(s)
    length = len(temp)
    for i in range(0, length/2):
        temp[i], temp[length-1-i] = temp[length-1-i], temp[i]
    return ''.join(temp)


if __name__ == '__main__':
    test = 'abcdef'
    print reverse_string(test)
    h = reversed(test)
    print ''.join(reversed(test))
    print test[::-1]