sum = 0
with open("day1input") as fh:
    calibration_values = []
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            nums = []
            for i,c in enumerate(line):
                # i gives the index and c gives each individual character
                if c.isdigit():
                    nums.append(c)
                for d,val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                    if line[i:].startswith(val):
                        # accounts for overlapping numbers
                        nums.append(str(d+1))
            score = int(nums[0]+nums[-1])
            sum += score

print (sum)