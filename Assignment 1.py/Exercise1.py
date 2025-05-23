# lists
# 1
names = ["Lily","Rona","Gili","Phiona","Linet"]
print("Rona")
print(names[1])

# 2 changing value of first element
names = ["Lily","Rona","Gili","Phiona","Linet"]
print(names)
names[0]= "Nana"
print(names)


# to add a sixth element to the list
names = ["Lily","Rona","Gili","Phiona","Linet"]
print(names)
names.append("Martha")
print(names)

# to add "Bathel" in the third position
names = ["Lily","Rona","Gili","Phiona","Linet", "Martha"]
print(names)
names.insert(2,"Bathel")
print(names)

# to remove the 4th element from the list
names = ["Lily","Rona","Bathel","Gili","Phiona","Linet", "Martha"]
print(names)
names.pop(3)
print(names)

# using negative index to print the last item
names = ["Lily","Rona","Bathel","Gili","Phiona","Linet", "Martha"]
print(names)
print(names[-1])


# using a range of indexes to print the 3rd, 4th and 5th elements
tools = ['cup','plate','jug','spoon','forke','knife','bowl']
print(tools)
print(tools[2:5])

# 8 making a copy of a list
countries = ['Uganda',  'Kenya','Tanzania']
countries_copy = countries.copy()
print(countries_copy)


# 9 loop through the list
countries = ['Uganda', 'Kenya', 'Tanzania']
for country in countries:
    print(country)
    
    # sorting a list in both ascending and descending order
    animals = ["hen","sheep","cattle","goat"]
print(animals)
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

digits = [3,9,2,7,4,5]
digits.sort()
print(digits)
digits.sort(reverse=True)
print(digits)

# output animals with letter a in them
animals = ["hen","sheep","cattle","goat"]
for animal in animals:
    if "a" in animal:
        print(animal)
        
#  joining two lists  
list1 = ['L', 'i', 'l', 'i', 'a', 'n', 'a']
list2 = ['N', 'a', 'n', 'a'] 
list3 = list1 + list2
print(list3)

first_names = ["Lilian", "Grace"]
second_names = ["Nankunda", "Achieng"]
full_names = first_names + second_names
print(full_names)

