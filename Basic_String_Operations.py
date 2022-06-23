astring = "Hello World"
print(len(astring))
print(astring.index('o'))
print(astring[3:7])
# [start:stop:step]
print(astring[3:7:2])
# reverse the string
print(astring[::-1])
print(astring.upper())
print(astring.lower())

# ********************************
print(astring.startswith("Hello"))
print(astring.endswith("HelLo"))

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
