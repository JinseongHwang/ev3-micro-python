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

# 지금은 flower_open() 함수와 flower_close() 함수에 임시 확인용 코드를 작성해뒀다.
# 꽃 형태의 로봇을 만들게 된다면, 앞에서 배웠던 것들을 응용해서 두 함수의 내부를 다시 작성해보자.


def flower_open():
    # 높은 경고음을 0.5초 간격으로 낸다
    brick.sound.beep(1000)
    time.sleep(0.5)


def flower_close():
    # 낮은 경고음을 0.5초 간격으로 낸다
    brick.sound.beep(500)
    time.sleep(0.5)


while True:
    # color_sensor.ambient() 는 주변광의 값을 측정해서 '%'로 반환합니다.
    if color_sensor.ambient() < 20:  # 20보다 어둡다면 꽃잎이 닫힌다.
        flower_close()
    else:  # 20보다 밝다면 꽃잎이 열린다.
        flower_open()
