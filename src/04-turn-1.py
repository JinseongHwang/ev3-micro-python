#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time

# B, C 모터 선언
motorB = Motor(Port.B)
motorC = Motor(Port.C)

# 300의 속도로 {DEGREE}도 회전 (시계방향)
DEGREE = 360 * 2  # test 상 360도(1바퀴)
motorB.run_angle(300, DEGREE, Stop.BRAKE, False)
motorC.run_angle(300, -DEGREE, Stop.BRAKE, True)
