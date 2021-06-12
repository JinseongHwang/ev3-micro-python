#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time

# https://pybricks.com/ev3-micropython/examples/robot_arm.html
# 위 URL에서 제공하는 코드를 번역(또는 의역)했습니다.
# Copyright (c) 2021 JinseongHwang

# EV3 Brick 생성
ev3 = EV3Brick()

# A 포트에 Gripper 모터를 연결한다.
gripper_motor = Motor(Port.A)

# B 포트에 Elbow 모터를 연결한다.
# 적절한 속도로 팔이 위로 올라가야 하며, 모터가 반시계 방향으로 회전하도록 일치시켜야 한다.
# 8톱니와 40톱니가 연결되어 있다.
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

# C 포트에 Base 모터를 연결한다.
# 터치 센서로부터 적절한 속도로 움직여야 하며, 모터가 시계 방향으로 회전하도록 일치시켜야 한다.
# 12톱니와 36톱니가 연결되어 있다.
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

# Elbow 모터와 Base 모터의 최대 동작 속도와 가속도를 각각 60과 120으로 제한한다.
# 제한하게 되면, 마치 공업용 로봇처럼 부드럽게 동작한다.
elbow_motor.control.limits(speed=60, acceleration=120)
base_motor.control.limits(speed=60, acceleration=120)

# S1에 터치 센서를 연결한다.
# 이 센서가 Robot Arm 회전의 시작 지점을 정의한다.
base_switch = TouchSensor(Port.S1)

# S3에 컬러 센서를 연결한다.
# 이 센서는 Elbow가 시작 지점인지, 아닌지를 판단한다.
# 센서는 하얀색 물체가 가까이에 있는지 없는지 감지한다.
elbow_sensor = ColorSensor(Port.S3)

# Elbow 를 설정한다.
# 우선 1초동안 아래로 내려가도록 한다.
# 그리고 천천히(초당 15도) 올라가는데, 컬러 센서에 하얀 색이 감지되면 멈춘다.
# 이후 그 각도를 0으로, 영점을 잡고 더 이상 움직이지 않도록 고정한다.
elbow_motor.run_time(-30, 1000)
elbow_motor.run(15)
while elbow_sensor.reflection() < 32:
    wait(10)
elbow_motor.reset_angle(0)
elbow_motor.hold()

# Base 를 설정한다.
# 터치 센서가 눌려질 때까지 회전한다.
# 이후 그 각도를 0으로, 영점을 잡고 더 이상 움직이지 않도록 고정한다.
base_motor.run(-60)
while not base_switch.pressed():
    wait(10)
base_motor.reset_angle(0)
base_motor.hold()

# Gripper 를 설정한다.
# 모터가 더 이상 움직일 수 없을 때까지 닫히는 방향으로 회전한다.
# Gripper 가 열릴 수 있도록 모터를 90도 회전한다.
# ** stall: 더 이상 움직일 수 없는 상태 **
gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)


def robot_pick(position):
    # 이 함수는 로봇 Base를 지정된 위치로 회전시킨다.
    # Elbow를 내리고, Gripper를 닫고, Elbow를 들어 올리는 순서로 물체를 집는다.

    # 집어올리는 자세를 취한다. Base 모터를 회전한다.
    base_motor.run_target(60, position)
    # 팔을 아래로 내린다.
    elbow_motor.run_target(60, -40)
    # wheel stack을 잡기 위해 Gripper를 닫는다.
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    # 잡은 wheel stack과 함께 팔을 들어 올린다.
    elbow_motor.run_target(60, 0)


def robot_release(position):
    # 이 함수는 로봇 Base를 지정된 위치로 회전시킨다.
    # Elbow를 내리고, Gripper를 열어서 물체를 내려놓는다. 그리고 팔을 다시 들어올린다.

    # 내려놓을 위치로 회전한다. Base 위치로 회전한다.
    base_motor.run_target(60, position)
    # 바닥에 wheel stack을 내려놓기 위해 팔을 내려놓는다.
    elbow_motor.run_target(60, -40)
    # wheel stack을 내려놓기 위해 Gripper를 연다.
    gripper_motor.run_target(200, -90)
    # 팔을 들어올린다.
    elbow_motor.run_target(60, 0)


# 경고음을 3번 울려서, 초기화가 완료되었음을 알립니다.
for i in range(3):
    ev3.speaker.beep()
    wait(100)

# Define the three destinations for picking up and moving the wheel stacks.
# wheel stack을 들어 올리거나 옮기기 위해 3가지 대상을 정의한다.
LEFT = 160
MIDDLE = 100
RIGHT = 40

# 아래는 이 프로그램의 main part이고, 무한 반복된다.
# 왼쪽의 wheel stack과 오른쪽 wheel stack의 위치를 변경한다.
#
# 1. 왼쪽의 wheel stack을 가운데로 옮긴다.
# 2. 오른쪽의 wheel stack을 왼쪽으로 옮긴다.
# 3. 가운데의 wheel stack을 오른쪽으로 옮긴다.
while True:
    # 왼쪽에서 가운데로 wheel stack을 옮긴다.
    robot_pick(LEFT)
    robot_release(MIDDLE)

    # 오른쪽에서 왼쪽으로 wheel stack을 옮긴다.
    robot_pick(RIGHT)
    robot_release(LEFT)

    # 가운데에서 오른쪽으로 wheel stack을 옮긴다.
    robot_pick(MIDDLE)
    robot_release(RIGHT)
