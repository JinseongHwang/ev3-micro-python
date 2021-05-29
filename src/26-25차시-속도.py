#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time

# 모터 선언
motorB = Motor(Port.B)
motorC = Motor(Port.C)

# B, C 모터를 100의 속도로 4초간 직진 -> 1바퀴 회전
motorB.run_time(100, 4000, Stop.BRAKE, False)
motorC.run_time(100, 4000, Stop.BRAKE, True)
