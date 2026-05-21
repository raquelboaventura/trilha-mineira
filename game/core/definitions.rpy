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
define deusa = Character(_("Deusa"), color="#ffd700")

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
image professor feliz = "professora/professor feliz.png"

# === Imagens do Charmes ===
image charmes normal = "images/Charmes/charmes_normal.png"
image charmes feliz = "images/Charmes/charmes_feliz.png"
image charmes assustado = "images/Charmes/charmes_assustado.png"
image charmes chocado = "images/Charmes/charmes_chocado.png"
image charmes chorando = "images/Charmes/charmes_chorando.png"

# === Imagens da Deusa ===
image deusa brava = "images/deusa/deusa_brava.png"
image deusa orgulhosa = "images/deusa/deusa_orgulhosa.png"
image deusa rindo = "images/deusa/deusa_rindo.png"

# Fallback alias para compatibilidade
image charme_normal = "images/Charmes/charmes_normal.png"

# === Alias para Aline ===
image aline triste = "aline/aline com triste.png"

define fastmove = MoveTransition(.2)

# musicas e efeitos
define audio.rain = "audio/rain.ogg"               # som de chuva ambiente
define audio.thunder = "audio/thunder.ogg"         # trovão normal
define audio.thunder_strong = "audio/thunder_strong.ogg" # trovão forte (impacto)
define audio.books_fall = "audio/books_fall.ogg"   # livros caindo da estante
define audio.whisper = "audio/whisper.ogg"         # voz misteriosa de Charme
define audio.suspense = "audio/suspense.ogg"       # música ambiente tensa
define audio.title = "audio/inicio.ogg"
define audio.sino = "audio/sino_escola.ogg"

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
image ministerio_cultura = im.Scale("gui/min-cult.png", 1280, 720)
image pnab = im.Scale("gui/pnab.png", 1280, 720)
image mmbg = im.Scale("gui/game_menu.png", 1280, 720)
image escola = im.Scale("images/bg aula.png", 1280, 720)
image cena2_biblioteca = im.Scale("images/bg biblioteca.png", 1280, 720)
image bg biblioteca = im.Scale("images/bg biblioteca.png", 1280, 720)
image bg_ouropreto = im.Scale("images/bg_ouropreto.png", 1280, 720)
image bg_tiradentes = im.Scale("images/bg_tiradentes.png", 1280, 720)
image bg_mariana = im.Scale("images/bg_mariana.png", 1280, 720)
image aleijadinho = "images/aleijadinho.png"
image tiradentes = "images/tiradentes.png"
image chicorei = "images/chicorei.png"

default acertos = {"Ouro Preto": 0, "Tiradentes": 0, "Mariana": 0}
default erros = {"Ouro Preto": 0, "Tiradentes": 0, "Mariana": 0}

init python:
    def obter_tipo_mineiro(total_acertos):
        if total_acertos == 4:
            return {
                "titulo": "Mineiro de Ouro (Historiador de Respeito)",
                "descricao": "Cê conhece cada ladeira, cada igreja e cada detalhe da Inconfidência! Um verdadeiro guia turístico honorário. Bão demais da conta!"
            }
        elif 2 <= total_acertos <= 3:
            return {
                "titulo": "Mineiro Dedo de Prosa",
                "descricao": "Gosta de conversar e conhece a história de ouvir contar, mas às vezes se perde na prosa e confunde alguns fatos. Já merece um café com pão de queijo!"
            }
        else:
            return {
                "titulo": "Mineiro Desconfiado (Uai Cético)",
                "descricao": "Aquele que desconfia de tudo, até das próprias respostas! Prefere ficar só observando antes de palpitar. Precisa viajar mais pela Trilha Mineira!"
            }


