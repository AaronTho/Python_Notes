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


# Botegga Dictionary Notes

players = {
    "ss": "Correa",
    "2b": "Altuva",
    "3b": "Bregmans",
    "DH": "Gattis",
    "OF": "Springer",

}

second_base = players['2b']
designated_hitter = players['DH']
print(second_base)
