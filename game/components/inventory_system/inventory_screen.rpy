# Guarda o texto que vai aparecer no tooltip
default tooltip_text = ""
default tracking_tooltip = False
# Guarda a posição atual do mouse
default tooltip_pos = (0, 0)
init python:
    descricoes = {
        "atletico": "⚽ Uai, é o Galo, sô!\nO Atlético Mineiro é o orgulho de muita gente em Minas.\nFundado lá em 1908, o time representa garra, paixão e aquele\njeitinho mineiro de nunca desistir.\nCê grita é 'Gaaaalooooo!' ou tá doido?",

        "bolinho": "😋 Bolinho de fubá quentinho, direto do forno!\nFeito com milho e carinho, esse trem é tradição nas casas\nmineiras desde o tempo das vovós. Acompanhado de café\ncoado, não tem erro: é amor em forma de quitanda!",

        "cruzeiro": "💙 O Cabuloso, uai!\nO Cruzeiro Esporte Clube nasceu em 1921, fundado por\nimigrantes italianos em BH. Cresceu, conquistou o Brasil e o\ncoração do povo com muito futebol bonito. Cinco estrelas no\npeito e orgulho mineiro demais da conta!",

        "diamante": "💎 Brilha mais que os olhos da vó vendo o neto comer bem!\nOs diamantes de Minas foram descobertos no século XVIII, e\no brilho dessas pedras preciosas atraiu gente do Brasil inteiro\npra cá. Até hoje, são símbolo da riqueza e da beleza das\nnossas terras.",

        "doce de leite": "🍯 Ô trem bão, sô!\nFeito com leite e açúcar, o doce de leite mineiro é famoso no\nBrasil todo. É cremoso, docim na medida certa e tem gosto de\ninfância. Dizem que quem prova uma vez, nunca mais esquece!",

        "niobio": "🔬 Trem chique demais da conta!\nO nióbio é um metal raro que Minas tem de sobra. É usado\npra deixar o aço mais forte, até em foguetes e aviões! Pouca\ngente sabe, mas o Brasil é o maior produtor do mundo.\nPotência, uai!",

        "ouro": "🏆 O ouro de Minas brilhou tanto que mudou o rumo da\nhistória!\nNo século XVIII, o Ciclo do Ouro trouxe riqueza, cidades novas\ne muita gente pra cá. Ouro Preto, Mariana e Sabará nasceram\ndesse tempo e ainda guardam o brilho da nossa história.",

        "pao de queijo": "🧀 Ah, o pão de queijo... patrimônio afetivo de Minas!\nFeito com polvilho e queijo de verdade, ele surgiu nas\nfazendas mineiras, quando as quitandeiras aproveitavam o\nrestinho do queijo pra não desperdiçar nada. Hoje é famoso\nno mundo inteiro!",

        "pastel e caldo de cana": "🥟🍹 É a dupla imbatível das feiras mineiras!\nO pastel vem quentinho e crocante, e o caldo de cana docim\ne geladinho. Essa combinação tá presente em quase toda\ncidade de Minas — é pra comer sorrindo e pedir mais um!",

        "queijo": "🧀 Queijo mineiro é tradição, história e carinho.\nDesde o século XVIII, o queijo artesanal é feito nas montanhas\nde Minas, com leite fresco e paciência. O queijo Canastra, por\nexemplo, é tão bom que virou Patrimônio Cultural do Brasil!"
    }


screen tooltip():
    if tooltip_text != "":
        $ tooltip_x = tooltip_pos[0]
        $ anchor_x = 1.0 if tooltip_x > 640 else 0.0
        $ offset_x = -15 if tooltip_x > 640 else 15
        frame:
            # background Frame("gui/tooltip_bg.png", 10, 10)  # opcional, pode trocar por uma cor
            background "#0008"
            xanchor anchor_x
            yanchor 1.0
            xoffset offset_x
            yoffset -25
            
            xpos tooltip_pos[0]
            ypos tooltip_pos[1]
            text tooltip_text style "tooltip_text_style"

screen inventory():
    modal True
    mousearea:
        hovered [SetVariable("tooltip_pos", renpy.get_mouse_pos()), SetScreenVariable("tracking_tooltip", True)]
        unhovered SetScreenVariable("tracking_tooltip", False)
    add "gui/overlay/confirm.png       "
    frame:
        style "inventory_frame"
        hbox:
            imagebutton:
                style "close_btn"
                idle "close" 
                hover "close_hover"
                action Hide("inventory")

        vbox:
            null height 95
            style "inventory_container"
            text "Trem de levar coisa" style "inventory_title"

            viewport id "vp":
                ysize 120
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_xsize 8
                vscrollbar_ysize 120
                vscrollbar_ypos 0
                vscrollbar_xpos 405
                vscrollbar_base_bar "components/inventory_system/images/gui/inv_vscrollbar_base_bar.png" 
                vscrollbar_thumb "components/inventory_system/images/gui/inv_vscrollbar_thumb.png"
                vscrollbar_unscrollable "hide"

                vpgrid cols 3:
                    style "inventory_grid"

                    for slot in range(inventory.slot_count):
                        frame:
                            xysize (120, 120)
                            if inventory.is_slot_unlocked(slot):
                                background Transform("components/inventory_system/images/gui/slot_bg.png", xysize=(120, 120))
                                if inventory.slots[slot]:
                                    for item, quantity in inventory.slots[slot].items():
                                        imagebutton:
                                            idle Transform(
                                                Image(f"components/inventory_system/images/icons/{item}.png"),
                                                xysize=(80, 80)
                                            )
                                            hover Transform(
                                                Image(f"components/inventory_system/images/icons/{item}.png"),
                                                xysize=(80, 80)
                                            )
                                            hovered [
                                                SetVariable("tooltip_text", descricoes.get(item, f"{item.replace('_', ' ').title()} — Sem descrição disponível.")),
                                                SetVariable("tooltip_pos", [p + o for p, o in zip(renpy.get_mouse_pos(), (20, -10))]),
                                                SetScreenVariable("tracking_tooltip", True)
                                            ]
                                            unhovered [
                                                SetVariable("tooltip_text", ""),
                                                SetScreenVariable("tracking_tooltip", False)
                                            ]

                                            action NullAction()
                                            xalign 0.5
                                            yalign 0.5
                                            xsize 80
                                            ysize 80

                                        $ Inv_item_name = item.replace('_', ' ')
                                        $ Inv_item_quantity = f"x{quantity}"   
                                      
                                        text Inv_item_name style "inventory_item_name"
                                        text Inv_item_quantity style "inventory_item_quantity"
                            else:
                                background Transform("components/inventory_system/images/gui/locked_slot_bg.png", xysize=(120, 120)) 
    if tracking_tooltip:
        timer 0.03 repeat True action SetVariable("tooltip_pos", [p + o for p, o in zip(renpy.get_mouse_pos(), (20, -10))])
    use tooltip