sequence = input()

question_num = input()

for i in range(int(question_num)):
    section = input().split(" ")
    copy_sequence = sequence
    
    sub_num_1 = int(section[0])
    sub_num_2 = int(section[1])

    if sub_num_1 < sub_num_2:
        sub_sequence = copy_sequence[sub_num_1: sub_num_2+1]
    else :
        sub_sequence = copy_sequence[sub_num_2: sub_num_1+1]
    
    checking_char = sub_sequence[0]
    
    # 1
    if int(checking_char) == 1:
        # 0
        if sub_sequence.find('0') >= 0:
            print("No")
        else:
            print("Yes")
    # 0
    else :
        # 1
        if sub_sequence.find('1') >= 0:
            print("No")
        else:
            print("Yes")

        
            

