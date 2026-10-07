import pyray as rl 

class animate():
    def __init__(self,texture: rl.Texture2D, dest_rect: rl.Rectangle|list|tuple, num_frames: int, animation_fps: float):
        #texture attribute
        self.texture = texture
        self.num_frames = num_frames
        self.animation_fps = animation_fps
        self.dest_rect = dest_rect
        #frame attribute
        self.frame_width = texture.width/num_frames
        self.frame_height = texture.height
        
        #animation state 
        self.current_frame = 0
        self.timer = 0.0
                
    def frame_forward(self, flip_x:bool= False, color: Color|list|tuple= rl.WHITE):
        # time and frame counter
        self.timer += rl.get_frame_time()
        frame_duration = 1./self.animation_fps

        # animation time and frame bounds, 
        # animation advance
        if self.timer >= frame_duration:
            self.timer -= frame_duration #note: if this is set to 0.0 then it will lag behind if delta time goes above frame_duration
            self.current_frame += 1 
            if self.current_frame >= self.num_frames:
                self.current_frame = 0 

        # animation flip
        # using negetive width to filp texture in the x axis
        if flip_x:
            width = self.frame_width
        else:
            width = -self.frame_width
        
        # animation source rectangle advance
        source_rect = rl.Rectangle(self.current_frame*self.frame_width, 0.0, width, self.frame_height)
        
        self.source_rect = source_rect
        
    # draw texture animation
    def draw_frame(self):
        origin = rl.Vector2(self.frame_width/2, self.frame_height/2)
        rl.draw_texture_pro(self.texture, self.source_rect, self.dest_rect, origin, 0.0, rl.WHITE)

''' Note: source tells the draw exactly where to cut the texture
                destination tells draw where to draw on the window
                origin is the pivot point of the texture(used for spin, rotate, etc)'''