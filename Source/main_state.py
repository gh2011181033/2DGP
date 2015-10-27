import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

marco = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('image\\background_1.png')

    def draw(self):
        self.image.draw(400, 300)



class Marco:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.state = "Stand"
        self.image = load_image('image\\Marco.png')
        self.image_2 = load_image('image\\M_running.png')
        self.image_3 = load_image('image\\M_running_2.png')
        self.image_4 = load_image('image\\Marco_2.png')

    def update(self):
        if self.state == "Stand":
            self.frame = (self.frame + 1) % 3
        elif self.state == "Stand_2":
            frame = 0
            self.frame = (self.frame +1) % 3
        elif self.state =="Run":
            frame = 0
            self.frame = (self.frame + 1) % 11
        elif self.state =="Run_2":
            frame = 0
            self.frame = (self.frame + 1) % 11
        elif self.state == "Stand" and self.x <=800:
            self.state = "Run"
        elif self.state == "Stand_2" and self.x <=800:
            self.state + "Run_2"




        #self.frame = (self.frame + 1) % 11
        #self.x += self.dir
        #if self.x >= 800:
        #    self.dir = -1
        #elif self.x <= 0:
        #    self.dir = 1

    def draw(self):
        if self.state == "Stand":
            self.dir = 1
            self.image.clip_draw(self.frame * 100, 0, 104, 124, self.x, 80)
        elif self.state == "Run":
            if self.dir == 1:
                self.x += 0.5
                self.image_2.clip_draw(self.frame * 200, 0, 95, 124, self.x, self.y)
        elif self.state == "Stand_2":
            self.dir = -1
            self.image_4.clip_draw(self.frame * 100, 0, 104, 124, self.x, 80)
        elif self.state == "Run_2":
            if self.dir == -1:
                self.x -=0.5
                self.image_3.clip_draw(self.frame * 200, 0, 93, 124, self.x, self.y)




def enter():
    global marco, grass
    marco = Marco()
    grass = Grass()


def exit():
    global marco, grass
    del(marco)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global marco
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                marco.state = "Stand"
            elif event.key == SDLK_LEFT:
                marco.state = "Stand_2"

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_RIGHT:
                marco.state = "Run"
            elif event.key == SDLK_LEFT:
                marco.state = "Run_2"



def update():
    marco.update()

def draw():
    clear_canvas()
    grass.draw()
    marco.draw()
    update_canvas()






