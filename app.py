#!/usr/bin/python3

# Play a chime when RPi pin 4 is pulled low (connected to ground)

import os
os.system("amixer sset PCM,0 90%")

import pygame.mixer
from gpiozero import Button

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.mixer.init()

pygame.mixer.music.load('chime.mp3')

btn = Button(4)
btn.when_pressed = pygame.mixer.music.play

import time
while True:
  time.sleep(60)
