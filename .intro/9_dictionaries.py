"""
Dictionaries is another data type like integers, strings, lists

defintion: consists of key and pair datas like a list
"""
# Example 1 - creating a dictionary
user = {
    "username": "Lincoln",
    "password": "idk",
    "age": 1000,
    "RAN": ["RANDOM", "asdsad"],
    "games": {
        "btd6": "100000000000000 hrs",
        "dfghe": "sdefsdefds"
    }
}

# Example 2 - getting length of dictionary
print(len(user))

# adding item to dictionary
user["fav food"] = "candy"

# print item
name = user["username"]
print(name)

# del item
del user["fav food"]

# checking if key is in dictionary
if "daniel" in user:
    print(user["daniel"])
else:
    print("key not in user")