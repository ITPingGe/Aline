#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys

from ship import Ship

def run_blue_sky():
    pygame.init()
    screen = pygame.display.set_mode((500, 550))
    pygame.display.set_caption("Blue Sky")
    bg_color = (230, 230, 230)
    ship = Ship(screen)

    while True:
        for evert in pygame.event.get():
            if evert.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()       # 让绘制在屏幕上可见

run_blue_sky()