init python:
    config.keymap['walk_left'] = [ 'K_LEFT', 'repeat_K_LEFT' ]
    config.keymap['walk_right'] = [ 'K_RIGHT', 'repeat_K_RIGHT' ]

init python:
    STEP_SOUNDS_N = 3
    
    def walk_sound():
        sound = 'sounds/step_{:02}.flac'.format(int(renpy.random.random()*STEP_SOUNDS_N))
        renpy.music.queue(sound, channel='sound', clear_queue=True)

init python:
    class Walkman(object):
        def __init__(self):
            self.position = 0
            self.bounds = (0, 1280)
            self.step = 100
            self.walkout_left = 'walkout_left'
            self.walkout_right = 'walkout_right'
            self.river = 'walk_river'
            self.result = None
        
        def walk_left(self):
            walk_sound()
            self.position -= self.step
            if self.position < self.bounds[0]:
                self.position = self.bounds[0]
                renpy.jump(self.walkout_left)
        
        def walk_right(self):
            walk_sound()
            self.position += self.step
            if self.position > self.bounds[1]:
                self.position = self.bounds[1]
                renpy.jump(self.walkout_right)
    
    def init_walkman():
        renpy.store.walkman = Walkman()

label walkout_left:
    $ walkman.result = 'left'
    jump walk_the_street_wait

label walkout_right:
    $ walkman.result = 'right'
    jump walk_the_street_wait

label walk_river:
    "dirty river"
    jump walk_the_street_wait

screen walk_the_street(walkman):
    imagemap:
        xoffset (-walkman.position)
        ground 'images/bg/street.png'
        hotspot (450, 360, 200, 130) action Jump(walkman.river)
    key "walk_left" action Function(walkman.walk_left)
    key "walk_right" action Function(walkman.walk_right)

label walk_the_street():
    show screen walk_the_street(walkman)
label walk_the_street_wait:
    if walkman.result:
        jump walk_the_street_return
    ""
    jump walk_the_street_wait
label walk_the_street_return:
    return walkman.result


label walk_wont_go_home:
    "It's not time to return home."
    jump walk_the_street_wait

label walk_wont_go_work:
    "It's not time to go to work."
    jump walk_the_street_wait

label walk_to_work():
    $ walkman.position = 0
    $ walkman.walkout_left = 'walk_wont_go_home'
    call walk_the_street
    $ print(_return)
    return
