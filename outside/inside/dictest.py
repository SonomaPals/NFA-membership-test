#(a+b)(c+d)+

mydic = {}
counterx = 0
countery = 0
counterz = 0
symbols = ['a', 'b','c','d']
len2 = len(symbols) * 2
for i in range(len2):
    mydic[i] = {}
for char in symbols:
    mydic[counterx][char] = []
    counterx = counterx + 1     
for char in symbols:
    counterz = counterz + 1
    mydic[countery][char] = counterz
    countery = countery + 1
       
print(mydic)