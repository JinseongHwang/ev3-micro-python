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

# 초음파 센서 선언
Ultrasonic_Sensor = UltrasonicSensor(Port.S1)

while True:
    # 현재 감지된 물체와의 거리를 Display
    brick.display.text(str(Ultrasonic_Sensor.distance()) + "mm")
    if Ultrasonic_Sensor.distance() >= 100:
        # 물체와의 거리가 10cm보다 길다면 직진
        motorB.run(300)
        motorC.run(300)
    else:
        # 물체와의 거리가 10cm보다 짧다면 정지
        motorB.stop(Stop.BRAKE)
        motorC.stop(Stop.BRAKE)
