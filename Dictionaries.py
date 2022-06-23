phonebook = {}
phonebook["John"] = 900000001
phonebook["Jack"] = 910000002
phonebook["Jill"] = 920000003
print(phonebook)
print(phonebook["John"])


# ****************************************************************
phonebook = {
    "John": 900000001,
    "Jack": 910000002,
    "Jill": 920000003
}
del phonebook["John"]
# phonebook.pop("John")
print(phonebook)


# **************
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
# your code goes here
phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
