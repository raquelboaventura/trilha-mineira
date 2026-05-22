label epilogo:
    scene bg biblioteca with fade
    play music audio.title fadein 2.0
    play sound audio.rain fadein 2.0 loop volume 0.3
    
    n "O som da chuva forte bate contra a janela. Vocês estão de volta à biblioteca da escola. Tudo está exatamente como antes."

    show aline surpresa at left with dissolve
    s "Gente... nós voltamos! Foi um sonho?"
    hide aline surpresa

    show julia seria at left with dissolve
    j "Eu não sei... Mas eu lembro de tudo. Mariana, Tiradentes, Ouro Preto..."
    hide julia seria
    
    m "Olhem a mesa!"
    
    n "Em cima da mesa, os cadernos de história estavam abertos exatamente nas páginas das personalidades que vocês conheceram. E ao lado deles..."
    
    show julia feliz at left
    j "Nossos rascunhos! O trabalho está praticamente pronto! Nós vivemos a história, escrever isso vai ser moleza!"
    hide julia feliz
    
    show aline sorrindo at left
    s "É isso aí! Quem diria que a recuperação ia ser a melhor viagem das nossas vidas?"
    hide aline sorrindo
    
    m "Acho que o professor tinha razão. A gente só precisava de 'força de vontade' e uma 'máquina do tempo'."
    
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene escola with fade
    play sound audio.sino volume 0.5
    play music audio.title fadein 1.0
    
    n "Duas semanas depois, na sala de aula."
    
    show professor feliz at left with dissolve
    p "Eu sabia que vocês conseguiriam. O trabalho de vocês ficou excelente, de longe a melhor pesquisa sobre Ouro Preto, Tiradentes e Mariana. Nota máxima para os três. Estão aprovados."
    hide professor feliz
    
    show aline feliz at left with dissolve
    s "Obrigada, professor! E obrigada, Charmes..."
    hide aline feliz
    
    show professor feliz at left
    p "Charmes? Quem é Charmes?"
    hide professor feliz
    
    m "Ninguém, professor. Apenas um amigo que nos ensinou a nunca mais dormir na aula."
    
    n "FIM DA JORNADA.\nVOCÊ COMPLETOU A TRILHA MINEIRA!"
    
    call screen tela_final
    
    return
