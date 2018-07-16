from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
from flatlib.chart import Chart
from flatlib import aspects


#Variables
date = Datetime('1949/08/19', '14:49', '-06:00')
pos = GeoPos('42n40', '91w06')
chart = Chart(date, pos, IDs=const.LIST_OBJECTS, hsys=const.HOUSES_PLACIDUS)

#Houses
house1 = chart.get(const.HOUSE1)
house2 = chart.get(const.HOUSE2)
house3 = chart.get(const.HOUSE3)
house4 = chart.get(const.HOUSE4)
house5 = chart.get(const.HOUSE5)
house6 = chart.get(const.HOUSE6)
house7 = chart.get(const.HOUSE7)
house8 = chart.get(const.HOUSE8)
house9 = chart.get(const.HOUSE9)
house10 = chart.get(const.HOUSE10)
house11 = chart.get(const.HOUSE11)
house12 = chart.get(const.HOUSE12)

#Objects
sun = chart.get(const.SUN)
moon = chart.get(const.MOON)
mercury = chart.get(const.MERCURY)
venus = chart.get(const.VENUS)
mars = chart.get(const.MARS)
jupiter = chart.get(const.JUPITER)
saturn = chart.get(const.SATURN)
uranus = chart.get(const.URANUS)
neptune = chart.get(const.NEPTUNE)
pluto = chart.get(const.PLUTO)
asc = chart.get(const.ASC)
mc = chart.get(const.MC)

# Finally create the chart
print ("\n------------------------------------------")
print ("Printing Chart...\n")

print ("Date: ", date)
print ("Location: ", pos)

print (asc)
print (mc)

print ("\n------------------------------------------\n")

def HousePrint():
    for obj in chart.objects:
        if house1.hasObject(obj):
            print(obj, " First House")
        if house2.hasObject(obj):
            print(obj, " Second House")
        if house3.hasObject(obj):
            print(obj, " Third House")
        if house4.hasObject(obj):
            print(obj, " Fourth House")
        if house5.hasObject(obj):
            print(obj, " Fifth House")
        if house6.hasObject(obj):
            print(obj, " Sixth House")
        if house7.hasObject(obj):
            print(obj, " Seventh House")
        if house8.hasObject(obj):
            print(obj, " Eighth House")
        if house9.hasObject(obj):
            print(obj, " Ninth House")
        if house10.hasObject(obj):
            print(obj, " Tenth House")
        if house11.hasObject(obj):
            print(obj, " Eleventh House")
        if house12.hasObject(obj):
            print(obj, " Twelfth House")

def AspectPrint():
    for obj1 in chart.objects:
        for obj2 in chart.objects:
            if aspects.hasAspect(obj1, obj2, const.ALL_ASPECTS):
                print (obj1, aspects.aspectType(obj1, obj2, const.ALL_ASPECTS),obj2)

HousePrint()
print ("\n------------------------------------------\n")
AspectPrint()






#ToDo
    #Print Object data and house data at once
    #for obj in chart.objects:
    #    house = chart.houses.getObjectHouse(obj)
    #    print (obj, house)


    #Prints House Coordinates
    #for obj in chart.objects:
        #print(chart.houses.getObjectHouse(obj))
