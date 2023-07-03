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
        # self.draw_up.append(( self.x,   (-1 if self.y==self.mh-2 else 0) + self.y+1))
        self.draw_up.append(( self.x-1, (-1 if self.y==self.mh-2 else 0) + self.y+1))
        self.draw_up.append(( self.x+1, (-1 if self.y==self.mh-2 else 0) + self.y+1))
        # self.draw_up.append(( self.x-1, (-1 if self.y==self.mh-2 else 0) + self.y+2))
        # self.draw_up.append(( self.x+1, (-1 if self.y==self.mh-2 else 0) + self.y+2))
        # down
        self.draw_down.append(( self.x,   (1 if self.y==1 else 0) + self.y+1))
        self.draw_down.append(( self.x,   (1 if self.y==1 else 0) + self.y))
        self.draw_down.append(( self.x-1, (1 if self.y==1 else 0) + self.y))
        self.draw_down.append(( self.x+1, (1 if self.y==1 else 0) + self.y))
        # self.draw_down.append(( self.x,   (1 if self.y==1 else 0) + self.y-1))
        self.draw_down.append(( self.x-1, (1 if self.y==1 else 0) + self.y-1))
        self.draw_down.append(( self.x+1, (1 if self.y==1 else 0) + self.y-1))
        # self.draw_down.append(( self.x-1, (1 if self.y==1 else 0) + self.y-2))
        # self.draw_down.append(( self.x+1, (1 if self.y==1 else 0) + self.y-2))
        # left
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x-1, self.y))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x,   self.y))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x,   self.y-1))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x,   self.y+1))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+1, self.y-1))
        # self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+1, self.y))
        self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+1, self.y+1))
        # self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+2, self.y-1))
        # self.draw_left.append(( (-1 if self.x==self.mw-2 else 0) + self.x+2, self.y+1))
        # right
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x+1, self.y))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x,   self.y))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x,   self.y-1))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x,   self.y+1))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x-1, self.y-1))
        # self.draw_right.append(( (1 if self.x==1 else 0) + self.x-1, self.y))
        self.draw_right.append(( (1 if self.x==1 else 0) + self.x-1, self.y+1))
        # self.draw_right.append(( (1 if self.x==1 else 0) + self.x-2, self.y-1))
        # self.draw_right.append(( (1 if self.x==1 else 0) + self.x-2, self.y+1))
    
    def go(self, forward=1):
        # if self.x>=1 and self.x<=15 and self.y>=1 and self.y<=16:
        
        if self.direction==0 and self.y>=2:
            self.y-=forward
            self.init_sprite()

        if self.direction==1 and self.x<=self.mw-3:
            self.x+=forward
            self.init_sprite()

        if self.direction==2 and self.y<=self.mh-3:
            self.y+=forward
            self.init_sprite()

        if self.direction==3 and self.x>=2:
            self.x-=forward
            self.init_sprite()

    def get_figure(self):
        if self.direction==0:
            return self.draw_up
        if self.direction==1:
            return self.draw_right
        if self.direction==2:
            return self.draw_down
        if self.direction==3:
            return self.draw_left
        
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
    
class Block:
    def __init__(self, x, y):
        self.x=y
        self.y=y
        self.blocks=[]
    
    def show(self):
        self.blocks.append((self.x, self.y))
        self.blocks.append((self.x, self.y+1))
        self.blocks.append((self.x, self.y+2))
        self.blocks.append((self.x, self.y+3))
        self.blocks.append((self.x, self.y+4))

        return self.blocks

class Game:
    def __init__(self, w=20, h=20):
        self.w=w
        self.h=h
        self.map=[['-' for _ in range(self.w)] for _ in range(self.h)]
        self.map_clear = copy.deepcopy(self.map)
        self.run=True

        self.direction=...
        self.t1=Tank(w//2, h//2, w, h)
        self.def_image_tank=self.t1.draw_up
        self.p1=None
        self.whizzbangs=[]
        self.rule=0
        # blocks=[]
        # blocks.append(Block(0, 0))
        # blocks.append(Block(17, 0))


    def play(self):
        while self.run:
            # вперёд 
            if keyboard.is_pressed('up'):
                self.def_image_tank=self.t1.get_figure()
                self.t1.go()

            # назад
            if keyboard.is_pressed('down'):
                self.def_image_tank=self.t1.get_figure()
                self.t1.go(forward=-1)

            # поворот налево
            if keyboard.is_pressed('left'):
                self.rule-=1
                if self.rule==-1:
                    self.rule=3
                self.t1.direction=self.rule
                self.def_image_tank=self.t1.get_figure()
                # t1.move('left')

            # поворот направо
            if keyboard.is_pressed('right'):

                self.rule=(self.rule+1)%4
                self.t1.direction=self.rule
                self.def_image_tank=self.t1.get_figure() # отображение танка
                # t1.move('right') # изменение отображения танка

            if keyboard.is_pressed('space'):
                # projectile = t1.projectile
                self.whizzbangs.append(self.t1.shoot())



            # отрисовка всех точек танка на карте
            for x, y in self.def_image_tank:
                self.map[y][x]='#'
            
            # отрисовка всех преград на карте
            # for block in blocks:
            #     if block is not None:
            #         for x, y in block.show():
            #             map[y][x]='%'

            # отрисовка снаряда
            for packet in self.whizzbangs:
                if packet is not None:
                    xs, ys = packet.get_position()
                    try:

                        if xs>=0 and xs<self.w and ys>=0 and ys<self.h:
                            # for block in blocks:
                                # if block is not None:
                                    # if (xs, ys) in block.show():
                                    #     block = None
                            self.map[ys][xs]='@'
                        else:
                            packet=None
                    except Exception as e:
                        print(xs, ys)
                        print(e)



            # отрисовка карты
            for l in self.map:
                print(*l)

            self.map=copy.deepcopy(self.map_clear)
            time.sleep(0.06)
            cls()

cls=lambda: os.system('clear')


if __name__=='__main__':
    # w=20;h=20

    Game(13, 13).play()

