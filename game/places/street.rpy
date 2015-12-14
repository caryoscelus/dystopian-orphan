init python:
    config.keymap['walk_left'] = [ 'K_LEFT', 'repeat_K_LEFT' ]
    config.keymap['walk_right'] = [ 'K_RIGHT', 'repeat_K_RIGHT' ]

init python:
    STEP_SOUNDS_N = 3
    
    renpy.music.register_channel('river', mixer='sfx', loop=True, stop_on_mute=False, tight=True, file_prefix="sounds/")
    renpy.music.register_channel('baby', mixer='sfx', loop=True, stop_on_mute=False, tight=True, file_prefix="sounds/")
    renpy.music.register_channel('river_splash', mixer='sfx', loop=False, stop_on_mute=False, tight=True, file_prefix="sounds/")
    renpy.music.register_channel('sound', mixer='sfx', loop=False, stop_on_mute=False, tight=True, file_prefix="sounds/")
    renpy.music.register_channel('crowd', mixer='sfx', file_prefix="sounds/")
    renpy.music.register_channel('engine', mixer='sfx', file_prefix="sounds/", loop=True)
    renpy.music.register_channel('music', mixer='music', file_prefix="music/", loop=True)
    
    def walk_sound():
        sound = 'step_{:02}.flac'.format(int(renpy.random.random()*STEP_SOUNDS_N))
        renpy.music.queue(sound, channel='sound', clear_queue=True)
        recalculate_street_ambience()
    
    def recalculate_street_ambience():
        river_pan = max(-walkman.position / 640.0, -1.0)
        if walkman.position < 600:
            river_amount = 1.0
        elif walkman.position > 980:
            river_amount = 0.05
        else:
            river_amount = (1000-walkman.position) / 400.0
        renpy.music.set_pan(river_pan, 0.1, channel='river')
        renpy.music.set_volume(0.5*river_amount, 0.1, channel='river')
        
        if walkman.position > 800:
            baby_pan = 0
            baby_amount = 1.0
        else:
            baby_pan = min((800-walkman.position)/400.0, 1.0)
            if walkman.position < 320:
                baby_amount = 0.04
            else:
                baby_amount = (walkman.position-300)/500.0
        renpy.music.set_pan(baby_pan, 0.1, channel='baby')
        renpy.music.set_volume(0.5*baby_amount, 0.1, channel='baby')
    
    def start_river_ambience():
        renpy.music.play('256012__jagadamba__flowing-river.wav', channel='river')
        recalculate_street_ambience()
    
    def start_baby_ambience():
        renpy.music.play('321712__eguaus__baby-crying.wav', channel='baby')
        recalculate_street_ambience()
    
    def stop_baby_ambience():
        renpy.music.stop('baby', 1.0)
    
    def stop_street_ambience():
        renpy.music.stop('river', 1.0)
        renpy.music.stop('baby', 1.0)

init python:
    class Walkman(object):
        def __init__(self):
            self.position = 0
            self.bounds = (0, 1280)
            self.step = 10
            self.walkout_left = 'walkout_left'
            self.walkout_right = 'walkout_right'
            self.river = 'walk_river'
            self.baby = 'walk_nothing_interesting'
            self.result = None
            self.status = None
        
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
    "You see a dirty river. It looks as filthy as always."
    jump walk_the_street_wait

screen walk_the_street(walkman):
    imagemap:
        xoffset (-walkman.position)
        ground 'images/bg/street.png'
        hotspot ( 450,  360,  200,  130) action Jump(walkman.river)
        hotspot ( 190,  600,  640,  120) action Jump(walkman.river)
        hotspot (1770,  370,  180,  110) action Jump(walkman.baby)
    add 'bg street trash':
        xoffset (-walkman.position*1.5+480)
    if walkman.status == 'notfound' or walkman.status == 'found':
        add 'bg baby':
            xoffset (-walkman.position)
    key "walk_left" action Function(walkman.walk_left)
    key "walk_right" action Function(walkman.walk_right)

label walk_the_street():
    $ walkman.result = None
    $ start_river_ambience()
    show screen walk_the_street(walkman)
label walk_the_street_wait:
    if walkman.result:
        jump walk_the_street_return
    empty ""
    jump walk_the_street_wait
label walk_the_street_return:
    hide screen walk_the_street
    $ stop_street_ambience()
    return walkman.result


label walk_wont_go_home:
    "It's not time to return home."
    jump walk_the_street_wait

label walk_wont_go_work:
    "It's not time to go to work."
    jump walk_the_street_wait

label walk_return_home:
    $ config.narrator_menu = False
    menu:
        "Go home?"
        "Yes":
            $ walkman.result = 'home'
        "No":
            pass
    jump walk_the_street_wait

label walk_go_work:
    $ config.narrator_menu = False
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
    $ config.narrator_menu = False
    menu:
        "You found a baby. Pick it up?"
        "Yes":
            $ walkman.status = 'pickup'
            $ walkman.baby = 'walk_nothing_interesting'
            $ walkman.river = 'walk_throw_baby_into_river'
            $ stop_baby_ambience()
            "You picked up a baby."
        "No":
            pass
    jump walk_the_street_wait

label walk_throw_baby_into_river:
    $ config.narrator_menu = False
    menu:
        "Throw baby into the river?"
        "Yes":
            $ walkman.status = 'drowned'
            $ walkman.river = 'walk_river'
            $ renpy.music.play('splash_{:02}.flac'.format(int(renpy.random.random()*4)), channel='river_splash')
        "No":
            pass
    jump walk_the_street_wait

label walk_home_baby():
    $ walkman.status = 'notfound'
    $ walkman.position = 1280
    $ walkman.walkout_right = 'walk_wont_go_work'
    $ walkman.walkout_left = 'walk_return_home'
    $ walkman.baby = 'walk_baby'
    $ start_baby_ambience()
    call walk_the_street
    return walkman.status
