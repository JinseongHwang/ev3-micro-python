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

# 터치 센서 선언
touch_sensor = TouchSensor(Port.S1)

while True:
    # 터치 센서가 눌려진 상태가 False라면, 앞으로 전진한다.
    if touch_sensor.pressed() == False:
        motorB.run(200)
        motorC.run(200)

    else:  # 터치 센서가 눌려졌다면, 멈춘다.
        motorB.stop(Stop.BRAKE)
        motorC.stop(Stop.BRAKE)
