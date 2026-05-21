label capitulo_3_tiradentes:
    scene bg_tiradentes with fade
    play music audio.suspense fadein 2.0
    
    n "A tontura da viagem no tempo e no espaço passa aos poucos. Agora, as ruas de pedra parecem um pouco diferentes. O ar carrega um clima tenso, quase como uma conspiração silenciosa."

    show aline surpresa at left
    with dissolve
    s "Uau... Onde a gente tá agora? Parecia Ouro Preto, mas as montanhas e as casas são diferentes."
    hide aline surpresa

    show julia seria at left
    with dissolve
    j "De acordo com as placas que não existem, estamos em algum lugar de Minas Gerais. Grande ajuda, não acha?"
    hide julia seria

    m "Peraí, eu lembro dessas ruas das fotos que o professor mostrou na aula. Isso aqui é Tiradentes!"

    show deusa rindo at left with dissolve
    deusa "Sim, [player_name]! Vocês viajaram no tempo e no espaço novamente, e caíram na bela e histórica Tiradentes."
    hide deusa

    # Aparece o Charmes
    show charmes normal at left with dissolve
    c "Exatamente. Tiradentes. Antiga Vila de São José del-Rei. Vocês não são tão desastrosos quanto eu pensava."
    hide charmes
    
    show aline feliz at left
    s "Charmes! Você veio com a gente!"
    hide aline feliz
    
    show charmes normal at left
    c "Infelizmente. O protocolo diz que eu devo acompanhar os alunos até o fim do castigo... quer dizer, da recuperação. E a próxima parada de vocês está enraizada no sangue da Inconfidência Mineira."
    hide charmes
    
    show julia seria at left
    j "Inconfidência o quê? Isso tem a ver com aquele cara... o Tiradentes, né?"
    hide julia seria
    
    show charmes normal at left
    c "Sim. Joaquim José da Silva Xavier. O mártir. Aquele que pagou o preço pelo movimento que queria libertar Minas Gerais das garras de Portugal."
    hide charmes

    m "Então foi aqui que tudo aconteceu..."

    show charmes normal at left
    c "Isso mesmo. Mas a história não é apenas feita de heróis, é feita de motivos. Aqui vai o desafio da Vila de São José. Prestem bem atenção."

    label quiz_tiradentes_1:
        c "A Inconfidência Mineira foi um movimento muito importante. Mas, o que exatamente motivou os inconfidentes a se revoltarem de forma tão extrema contra a Coroa Portuguesa?"
        hide charmes
        
        show deusa orgulhosa at left with dissolve
        deusa "Aqui vai minha dica: lembrem-se da opressão econômica da época. A Coroa exigia uma cota gigantesca de ouro e confiscava tudo se a meta não fosse atingida. Como esse imposto era chamado?"
        hide deusa

        menu:
            "A) A cobrança abusiva de impostos, especificamente a Derrama.":
                jump quiz_correto_td
            "B) A invasão de tropas francesas e espanholas no Brasil.":
                jump quiz_errado_td
            "C) A falta de incentivo à produção local de queijo e café.":
                jump quiz_errado_td

    label quiz_correto_td:
        $ acertos["Tiradentes"] += 1
        $ points += 1
        show charmes normal at left
        c "Correto. A Derrama era o verdadeiro terror da época. A coroa cobrava impostos absurdos sobre o ouro, e quando a meta não era atingida, eles simplesmente confiscavam os bens de quem trabalhou."
        jump segue_historia_tiradentes

    label quiz_errado_td:
        $ erros["Tiradentes"] += 1
        show charmes chocado at left, shake
        c "Totalmente errado. Recomendo que estudem mais se quiserem voltar para o século de vocês. A resposta certa era a cobrança opressiva de impostos e a instituição da Derrama."
        jump segue_historia_tiradentes

    label segue_historia_tiradentes:
        hide charmes
        show julia seria at left
        j "Imagina só, alguém invadir sua casa e levar as suas coisas só porque a cidade não encontrou ouro suficiente para o Rei..."
        hide julia seria
        
        show aline triste at left
        s "Isso é muito injusto! Dá até para entender por que eles ficaram tão bravos."
        hide aline triste
        
        n "Antes que pudessem continuar, uma figura imponente surge das sombras da rua. Um homem de uniforme militar, com um olhar profundo e determinado."
        
        show tiradentes at left with dissolve
        $ adicionar_item()
        tira "A injustiça, jovens, é a faísca que acende a chama da liberdade."
        hide tiradentes
        
        m "Joaquim José da Silva Xavier! O Tiradentes!"
        
        show tiradentes at left
        tira "Em carne e alma. Nós sonhamos com uma terra livre, onde nosso ouro e nosso suor não fossem roubados por coroas distantes. A Derrama era apenas o símbolo da nossa escravidão."
        hide tiradentes
        
        show julia seria at left
        j "Foi por isso que vocês planejaram a revolta, não foi?"
        hide julia seria
        
        show tiradentes at left
        tira "Sim. Sonhamos com uma república independente. Meu destino foi trágico, mas minhas ideias viveram."
        hide tiradentes with dissolve
        
        show charmes normal at left
        c "Belo discurso, não acham? Muito bem. Vocês conseguiram provar que sabem o básico sobre as motivações desta cidade."
        c "Porém, saber as causas não é a mesma coisa que conhecer os sacrifícios. Ainda há muito o que aprender em Tiradentes antes de ganharem o próximo selo."

        n "Charmes dá um sorriso torto, e a figura dele começa a desaparecer lentamente nas sombras de um beco."

        show charmes feliz at left
        c "Boa sorte, estudantes. Vocês vão precisar."
        hide charmes with dissolve

        n "Aline, Julia e você se olham. Mas não há tempo para descanso. O chão volta a tremer e a luz envolve vocês novamente..."
        
        stop music fadeout 2.0
        scene black with dissolve
        pause 1.0

        jump capitulo_4_mariana
