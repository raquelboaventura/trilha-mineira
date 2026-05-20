label capitulo_2_ouro_preto:
    # ====== CIDADE OURO PRETO =======
    # Continuação da Cena da Biblioteca para Ouro Preto
    c "Sério... Todo ano a mesma coisa. Alunos de recuperação que não sabem a diferença entre Barroco e Rococó."

    # Transição visual para a cidade
    scene bg_ouropreto with fade
    play music audio.inicio fadein 2.0

    n "O ar pesado da biblioteca é substituído pelo cheiro de café passado e pedra úmida. O sol brilha forte sobre telhados coloniais."

    show charme_normal at right with dissolve
    c "Bem-vindos a Vila Rica. Ou Ouro Preto, para os íntimos do século XXI."

    show julia brava at left, shake
    j "Vila o quê? Eu estava na biblioteca! Eu quero minha casa, agora!"

    show aline surpresa at center, bounce
    s "Gente... Olha essas roupas! As pessoas parecem... antigas? [player_name], onde é que a gente se meteu?"

    m "Eu não faço ideia, Aline. Mas aquele ali... você é o 'Charmes'?"

    c "Em carne, osso e mau humor. Para saírem daqui, vocês precisam provar que aprenderam o que o professor pediu. Bem-vindos ao seu primeiro exame prático."

    # Início do Primeiro Quiz - Ouro Preto
    label quiz_ouropreto_1:
        c "Vamos começar com o básico para ver se vocês não são casos perdidos. Como esta cidade era chamada antes de ser Ouro Preto?"

        menu:
            "A) Ouro Branco":
                jump quiz_errado_op
            "B) Vila Rica":
                jump quiz_correto_op
            "C) Vila Velha":
                jump quiz_errado_op

    label quiz_correto_op:
        $ points += 1 # Adiciona ponto se você tiver definido essa variável
        show charme_normal at right, bounce
        c "Míseros pontos para o esforço básico. Sim, Vila Rica. Fundada pela sede de riqueza dos bandeirantes no interior das Gerais."
        jump segue_historia_ouropreto

    label quiz_errado_op:
        show charme_normal at right, shake
        c "Erraram. E o professor ainda disse que vocês eram os melhores alunos dele... Que decepção."
        jump segue_historia_ouropreto

    label segue_historia_ouropreto:
        show julia seria at left
        j "Isso é loucura. A gente está em um jogo? [player_name], faz alguma coisa!"
        
        m "Se for um jogo, a gente tem que ganhar para sair. Vamos manter o foco."
        
        c "Foco é bom. Porque vocês têm visita."
        hide charme_normal with dissolve
        
        n "De repente, um homem com roupas antigas e ferramentas de escultura nas mãos se aproxima. Suas feições são marcadas pelo esforço e pela genialidade."
        
        show aleijadinho at center with dissolve
        ale "Quem são vocês, jovens? Parecem perdidos neste mar de ladeiras e pedras."
        
        show aline surpresa at left
        s "Você... você é o Antônio Francisco Lisboa? O Aleijadinho?!"
        
        ale "Vejo que minha fama cruzou os séculos. Sim, sou eu. Minha arte e minhas esculturas estão em cada canto desta terra de Vila Rica."
        
        j "Uau, nós estamos literalmente falando com a história!"
        
        ale "A história é feita de pedra, sabão e muito suor. Mas me digam, o que vieram aprender sobre nossa riqueza?"
        hide aleijadinho with dissolve

label quiz_final_cidade:
    scene bg_ouropreto
    show aline feliz at left
    
    s "Para ganharmos o último selo de Ouro Preto, precisamos responder uma última coisa!"
    
    menu:
        "Qual a principal riqueza que atraiu tanta gente para esta região?"
        
        "A mineração de Ouro":
            $ points += 1
            show aline sorrindo at left
            s "Exato! Foi a corrida do ouro que fez Vila Rica crescer tanto!"
            jump transicao_proxima_cidade
            
        "O plantio de café":
            show aline brava at left
            s "Não, o café foi importante em outras épocas e regiões! Aqui o foco era o ouro!"
            jump transicao_proxima_cidade

label transicao_proxima_cidade:
    hide aline
    show julia seria at left
    
    j "O tempo está passando. Parece que não podemos ficar parados aqui por muito tempo."
    
    n "Vocês se despedem de Ouro Preto, levando na bagagem o conhecimento da primeira cidade."
    
    stop music fadeout 2.0
    scene black with dissolve
    pause 1.0
    
    n "O cenário ao redor se dissolve como fumaça, e o chão sob os pés de vocês parece se transformar..."
    
    jump capitulo_3_tiradentes
