import csv

hero_start_row_num = 3


f = open('./spread.csv', 'r')
csvReader = csv.reader(f)

entire_data = []
for row in csvReader:
    entire_data.append(row)

heroes = []
for i in range(hero_start_row_num, len(entire_data)):
    hero = dict()
    for j in range(0, len(entire_data[i])):
        hero[entire_data[0][j]] = entire_data[i][j]
    heroes.append(hero)


print(heroes[1])
f.close()



