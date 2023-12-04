values_list = []
with open("day3input") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            values_list.append(line)

def check(list1,row,column):
    for r in range(row-1,row+2):
        for c in range(column-1,column+2):
            if r>=0 and r<len(list1) and c>=0 and c<len(list1[0]):
                if not list1[r][c].isdigit() and list1[r][c] != ".":
                    return True
    return False

passing = False
sum = 0

for row in range(0,len(values_list)):
    temp_num = ''
    for column in range(0,len(values_list[0])):
        char = values_list[row][column]
        if char.isdigit():
            temp_num += char
            if passing == False:
                passing = check(values_list,row,column)

        elif char == ".":
            if passing == True:
                print(temp_num)
                sum += int(temp_num)
            temp_num = ''
            passing = False

        else:
            if passing == True:
                print(temp_num)
                sum += int(temp_num)
            temp_num = ''
            passing = False

    if passing == True:
        print(temp_num)
        sum += int(temp_num)
    passing = False

print (sum)


