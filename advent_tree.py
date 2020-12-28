from gpiozero import LEDBoard
from gpiozero import LED
from gpiozero.tools import random_values
from signal import pause
from time import sleep

def random_flicker():
    tree = LEDBoard(*range(2,28),pwm=True)
    for led in tree:
        led.source_delay = 0.1
        led.source = random_values()
    pause()

def advent_tree():
    tree = {
        "one" : LED(4),
        "two" : LED(15),
        "three" : LED(13),
        "four" : LED(21),
        "five" : LED(25),
        "six" : LED(8),
        "seven" : LED(5),
        "eight" : LED(10),
        "nine" : LED(16),
        "ten" : LED(17),
        "eleven" : LED(27),
        "twelve" : LED(26),
        "thirteen" : LED(24),
        "fourteen" : LED(9),
        "fifteen" : LED(12),
        "sixteen" : LED(6),
        "seventeen" : LED(20),
        "eighteen" : LED(19),
        "nineteen" : LED(14),
        "twenty" : LED(18),
        "twentyone" : LED(11),
        "twentytwo" : LED(7),
        "twentythree" : LED(23),
        "twentyfour" : LED(22),
        "star" : LED(2),
    }

    advent_time = True

    while advent_time:
        keys = tree.keys()
        for key in keys:
            tree[key].on()
            sleep(0.5)
        advent_time = False

advent_tree()
sleep(1)
random_flicker()
