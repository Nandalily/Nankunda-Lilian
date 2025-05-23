# outpu favourite brand
x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])
print(x[1])
print(x[2])
print(x[3])

# using negative indexing to print 2nd last item
x = ("samsung", "iphone", "tecno", "redmi")
print(x[-2])

# update iphone to itel
x = ("samsung", "iphone", "tecno", "redmi")
y = tuple(x)
y = ("samsung", "itel", "tecno", "redmi")
print(y)

x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

# 3 adding Huawei to the tuple
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
x_list.append("Huawei")
x = tuple(x_list)
print(x)

# 5 loop through the tuple
x = ("samsung", "iphone", "tecno", "redmi", "Huawei")
for brand in x:
    print(brand)
    
#  count the number of times "samsung" appears in the tuple
x = ("samsung", "iphone", "tecno", "redmi", "Huawei", "samsung")
count = x.count("samsung")

# 6 to delete the first item in the tuple
x = ("samsung", "iphone", "tecno", "redmi", "Huawei")
x_list = list(x)
x_list.pop(0)
x = tuple(x_list)
print(x)

# using tuple constructor to create a  a tuple of cities in Uganda
cities = tuple(("Kampala", "Mbarara", "Gulu", "Jinja", "Masaka"))
print(cities)

# 8 to unpack the tuple above

cities = ("Kampala", "Mbarara", "Gulu", "Jinja", "Masaka")
city1, city2, city3, city4, city5 = cities
print(city1)
print(city2)
print(city3)
print(city1, city2, city3, city4, city5)


# 9 range of indeses to print the 2nd, 3rd and 4th cities
cities = ("Kampala", "Mbarara", "Gulu", "Jinja", "Masaka")
print(cities[1:4])

# 10 joining two tuples
first = ("Nankunda")
second = ("LIlian")
name = first + second
print(name)


# 11 multiplying a tuple by 3
colors = ("red", "blue", "green")
colors = colors * 3
print(colors)

# 12 number of time 8 appeara in
tuple = (1, 3, 7, 8, 7, 5, 8, 6, 8,5)
count = tuple.count(8)
print(count)