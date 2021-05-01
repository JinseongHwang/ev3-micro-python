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

# 직진
# B, C 모터를 300의 속도로 3초(3,000ms)간 회전
motorB.run_time(300, 3000, Stop.BRAKE, False)
motorC.run_time(300, 3000, Stop.BRAKE, True)
