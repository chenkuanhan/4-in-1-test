input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']



for i in range(len(input1)):
  dic1 = {input1[i]:input1.count(input1[i])}
  print(dic1)
