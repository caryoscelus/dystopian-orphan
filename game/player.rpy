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

screen character_create():
    window:
        xalign 0.5 yalign 0.5 
        xfill False yfill False
        has vbox
        text "Your name:"
        input changed player.set_name exclude '{}[]()'
        text "Your gender:"
        hbox:
            textbutton "male" action SetField(player, 'gender', 0)
            textbutton "female" action SetField(player, 'gender', 1)
        textbutton "Ok!" action Return()

label character_create:
    call screen character_create()
