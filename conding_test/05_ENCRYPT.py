import sys

rl = lambda: sys.stdin.readline()
test_case_count = rl().strip()
result = []

for i in range(int(test_case_count)):
    str_encrypt = lambda: sys.stdin.readline()
    str_encrypt = rl().strip()
    str_result = ''
    str_result_2 = ''
    len_str = len(str_encrypt)

    for i in range(len_str):
        if i % 2 == 0:
            str_result += str_encrypt[i]
        else:
            str_result_2 += str_encrypt[i]

    result.append(str_result + str_result_2)

for data in result:
    print(data)

# 이렇게 한 줄로 가능
# for i in range(input()):x=raw_input();print x[::2]+x[1::2]
