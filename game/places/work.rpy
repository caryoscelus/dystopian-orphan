# control room

init python:
    class Workman(object):
        def __init__(self):
            self.printout = 'work_printout'
            self.cord = 'work_cord'
            self.work = 'work_work'
            self.leave = 'work_leave'
            self.result = None
            self.has_worked = False
    
    def init_workman():
        renpy.store.workman = Workman()

screen control_room:
    imagemap:
        ground "images/bg/control-room.png"
        alpha False
        hotspot ( 760,  340,  190,   80) action Jump(workman.printout)
        hotspot ( 290,  360,  110,   90) action Jump(workman.cord)
        hotspot ( 370,  200,  370,  200) action Jump(workman.work)
        hotspot (   0,  540, 1280,  180) action Jump(workman.leave)

label control_room:
    play engine "engine.mp3"
    $ workman.result = None
    show screen control_room
label control_room_wait:
    if workman.result:
        jump control_room_return
    empty ""
    jump control_room_wait
label control_room_return:
    stop engine
    hide screen control_room
    return workman.result

define printout = Character(None, what_font="fonts/GNUTypewriter.otf", window_background='images/bg/printout.png', window_xpadding=100, window_ypadding=80, what_prefix="{cps=0}", what_suffix="{/cps}")

label work_printout:
    $ config.narrator_menu = False
    menu:
        "Print prediction?"
        "Yes":
            play sound 'printer.flac'
            pause 3.5
            $ say_align = 0.0
            printout "Years left for this community to live: approximately [life_prediction]."
        "No":
            pass
    jump control_room_wait

label work_cord:
    $ config.narrator_menu = False
    menu:
        "Unplug lifesupport controlling mainframe?"
        "Yes":
            $ workman.result = 'kill_cord'
        "No":
            pass
    jump control_room_wait

label work_work:
    $ workman.has_worked = True
    "You do your job.."
    jump control_room_wait

label work_leave:
    $ config.narrator_menu = False
    menu:
        "Leave?"
        "Yes":
            if workman.has_worked:
                $ workman.result = 'leave'
            else:
                "You should finish your workday before leaving."
        "No":
            pass
    jump control_room_wait

label work:
    $ workman.has_worked = False
    call control_room
    return _return
