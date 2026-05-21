label capitulo_2_ouro_preto:
    # ====== CIDADE OURO PRETO =======
    # Continuação da Cena da Biblioteca para Ouro Preto
    c "Sério... Todo ano a mesma coisa. Alunos de recuperação que não sabem a diferença entre Barroco e Rococó."

    # Transição visual para a cidade
    scene bg_ouropreto with fade
    play music audio.inicio fadein 2.0

    n "O ar pesado da biblioteca é substituído pelo cheiro de café passado e pedra úmida. O sol brilha forte sobre telhados coloniais."

    show charmes normal at left with dissolve
    c "Bem-vindos a Vila Rica. Ou Ouro Preto, para os íntimos do século XXI."
    hide charmes

    show julia brava at left, shake
    j "Vila o quê? Eu estava na biblioteca! Eu quero minha casa, agora!"
    hide julia brava

    show aline surpresa at left
    s "Gente... Olha essas roupas! As pessoas parecem... antigas? [player_name], onde é que a gente se meteu?"
    hide aline surpresa

    m "Eu não faço ideia, Aline. Mas aquele ali... você é o 'Charmes'?"

    show charmes normal at left with dissolve
    c "Em carne, osso e mau humor. Sou Charmes, um mago que pode carregar as pessoas por entre o espaço e o tempo. Não sou bom, nem mau, apenas cumpro minhas obrigações."
    c "Para saírem daqui e retornarem ao seu tempo, vocês precisam provar que aprenderam o que o professor pediu. Bem-vindos ao seu primeiro exame prático."
    hide charmes

    # Entrada da Deusa
    show deusa brava at left with flash
    deusa "Espere, Charmes! Eu não vou deixar você prender esses estudantes aqui no passado sem ajuda!"
    hide deusa

    show charmes chocado at left, shake
    c "D-Deusa?! O que você está fazendo aqui em Vila Rica?"
    hide charmes

    show deusa orgulhosa at left with dissolve
    deusa "Eu vim defender os alunos e ajudá-los. Eu sou uma divindade bondosa e gentil, e garantirei que eles retornem ao tempo deles."
    deusa "Eu viajarei com vocês, jovens! Sempre que tiverem um quiz, darei dicas preciosas para ajudá-los a passar."
    hide deusa

    show charmes normal at left with dissolve
    c "Tsc... Faça como quiser, Deusa. Mas as regras do exame ainda são válidas. Se falharem, não haverá retorno."
    hide charmes

    # Início do Primeiro Quiz - Ouro Preto
    label quiz_ouropreto_1:
        show charmes normal at left
        c "Vamos começar com o básico para ver se vocês não são casos perdidos. Como esta cidade era chamada antes de ser Ouro Preto?"
        hide charmes
        
        show deusa rindo at left with dissolve
        deusa "Eu ajudo! Lembrem-se de que a riqueza desta região era abundante, por isso o nome da vila refletia toda essa fortuna mineral!"
        hide deusa

        menu:
            "A) Ouro Branco":
                jump quiz_errado_op
            "B) Vila Rica":
                jump quiz_correto_op
            "C) Vila Velha":
                jump quiz_errado_op

    label quiz_correto_op:
        $ acertos["Ouro Preto"] += 1
        $ points += 1 # Adiciona ponto se você tiver definido essa variável
        show charmes normal at left
        c "Míseros pontos para o effort básico. Sim, Vila Rica. Fundada pela sede de riqueza dos bandeirantes no interior das Gerais."
        jump segue_historia_ouropreto

    label quiz_errado_op:
        $ erros["Ouro Preto"] += 1
        show charmes chocado at left, shake
        c "Erraram. E o professor ainda disse que vocês eram os melhores alunos dele... Que decepção."
        jump segue_historia_ouropreto

    label segue_historia_ouropreto:
        hide charmes
        show julia seria at left
        j "Isso é loucura. A gente está em um jogo? [player_name], faz alguma coisa!"
        hide julia seria
        
        m "Se for um jogo, a gente tem que ganhar para sair. Vamos manter o foco."
        
        show charmes normal at left
        c "Foco é bom. Porque vocês têm visita."
        hide charmes with dissolve
        
        n "De repente, um homem com roupas antigas e ferramentas de escultura nas mãos se aproxima. Suas feições são marcadas pelo esforço e pela genialidade."
        
        show aleijadinho at left with dissolve
        $ adicionar_item()
        ale "Quem são vocês, jovens? Parecem perdidos neste mar de ladeiras e pedras."
        hide aleijadinho
        
        show aline surpresa at left
        s "Você... você é o Antônio Francisco Lisboa? O Aleijadinho?!"
        hide aline surpresa
        
        show aleijadinho at left
        ale "Vejo que minha fama cruzou os séculos. Sim, sou eu. Minha arte e minhas esculturas estão em cada canto desta terra de Vila Rica."
        hide aleijadinho
        
        show julia seria at left
        j "Uau, nós estamos literalmente falando com a história!"
        hide julia seria
        
        show aleijadinho at left
        ale "A história é feita de pedra, sabão e muito suor. Mas me digam, o que vieram aprender sobre nossa riqueza?"
        hide aleijadinho with dissolve

label quiz_final_cidade:
    scene bg_ouropreto
    show aline feliz at left
    
    s "Para ganharmos o último selo de Ouro Preto, precisamos responder uma última coisa!"
    hide aline feliz
    
    show deusa orgulhosa at left with dissolve
    deusa "Lembrem-se do que Aleijadinho e o povo desta terra vieram extrair nas montanhas de Vila Rica. Essa é a chave!"
    hide deusa
    
    menu:
        "Qual a principal riqueza que atraiu tanta gente para esta região?"
        
        "A mineração de Ouro":
            $ acertos["Ouro Preto"] += 1
            $ points += 1
            show aline sorrindo at left
            s "Exato! Foi a corrida do ouro que fez Vila Rica crescer tanto!"
            hide aline sorrindo
            jump transicao_proxima_cidade
            
        "O plantio de café":
            $ erros["Ouro Preto"] += 1
            show aline brava at left
            s "Não, o café foi importante em outras épocas e regiões! Aqui o foco era o ouro!"
            hide aline brava
            jump transicao_proxima_cidade

label transicao_proxima_cidade:
    show julia seria at left
    
    j "O tempo está passando. Parece que não podemos ficar parados aqui por muito tempo."
    hide julia seria
    
    n "Vocês se despedem de Ouro Preto, levando na bagagem o conhecimento da primeira cidade."
    
    stop music fadeout 2.0
    scene black with dissolve
    pause 1.0
    
    n "O cenário ao redor se dissolve como fumaça, e o chão sob os pés de vocês parece se transformar..."
    
    jump capitulo_3_tiradentes
