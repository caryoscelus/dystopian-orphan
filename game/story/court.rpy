define letter = Character(None, what_font="fonts/GNUTypewriter.otf", window_background='images/bg/letter.png', window_xpadding=100, window_ypadding=70, what_color="#000", what_prefix="{cps=0}", what_suffix="{/cps}")

label court_letter:
    letter "[player.name], it is our duty to inform you of the fact that you are
    required at the Higher Court to be justly judged on the matter of your
    alleged founding of a baby, tomorrow at seven o'clock in the morning.
    {p}Refusal to do so without proper explanation might result in severe
    consequences for you, such as an appropriate fine or guilt verdict
    {p}Please cooperate with the Justice for your own good."
    return

define judge = Character('The Judge')
define officials = Character('Officials')
define prosecutor = Character('Prosecutor')
define defender = Character('Public Defender')
define juvenile = Character('Juvenile Attorney')
define crowd = Character('Crowd')

label court:
    $ say_align = 1.0
    stop music
    scene bg court
    play crowd "crowd.mp3" loop
    pause 5.0
    
    play sound "circus-drum.flac"
    
    pause 10.0
    
    $ renpy.music.set_volume(0.2, 1.0, channel='crowd')
    show bg court judge as judge:
        alpha 0.0
        linear 1.0 alpha 1.0
    
    judge "Good morning, ladies and gentlemen."
    judge "We'll discuss the case of another baby today."
    judge "Are sides ready?"
    officials "Yes, your honor!"
    judge "All right, lets hear from you!"
    prosecutor "Your honor, we have yet another case of baby claimed to be found
    on the street. I think this is suspicious."
    judge "Hmph, i don't care what you think! What are the facts?"
    prosecutor "On the december 14th the defendant [player.name] came home with
    this baby in hands."
    prosecutor "[player.He] might have been hiding it before and now
    decided to reveal it as found in the streets!"
    judge "Okay, that sounds like a reasonable theory. Enough."
    judge "Lets hear from you now!"
    defender "Your honor, there is no evidence supporting that claim!"
    defender "We believe [player.name] is telling the truth and have found the
    baby on the street."
    defender "To support that claim we propose to make a DNA expertise!"
    prosecutor "Ha-ha, lets do it!"
    juvenile "Objection, your honor!"
    juvenile "That would be against 3rd article of The Juvenile Law, part 4."
    judge "Yes, indeed."
    judge "We will not call for DNA expertise until the child in question is 18
    years old."
    judge "Anyway, lets cut the crap and start some questioning!"
    prosecutor "As you wish, your honor."
    prosecutor "However, we do not have any witnesses except for the defendant
    and the child themselves."
    juvenile "Objection! You cannot call that poor child proper witness!"
    juvenile "I will not give my permission to question her!"
    judge "Shut up, we understand that already. Lets hear from this
    [player.name] then."
    prosecutor "Do you remember exact time when you found the baby?"
    
    $ config.narrator_menu = True
    $ menu_offset = (0, 640)
    
    menu:
        "Do you remember exact time when you found the baby?"
        "Yes":
            prosecutor "Well, what was it?"
            $ found_time = renpy.input("Time:", default="18:00", allow="0123456789:.", length=5)
            prosecutor "Ha-ha, we got you there! That is an obvious lie, because you were seen on the work three minutes after that!"
            prosecutor "I actually have a witness for that."
            prosecutor "The defendant actually wants to confuse this court!"
        "No":
            prosecutor "Your honor, as you can see defendant does not wish to cooperate with this court!"
            prosecutor "It's the best sign of guilt, i tell you."
    judge "Hmph, that might be true."
    judge "Lets proceed!"
    prosecutor "Has anybody seen you picking up that baby?"
    $ menu_offset = (0, 640)
    menu:
        "Has anybody seen you picking up that baby"
        "Yes":
            prosecutor "Well, why don't you bring this person to the court?"
            defender "Objection, you honor! Defendant must have meant the baby could see [player.him]!"
            judge "Is that so? Objection sustained!"
        "No":
            prosecutor "See, there's none to prove you are innocent!"
            defender "Objection! Defendant is innocent until proved guilty!"
            judge "That sounds plausible to me."
    
    show bg story as story
    t "...this continued for hours..."
    hide story
    
    judge "Okay, hearing is over. We think that defendant, [player.name], is a good,
    law-abiding citizen and should be rewarded for babysitting!"
    judge "In the name of this court, holy judstice and my eternal life."
    play sound "amen.flac"
    judge "Amen!"
    $ renpy.music.set_volume(0.7, channel='crowd')
    play crowd "amen_choir.flac" noloop
    crowd "{size=40}AMEN!!!{/size}"
    return
