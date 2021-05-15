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

# 초음파 센서 선언
Ultrasonic_Sensor = UltrasonicSensor(Port.S1)

while True:
    #  화면의 글자를 지우고나서, 현재 감지된 물체와의 거리를 표시한다
    brick.display.clear()
    brick.display.text(str(Ultrasonic_Sensor.distance()) + "mm")

    if Ultrasonic_Sensor.distance() >= 100:
        # 물체와의 거리가 10cm보다 길다면 직진
        motorB.run(300)
        motorC.run(300)
    else:
        DEGREE = 90 * 2
        # 시계 방향(우회전)으로 90도 회전 (포인트턴)
        motorB.run_angle(300, DEGREE, Stop.BRAKE, False)
        motorC.run_angle(300, -DEGREE, Stop.BRAKE, True)
