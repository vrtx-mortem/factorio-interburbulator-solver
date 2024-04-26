#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import sys

class Vector:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, b: Vector) -> Vector:
        vec = Vector(self.x, self.y, self.z)
        vec.x += b.x
        vec.y += b.y
        vec.z += b.z
        return vec

    def __sub__(self, b: Vector) -> Vector:
        return self.__add__(-b)

    def __mul__(self, b: float) -> Vector:
        vec = Vector(self.x, self.y, self.z)
        vec.x *= b
        vec.y *= b
        vec.z *= b
        return vec

    def __truediv__(self, b: float) -> Vector:
        return self.__mul__(1/b)

    def __str__(self) -> str:
        return f'{self.x:.8f}\t{self.y:.8f}\t{self.z:.8f}'

def solve(
    grid_size: int,
    target: list[float, float], # y, x
    top_left: Vector,
    bottom_left: Vector,
    top_right: Vector,
) -> Vector:
    x = bottom_left - top_left
    y = top_right - top_left
    
    xp = (target[1] - 0.5) / grid_size
    yp = (target[0] - 0.5) / grid_size

    return x * xp + y * yp + top_left

def interactive() -> None:
    def ask(prompt: str) -> list:
        return [float(_) for _ in input(prompt).strip().replace(' ', '').split(',')]
    try:
        grid_size = ask('Grid size: ')
        target = ask('Target cell: ')
        top_left = ask('Top left (x,y,z): ')
        bottom_left = ask('Bottom left (x,y,z): ')
        top_right = ask('Top right (x,y,z): ')

        grid_size = int(grid_size[0])
        assert(grid_size > 0)
        target = [int(_) for _ in target]
        top_left = Vector(*top_left)
        bottom_left = Vector(*bottom_left)
        top_right = Vector(*top_right)
        answer = solve(grid_size, target, top_left, bottom_left, top_right)
        print(answer)
    except KeyboardInterrupt:
        return
    except:
        print('Wrong input')

def main() -> None:
    if len(sys.argv) < 2:
        interactive()
        return
    if sys.argv[1] != 'lazy':
        print(':)')
        return
    # factorio/mods/space-exploration_0.6.128.zip/scripts/interburbulator.lua
    challenges = {
        1: {'grid_size':3, 'target':[2, 2], 'top_left':Vector(1, 0, 0), 'top_right':Vector(1, 1, 0), 'bottom_left':Vector(1, 0, 1)},
        2: {'grid_size':4, 'target':[2, 3], 'top_left':Vector(1, 0, 0), 'top_right':Vector(0, 1, 0), 'bottom_left':Vector(0, 0, 1)},
        3: {'grid_size':5, 'target':[3, 1], 'top_left':Vector(1, 1, 1), 'top_right':Vector(0, 1, 0), 'bottom_left':Vector(0, 0, 1)},
        4: {'grid_size':6, 'target':[4, 4], 'top_left':Vector(-1, 0, 0), 'top_right':Vector(0, 1, 0), 'bottom_left':Vector(0, 0, 1)},
        5: {'grid_size':7, 'target':[2, 4], 'top_left':Vector(1, 0, 0), 'top_right':Vector(0, 2, 0), 'bottom_left':Vector(0, 0, 7)},
        6: {'grid_size':8, 'target':[7, 7], 'top_left':Vector(1, 6, 1), 'top_right':Vector(8, 0, 3), 'bottom_left':Vector(3, 9, 8)},
        7: {'grid_size':10, 'target':[3, 6], 'top_left':Vector(0.1, 0.6, 0.1), 'top_right':Vector(0.8, -0.1, 0.3), 'bottom_left':Vector(0.3, 0.9, 0.8)},
        8: {'grid_size':15, 'target':[13, 15], 'top_left':Vector(0.87, 0.49, 0.89), 'top_right':Vector(0.48, 0.48, 0.2), 'bottom_left':Vector(0.45, 0.86, 0.83)},
        9: {'grid_size':20, 'target':[17, 2], 'top_left':Vector(-436, 563, -811), 'top_right':Vector(772, 30, 917), 'bottom_left':Vector(980, 576, 286)},
        10:{'grid_size':50, 'target':[33, 44], 'top_left':Vector(1.618033, 0.9887498, 0.48204586), 'top_right':Vector(2.414213, 0.5623730, 0.9504880), 'bottom_left':Vector(3.302775, 0.6377319, 0.9464655)},
    }
    for number, burbul in challenges.items():
        answer = solve(
            burbul['grid_size'], burbul['target'], burbul['top_left'], burbul['bottom_left'], burbul['top_right']
        )
        print(f'{number:2d}\t{answer}')

if __name__ == '__main__':
    main()
