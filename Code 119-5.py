string = "abcacax"
i = 0
j  = len(string)-1
my_dic = {}
list1 = []
while i <= j:
  print(string.count(string[i]))
  list1.append(string.count(string[i]))
  i +=1

print(list1)
print(set(list1))
