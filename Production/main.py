//idk what im doing this is my best atempt until I have time to figure it out properly

import board
from kmk.kmk_keyboard Import KMKKeyboard
from kmk.kays import KC
from kmk.scanner import MatrixScanner
from kmk.scanners import DiodeOrientation

Keyboard = KMKKeyBoard()

keyboard.col_pins = ('GPIO01', 'GPIOo2', 'GPIO03', 'GPIO04', 'GPIO05', 'GPIO06', 'GPIO43', 'GPIO09', GPIO08', 'GPIO07', 'GPIO44')
keyboard.row_pins = () 

keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
	[KC.ESCAPE, KC.LALT, KC.LSHIFT, KC.RCTRL]
]

if__name__ =='__main__':
	keyboard.go()