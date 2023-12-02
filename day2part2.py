sum = 0
power = 0
game_num = 1
with open("day2input") as fh:
    for line in fh:
        if line != "\n":
            passing = True
            min_red = 0
            min_blue = 0
            min_green = 0
            line = line.strip("\n")
            line = line.split(": ")[1] # only gives info about sets per game
            game_temp = line.split("; ")
            game = []
            for each in game_temp:
                temp = []
                temp.append(each)
                game.append(temp)
            for set in game:
                for each in set:
                    split_set = each.split(", ")
                    for each_set in split_set:
                        bigger_split = each_set.split(" ") # splits into colors and values
                        # conditions
                        if bigger_split[1] == 'green':
                            if int(bigger_split[0]) > min_green:
                                min_green = int(bigger_split[0])

                        elif bigger_split[1] == 'red':
                            if int(bigger_split[0]) > min_red:
                                min_red = int(bigger_split[0])

                        elif bigger_split[1] == 'blue':
                            if int(bigger_split[0]) > min_blue:
                                min_blue = int(bigger_split[0])

            game_num += 1
            power = min_blue*min_green*min_red
            print (power)
            sum += power

print (sum)