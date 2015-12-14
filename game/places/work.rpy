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
    menu:
        "Print prediction?"
        "Yes":
            prediction "Years left for this community to live: [life_prediction]."
        "No":
            pass
    jump control_room_wait

label work_cord:
    menu:
        "Unplug lifesupport controlling mainframe?"
        "Yes":
            $ workman.result = 'kill_cord'
        "No":
            pass
    jump control_room_wait

label work_work:
    $ workman.has_worked = True
    "You do job.."
    jump control_room_wait

label work_leave:
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
