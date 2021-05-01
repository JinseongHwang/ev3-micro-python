#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time


# display size: (0, 0) ~ (177, 127)

brick.display.clear()  # 화면 초기화
brick.display.text('Hello, I\'m EV3.', (20, 50))  # 20, 50 위치에 문자열 출력
time.sleep(3)
