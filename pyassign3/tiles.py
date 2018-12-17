#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:35:26 2018

@author: wangzekun
"""

import turtle as t
import copy

#--------------------------------------------------------------------------
#Brick Module
#--------------------------------------------------------------------------


global result
result = []


def generate(lenth,width): #生成一个长为lenth，宽为width的墙
    squ = []
    for w in range(width):
        lenrange = []
        for l in range(lenth):
            lenrange.append(0)
        squ.append(lenrange)
    return squ


def isvalidl(wall,x,y,brickl,brickw): #判断对于wall的x,y位置能否横铺长为brickl，宽为brickw的砖
    if x+brickl > len(wall[0]) or y+brickw > len(wall):
        return False
    else:
        for w in range(brickw):
            for l in range(brickl):
                if wall[y+w][x+l] == 1:
                    return False
    return True


def isvalidw(wall,x,y,brickl,brickw): #判断对于wall的x,y位置能否纵铺长为brickl，宽为brickw的砖
    if x+brickw > len(wall[0]) or y+brickl > len(wall):
        return False
    else:
        for w in range(brickw):
            for l in range(brickl):
                if wall[y+l][x+w] == 1:
                    return False
    return True


def isempty(wall): #返回墙的第一个空白位置，如果全部铺满则返回[None,None]
    l = len(wall[0])
    w = len(wall)
    for i in range(w):
        for j in range(l):
            if wall[i][j] == 0:
                return [j,i]
    return[None,None]
    
    
def add(wall,brickl,brickw,ans): #铺砖的函数，在事先定义好的二维列表墙wall上铺长为brickl，宽为brickw的砖
    emptypos = isempty(wall) #返回墙的第一个空位
    if emptypos == [None,None]: #如果墙全部铺满则在结果列表result中加上这块砖的格子
        result.extend([ans])
    else:
        if isvalidl(wall,emptypos[0],emptypos[1],brickl,brickw) == True: #对于竖着铺的递归
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
            #对于横着铺的递归，这里加上了砖的长宽不等，这样可以在运算过程中避免重复
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
def draw(result,wall): #对于定义好的墙wall，将result表示的方案可视化
    l = len(wall[0])
    w = len(wall)
    d = t.Turtle()
    d.pensize(3)
    d.speed(0)
    d.shape('circle')
    #定义turtle
    for i in range(2): #画出墙的框架
        d.fd(30*l)
        d.left(90)
        d.fd(30*w)
        d.left(90)
    for bricks in result: 
        #对于每一格分别判断这个格子的四个边是否在砖块内，如果在砖块内，这条边就不画，否则会画出
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






def main(): #主函数
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
    
    
if __name__ == '__main__':
    main()