from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
import matplotlib.pyplot as plt
import random

temp = [30,29,28,32,30,31,31,30,29,29]
humidity = [70,75,70,73,72,68,69,70,72,73]

def alert(request):
    x = open('assets/data.txt')
    y = x.read()
    x.close()
    return render(request, 'alert.html',{"temp":y[0],"hum":y[1],"light":y[2],"fan":y[3],"ultra":y[4]})

def cam(request):
    return render(request,'cam.html')

def term(request):
    x= [1,2,3,4,5,6,7,8,9,10]
    for i in range(1,len(temp)):
        temp[i-1] = temp[i]
        humidity[i-1] = humidity[i]
    temp[9] = random.sample(range(27,33),1)[0]
    humidity[9] = random.sample(range(70,75),1)[0]
    plt.plot(x,temp)
    plt.savefig('assets/images/temp.jpg')
    plt.close()
    plt.plot(x,humidity)
    plt.savefig('assets/images/hum.jpg')
    plt.close()
    return render(request, 'term.html')