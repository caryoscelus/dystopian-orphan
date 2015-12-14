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
            self.baby = 'walk_nothing_interesting'
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
        hotspot ( 450,  360,  200,  130) action Jump(walkman.river)
        hotspot (1770,  370,  180,  110) action Jump(walkman.baby)
    key "walk_left" action Function(walkman.walk_left)
    key "walk_right" action Function(walkman.walk_right)

label walk_the_street():
    $ walkman.result = None
    show screen walk_the_street(walkman)
label walk_the_street_wait:
    if walkman.result:
        jump walk_the_street_return
    empty ""
    jump walk_the_street_wait
label walk_the_street_return:
    hide screen walk_the_street
    return walkman.result


label walk_wont_go_home:
    "It's not time to return home."
    jump walk_the_street_wait

label walk_wont_go_work:
    "It's not time to go to work."
    jump walk_the_street_wait

label walk_return_home:
    menu:
        "Go home?"
        "Yes":
            $ walkman.result = 'home'
        "No":
            pass
    jump walk_the_street_wait

label walk_go_work:
    menu:
        "Go to work?"
        "Yes":
            $ walkman.result = 'work'
        "No":
            pass
    jump walk_the_street_wait

label walk_to_work():
    $ walkman.position = 0
    $ walkman.walkout_left = 'walk_wont_go_home'
    $ walkman.walkout_right = 'walk_go_work'
    $ walkman.baby = 'walk_nothing_interesting'
    $ walkman.river = 'walk_river'
    call walk_the_street
    return

label walk_home():
    $ walkman.position = 1280
    $ walkman.walkout_right = 'walk_wont_go_work'
    $ walkman.walkout_left = 'walk_return_home'
    $ walkman.baby = 'walk_nothing_interesting'
    $ walkman.river = 'walk_river'
    call walk_the_street
    return

label walk_nothing_interesting:
    "There is nothing interesting here.."
    jump walk_the_street_wait

label walk_baby:
    $ walkman.status = 'found'
    menu:
        "You found a baby. Pickup?"
        "Yes":
            $ walkman.status = 'pickup'
            $ walkman.baby = 'walk_nothing_interesting'
            $ walkman.river = 'walk_throw_baby_into_river'
            hide baby street
            "You picked up a baby."
        "No":
            pass
    jump walk_the_street_wait

label walk_throw_baby_into_river:
    menu:
        "Throw baby into the river?"
        "Yes":
            $ walkman.status = 'drowned'
            $ walkman.river = 'walk_river'
        "No":
            pass
    jump walk_the_street_wait

label walk_home_baby():
    $ walkman.status = 'notfound'
    $ walkman.position = 1280
    $ walkman.walkout_right = 'walk_wont_go_work'
    $ walkman.walkout_left = 'walk_return_home'
    $ walkman.baby = 'walk_baby'
    call walk_the_street
    return walkman.status
