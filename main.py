import os
# import pyautogui as pag # emitate keys or mouse
# import pygame # listen gui keys
import time
import keyboard # listen keys
import random 
import itertools
import copy
import sys
import logging



class Map:
    def __init__(self, w=20, h=20):
        self.w=w
        self.h=h
        self.badge='.'
        self.battlefield=[[self.badge]*self.w for _ in range(self.h)]
        # self.battlefield_clear=list(self.battlefield)
        self.battlefield_clear=copy.deepcopy(self.battlefield)

    def show(self)->...:
        for l in self.battlefield:
            print(*l)

    def update(self)->...:
        # self.battlefield=list(self.battlefield_clear)
        self.battlefield=copy.deepcopy(self.battlefield_clear)

    def get(self)->list[list]:
        return self.battlefield


class Projectile:
    def __init__(self, map:Map, direction, x:int, y:int):
        self.direction=direction
        self.x=x
        self.y=y
        self.map=map
        self.start_speed=2
    
    def get_position(self):
        if self.direction==0: 
            self.y-=1+self.start_speed
        if self.direction==1: 
            self.x+=1+self.start_speed
        if self.direction==2: 
            self.y+=1+self.start_speed
        if self.direction==3: 
            self.x-=1+self.start_speed
        
        self.start_speed=0
        


        return self.x, self.y

    def __del__(self):
        logging.debug('снаряд унечтожен')


class Block:
    def __init__(self, map:Map, x:int, y:int):
        self.x=x
        self.y=y
        self.blocks = [
            ((self.x, self.y)),
            ((self.x, self.y+1)),
            ((self.x, self.y+2)),
            ((self.x, self.y+3)),
            ((self.x, self.y+4)),
            ((self.x, self.y+5)),
            ((self.x, self.y+6)),
            ((self.x, self.y+7)),
            ((self.x, self.y+8)),
        ]
        self.map=map

    def draw(self):
        for x, y in self.blocks:
            self.map.battlefield[y][x]='%'

        



class Tank:
    def __init__(self, map: Map, position: tuple, block: Block):
        self.map=map
        self.block=block
        self.x,self.y=position
        
        self.mw=self.map.w
        self.mh=self.map.h

        self.direction=0

        self.init_sprite()
        self.angle=0

        self.health=10

        self.f1i=...
        self.f2i=...
        self.r1i=...

    def init_sprite(self):
        # up
        self.draw_up=[
            (( self.x,   self.y-1)),
            (( self.x,   self.y)),
            (( self.x-1, self.y)),
            (( self.x+1, self.y)),
            (( self.x-1, self.y+1)),
            (( self.x+1, self.y+1))
        ]
        # down
        self.draw_down=[
            (( self.x,   self.y+1)),
            (( self.x,   self.y)),
            (( self.x-1, self.y)),
            (( self.x+1, self.y)),
            (( self.x-1, self.y-1)),
            (( self.x+1, self.y-1))
        ]
        # left
        self.draw_left=[
            (( self.x-1, self.y)),
            (( self.x,   self.y)),
            (( self.x,   self.y-1)),
            (( self.x,   self.y+1)),
            (( self.x+1, self.y-1)),
            (( self.x+1, self.y+1))
        ]
        # right
        self.draw_right=[
            (( self.x+1, self.y)),
            (( self.x,   self.y)),
            (( self.x,   self.y-1)),
            (( self.x,   self.y+1)),
            (( self.x-1, self.y-1)),
            (( self.x-1, self.y+1))
        ]
    
    def get_info(self):
        if self.angle==0:
            # self.f1i=f'({self.y-1}, {self.x-1}):{self.map.battlefield[self.y-1][self.x-1]}'
            # self.f2i=f'({self.y-1}, {self.x+1}):{self.map.battlefield[self.y-1][self.x+1]}'
            # self.r1i=f'({self.y+1}, {self.x})  :{self.map.battlefield[self.y+1][self.x]}'

            self.f1i=self.map.battlefield[self.y-1][self.x-1]
            self.f2i=self.map.battlefield[self.y-1][self.x+1]
            self.r1i=self.map.battlefield[self.y+1][self.x]

        elif self.angle==1:
            # self.f1i=f'({self.y-1}, {self.x+1}):{self.map.battlefield[self.y-1][self.x+1]}'
            # self.f2i=f'({self.y+1}, {self.x+1}):{self.map.battlefield[self.y+1][self.x+1]}'
            # self.r1i=f'({self.y}, {self.x-1})  :{self.map.battlefield[self.y][self.x-1]}'

            self.f1i=self.map.battlefield[self.y-1][self.x+1]
            self.f2i=self.map.battlefield[self.y+1][self.x+1]
            self.r1i=self.map.battlefield[self.y][self.x-1]

        elif self.angle==2:
            # self.f1i=f'({self.y+1}, {self.x-1}):{self.map.battlefield[self.y+1][self.x-1]}'
            # self.f2i=f'({self.y+1}, {self.x+1}):{self.map.battlefield[self.y+1][self.x+1]}'
            # self.r1i=f'({self.y-1}, {self.x})  :{self.map.battlefield[self.y-1][self.x]}'

            self.f1i=self.map.battlefield[self.y+1][self.x-1]
            self.f2i=self.map.battlefield[self.y+1][self.x+1]
            self.r1i=self.map.battlefield[self.y-1][self.x]

        else:
            # self.f1i=f'({self.y-1}, {self.x-1}):{self.map.battlefield[self.y-1][self.x-1]}'
            # self.f2i=f'({self.y+1}, {self.x-1}):{self.map.battlefield[self.y+1][self.x-1]}'
            # self.r1i=f'({self.y}, {self.x+1})  :{self.map.battlefield[self.y][self.x+1]}'

            self.f1i=self.map.battlefield[self.y-1][self.x-1]
            self.f2i=self.map.battlefield[self.y+1][self.x-1]
            self.r1i=self.map.battlefield[self.y][self.x+1]

    def left(self):
        if self.f1i=='.' and self.f2i=='.' and self.r1i=='.': #нет ли каких-либо ограничений для поворота
            self.angle-=1
            if self.angle==-1:
                self.angle=3
            
            self.get_info() # при повороте обновляем данные
            self.direction=self.angle

    def right(self):
        if self.f1i=='.' and self.f2i=='.' and self.r1i=='.':
            self.angle=(self.angle+1)%4
            self.get_info()
            self.direction=self.angle

    def go(self, forward:int=1): # педаль газа
        # if self.x>=1 and self.x<=15 and self.y>=1 and self.y<=16:
        # if forward==-1:
        #     logging.debug(f'{self.x}, {self.y}')
        if self.direction==0: # перед к северу
            logging.debug('перед к северу')
            if forward>0:
                logging.debug('north')
                if self.y>=2 and self.map.battlefield[self.y-2][self.x]=='.' and self.map.battlefield[self.y-1][self.x-1]=='.' and self.map.battlefield[self.y-1][self.x+1]=='.': # and (self.x, self.y-2) not in self.block.blocks and (self.x-1, self.y-2) not in self.block.blocks and (self.x+1, self.y-2) not in self.block.blocks: 
                    # self.y<self.mh-2:
                    self.y-=forward
                    self.init_sprite()
            else:
                logging.debug('south')
                if self.y<self.mh-2 and self.map.battlefield[self.y+1][self.x]=='.' and self.map.battlefield[self.y+2][self.x-1]=='.' and self.map.battlefield[self.y+2][self.x+1]=='.': # and (self.x, self.y) not in self.block.blocks: # and (self.x-1, self.y) not in self.block.blocks and (self.x+1, self.y) not in self.block.blocks:
                    self.y-=forward
                    self.init_sprite()

        if self.direction==1:
            logging.debug('перед к востоку')
            if forward>0:
                logging.debug('east')
                if self.x<self.mw-2 and self.map.battlefield[self.y][self.x+2]=='.' and self.map.battlefield[self.y-1][self.x+1]=='.' and self.map.battlefield[self.y+1][self.x+1]=='.':
                    self.x+=forward
                    self.init_sprite()
            else:
                logging.debug('west')
                if self.x>=2 and self.map.battlefield[self.y][self.x-1]=='.' and self.map.battlefield[self.y-1][self.x-2]=='.' and self.map.battlefield[self.y+1][self.x-2]=='.':
                    self.x+=forward
                    self.init_sprite()

        if self.direction==2: # перед к югу
            logging.debug('перед к югу')
            if forward>0: # движение вперед
                logging.debug('south')
                if self.y<self.mh-2 and self.map.battlefield[self.y+2][self.x]=='.' and self.map.battlefield[self.y+1][self.x-1]=='.' and self.map.battlefield[self.y+1][self.x+1]=='.':
                    self.y+=forward
                    self.init_sprite()

            else: # движение назад
                logging.debug('north')
                if self.y>=2 and self.map.battlefield[self.y-1][self.x]=='.' and self.map.battlefield[self.y-2][self.x-1]=='.' and self.map.battlefield[self.y-2][self.x+1]=='.': # and (self.x, self.y) not in self.block.blocks and (self.x-1, self.y) not in self.block.blocks and (self.x+1, self.y) not in self.block.blocks:
                    self.y+=forward
                    self.init_sprite()


        if self.direction==3:
            logging.debug('перед к западу')
            if forward > 0:
                logging.debug('west')
                if self.x>=2 and self.map.battlefield[self.y][self.x-2]=='.' and self.map.battlefield[self.y-1][self.x-1]=='.' and self.map.battlefield[self.y+1][self.x-1]=='.':
                    self.x-=forward
                    self.init_sprite() # отрисовать заново все спрайты с учётом новых координат
            else:
                logging.debug('east')
                if self.x<self.mw-2 and self.map.battlefield[self.y][self.x+1]=='.' and self.map.battlefield[self.y-1][self.x+2]=='.' and self.map.battlefield[self.y+1][self.x+2]=='.':
                    self.x-=forward
                    self.init_sprite()
        
        self.get_info()

    def get_figure(self):
        if self.direction==0:
            return self.draw_up
        if self.direction==1:
            return self.draw_right
        if self.direction==2:
            return self.draw_down
        if self.direction==3:
            return self.draw_left
        
    def draw(self):
        for x, y in self.get_figure():
            self.map.battlefield[y][x]='#'

    def shoot(self):
        return Projectile(self.map, self.direction, self.x, self.y)
        # return self.x, self.y, self.direction # возвращаем позицию выстрела и направление

    def __del__(self):
        logging.debug('Убит')
        # sys.exit()


class Bot(Tank):
    def __init__(self, map:Map, position:tuple[int,int], block:Block, whizzbang:list):
        super().__init__(map, position, block)
        self.get_info()
        self.whizzbang=whizzbang
        
    
    def vision(self):
        ...
    
    def autopilot(self):
        self.left()
        # self.whizzbang.append(self.shoot())
        self.go()
    
    def draw(self):
        self.autopilot()
        super().draw()




    



class Game:
    def __init__(self):
        self.map=Map(30, 30)
        self.b1=Block(self.map, 10, 0)
        self.player=Tank(self.map, (self.map.w//2, self.map.h//2), self.b1)

        self.player.get_info() # получаем данные об окружении
        self.flameshots=[]
        self.enemies=[
            Bot(self.map, (1,4), self.b1, self.flameshots),
            # Tank(self.map, (self.map.w-2,4), self.b1)
        ]
        self.enemies[0].direction=2



        self.FPS=20
        self.run=True

    def play(self):
        while self.run:
            # отрисовка преград
            self.b1.draw()

            for enemy in self.enemies:
                if enemy is not None: enemy.draw()

            # вперёд 
            if keyboard.is_pressed('up'):
                self.player.go(forward=1)
            
            # назад
            if keyboard.is_pressed('down'):
                self.player.go(forward=-1)

            # поворот влево
            if keyboard.is_pressed('left'):
                self.player.left()
                # self.flameshots.append(self.enemies[0].shoot())

            # поворот вправо
            if keyboard.is_pressed('right'):
                self.player.right()

            if keyboard.is_pressed('space'):
                # projectile = t1.projectile
                self.flameshots.append(self.player.shoot())





            # отрисовка всех точек танка на карте
            self.player.draw()



            # отрисовка снаряда
            for i in range(len(self.flameshots)):
                if self.flameshots[i] is not None:
                    xs, ys = self.flameshots[i].get_position()
                    if xs>=0 and xs<self.map.w and ys>=0 and ys<self.map.h:
                        if self.map.battlefield[ys][xs]=='%':
                            #self.map.battlefield[ys][xs]='.'
                            logging.warning(f'{self.b1.blocks}')
                            logging.warning(f'ys: {ys}, xs: {xs}')
                            # sys.exit()
                            self.b1.blocks.remove((xs, ys))
                            self.flameshots[i]=None
                            break
                        elif self.map.battlefield[ys][xs]=='#':
                            # self.b1.blocks.remove((xs, ys))


                            for k in range(len(self.enemies)):
                                if self.enemies[k] is not None:
                                    if (xs,ys) in self.enemies[k].get_figure():
                                        self.enemies[k].health-=1
                                        if self.enemies[k].health==0:
                                            self.enemies.remove(self.enemies[k])
                                        break
                            
                            logging.warning(f'ys: {ys}, xs: {xs}')
                            self.flameshots[i]=None
                            break
                        else:
                            self.map.battlefield[ys][xs]='@'
                    else:
                        self.flameshots[i]=None




            # отрисовка карты
            self.map.show()
            logging.debug(f'{self.player.x}, {self.player.y}, {self.b1.blocks}, {self.player.direction}')
            logging.debug(f'{self.player.angle}, {self.player.f1i}, {self.player.f2i}, {self.player.r1i}')
            # logging.warning(f'{self.t2.get_figure() if self.t2 is not None else "death"}')
            # self.map=copy.deepcopy(self.map_clear)
            self.map.update()
            time.sleep(1/self.FPS)
            cls()

cls=lambda: os.system('clear')


if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    Game().play()

