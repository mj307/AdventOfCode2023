card_num = 1
card_dict = {}
card_copies = {}
with open("day4input") as fh:
    line = [line.strip("\n") for line in fh]
    for a in range(1,len(line)+1):
        card_dict[a] = 1
    for each in line:
        count = 0
        cards = 0
        colon_index = each.find(": ")
        each = each[colon_index+2:].split(" | ")
        winning = each[0].split(" ")
        mine = each[1].split(" ")
        for num in winning:
            if num in mine and num.isdigit():
                count += 1
        for a in range(1,count+1):
            card_dict[card_num + a] += card_dict[card_num]
        card_num += 1


sum = 0
for a in card_dict.values():
    sum += a
print (sum)