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

# 반사값과 모터의 속도는 원하는 값으로 수정할 수 있다.
# 단, 모터 속도가 너무 빠르면 반사값을 측정하는 주기가 길어져서 정확도가 낮아진다.

while True:
    if color_sensor.reflection() < 30:  # 반사값이 30보다 작다면,
        motorB.run(150)  # 모터 B를 150의 속도로 동작하고
        motorC.run(0)  # 모터 C를 정지한다
    else:  # 반사값이 30 이상이라면,
        motorB.run(0)  # 모터 B를 정지하고
        motorC.run(150)  # 모터 C를 150의 속도로 동작한다
