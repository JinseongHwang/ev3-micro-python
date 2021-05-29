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

# 컬러 센서 선언
color_sensor = ColorSensor(Port.S1)

while True:
    # color_sensor.ambient() 는 주변광의 값을 측정해서 '%'로 반환합니다.
    if color_sensor.ambient() < 20:  # 20보다 작다면(어둡다면)
        motorB.run(100)  # 시계 방향으로 회전하며 밝은 곳을 찾는다.
        motorC.run(-100)
    else:  # 20보다 밝은 곳을 찾았다면
        motorB.run(200)  # 직진한다.
        motorC.run(200)
