""" There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get into bus (The first item) 
and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array). 
Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

LEVEL : 7kyu """

def number(bus_stops):
    cnt1=cnt2=0
    for i in bus_stops:
        cnt1+=i[0]
        cnt2+=i[1]
    return cnt1-cnt2

