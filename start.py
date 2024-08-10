price = [19,23,21,15,16,18,21]
demand = [55,7,20,123,88,76,26]

# Fisrt method:
priceAvg = sum(price)/len(price)
demandAvg = sum(demand)/len(demand)
sumXY = 0
for i in range (len(price)):
    sumXY = sumXY + (price[i] - priceAvg) * (demand[i] - demandAvg)
print(sumXY)

# Second method:
XY = 0
for i in range(len(demand)):
    XY = XY + price[i] * demand[i]
print(XY - (sum(price)*sum(demand))/len(price))