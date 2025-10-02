my_list = [1,10,3,4]
print(my_list)

my_list.append(5)
print(my_list)

my_list.extend([6,7,8,9])
print(my_list)

my_list.insert(2,9)
print(my_list)

my_list.remove(9)
print(my_list)

popping = my_list.pop(7)
print(my_list, "removed element is: ", popping)

counting = my_list.count(4)
print(counting)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

length = len(my_list)
print(my_list)

minimum = min(my_list)
print(minimum)

maureen = my_list.copy()
print(maureen)

clear = 3 in my_list
print(clear)

my_list.clear(3)
print(my_list)

