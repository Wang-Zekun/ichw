#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:35:26 2018

@author: wangzekun
"""
import turtle as t
#--------------------------------------------------------------------------
#Brick Module
#--------------------------------------------------------------------------
import copy
global result
result = []

def generate(lenth,width): #Generate a lenth*width wall
    squ = []
    for w in range(width):
        lenrange = []
        for l in range(lenth):
            lenrange.append(0)
        squ.append(lenrange)
    return squ

def isvalidl(wall,x,y,brickl,brickw):
    if x+brickl > len(wall[0]) or y+brickw > len(wall):
        return False
    else:
        for w in range(brickw):
            for l in range(brickl):
                if wall[y+w][x+l] == 1:
                    return False
    return True

def isvalidw(wall,x,y,brickl,brickw):
    if x+brickw > len(wall[0]) or y+brickl > len(wall):
        return False
    else:
        for w in range(brickw):
            for l in range(brickl):
                if wall[y+l][x+w] == 1:
                    return False
    return True

def isempty(wall):
    l = len(wall[0])
    w = len(wall)
    for i in range(w):
        for j in range(l):
            if wall[i][j] == 0:
                return [j,i]
    return[None,None]
    
def transtowall(wall,ans):
    l = len(wall[0])
    w = len(wall)
    wall2 = copy.deepcopy(wall)
    for brick in ans:
        for num in brick:
            wall2[num//l][num%l]=1
    return wall2
    

def add(wall,brickl,brickw,ans):
    emptypos = isempty(wall)
    if emptypos == [None,None]:
        result.extend([ans])
    else:
        if isvalidl(wall,emptypos[0],emptypos[1],brickl,brickw) == True:
            ans2 = copy.deepcopy(ans)
            appendlist = []
            for y in range(brickw):
                for x in range(brickl):
                    wall[emptypos[1]+y][emptypos[0]+x] = 1
                    appendlist.append((emptypos[1]+y)*len(wall[0])+emptypos[0]+x)
            ans.append(tuple(appendlist))
            appendlist = []
            add(wall,brickl,brickw,ans)
            for y in range(brickw):
                for x in range(brickl):
                    wall[emptypos[1]+y][emptypos[0]+x] = 0
            ans = ans2
            
        if isvalidw(wall,emptypos[0],emptypos[1],brickl,brickw) == True and brickl != brickw :
            ans2 = copy.deepcopy(ans)
            appendlist = []
            for y in range(brickw):
                for x in range(brickl):
                    wall[emptypos[1]+x][emptypos[0]+y] = 1
                    appendlist.append((emptypos[1]+x)*len(wall[0])+emptypos[0]+y)
            ans.append(tuple(appendlist))
            appendlist = []
            add(wall,brickl,brickw,ans)
            for y in range(brickw):
                for x in range(brickl):
                    wall[emptypos[1]+x][emptypos[0]+y] = 0
            ans = ans2
        return

#--------------------------------------------------------------------------
#Turtle Module
#--------------------------------------------------------------------------
def draw(result,wall):
    l = len(wall[0])
    w = len(wall)
    d = t.Turtle()
    d.pensize(3)
    d.speed(0)
    d.shape('circle')
    for i in range(2):
        d.fd(30*l)
        d.left(90)
        d.fd(30*w)
        d.left(90)
    for bricks in result:
        for value in bricks:
            d.penup()
            d.goto(30*(value%l),30*(value//l))
            if (value-l) not in bricks:
                d.pendown()
            d.fd(30)
            d.left(90)
            d.penup()
            if (value+1) not in bricks:
                d.pendown()
            d.fd(30)
            d.left(90)
            d.penup()
            if (value+l) not in bricks:
                d.pendown()
            d.fd(30)
            d.left(90)
            d.penup()
            if (value-1) not in bricks:
                d.pendown()
            d.fd(30)
            d.left(90)
            d.penup()
    d.goto(0,0)
    d.done()


l = int(input('Insert lenth of wall: '))
w = int(input('Insert width of wall: '))
bl = int(input('Insert lenth of brick: '))
bw = int(input('Insert width of brick: '))
wall = generate(l,w)
add(wall,bl,bw,[])
for i in range(len(result)):
    print('Method'+str(i+1)+': ')
    print(result[i])
if len(result)==0:
    print('No solution to fill the wall.')
else:
    print(str(len(result)) + ' Solutions in total, which to print? ')
    method = int(input())-1
    draw(result[method],wall)   
    