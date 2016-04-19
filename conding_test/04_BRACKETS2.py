brackets = dict([')(', '][', '}{',])

def match(xs):
    s = []
    for x in xs:
        if x in '[{(':
            s.append(x)
        elif s and s[-1] == brackets[x]:
            s.pop()
        else:
            return False
    if s:
        return False
    return True


for _ in range(int(input())):
    if match(input()):
        print('YES')
    else:
        print('NO')
