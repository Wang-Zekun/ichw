#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 17:51:30 2018

@author: wangzekun
"""

import turtle
import math 

def CreatePlanet(name,size,posx,color):
    name = turtle.Turtle()
    name.speed(0)
    name.color(color)
    name.shape("circle")
    name.shapesize(size,size,1)
    name.penup()
    name.goto(posx,0)
    name.pendown()
    return name

def Movement(name,a,b,deg,speed,delta):
        x = a * math.cos(10*3.14159265359*deg/speed/360) + delta
        y = b * math.sin(10*3.14159265359*deg/speed/360)
        name.goto(x,y)

def main():
    Sun = turtle.Turtle()
    Mer = turtle.Turtle()
    Ven = turtle.Turtle()
    Ear = turtle.Turtle()
    Mar = turtle.Turtle()
    Jup = turtle.Turtle()
    Sat = turtle.Turtle()
    Ura = turtle.Turtle()
    Nep = turtle.Turtle()
    
    Sun = CreatePlanet(Sun,1,0,"red")
    Mer = CreatePlanet(Mer,0.2,27,"grey")
    Ven = CreatePlanet(Ven,0.6,36,"gold")
    Ear = CreatePlanet(Ear,0.64,53,"green")
    Mar = CreatePlanet(Mar,0.36,76.4,"orange")
    Jup = CreatePlanet(Jup,1.78,114.1,"brown")
    Sat = CreatePlanet(Sat,1.50,210,"khaki")
    Ura = CreatePlanet(Ura,1.00,281,"azure")
    Nep = CreatePlanet(Nep,0.95,324,"blue")
    
    
    for times in range(1000):
        for deg in range(3600):
            Movement(Mer,19.5,18,deg,0.24,7.5)
            Movement(Ven,36,36,deg,0.62,0)
            Movement(Ear,50,50,deg,1,3)
            Movement(Mar,65,64,deg,1.88,11.4)
            Movement(Jup,100,99,deg,2.98,14.1)
            Movement(Sat,183,181,deg,7.35,27)
            Movement(Ura,243,240,deg,10.5,38)
            Movement(Nep,300,299,deg,20.0,24)
    
if __name__=="__main__":
    main()
