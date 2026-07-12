# Import modules needed
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner, KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

gooberPad = KMKKeyboard()

# media keys(vol, skipping pausing)
gooberPad.extensions.append(MediaKeys())

#Create the 3x3 matrix
keyMatrix = MatrixScanner(
    column_pins=[board.D0, board.D1, board.D2],
    row_pins=[board.D3, board.D10, board.D9],
    diode_orientation=DiodeOrientation.COL2ROW # this might be wrong, idk
)
# encoder button setup
encoderButton = KeysScanner(
    pins = [board.D6],
    value_when_pressed = False,
    pull=True
)

# hook up keymatrix and the encoder button to the gooberPad
gooberPad.matrix = [keyMatrix, encoderButton]

encoder = EncoderHandler()
# adding the encoder pins to encoder. Using none as last argument since the encoder's button is already assigned
encoder.pins(
    (board.D8, board.D7, None),
)
# add the encoder to the gooberPad
gooberPad.modules.append(encoder)

#Assign basic functions
gooberPad.keymap = [
    [
        # Row 1
        KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
        # Row 2
        KC.LGUI(KC.TAB), KC.UP, KC.LALT(KC.F4),
        # Row 3
        KC.LEFT, KC.DOWN, KC.RIGHT,
        # Encoder button
        KC.MUTE
    ]
]
encoder.map = [
    # Layer 0
    ((KC.VOLD, KC.VOLU),) 
]

if __name__ == '__main__':
    gooberPad.go()