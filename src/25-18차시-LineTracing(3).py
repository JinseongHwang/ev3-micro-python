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

CRITERIA = 20  # 반사값 기준 설정

speed = 150  # 모터 속도

DEGREE = 360 * 2  # 360도 (1바퀴)

while True:
    if color_sensor1.reflection() > CRITERIA and color_sensor2.reflection() > CRITERIA:
        # 센서 2개 모두 선 위에 있지 않을 경우, 직진한다.
        motorB.run(speed)
        motorC.run(speed)

    elif color_sensor1.reflection() > CRITERIA and color_sensor2.reflection() <= CRITERIA:
        # 오른쪽 센서 1개만 선 위에 올라갔을 경우, 오른쪽으로 회전한다.
        motorB.run(speed)
        motorC.run(0)

    elif color_sensor1.reflection() <= CRITERIA and color_sensor2.reflection() > CRITERIA:
        # 왼쪽 센서 1개만 선 위에 올라갔을 경우, 왼쪽으로 회전한다.
        motorB.run(0)
        motorC.run(speed)

    elif color_sensor1.reflection() <= CRITERIA and color_sensor2.reflection() <= CRITERIA:
        # 센서 2개 모두 선 위에 올라갔을 경우, 시계 방향으로 180도(반바퀴) 포인트 턴 한다.
        motorB.run_angle(300, DEGREE / 2, Stop.BRAKE, False)
        motorC.run_angle(300, -DEGREE / 2, Stop.BRAKE, True)
