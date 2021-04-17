#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time

# B, C 모터 선언
motorB = Motor(Port.B)
motorC = Motor(Port.C)

# B, C 모터를 300의 속도로 2초(2,000ms)간 앞으로 전진
# 4번째 인자;
# True: 하나씩 실제로 동작함
# False: 동시에 동작하기 위해 True 인자를 가진 함수가 나올 때까지 대기 후 함께 실행
motorB.run_time(300, 2000, Stop.BRAKE, False)
motorC.run_time(300, 2000, Stop.BRAKE, True)
