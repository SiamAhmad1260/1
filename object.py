import pyray as rl 

class Object:
    def __init__(self, object_form: rl.Texture2D , pos: rl.Vector2, static_obj: bool= False,  mass: float= 1.0, max_velocity:float|None=None, acceleration: float = 1):
        # object data
        self.object = object_form
        self.pos = pos 
        self.static_obj = static_obj
        # physics data
        self.mass = mass 
        self.acceleration = acceleration
        self.speed_curve = self.acceleration * rl.get_fps() 
        self.speed = self.speed + self.acceleration * self.speed 
    def move(self) -> rl.Vector2:
        

