# Definição de Personagens Existentes (s, m)
define s = Character(_("Aline"), color="#f75f00", image="side")
define j = Character(_("Julia"), color="#cc4ac6", image="side") # P1 no seu roteiro
define m = Character(_("[player_name]"), color="#050579") # J (Jogador) no seu roteiro
define c = Character(_("Charmes"), color="#b90000")
# Novos Personagens para o Diálogo
define p = Character(_("Professor"), color="#27bd2e", image="side") # Novo personagem

# Narrador
define n = Character(None, window_style="narrador_window", what_style="narrador_text")

# === Imagens da personagem Aline ===
image aline assustada = "aline/aline assustada.png"
image aline brava = "aline/aline brava.png"
image aline com_fome_com_duvida = "aline/aline com fome e com duvida.png"
image aline com_triste = "aline/aline com triste.png"
image aline desinteressada = "aline/aline desinteressada.png"
image aline feliz = "aline/aline feliz.png"
image aline feliz_svg = "aline/aline feliz.svg"
image aline fez_merda = "aline/aline fez merda.png"
image aline seria = "aline/aline seria.png"
image aline sorrindo = "aline/aline sorrindo.png"
image aline super_saiaji= "aline/aline super saiajin.png"
image aline surpresa = "aline/aline surpresa.png"
image aline timida = "aline/aline timida.png"

# === Imagens da personagem Julia ===
image julia brava = "julia/julia brava.png"
image julia feliz = "julia/julia feliz.png"
image julia peixe = "julia/julia peixe.png"
image julia saco_cheio = "julia/julia saco cheio.png"
image julia seria = "julia/julia seria.png"

# === Imagens da Professor ===
image professor normal = "professora/professor normal.png"
image professor pensativo = "professora/professor pensativo.png"
image professor cansado = "professora/professor cansado.png"
image professor triste = "professora/professor triste.png"

define fastmove = MoveTransition(.2)

# musicas 
define music.escola = "audio/escola.ogg"
define music.title = "audio/inicio.ogg"

# efeitos de som
define audio.rain = "audio/rain.ogg"               # som de chuva ambiente
define audio.thunder = "audio/thunder.ogg"         # trovão normal
define audio.thunder_strong = "audio/thunder_strong.ogg" # trovão forte (impacto)
define audio.books_fall = "audio/books_fall.ogg"   # livros caindo da estante
define audio.whisper = "audio/whisper.ogg"         # voz misteriosa de Charme
define audio.suspense = "audio/suspense.ogg"       # música ambiente tensa
define audio.sino = "audio/sino escola.ogg"

# Efeitos

# Flash branco (como um relâmpago)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# Flash preto (para apagões ou cortes rápidos)
define flash_black = Fade(0.1, 0.0, 0.5, color="#000")

default player_name = ""

init python:
    itens = [
        "atletico", "bolinho", "cruzeiro",
        "diamante", "doce de leite", "niobio", "ouro",
        "pao de queijo", "pastel e caldo de cana", "queijo"
    ]

    def adicionar_item():
        random_item = renpy.random.choice(itens)
        if random_item not in inventory.slots:
            inventory.add_item(random_item, quantity=renpy.random.randint(1, 99))

transform logoappear:
    xalign .5 yalign .3 yoffset 20 alpha 0
    linear .5 alpha 1.0 yoffset 0

transform slowbounce:
    xalign 0.0
    yalign 1.0
    yoffset 0
    linear .2 yoffset 12
    linear .2 yoffset 0

transform bounce:
    xalign 0.0
    yalign 1.0
    yoffset 0
    linear .1 yoffset 12
    linear .1 yoffset 0


transform bounce2:
    xalign 0.0
    yalign 1.0
    yoffset 0
    linear .07 yoffset 12
    linear .07 yoffset 0
    linear .07 yoffset 8
    linear .07 yoffset 0

transform shake:
    xalign 0.0
    yalign 1.0
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    repeat 5
    xoffset 0

transform laugh:
    xalign 0.0
    yalign 1.0
    xoffset -10
    yoffset -10
    rotate 5
    linear 0.06 rotate -5
    linear 0.06 rotate 5
    repeat 4
    rotate 0


# Imagens de fundo e menu
default book = False
image ministerio_cultura = "gui/min-cult.png"
image pnab = "gui/pnab.png"
image mmbg = "gui/game_menu.png"
image escola = "images/bg aula.png"
image cena2_biblioteca = "images/bg biblioteca.png"

# Stats
default engraçado = 1
default grosso = 2
default fofo = 3

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
    with Pause(3)
    scene black with dissolve
    
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
    show screen gameUI
    $ player_name = renpy.call_screen("nome_input")
    if player_name:
        $ player_name = player_name.strip()
    else:
        $ player_name = "Jogador"
    $ preferences.text_cps = 40
    stop music fadeout 1.0
    scene escola
    # --- Início da nova história: Cena 1 - Sala de aula ---
    # Professor fala
    show professor normal at left, slowbounce
    with dissolve
    pause 2.0
    play music escola fadein 1.0
    p "... então, foi assim que o Palácio da Liberdade foi construído. É uma história fascinante, mas pouco conhecida pelos mineiros de hoje."
    hide professor normal
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
    p "E por hoje é isso, pessoal. Dispensados. Menos vocês, {b}[player_name]{/b}, {b}Julia{/b} e {b}Aline{/b}. Precisamos conversar."
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

    show professor normal at left
    with dissolve
    p "Vocês sabem que eu detesto ter que fazer isso, mas o desempenho de vocês esse semestre foi péssimo."
    hide professor normal

    show professor cansado at left
    with dissolve
    p "Enfim... Não importa mais."
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
    j "Não. {glitch=1.1}{color=#0f0}{b}Tudo menos isso.{/b}{/color}{/glitch} Pode me reprovar, mas não trabalho em grupo!"
    hide julia brava

    show aline brava at left
    with dissolve
    s "É verdade! Com quem a gente nem conhece?"
    hide aline brava

    show professor cansado at left
    with dissolve
    p "É isso ou um ensaio de 50 páginas sobre a história de Minas Gerais. À mão."
    hide professor cansado

    show aline super_saiaji at left
    with dissolve
    s "Antes estava ruim, agora piorou..."
    hide aline assustada

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
        p "O trabalho vai ser contar um pouco da história destas três cidades, pelo ponto de vista de três personalidades históricas de cada uma delas." 
        p "Quero que vocês ajam como se fossem essas pessoas e contem sobre suas contribuições históricas."
        hide professor normal
        jump explicacao_trabalho

    label explicacao_trabalho:
        show professor normal at left
        with dissolve
        p "Sim e não, {b}Aline{/b}, nada de cenário. Mas quero que vocês tentem entender quem foram essas pessoas."
        p "E a melhor forma de fazer isso é tentando se colocar no lugar delas..."
        hide professor normal

        show julia feliz at left
        with dissolve
        j "Do que a gente vai precisar? Deixa eu pensar... força de vontade, uma máquina do tempo..."
        hide julia feliz

        n "O professor ignorou o comentário de {b}Julia{/b}."

        show professor normal at left
        with dissolve
        p "Acho que vão precisar só da força de vontade de vocês e a biblioteca da escola."
        p "Os livros de que vocês vão precisar estão todos aí."
        hide professor normal

        n "O olhar que o professor lançou a eles já dizia tudo."

        show professor feliz at left
        with dissolve
        p "Eu confio em vocês, pessoal... vocês sempre foram meus melhores alunos." 
        p "A história do nosso Estado é riquíssima, vocês vão se divertir. Enfim, liberados... vocês têm duas semanas, ok?"
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
    j "Eu poderia estar no conforto da minha casa, assistindo um filminho. Mas tenho que vir pra escola na chuva..."
    hide julia seria

    show aline sorrindo at left
    s "Ah, eu gosto da chuva..."
    hide aline sorrindo

    n "Julia revira os olhos."

    show julia brava at left
    j "Bicho do mato..."
    hide julia brava

    show aline brava at left
    with hpunch
    s "O que você disse?!"
    hide aline brava

    show julia brava at left
    j "Bicho. Do. Mato."
    hide julia brava

    show aline brava at left
    s "Pelo menos eu não fico reclamando o tempo todo!"
    hide aline brava

    m "Opa, sem briga!"

    show julia brava at left
    with vpunch
    j "Não quero fazer trabalho com vocês. Vou fazer sozinha."
    hide julia brava

    show aline brava at left
    s "Também não quero com essa chata!"
    hide aline brava

    show julia brava at left
    j "Chata?!"
    hide julia brava

    show aline brava at left
    s "Insuportável!"
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
    play sound "audio/charmes.ogg" fadein 2.5
    c "Eu {color=#00FF00}{b}odeio{/b}{/color} meu trabalho."

label cena3_charmes:
    scene bg floresta with fade
    
    j "Quem é você??"
    s "Onde nós estamos?!"
    
    play sound "audio/thunder.opp" # Som de trovão
    c "Silêncio, crianças insolentes!"
    
    with hpunch # Efeito de tremor na tela
    
    c "Já é a 27354 vez só nesse quinquênio... será que vocês nunca aprendem?"
    c "Sempre tenho que ensinar uma lição cósmica e atemporal a todos, todos!"
    
    m "Do que você tá falando?"
    
    c "Estou falando que vocês não vão aprender da maneira tradicional!"
    
    play sound "audio/thunder.ogg"
    c "A lista de infrações dos três é gigantesca..."
    c "Não prestaram atenção nas aulas de história, desdenharam da importância dos antepassados, não levaram o professor a sério, arranjaram briga, foram desrespeitosos com os colegas, não fizeram as tarefas de casa..."

    "E, então, um homem barbudo e assustador, vestindo uma capa preta e segurando um cajado aparece diante deles."
    "Um raio, seguido de um trovão estrondoso, iluminou o ambiente: uma floresta escura e densa, cheia de árvores enormes que faziam sombras gigantescas por todos os lados."

    menu:
        "Lista de infrações? Mas você nem conhece a gente! Quem é você?":
            pass

    c "Eu conheço tudo! Sempre estou de olho nos alunos de história. Vocês foram os piores do ano."

    j "Quem disse que não?"

    c "Vocês precisam aprender uma lição."
    c "Eu sou o responsável por disciplinar alunos como vocês. Caso não consigam as três coisas que eu vou pedir, vão ficar presos no limbo temporal!"

    s "Olha, não quero ir pra lugar nenhum com essa grossa."

    m "Não vou retirar o que eu disse."

    c "Vocês só podem sair quando aprenderem a lição."

    m "E como vamos aprender?"

# Rótulo para permitir repetir a explicação
label explicacao_regras:
    c "Essa é a parte interessante. Vocês precisam me trazer 3 itens de 3 cidades mineiras diferentes... cada um deles têm um propósito."
    c "Cada uma das 3 cidades tem 3 perguntas a serem respondidas. Quando tiverem o item e responderem as 3 perguntas corretamente, podem avançar para a próxima cidade."

    j "Então são... 3 itens e 9 perguntas? Pegamos um item, respondemos as 3 perguntas e vamos para a próxima cidade?"
    s "E como vamos pra essas 3 cidades? Você sabe que Minas é grande, vamos demorar dias pra ir de carro pra cada cidade."
    s "Além disso, a gente tem 13 anos, ninguém aqui tem carro ou sabe dirigir. O senhor tem carro?"

    c "E quem disse que vocês vão de carro? Eu vou mandar vocês para o passado com meus poderes!"
    c "Vocês vão aprender em primeira mão a história de Minas Gerais."
    c "E só podem voltar quando conseguirem os itens e responderem as perguntas."

    menu:
        "Parece... interessante?":
            pass
        "Vai ter pausa pro lanche?":
            pass
        "Que chatice...":
            pass

    j "Sempre que alguém volta no tempo, não tem uma regra de que a gente não pode interferir em nada ou a linha do tempo fica bagunçada? Vi isso em algum filme."
    c "Exatamente! Vocês precisam se misturar e descobrir onde está o objeto."
    c "É proibido interferir em acontecimentos históricos."
    j "Essa última foi bem específica..."
    c "Procedimento padrão em viagens no tempo."
    s "Uai, tem um procedimento padrão?"
    c "Mas é claro que tem."

    c "Enfim! A primeira cidade é Mariana. Vocês precisam encontrar o formão de Aleijadinho. Prontos?"

    menu:
        "Acho que sim?":
            jump continuar_historia
        "Não. Não entendi nada, explica de novo!":
            jump explicacao_regras

label continuar_historia:
    c "Prontos ou não... Lá vou eu!"

    stop music fadeout 1.0
    scene black with fade
    play sound "audio/vento.ogg" # Som de transição

    "E tudo fica escuro."

    scene bg estrada_sol with flash
    
    "Sol. Lá estavam eles, à beira de uma estrada, debaixo de um sol de rachar o coco."

    j "Valha, minha nossa senhora..."
    s "Chuva, raios, trovões… E agora sol? É, o cara é poderoso, mesmo."

    return
