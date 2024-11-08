#Dictionary
#A collection of {key:value} pairs ordered and changeable. No duplicates.

capitals = {"USA":"Washington D.C",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}
"""
if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

print(capitals)
capitals.update({"Germany":"Berlin"})   #add to dictionary
print(capitals)
"""
#capitals.update({"USA":"Detroit"})      #updates USA key
#print(capitals)
#capitals.pop("China")                   #removes China key and associated value
#print(capitals)
#capitals.popitem()                      #removes the last key:value pair that was inserted.
#print(capitals)
#capitals.clear()                        #clears dictionary
"""
print("----------")

keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key, end=" ")
print("----------")
"""
values = capitals.values()
print(values)
print()
for value in values:
    print(value, end=" ")
print("----------")
"""
items = capitals.items()
print(items)
print("----------")

for key, value in capitals.items():
    print(f"{key}: {value}")


"""