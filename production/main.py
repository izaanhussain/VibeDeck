import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# RGB LED

rgb = RGB(
    pixel_pin=board.D6,
    num_pixels=1,
    val_limit=100,
    hue_default=0,
    sat_default=255,
    val_default=100,
)

keyboard.extensions.append(rgb)

# vibedeck keys

PINS = [
    board.D1,   # SW1
    board.D10,  # SW2
    board.D8,   # SW3
    board.D9,   # SW4
    board.D7,   # SW5
    board.D2,   # SW6
    board.D3,   # SW7
    board.D4,   # SW8
    board.D5,   # SW9
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# keymaping

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
        KC.G,
        KC.H,
        KC.I,
    ]
]

if __name__ == "__main__":
    keyboard.go() 