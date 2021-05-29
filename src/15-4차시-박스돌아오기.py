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

for i in range(4):
    while True:
        if Ultrasonic_Sensor.distance() < 200:  # 20cm
            motorB.run(300)
            motorC.run(300)

        else:
            if i < (4 - 1):
                # B, C 모터를 300의 속도로 1.5초간 직진
                motorB.run_time(300, 1500, Stop.BRAKE, False)
                motorC.run_time(300, 1500, Stop.BRAKE, True)

                DEGREE = 90 * 4  # 시계 방향으로 90도 회전 (포인트턴)
                motorB.run_angle(300, DEGREE / 2, Stop.BRAKE, False)
                motorC.run_angle(300, -DEGREE / 2, Stop.BRAKE, True)

                # B, C 모터를 300의 속도로 1.7초간 직진
                motorB.run_time(300, 1700, Stop.BRAKE, False)
                motorC.run_time(300, 1700, Stop.BRAKE, True)

            break

# 모터 정지
motorB.stop(Stop.BRAKE)
motorC.stop(Stop.BRAKE)
