# Numbers - Integer, Float, ComplexNumber
a=10
b=20.4
c='pushpa'
print(a)
print(type(a))
print(type(b))
print(type(c))

# print("###Integer###")
a=10
# print("###Float###")
b=20.4
# print("###ComplexNumber###")
j=2j+7
print(type(j))
print(j)
# print("###Dictionary###")
dic1={1:"hello",2:"pushpa",3:"how r u"}
dic2={"a":"push","b":"Agar"}
print(dic1[1])
print(dic1[3])
print(dic1)
print(dic1[2])
print(dic2["a"])


# print("###Boolean###")
boo=True
boo1=False
print(boo, boo1)
# print("###Set###")
set1=set("pushpa")
print(set1)
set2=set("Agarsha")
print(set2)
# Sequence - Strings, List , Tuple
print("###Strings###")

# len, lower, upper, concat, find, replace, split, join

str1 = "This is a first code"
list3 =  str1.split(" ")
print(list3)
str3="PUSHPA SATHISH"
str2 = 'This is a second code'
# str3 = '''This is a third code
# This is fourth line'''
print(str1.upper())
print(str3.lower())
print(len(str1))
print(str1+str2)
print(str1.find("a"))
print(str1.replace("a","b"))
print(str2.replace('This',"that"))
print('#'.join(str1))
print("$".join(str3))


# print("###List###")
    # append, insert, index, remove, sort, reverse, pop, Slices, extend
list1 = [1,2,4,5]
list2 = [1,2,4,5]
print(len(list1))
list1.append(6)
list1.insert(2,3)
print(list1)
print(list1.index(4))
list1.remove(4)
list1.sort()
list1.pop()
print(list1)
print(list1[3:4])
list2.extend(list1)
print(list2)



# print("###Tuple##")

tu = (1,2,3,4)
print(tu)

