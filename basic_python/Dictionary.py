import os
mydictionary={"a":"apple","b":"ball","c":"cat"}#""dictionary can have list in it""
print(list(mydictionary))     # contains list of all elements of dictionary
print(mydictionary.items())   #prints keys and values both
print(mydictionary.values())  # prints values only
print(mydictionary.keys())    #prints keys only
print(mydictionary)
updateDict={"d":"dog","e":"egg"}
mydictionary.update(updateDict)
print(mydictionary)

print(mydictionary.get("a"))
print(mydictionary["b"])
'''both the above line will print same if the key give  but if key 
 is not present .get will give output none and [] will give error'''