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
color_sensor1 = ColorSensor(Port.S1)
color_sensor2 = ColorSensor(Port.S2)

DEGREE = 45 * 4

while True:
    motorB.run(300)
    motorC.run(300)

    if color_sensor1.reflection() < 15:
        # 시계방향으로 포인트턴
        motorB.run_angle(300, DEGREE / 2, Stop.BRAKE, False)
        motorC.run_angle(300, -DEGREE / 2, Stop.BRAKE, True)

    if color_sensor2.reflection() < 15:
        # 반시계방향으로 포인트턴
        motorB.run_angle(300, -DEGREE / 2, Stop.BRAKE, False)
        motorC.run_angle(300, DEGREE / 2, Stop.BRAKE, True)
