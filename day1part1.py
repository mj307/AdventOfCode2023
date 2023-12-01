sum = 0
with open("day1input") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            result = [int(char) for char in line if char.isdigit()]
            if len(result) == 1:
                result = [result[0], result[0]]
            else:
                result = [result[0],result[-1]]
            result_string = ''.join(map(str, result))
            #print (result_string)
            sum += int(result_string)

print (sum)


