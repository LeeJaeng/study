people_num = input()

people_list = list()
for i in range(int(people_num)):
    person_name = input()
    people_list.append(person_name)

for name in people_list:
    print("Hello, " + name + "!")

