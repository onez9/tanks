import os
# import pyautogui as pag # emitate keys or mouse
# import pygame # listen gui keys
import time
import keyboard # listen keys
import random 
import itertools
import copy
import sys

class Tank:
    def __init__(self, x, y, mw, mh):
        self.x=x
        self.y=y
        
        self.mw=mw
        self.mh=mh

        self.x_projectile=x
        self.y_projectile=y

        self.direction=0

        self.init_sprite()

    def init_sprite(self):
        self.projectile=[]

        self.projectile.append((self.x_projectile, self.y_projectile)) # начальное положение снаряда

        self.draw_up=[]
        self.draw_down=[]
        self.draw_left=[]
        self.draw_right=[]

        # up
        self.draw_up.append(( self.x,   (-1 if self.y==self.mh-2 else 0) + self.y-1))
        self.draw_up.append(( self.x,   (-1 if self.y==self.mh-2 else 0) + self.y))
        self.draw_up.append(( self.x-1, (-1 if self.y==self.mh-2 else 0) + self.y))
        self.draw_up.append(( self.x+1, (-1 if self.y==self.mh-2 else 0) + self.y))
        self.draw_up.append(( self.x,   (-1 if self.y==self.mh-2 else 0) + self.y+1))
        self.draw_up.append(( self.x-1, (-1 if self.y==self.mh-2 else 0) + self.y+1))
        self.draw_up.append(( self.x+1, (-1 if self.y==self.mh-2 else 0) + self.y+1))
        self.draw_up.append(( self.x-1, (-1 if self.y==self.mh-2 else 0) + self.y+2))
        self.draw_up.append(( self.x+1, (-1 if self.y==self.mh-2 else 0) + self.y+2))
        # down
        self.draw_down.append(( self.x,   (1 if self.y==1 else 0) + self.y+1))
        self.draw_down.append(( self.x,   (1 if self.y==1 else 0) + self.y))
        self.draw_down.append(( self.x-1, (1 if self.y==1 else 0) + self.y))
        self.draw_down.append(( self.x+1, (1 if self.y==1 else 0) + self.y))
        self.draw_down.append(( self.x,   (1 if self.y==1 else 0) + self.y-1))
        self.draw_down.append(( self.x-1, (1 if self.y==1 else 0) + self.y-1))
        self.draw_down.append(( self.x+1, (1 if self.y==1 else 0) + self.y-1))
        self.draw_down.append(( self.x-1, (1 if self.y==1 else 0) + self.y-2))
        self.draw_down.append(( self.x+1, (1 if self.y==1 else 0) + self.y-2))
        # left
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x-1, self.y))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x,   self.y))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x,   self.y-1))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x,   self.y+1))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+1, self.y-1))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+1, self.y))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+1, self.y+1))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+2, self.y-1))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+2, self.y+1))
        # right
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x+1, self.y))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x,   self.y))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x,   self.y-1))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x,   self.y+1))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x-1, self.y-1))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x-1, self.y))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x-1, self.y+1))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x-2, self.y-1))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x-2, self.y+1))
    
    def go(self):
        # if self.x>=1 and self.x<=15 and self.y>=1 and self.y<=16:
        
        if self.direction==0 and self.y>=2:
            self.y-=1
            self.init_sprite()

        if self.direction==1 and self.x<=self.mw-3:
            self.x+=1
            self.init_sprite()

        if self.direction==2 and self.y<=self.mh-3:
            self.y+=1
            self.init_sprite()

        if self.direction==3 and self.x>=2:
            self.x-=1
            self.init_sprite()



    def shoot(self):
        return Projectile(self.direction, self.x, self.y)
        # return self.x, self.y, self.direction # возвращаем позицию выстрела и направление

class Projectile:
    def __init__(self, direction, x, y):
        self.direction=direction
        self.x=x
        self.y=y
    
    def get_position(self):
        if self.direction==0: self.y-=1
        if self.direction==1: self.x+=1
        if self.direction==2: self.y+=1
        if self.direction==3: self.x-=1

        return self.x, self.y
    
    


cls=lambda: os.system('clear')


if __name__=='__main__':
    w=40;h=40

    map=[['-' for _ in range(w)] for _ in range(h)]

    map_clear = copy.deepcopy(map)
    x_shoot=...
    y_shoot=...
    direction=...
    t1=Tank(w//2, h//2, w, h)
    my_tank=t1.draw_up
    play = True
    p1=None
    whizzbangs=[]
    rule=0
    # try:
    while play:

        if keyboard.is_pressed('up'):
            my_tank=t1.draw_up
            t1.go()

        if keyboard.is_pressed('down'):
            my_tank=t1.draw_down
            # t1.move('down')

        if keyboard.is_pressed('left'):
            my_tank=t1.draw_left
            rule-=1
            if rule==-1:
                rule=3
            t1.direction=rule
            # t1.move('left')

        if keyboard.is_pressed('right'):
            my_tank=t1.draw_right # отображение танка
            rule=(rule+1)%3
            t1.direction=rule
            # t1.move('right') # изменение отображения танка

        if keyboard.is_pressed('space'):
            # projectile = t1.projectile
            whizzbangs.append(t1.shoot())



        # отрисовка всех точек танка на карте
        for x, y in my_tank:
            map[y][x]='#'
        
        # отрисовка снаряда
        for packet in whizzbangs:
            if packet is not None:
                xs, ys = packet.get_position()
                try:

                    if (xs>=0 and xs<w and ys>=0 and ys<h):
                        map[ys][xs]='@'
                    else:
                        packet=None
                except Exception as e:
                    print(xs, ys)
                    print(e)



        # отрисовка карты
        for l in map:
            print(*l)

        map=copy.deepcopy(map_clear)
        time.sleep(0.06)
        cls()
    # except Exception as e:
    #     ...
    #     print(e)
