#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time

# B, C 모터 선언
motorB = Motor(Port.B)  # 왼쪽 바퀴
motorC = Motor(Port.C)  # 오른쪽 바퀴

# 커브
# B, C의 속도를 다르게 하여 회전
# test 상 왼쪽으로 90도 회전하며 커브
motorB.run_time(300, 3000, Stop.BRAKE, False)
motorC.run_time(450, 3000, Stop.BRAKE, True)
