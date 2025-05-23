# Strings
# concatenating two variables integer and string
x = 10
y = "Hello"
print(str(x) + y)  

# 2outputing string without spaces
txt = "    Hello   World  "
print(txt)  # prints with spaces
print(txt.strip())
print("".join(txt.split())) 

# 3 converting the value of txt to uppercase
txt = "Hello World"
print(txt.upper()) 

# replace W with U in the string above
txt = "Hello World"
print(txt.replace("W", "U"))

# 5 returning range of characters in the 2nd, 3rd and 4th position
y = " I am a Proud Ugandan"
print(y[2:5])

# 6 x = "All "Data Scientists " are cool!"  gives and error
x = 'All Data Scientists are cool!' 
print(x)
