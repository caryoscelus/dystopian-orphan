init python:
    PRONOUNS = {
        'he'    : ('he',  'she'),
        'him'   : ('him', 'her'),
        'his'   : ('his', 'her'),
        'He'    : ('He',  'She'),
        'Him'   : ('Him', 'Her'),
        'His'   : ('His', 'Her'),
    }
    
    class NameCharacter(object):
        def __init__(self, name, gender):
            self.name = name
            self.gender = gender
        
        def set_name(self, name):
            self.name = name
    
    def get_gender_f(pronoun):
        def f(self):
            return PRONOUNS[pronoun][self.gender]
        return f
    
    for pronoun in PRONOUNS:
        if not hasattr(NameCharacter, pronoun):
            setattr(NameCharacter, pronoun, property(get_gender_f(pronoun)))
    
    def init_player(name, gender):
        renpy.store.player = NameCharacter(name, gender)
    
    def init_girl(name):
        renpy.store.girl = NameCharacter(name, 1)

screen character_create():
    window:
        xalign 0.5 yalign 0.5 
        xfill False yfill False
        has vbox
        text "Your name:"
        input changed player.set_name exclude '{}[]()'
        text "Your gender:"
        hbox:
            textbutton "male" action SetField(player, 'gender', 0) text_bold (player.gender == 0)
            textbutton "female" action SetField(player, 'gender', 1) text_bold (player.gender == 1)
        textbutton "Ok!" action Return()

label character_create:
    call screen character_create()
    return

screen kid_name():
    window:
        xalign 0.5 yalign 0.5 
        xfill False yfill False
        has vbox
        text "How do you name your baby girl?"
        input changed girl.set_name exclude '{}[]()'
        textbutton "Ok!" action Return()

label kid_name:
    call screen kid_name()
    return
