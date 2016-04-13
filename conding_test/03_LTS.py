test_case_num = input()
result = []

for i in range(int(test_case_num)):
    longest = 0
    seq_range = int(input())
    seq = input().split(' ')

    num = 0
    sub_long = 0
    for i in range(seq_range):
        int_seq = int(seq[i])
        if int_seq > num:
            sub_long += 1
            num = int_seq
            if longest < sub_long:
                longest = sub_long
        else:
            sub_long = 0
            num = 0
            if (seq_range - i) < sub_long:
                break;
    result.append(longest)

for data in result:
    print(data)


