label capitulo_1_prologo:
    # --- Início da nova história: Cena 1 - Sala de aula ---
    # Professor fala
    show professor normal at left, slowbounce
    with dissolve
    p "... então, foi assim que o Palácio da Liberdade foi construído. É uma história fascinante, mas pouco conhecida pelos mineiros de hoje."
    hide professor normal
    python:
        itens = ["atletico", "bolinho", "cruzeiro", 
        "diamante", "doce de leite", "niobio", "ouro", 
        "pao de queijo", "pastel e caldo de cana", "queijo"]

        def adicionar_item():
            random_item = renpy.random.choice(itens)
            if random_item not in inventory.slots:
                inventory.add_item(random_item, quantity=random.randint(1, 99))

        
    play sound "audio/sino_escola.ogg" 

    n "O sino toca, encerrando a aula com um som estridente."

    show professor normal at left, bounce
    with dissolve
    $ adicionar_item()
    $ adicionar_item()
    $ adicionar_item()
    $ adicionar_item()
    $ adicionar_item()
    $ adicionar_item()
    p "E por hoje é isso, pessoal. Dispensados. Menos vocês, {b}Eu{/b}, {b}Julia{/b} e {b}Aline{/b}. Precisamos conversar."
    hide professor normal

    # Aline fala
    show aline feliz at left
    with dissolve
    s  "Vish."  with hpunch 
    hide aline feliz

    # Julia fala
    show julia seria at left
    with moveinleft
    j "Lá vem..." 
    hide julia seria

    n "{b}Julia{/b} suspira e revira os olhos, terminando de colocar as coisas na mochila. O professor espera que os três se aproximem de sua mesa e pega três folhas de papel."

    show professor cansado at left
    with dissolve
    p "Meus parabéns, vocês acabaram de ganhar uma passagem direto para a {b}recuperação{/b}!"
    hide professor cansado

    # --- Escolha de resposta do jogador ---
    menu resposta_recuperacao:
        "1 - Tá de brincadeira?!":
            m "Tá de brincadeira?!"
        "2 - Recuperação? O que fizemos de errado?":
            m "Recuperação? Mas eu achei que estava me saindo bem..."
        "3 - Quem fica de recuperação em história, professor?":
            m "Quem fica de recuperação em história, professor? Nem sabia que isso era possível!"

    # Aline fala de novo
    show aline surpresa at left, bounce
    with dissolve
    s "Quem fica de recuperação em {size=30}{i} {bt=3}história{/bt}{/i}{/size}, professor? "
    hide aline surpresa

    show professor normal at left
    with dissolve
    p "Vocês três."
    hide professor normal

    n "O professor coça a cabeça, parecendo quase tão desconfortável quanto os três alunos."

    show professor pensativo at left
    with dissolve
    p "Vocês sabem que eu detesto ter que fazer isso, mas o desempenho de vocês esse semestre foi {move}péssimo{/move}. {b}Aline{/b} ficou fazendo crochê e não prestou atenção no trabalho que foi feito em sala de aula."
    hide professor pensativo

    show professor triste at left, bounce2
    with dissolve
    p "{b}Julia{/b} entregou pelo menos umas duas provas... ia dizer em branco, mas elas estavam {size=30}{b}sujas de terra.{/b}{/size} E isso porque nem tem terra dentro da sala!"
    hide professor triste

    show professor normal at left
    with dissolve
    p "E você..."
    hide professor normal

    # --- Nova escolha ---
    menu desculpa_jogador:
        "1 - Eu nem joguei tanto assim no celular durante a aula...":
            m "Eu nem joguei tanto assim no celular durante a aula..."
        "2 - É que essa mesa é tão confortável para tirar um cochilo...":
            m "É que essa mesa é tão confortável para tirar um cochilo..."
        "3 - Eu sou inocente!":
            m "Eu sou inocente! Deve ter sido um erro do sistema..."

    show professor cansado at left
    with dissolve
    p "Enfim... Não importa mais. Inês já é morta e não tem muito o que eu possa fazer por vocês."
    hide professor cansado

    show julia brava at left
    with dissolve
    j "E o que a morte da Inês tem a ver com estarmos de recuperação? Quem é Inês?"
    hide julia brava

    show aline feliz at left
    with dissolve
    s "Não fala assim da morta, {b}Julia{/b}! Meus sentimentos, professor. Era sua parente?"
    hide aline feliz

    m "Não, pessoal! Essa é uma expressão que significa que agora não adianta mais. Tipo “não adianta chorar pelo leite derramado”. Ele quis dizer que estamos mesmo ferrados."

    show aline timida at left, bounce
    with dissolve
    s "Ah."
    hide aline timida

    n "O professor segurou o riso e entregou uma folha de papel para cada. Bem no alto, em letras garrafais, estava escrito {b}“Trabalho em Grupo”{/b}."

    show julia brava at left, shake
    with dissolve
    j "Não. {glitch=1.1}{color=#0f0}{b}Tudo menos isso.{/b}{/color}{/glitch} Pode me reprovar, chamar minha mãe, o papa... quem você quiser, mas não passa trabalho em grupo! Já não basta ser recuperação, ainda é em grupo?!"
    hide julia brava

    show aline brava at left
    with dissolve
    s "É verdade! Qual a graça de fazer trabalho em grupo com quem a gente nem conhece?"
    hide aline brava

    show professor cansado at left
    with dissolve
    p "É isso ou um ensaio de 50 páginas sobre a história de Minas Gerais. À mão."
    hide professor cansado

    show aline super_saiaji at left
    with dissolve
    s "Antes estava ruim, agora piorou..."
    hide aline super_saiaji

    show professor feliz at left, laugh
    with dissolve
    p "Pensem nisso como uma forma de fazer novos amigos, que tal? Sei que vocês vão se dar bem, sem dúvida alguma."
    hide professor feliz

    # --- Escolha de formato ---
    label escolha_trabalho:
        menu escolha_formato:
            "1 - Prefiro o trabalho em grupo.":
                $ book = False
                jump apos_escolha
            "2 - Prefiro o ensaio de 50 páginas.":
                $ book = True 
                show professor normal at left
                with dissolve
                p "Eu mencionei que são 50 páginas... frente e verso?"
                hide professor normal
                m "Mudei de ideia! Pode ser o trabalho em grupo mesmo."
                $ book = False
                jump apos_escolha
            "3 - (ficar em silêncio)":
                $ book = False
                jump apos_escolha

    label apos_escolha:
        show professor normal at left
        with dissolve
        p "Enfim, vamos lá. Escolhi três cidades e três personalidades históricas de cada uma delas."
        p "O trabalho vai ser contar um pouco da história destas três cidades, pelo ponto de vista de cada uma das personalidades."
        p "Não, não quero uma apresentação de slides, um trabalho escrito ou nada do tipo. Quero que vocês ajam como se fossem essas pessoas e contem sobre suas contribuições históricas."
        hide professor normal

        show julia seria at left
        with dissolve
        j "Se eu disser o que eu acho, vão me expulsar."
        hide julia seria

        show aline feliz at left
        with dissolve
        s "Então você quer que a gente faça um teatro?! Posso ser uma árvore?!"
        hide aline feliz

        menu o_que_eu_acho:
            "1 - Parece legal!":
                jump explicacao_trabalho
            "2 - Prefiro não comentar...":
                jump explicacao_trabalho
            "3 - Não entendi, pode explicar de novo?":
                jump repetir_explicacao

    label repetir_explicacao:
        show professor normal at left
        with dissolve
        p "O trabalho vai ser contar um pouco da história destas três cidades, pelo ponto de vista de três personalidades históricas de cada uma delas. Quero que vocês ajam como se fossem essas pessoas e contem sobre suas contribuições históricas."
        hide professor normal
        jump explicacao_trabalho

    label explicacao_trabalho:
        show professor normal at left
        with dissolve
        p "Sim e não, {b}Aline{/b}, nada de cenário, figurino ou coisas do tipo. Mas quero que vocês tentem entender quem foram essas pessoas, quero que entendam de verdade. E a melhor forma de fazer isso é tentando se colocar no lugar delas..."
        hide professor normal

        show julia feliz at left
        with dissolve
        j "Do que a gente vai precisar? Deixa eu pensar... cartolina, força de vontade, uma {fi=0-0.5}máquina do tempo{/fi}... coisas bem fáceis de conseguir, professor."
        hide julia feliz

        n "O professor ignorou o comentário de {b}Julia{/b}, limpando a garganta antes de continuar."

        show professor normal at left
        with dissolve
        p "Acho que vão precisar só da {b}força de vontade{/b} de vocês e a {b}biblioteca da escola{/b}. Nada de Uiquipédia ou Chat PTG."
        p "E não adianta tentar me enganar, eu sei bem quando meus alunos pesquisaram de verdade. Os livros de que vocês vão precisar estão todos aí. Mais alguma pergunta?"
        hide professor normal

        n "O olhar que o professor lançou a eles já dizia tudo. Os três engoliram em seco, porque nunca tinham visto o professor tão sério assim."

        show professor feliz at left
        with dissolve
        p "Eu confio em vocês, pessoal... vocês sempre foram meus melhores alunos. Entendo que às vezes alguns assuntos parecem desinteressantes, mas vocês precisam dar uma chance. Vocês confiam em mim?"
        p "A história do nosso Estado é riquíssima, vocês vão se divertir fazendo o trabalho. Enfim, liberados... vocês têm duas semanas para fazer o trabalho, ok?"
        hide professor feliz

        n "O professor olha com carinho para os alunos. Ele também já esteve naquela situação, sempre tem uma matéria na escola em que não vamos muito bem e momentos em que nos interessamos menos ainda. Mas ele sabia que se sairiam bem."

    scene black with dissolve
    show text "Duas semanas! É melhor começar logo!" at truecenter with dissolve
    with Pause(2)
    n "Julia enterra a cabeça nas mãos, choramingando pela décima quinta vez. Sim, décima quinta. Aline contou cada uma delas e cronometrou o intervalo entre elas."
    play music "audio/rain.ogg" fadein 1.0 loop
    n "Uma chuva pesada caia do lado de fora, raios e trovões retumbavam e iluminavam a tarde sombria. E, como se a tarde já não estivesse sinistra o bastante, as luzes piscaram pela sexta vez. Sim, Aline contou isso também."

    # === CENA 2 – Biblioteca ===
label cena2_biblioteca:

    # Som ambiente de chuva e trovões

    play sound "audio/thunder.ogg"

    scene bg biblioteca with fade

    # Luzes piscando
    with flash
    with hpunch

    show julia saco_cheio at left
    j "Ânimo, pessoal!"
    hide julia saco_cheio
    m "Acaba, pelo amor de Deus, acaba!"

    show julia seria at left
    j "Eu poderia estar no conforto da minha casa, deitada na minha cama, enrolada nas minhas cobertas, assistindo um filminho e comendo pipoca. Mas, nãoooo... tenho que vir pra escola, no meio da chuva, ou minhas férias já eram..."
    hide julia seria

    show aline sorrindo at left
    s "Décima sexta vez..."
    hide aline sorrindo

    n "Aline murmura, adicionando mais um choramingo à sua contagem. Julia olha sem entender nada, mas logo volta a se lamentar."

    show julia saco_cheio at left
    j "Deveria ser proibido por lei ter que sair de casa na chuva, sério."
    hide julia saco_cheio

    show aline feliz at left
    s "Ah, eu gosto... Teve uma vez que caí numa poça de lama enorme enquanto tentava pegar uma lesma. Não consegui me levantar e tive que me arrastar até sair daquele monte de barro. Mas consegui pegar a lesma!"
    hide aline feliz
    
    n "Impaciente e frustrada com a situação, Julia revira os olhos e suspira."
    
    show julia brava at left
    j "Bicho do mato..."
    hide julia brava
    
    n "Julia murmura, claramente sem entender o entusiasmo de Aline por lama e lesmas."

    show aline brava at left
    with hpunch
    s "Epa, o que você disse, Julia?! Repete!"
    hide aline brava

    show julia brava at left
    j "Bicho. Do. Mato."
    hide julia brava

    show aline brava at left
    s "Pelo menos eu não fico reclamando a cada 5 segundos. Já entendemos que você quer ir pra casa!"
    hide aline brava

    m "Opa, opa, opa! Sem briga, pessoal. Nós temos que fazer o tra-..."

    n "Mas você nem consegue terminar de falar. Julia bate as mãos na mesa e se levanta de repente."

    show julia brava at left
    with vpunch
    j "Não quero. Não vou. Chega. Vou fazer sozinha. Isso SE eu fizer. Nem conheço vocês, estudo aqui há menos de dois meses, fala sério."
    hide julia brava

    n "Aline também se levanta, agarrando sua mochila como se fosse um escudo."

    show aline brava at left
    s "Também não quero fazer trabalho com essa chata!"
    hide aline brava

    show julia brava at left
    j "Chata, sério? Estamos no berçário? Pré-escola?"
    hide julia brava

    show aline brava at left
    s "Insuportável, que tal?!"
    hide aline brava

    show julia brava at left
    j "Escuta aqui, sua—"
    hide julia brava


    # Raio e trovão
    play sound "audio/thunder_strong.ogg"
    with flash
    with vpunch

    n "Mas Julia mal teve tempo de pensar em terminar a frase, um clarão rasgou os céus, seguido de um estrondo assustador que fez a terra tremer."

    m "Mas o quê..."

    # Livros caindo e vento
    play sound "audio/books_fall.ogg"
    play sound "audio/vento.ogg"
    with hpunch
    with vpunch

    n "De repente, as portas começaram a bater, livros caíam das prateleiras e o vento parecia estar... muito irritado com vocês? Todas as luzes piscaram. Uma, duas, três vezes. Até se apagarem de vez."

    # Efeito de escurecimento total
    with flash
    scene black with fade
    stop sound fadeout 1.0
    stop music fadeout 1.5

    n "E então, silêncio. O vento, a chuva e todo o barulho parou de repente. Calmaria antes da tempestade? Mas... no meio da tempestade?"

    s "Gente... o que aconteceu? Eu não tô enxergando nada!"

    m "Acho que a energia acabou...?"

    n "Mas, ainda assim, alguma coisa estava muito errada. Seus cadernos não estavam em cima da mesa. Na verdade, nem a mesa estava lá. Um arrepio em sua nuca dizia que aquele lugar não era a biblioteca da escola..."

    # Efeito de voz misteriosa surgindo
    with dissolve

    pause .5
    play sound "audio/charmes.ogg" fadein 0.5
    c "Eu {color=#00FF00}{b}odeio{/b}{/color} meu trabalho."

    jump capitulo_2_ouro_preto
