screen school:
    imagemap:
        ground "images/bg/school.png"
        hotspot (880, 0, 160, 200) action Jump('school_wait_or')
        hotspot (600, 540, 100, 90) action Jump('school_book')

label school_wait_or:
    menu:
        "Wait for teacher?"
        "Yes":
            $ school_finish = True
            "You wait until teacher finally arrives."
        "No":
            "You can't leave classroom until you meet the teacher."
    jump school_wait

label school_book:
    menu:
        "Read the book?"
        "Yes":
            $ school_finish = True
            "This is a history book."
            "\"Old legends say that people used to leave outside the Sphere, under
            thing they called Sky.\""
            "\"Surely this is no more than a dream for a larger world: we all know
            that environment outside is extremely hazardous.\""
            "..."
            "\"The history has already ended. And soon the humanity will follow.\""
            "\"Even after we attained immortality, we cannot live without resources
            which come to an end.\""
            "..."
        "No":
            pass
    jump school_wait

label school:
    $ school_finish = False
    show screen school
label school_wait:
    if school_finish:
        jump school_return
    empty ""
    jump school_wait
label school_return:
    hide screen school
    return
