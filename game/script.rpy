
# O label splashscreeexistente foi mantido

label splashscreen:
    scene black
    with Pause(1)

    $ renpy.movie_cutscene("gui/splash-l3.webm")
    
    scene black
    with Pause(1)

    show pnab with dissolve
    
    with Pause(2) 
    scene black
    show text "Bem-vindo ao jogo!" at truecenter with dissolve
    play music title
    with Pause(3)
    scene black with dissolve
    
    play music title fadein 1.0
    return


label showtitle:
    pause .1
    play music title
    show professor at logoappear
    pause 1
    show mmbg behind logo with Dissolve(.7)
    pause .8
    show mmbuttonframe with Dissolve(.6)
    return


# Início do Jogo e Cena 1 (Sala de Aula)

label start:
    $ player_name = renpy.call_screen("nome_input")
    if player_name:
        $ player_name = player_name.strip()
    else:
        $ player_name = "Jogador"
    n "Seja bem vindo [player_name]! Espero que você goste da história que preparamos para você."
    $ preferences.text_cps = 40
    stop music fadeout 1.0
    scene escola
    jump capitulo_1_prologo
