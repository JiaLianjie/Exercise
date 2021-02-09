import random
import matplotlib.pyplot as plt
num = int(input("次数："))
var = range(1, num+1)
value = []
pos, neg, rate = 0, 0, 0
for i in range(num):
    choice = random.choice(range(0,10))
    if choice == 0:
        pos += 1
        rate = (pos / (i+1)) * 100
        value.append(rate)
    else:
        neg += 1
        rate = (pos / (i+1)) * 100
        value.append(rate)
plt.figure()
plt.plot(var, value)#横轴为次数，纵轴为正面的概率
plt.show()