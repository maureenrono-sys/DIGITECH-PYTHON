my_dict = {"name": "Maureen", "age":22, "tribe":"Nandi"}
print(my_dict)

#my_dict.clear()
#print(my_dict)

backup = my_dict.copy()
print(backup)


#assigning constant values to all the keys
keys = ["name", "age", "city"]
values = "unknown"
default = dict.fromkeys(keys,values)
print(default)

getting = backup.get("age")
print(getting)

key1 = backup.keys()
print(key1)

value1 = my_dict.values()
print(value1)

all_item = backup.items()
print(all_item)

popping = backup.pop("name")
print(popping)
print(backup)

popitem = my_dict.popitem()
print(popitem)
print(my_dict)

new_dict = {"name":"Haddasssah","country":"Kenya"}
setdefault = new_dict.setdefault("name", "Giriama")
print(setdefault)

updating = my_dict.update(new_dict)
print(my_dict)

new_keys = ["school", "gender", "class"]
new_values = ["Barani", "Female", 8]
complete_dict = dict(zip(new_keys,new_values))
print(complete_dict)