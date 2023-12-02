game_num = 1
sum = 0
with open("day2input") as fh:
    for line in fh:
        if line != "\n":
            passing = True
            line = line.strip("\n")
            line = line.split(": ")[1] # only gives info about sets per game
            game_temp = line.split("; ")
            #print (set_temp)
            game = []
            for each in game_temp:
                temp = []
                temp.append(each)
                game.append(temp)
            #print (game)
            for set in game:
                for each in set:
                    #print (each)
                #'''
                    split_set = each.split(", ")
                    for each_set in split_set:
                        bigger_split = each_set.split(" ") # splits into colors and values
                        # conditions
                        if bigger_split[1] == 'green':
                            if int(bigger_split[0]) > 13:
                                passing = False
                                break
                        elif bigger_split[1] == 'red':
                            if int(bigger_split[0]) > 12:
                                passing = False
                                break
                        elif bigger_split[1] == 'blue':
                            if int(bigger_split[0]) > 14:
                                passing = False
                                break

            if passing:
                sum += game_num
            game_num += 1

print (sum)



