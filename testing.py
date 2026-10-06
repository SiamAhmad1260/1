import pyray as rl 
import os 
import anim

rl.init_window(1080, 720, b'testing')

player = rl.load_texture(b'assets/male/cole/base/move.png')
move = anim.anim(player, rl.Rectangle(300,400, 50,50), 6, 8.0)

while not rl.window_should_close(): 
    rl.begin_drawing()
    rl.clear_background(rl.GRAY)
    move.animate()
    rl.end_drawing()
