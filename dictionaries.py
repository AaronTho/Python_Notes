# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}


# adds a new key to an existing dictionary
customer["birthdate"] = "Jan 1 1980"
print(customer['name'])
# get will return "none" instead of an error if the key is not in the dictionary
print(customer.get("birthdate"))
