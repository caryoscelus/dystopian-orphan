define partyhost = Character('Honorary Parent')
define teacher = Character('The Teacher')
define kid = Character('[girl.name]')

label kid:
    scene bg story
    t "Time flew past you and soon you found yourself celebrating seventh
    birthday of the girl you found..."
    
    scene bg birthday
    
    show bg birthday people as people:
        alpha 0.0
        linear 3.0 alpha 1.0
    
    pause 3.0
    
    partyhost "..We all gathered today to celebrate birthday of our beloved
    [girl.name]!"
    partyhost "I must say, she has reached a very important age."
    partyhost "She will go to The Last School very soon.."
    partyhost "Let us all pray for her successful education!"
    pause 1.0
    partyhost "Do you want to say anything, [girl.name]?"
    kid "Uhm, can i just eat the cake?"
    partyhost "..Uh, sure."
    
    scene bg story
    t "...when [girl.name] went to school, you faced new problems."
    t "Once you were summoned by teacher to talk about her behaviour..."
    
    call school
    scene bg school
    teacher "Aww, sorry, i don't have time for you know. Please wait for [girl.name] and take her home."
    pause 1.0
    show kid default:
        zoom 0.5
    kid ".."
    
    return
