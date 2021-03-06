# Write some code that finds all the numbers between 1 and 700 that are divisible by
# 8 and 14 and stores them in a list.
#---YOUR CODE HERE---------------------------------------
l = []
for i in range(1,701):
    if i % 8 == 0 and i % 14 == 0:
        l.append(i)

print(l)
#--------------------------------------------------------

# Write some code that asks a user for an item
# and stores it in a list called groceries. Keep
# asking them for an item until they type "stop".
# Print out the list.
#---YOUR CODE HERE---------------------------------------
item = input("what do you want to add? ")
groceries = list()
while item.lower() != "stop":
    groceries.append(item)
print(groceries)
#--------------------------------------------------------

# Write some code that loops (a for loop) through each string in the list
# below and only prints out those that have exclusively numbers.
#---YOUR CODE HERE---------------------------------------
myList = ["hello123", "19348", "hweuh12", "13", "0", "green"]

for item in myList:
    if item.isnumeric():
        print(item)
#--------------------------------------------------------
