#label main_menu:
    #return

label start:
    $ life_prediction = 100500
    $ init_player('John Doe', int(renpy.random.random()*2))
    $ init_girl('Lilly')
    $ init_walkman()
    $ init_workman()
    $ gameover = False
    if config.developer:
        menu:
            "character_create":
                call character_create
                "[player.His] name was [player.name], [player.he] was a good person."
            "kid_name":
                call kid_name
            "walk to work":
                call walk_to_work
            "control_room":
                call control_room
            "court letter":
                call court_letter
            "court":
                call court
            "the_story":
                call the_story
            "credits":
                call credits
            "the_game":
                call the_game
    else:
        call the_game
    return

label the_game:
    scene bg story
    call character_create
    call the_story
    call credits
    return

label the_story:
    call baby
    if gameover:
        return
    call kid
    if gameover:
        return
    #call teen
    #if gameover:
        #return
    #call adult
    call game_over
    "STORY ENDS HERE :("
    return

label game_over:
    $ gameover = True
    "GAME OVER"
    return
