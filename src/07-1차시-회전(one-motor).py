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

# 좌회전: motorB 고정, motorC 회전
# 300의 속도로 {DEGREE / 2}도 만큼 회전
DEGREE = 360 * 2  # test 상 360도(1바퀴)
motorC.run_angle(300, DEGREE / 2, Stop.BRAKE, True)

time.sleep(1)

# 우회전: motorB 회전, motorC 고정
# 300의 속도로 {DEGREE / 2}도 만큼 회전
DEGREE = 360 * 2  # test 상 360도(1바퀴)
motorB.run_angle(300, DEGREE / 2, Stop.BRAKE, True)
