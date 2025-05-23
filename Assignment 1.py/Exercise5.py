
# Dictionaries store ordered pairs of key and value
# using dictionary to print the value of the shoe size

shoes = {
	# "brand": "Nick",
	"color": "black",
	"size": 40
}
print(shoes["size"])
print(shoes["color"])
print(shoes["brand"])

# 2 to change the value of Nick to Adidas
shoes["brand"] = "Adidas"
print(shoes["brand"])
print(shoes)

# to add value pair of type sneakers to the dictionary
shoes["type"] = "sneakers"
print(shoes["type"])
print(shoes)


# 4 returning a list of all the keys in the dictionary
print(shoes.keys())

# 5 list of all the values in the dictionary
print(shoes.values())

# 6 if key size exixts in the dictionary
if "size" in shoes:
    print("yes")
    
    # 7 loop through the dictionary
for key, value in shoes.items():
    print(key, value)
    
    
#   to remove color from the dictionary
shoes.pop("color")
print(shoes)

# 9 to empty the dictionary
shoes.clear()
print(shoes)

# 10 a copy of a dictionary
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoes2 = shoes.copy()
# print(shoes2) 


# # nested dictionaries
# shoes = {
#     "brand": "Nick",
#     "color": "black",
#     "size": 40,
#     "details": {
#         "price": 5000,
#         "stock": 20
#     }
# }
# print(shoes["details"]["price"])
# print(shoes["details"]["stock"])
# print(shoes["details"]["price"] + shoes["details"]["stock"])



Students = {
    "name": "Nick",
    "age": 20,
    "class": "A",
}
print(Students)
print(Students["name"])
print(Students["age"])
print(Students["class"])
# changing the value of name to "Cathy"
Students["name"] = "Cathy"
print(Students)

# adding a type of subject  to the dictionary
Students["subject"] = "Math"
print(Students)

print(Students["subject"])

# 4 to remove age from the dictionary
Students.pop("age")
print(Students)

# 5 to check if class exists in the dictionary
if "class" in Students:
    print("yes")
    
    


# nested dictionaries
Students = {
    "name": "Nick",
    "age": 20,
    "class": "A",
    "details": {
        "subject": "Math",
        "grade": "A+"
    }
}
print(Students["details"]["subject"])
print(Students["details"]["grade"])

# # 7 to loop through the dictionary
# for key, value in Students.items():
#     print(key, value)
# 8 to empty the dictionary
Students.clear()
print(Students)


# 10 to return a list of all the keys in the dictionary
print(Students.keys())

# 11 to return a list of all the values in the dictionary
print(Students.values())


# 12 to check if age exists in the dictionary
if "age" in Students:
    print("yes")
    
# 13 to loop through the dictionary
for key, value in Students.items():
    print(key, value)
    
# 14 to remove class from the dictionary
Students.pop("class")
print(Students)

# 15 to empty the dictionary
Students.clear()
print(Students)