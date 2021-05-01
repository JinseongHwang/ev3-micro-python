#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time

"""
1초 간격으로 5번 경고음을 울리고, heart 이미지를 보여준다.
"""

# Play another beep sound.
# This time with a higher pitch(1000 Hz) and longer duration(100 ms).
# @args (frequency: Hz, duration: ms, volume: %)

for i in range(5):
    # 매개변수 설명
    # 1. 주파수 (Hz) / 2. 시간 (ms) / 3. 음량 (%)
    brick.sound.beep(1000, 100)
    time.sleep(1)

# heart.jpg를 화면에 출력하고, 가운데 정렬하고, 기존의 화면을 지우고 출력한다.
brick.display.image('../img/heart.jpg', Align.CENTER, clear=True)
time.sleep(3)
