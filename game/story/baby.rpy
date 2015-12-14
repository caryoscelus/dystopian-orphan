label baby:
    play music "technodesert.flac"
    $ renpy.music.set_volume(0.5)
    $ life_prediction = 110
    scene bg story
    t "It all started on what seemed to be a regular, boring day."
    t "In the morning, you went to work as usual..."
    call walk_to_work
    call work
    if _return == 'kill_cord':
        t "...and then you decided this miserable community should come to an end
        and turned off the lifesupport computer..."
        jump kill_cord_ending
    t "...and after work was done, you headed for home..."
    call walk_home_baby
    if _return == 'notfound':
        jump notfound_ending
    elif _return == 'found':
        jump found_ending
    elif _return == 'drowned':
        jump drowned_ending
    t "...you have found a baby and took it home."
    t "This surely wasn't a pleasant decision, but you couldn't bring yourself
    to behave differently."
    t "That was how you started raising a kid..."
    $ life_prediction = 107
    call talk_about_baby
    call court_notice
    return

label notfound_ending:
    t "...and then nothing happened really."
    t "It was a very regular day indeed."
    call game_over
    "YOU WERE NOT VERY ATTENTIVE"
    return

label found_ending:
    t "...you have found a baby, but couldn't decide what to do with it and left
    it alone."
    t "Who knows what could have happened were you to act more decisive?"
    call game_over
    "YOU WERE NOT VERY DECISIVE"
    return

label drowned_ending:
    t "...you have found a baby and decided to throw it into the dirty river, so
    that it won't consume valuable resources."
    t "You think that community can be thankful for your illegal, but quite proper
    deed."
    call game_over
    "YOU FOUGHT FOR YOUR LIFE"
    return


define neighbour0 = Character("A neighbour", what_color="#fcc")
define neighbour1 = Character("Another neighbour", what_color="#cfc")
define neighbour2 = Character("Yet another neighbour", what_color="#ccf")

label talk_about_baby:
    scene bg near home
    neighbour0 "Holy crackers! Is that a baby?!"
    neighbour1 "Baby?! Who said baby?"
    $ menu_offset = True
    menu:
        "Uhm.. yes, i found it lying on the street..":
            neighbour0 "On the street! Poor baby!"
        "Yes, it's a baby. And i'm gonna take care of it.":
            neighbour0 "Please don't tell me it's yours."
            $ menu_offset = True
            menu:
                "Of course not! Even i wouldn't commit such a sin.":
                    neighbour0 "Oh, i'm so relieved."
                "Maybe it is..":
                    neighbour0 "WHAT?! YOU CRAZY?"
                    $ menu_offset = True
                    menu:
                        "Just joking":
                            neighbour0 ".."
                            neighbour0 "Don't joke like that."
                        "Please, calm down! It's not my baby!":
                            neighbour0 "I'M CALM!"
                            neighbour0 "Hmph, couldn't you tell it from the start?"
    neighbour1 "Anyway, you gotta go tell government about it!"
    neighbour2 "Wait, wait! Why would you do that?"
    neighbour1 "Hmm, what do you propose?"
    neighbour2 "Just think about it: it's going to take our precious resources
    away!"
    neighbour2 "Are you willing to say goodbye to maybe years of your life?!"
    neighbour0 "Don't tell me you're.."
    "Baby" "Ma-aaah!"
    neighbour1 "You see, it's too late for this. Killing speaking babies is
    against the law."
    neighbour2 "Shit! You stupid fuck, why would you pick it up in the first
    place?!"
    
    scene bg story
    t "...not everybody was happy with your decision, but there was no going back."
    t "But before proceeding, you had to pick a name for your girl."
    call kid_name
    return

label court_notice:
    t "Few days later, you found a letter under the door..."
    scene bg home room
    show baby default:
        zoom 0.33
        xoffset 700 yoffset 270
    call court_letter
    
    scene bg story
    t "...you had no choice, but to face the consequences of your actions and
    went to the high court..."
    
    call court
    
    scene bg story
    t "...it turned out to be a fortunate session for you."
    t "The law was on your side and you were even assigned with a solid pension
    for raising a child."
    t "Next day was the last for you to go to the work until child is four years
    old..."
    
    play music "technodesert.flac"
    
    call walk_to_work
    call work
    if _return == 'kill_cord':
        t "...and then you decided this miserable community should come to an end
        and turned off the lifesupport computer..."
        jump kill_cord_ending
    
    return
