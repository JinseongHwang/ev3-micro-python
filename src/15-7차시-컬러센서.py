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

# N번째 검은 선에서 멈춘다.
N = 3

# 반복문
for count in range(N):
    motorB.run(300)
    motorC.run(300)

    # 반사값이 15보다 작으면 while 종료
    while True:
        if color_sensor.reflection() < 15:
            break

    brick.sound.beep()

# 모터 정지
motorB.stop(Stop.BRAKE)
motorC.stop(Stop.BRAKE)
