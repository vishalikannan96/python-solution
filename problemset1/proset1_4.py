#valume of sphere
'''def vol_sphere(r1):
    global pi
    return (4/3)*pi*r*r*r

pi=3.142
r=int(input())
print(vol_sphere(r))'''

#Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
#Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for
#60 copies?

'''def wholesale():
    bookprice=24.95
    discount=(100-40)/100
    firstshipcost=3
    copies=60
    remshipcost=0.75*(copies-1)
    totalcost=(bookprice*discount*copies)+firstshipcost+remshipcost
    return totalcost
print(wholesale())'''

#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
#tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

import math
strtime=((6*60)+52)*60 #hr to min
easypace=((8*60)+15)*2
tempo=((7*60)+12)*3
time=(strtime+easypace+tempo)/(60*60)
time_flo=math.floor(time)
min=(time-time_flo)*60
min_flo=math.floor(min)
sec=(min-min_flo)*60
print(time_flo,":",int(min),":",int(sec))




