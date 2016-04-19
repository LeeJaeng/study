dictionary = {
    '20': ' ',
    '21': '!',
    '24': '$',
    '25': '%',
    '28': '(',
    '29': ')',
    '2a': '*',
}

result = []
for _ in range(int(input().strip())):
    uri = input().strip()

    keep = []
    temp =''
    i = 0
    while i < len(uri):
        if uri[i] == '%':
            if uri[i+1:i+3] in dictionary.keys():
                keep.append(uri[i:i+3].replace(uri[i:i+3], dictionary[uri[i+1:i+3]], 1))
                i += 3
            else:
                keep.append(uri[i])
                i += 1
        else:
            keep.append(uri[i])
            i += 1

    result_uri =''
    for data in keep:
        result_uri += data
    result.append(result_uri)

for data in result:
    print(data)


"""
파이썬 라이브러리 쓰면 됨
from urllib.parse import unquote
for case in range(int(input())):
    S = input()
    print(unquote(S))
"""
