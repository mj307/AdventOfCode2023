sum = 0
with open("day4input") as fh:
    line = [line.strip("\n") for line in fh]
    #print (line)
    for each in line:
        points = 0
        colon_index = each.find(": ")
        each = each[colon_index+2:].split(" | ")
        winning = each[0].split(" ")
        mine = each[1].split(" ")
        #print (each)
        #print ("**************")
        #print (winning)
        #print (mine)
        for num in winning:
            if num in mine and num.isdigit():
                #print (num)
                if points == 0:
                    points = 1
                else:
                    points *= 2
                #print (points)
        sum += points
        #print (points)

print (sum)


