"""
import operator

for _ in range(int(input().strip())):
    points = []
    for _ in range(3):
        p = input().strip().split()
        points.append((int(p[0]), int(p[1])))

    sameX = dict()
    sameY = dict()
    for point in points:
        if point[0] in sameX.keys():
            sameX[point[0]] += 1
        else:
            sameX[point[0]] = 0
        if point[1] in sameY.keys():
            sameY[point[1]] += 1
        else:
            sameY[point[1]] = 0

    sortedX = sorted(sameX.items(), key=operator.itemgetter(1))
    sortedY = sorted(sameY.items(), key=operator.itemgetter(1))

    print('{0} {1}'.format(sortedX[0][0], sortedY[0][0]))

2개는 숫자가 같고 나머지 한개는 다를 때

그 나머지 숫자를 찾기 위해 bit 연산을 함
"""
for i in range(int(input())):
    x = y = 0
    for i in range(3):
        p = input().strip().split()
        x ^= int(p[0])
        y ^= int(p[1])
    print('{0} {1}'.format(x, y))
