
# sets
# using set() constructor to create a set of 3 beverages
beverages = {"water", "juice", "soda"}
print(beverages)

# correct method to add 2 more items to the set
beverages.add("milk")
beverages.add("tea")
print(beverages)

# checking if microwave is in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)


# 4 to remove " kettle" from the set

mySet.remove("kettle")
print(mySet)

# loop through the set
for item in mySet:
    print(item)
    
    
    # adding elements to a list to a set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
myList = ["flat iron", "rice cooker", ]
mySet.update(myList)
print(mySet)


# joining two sets
set1 = { 19, 20, 21}
set2 = {'Hannah', 'Martha', 'Phiona'}
set3 = set1.union(set2)
print(set3)


