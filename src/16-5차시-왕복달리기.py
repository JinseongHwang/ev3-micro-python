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

# N번을 왕복한다.
N = 2

for count in range(2 * N):
    motorB.run(300)
    motorC.run(300)

    while True:
        # 검은 선을 만났을 경우 (반사값이 15 미만)
        if color_sensor.reflection() < 15:
            # 180도 포인트 턴
            DEGREE = 360 * 2  # test 상 180도

            # 반시계 방향으로 반바퀴 회전 (포인트턴)
            motorB.run_angle(300, -DEGREE / 2, Stop.BRAKE, False)
            motorC.run_angle(300, DEGREE / 2, Stop.BRAKE, True)
            break

    brick.sound.beep()

# 모터 정지
motorB.stop(Stop.BRAKE)
motorC.stop(Stop.BRAKE)
