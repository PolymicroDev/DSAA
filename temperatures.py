days = {}
with open("Desktop/GitHub/nyc","r") as data:
    for line in data:
        tokens = line.split(',')
        day = tokens[0]
        temp = int(tokens[1])
        days[day] = temp

nums = [1,2,3,4,5]
sum = 0
for idx,key in enumerate(days):
    if idx <= 7:
        sum+=days[key]

average = sum/7
print(f"Average temperature was {average}")

#max = list(days.values())[0]

#for temp in list(days.values()):
#    if temp>max:
#        max = temp

max = days["Jan 1"]
for idx,key in enumerate(days):
    if idx <= 10: #assuming i don't know how many lines are in the file
        if days[key]>max:
            max = days[key]

print(f"Max of first 10 days: {max}")

#Task 2
print("The temperature on Jan 9 was: " + str(days["Jan 9"]))
print("The temperature on Jan 4 was: " + str(days["Jan 4"]))





    
    
        

