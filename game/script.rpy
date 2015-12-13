label main_menu:
    return

label start:
    $ init_player('John Doe', 0)
    $ init_walkman()
    menu:
        "character_create":
            call character_create
            "[player.His] name was [player.name], [player.he] was a good person."
        "walk to work":
            call walk_to_work
        "control_room":
            call control_room
        "court":
            call court
        "the_story":
            call the_story
        "credits":
            call credits
        "the_game":
            call the_game
    return

label the_game:
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
    call teen
    if gameover:
        return
    call adult
    return
