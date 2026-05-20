# Definição de Personagens Existentes (s, m)
define s = Character(_("Aline"), color="#f75f00", image="side")
define j = Character(_("Julia"), color="#cc4ac6", image="side") # P1 no seu roteiro
define m = Character(_("[player_name]"), color="#050579") # J (Jogador) no seu roteiro
define c = Character(_("Charmes"), color="#b90000")
# Novos Personagens para o Diálogo
define p = Character(_("Professor"), color="#27bd2e", image="side") # Novo personagem
define ale = Character(_("Aleijadinho"), color="#a4713c")
define tira = Character(_("Tiradentes"), color="#d42c2c")
define chico = Character(_("Chico Rei"), color="#e0a92f")

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

# musicas e efeitos
define audio.rain = "audio/rain.ogg"               # som de chuva ambiente
define audio.thunder = "audio/thunder.ogg"         # trovão normal
define audio.thunder_strong = "audio/thunder_strong.ogg" # trovão forte (impacto)
define audio.books_fall = "audio/books_fall.ogg"   # livros caindo da estante
define audio.whisper = "audio/whisper.ogg"         # voz misteriosa de Charme
define audio.suspense = "audio/suspense.ogg"       # música ambiente tensa
define audio.title = "audio/inicio.ogg"
define audio.sino = "audio/sino escola.ogg"

# Efeitos

# Flash branco (como um relâmpago)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# Flash preto (para apagões ou cortes rápidos)
define flash_black = Fade(0.1, 0.0, 0.5, color="#000")

default player_name = ""
default points = 0

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
image bg_ouropreto = "images/bg_ouropreto.png"
image bg_tiradentes = "images/bg_tiradentes.png"
image bg_mariana = "images/bg_mariana.png"
image aleijadinho = "images/aleijadinho.png"
image tiradentes = "images/tiradentes.png"
image chicorei = "images/chicorei.png"


