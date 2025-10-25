import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between",startDate,"and",endDate)
    randomGenerator=random.random()
    dateFormat ='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startDate,dateFormat))
    endtime=time.mktime(time.strptime(endDate,dateFormat))
    randomtime=starttime+randomGenerator*(endtime-starttime)
    RandomDate=time.strftime(dateFormat,time.localtime(randomtime))
    time.localtime(randomtime)
    return RandomDate
    print("Random date =",getRandomDate("1/1/20",12/12/2024)) 