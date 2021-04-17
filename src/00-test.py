#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color, Align
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# Create your objects here.
# ev3 = EV3Brick()

# Play a sound
# ev3.speaker.beep()


# Write your program here.

def exec_normal_beep():
    brick.sound.beep()


def exec_higher_beep():
    # Play another beep sound.
    # This time with a higher pitch(1000 Hz) and longer duration(100 ms).
    # @args (frequency: Hz, duration: ms, volume: %)
    brick.sound.beep(1000, 100)


def exec_motor():
    try:
        # Initialize a motor at port B
        test_motor = Motor(Port.B)

        # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
        test_motor.run_target(500, 90)

    except:
        print('Exception when connecting motor')
        time.sleep(1)


def change_light():
    brick.light(Color.RED)  # 붉은 라이트 출력
    time.sleep(1)
    brick.light(None)  # 라이트 끄기
    time.sleep(1)


def press_any_button():
    print('Press any button please.')
    while not any(brick.buttons()):  # 아무 버튼도 눌려지지 않으면 대기
        pass

    print('ok')  # 아무 버튼이나 눌려지면 ok 를 출력한다.


def print_hello():
    # display size: (0, 0) ~ (177, 127)
    brick.display.clear()
    brick.display.text('Hello', (10, 50))  # (10, 50) 위치에 Hello 출력
    time.sleep(1)
    brick.display.text('World')  # Hello 아래에 World 출력
    time.sleep(1)
    # alpaca.jpg를 화면에 출력하고, 가운데 정렬하고, 기존의 화면을 지우지 않고 겹쳐서 출력한다.
    brick.display.image('../img/alpaca.jpg', Align.CENTER, clear=False)
    time.sleep(1)


def main():
    exec_normal_beep()
    exec_motor()
    change_light()
    press_any_button()
    print_hello()
    exec_higher_beep()


if __name__ == "__main__":
    main()
