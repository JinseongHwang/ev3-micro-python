#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time

# heart.jpg를 화면에 출력하고, 가운데 정렬하고, 기존의 화면을 지우고 출력한다.
brick.display.image('../img/heart.jpg', Align.CENTER, clear=True)
time.sleep(3)
