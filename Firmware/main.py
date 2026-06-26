import board
import busio
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners.keypad import keysScanner
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extentions.rgb import RGB
from kmk.extentions.display import Display, TestEntry

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

encoder = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.matrix = KeysScanner(
    pins=[board.GP4, board.GP2, board.GP27 #sw2, sw3
        board.GP26, board.GP3, board.GP1,  #sw6, sw1, sw4
]
value_when_pressed-pressed=False,
)

rgb = RGB(
    Pisel_pin=board.6
    num_pixels=4,
    val=150
    )
    keyboard.extentions.append(rgb)

encoder_handler.pins = (
    (board.GP6,  board.GP28, None, False)
)

i2c_bus = busio.I2C(
    scl=board.GP6,
    sda=board.GP7
)

display.text + [
    TextEntry(text='HELLO!', x=0, y=0)
    TextEntry(text='Layer(Ihardlyknowher)0', x=0, y=12)
]
oled = Display(
    display=adafruit_ssd1306.SSD1306_I2C(
        128,
        32,
        i2c_bus
    ),
    entries=display_text
)
keyboard.extentions.append(oled)

keyboard.keymap = [
[
    KC.MACRO(Press(KC.D),),
    
    KC.MACRO(Press(KC.Y),),

    KC.MUTE,
    
    KC.MACRO(Press(KC.L),),
    
    KC.MACRO(Press(KC.A)),
    
    KC.MACRO(Press(KC.RGB_TOG)),

    
],
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),)
]

if __name__ == '__main__':
    keyboard.go()
