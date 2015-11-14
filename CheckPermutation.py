__author__ = 'tianzhang'


def set_hash(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 0
    return d

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    d1 = set_hash(s1)
    d2 = set_hash(s2)

    for key in d1.keys():
        if key not in d2 or d1[key] != d2[key]:
            return False

    return True


if __name__ == '__main__':
    print check_permutation('abd', 'sb')
    print check_permutation('sssgcg', 'ojhalb')
    print check_permutation('abcdeeb', 'abcbedb')