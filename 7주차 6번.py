import math

d = [1, 2, 3, 4, 5]
print("총점은? :",sum(d))

mean = sum(d) / len(d)
print("평균은? :",mean)

vsum = 0
for x in d:
    vsum = vsum + (x - mean) ** 2
var = vsum / len(d)
print("분산은? :",var)

std = math.sqrt(var)
print("표준편차는? :",std)
