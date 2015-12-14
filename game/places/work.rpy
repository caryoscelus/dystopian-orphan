# control room

init python:
    class Workman(object):
        def __init__(self):
            self.printout = 'work_printout'
            self.cord = 'work_cord'
            self.work = 'work_work'
            self.leave = 'work_leave'
            self.result = None
    
    def init_workman():
        renpy.store.workman = Workman()

screen control_room:
    imagemap:
        ground "images/bg/control-room.png"
        alpha False
        hotspot ( 760,  340,  190,   80) action Jump(workman.printout)
        hotspot (0, 10, 10, 10) action Jump(workman.cord)
        hotspot ( 370,  200,  370,  200) action Jump(workman.work)
        hotspot (   0,  540, 1280,  180) action Jump(workman.leave)

label control_room:
    $ workman.result = None
    show screen control_room
label control_room_wait:
    if workman.result:
        jump control_room_return
    empty ""
    jump control_room_wait
label control_room_return:
    hide screen control_room
    return workman.result

label work_printout:
    "printout"
    jump control_room_wait

label work_cord:
    "cord"
    jump control_room_wait

label work_work:
    "work"
    jump control_room_wait

label work_leave:
    "leave"
    jump control_room_wait
