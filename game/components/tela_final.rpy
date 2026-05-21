# ==========================================
# == 🏆 Final Stats and Personality Screen ==
# ==========================================
# Beautifully displays player performance and their custom "Mineiro Type".

screen tela_final():
    modal True
    default tracking_tooltip = False
    
    mousearea:
        hovered [SetVariable("tooltip_pos", renpy.get_mouse_pos()), SetScreenVariable("tracking_tooltip", True)]
        unhovered SetScreenVariable("tracking_tooltip", False)
    
    # Pre-evaluate variables for text interpolation
    $ op_acertos = acertos["Ouro Preto"]
    $ op_erros = erros["Ouro Preto"]
    $ td_acertos = acertos["Tiradentes"]
    $ td_erros = erros["Tiradentes"]
    $ ma_acertos = acertos["Mariana"]
    $ ma_erros = erros["Mariana"]
    $ perfil = obter_tipo_mineiro(points)
    $ perfil_titulo = perfil["titulo"]
    $ perfil_desc = perfil["descricao"]
    $ player_name_upper = player_name.upper()
    
    # Dark semi-transparent background overlay
    add Solid("#120c1fdd")
    
    # Main outer frame
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 600
        background Frame("gui/bg peach.png", 30, 30)
        padding (40, 45, 40, 20)
        
        vbox:
            xalign 0.5
            spacing 12
            
            # Header Title
            text _("RELATÓRIO DA TRILHA DE [player_name_upper]") style "final_title"
            
            # Cities Stats Row
            hbox:
                xalign 0.5
                spacing 40
                
                # Ouro Preto Card
                frame:
                    style "final_city_card"
                    vbox:
                        xalign 0.5
                        spacing 5
                        text _("Ouro Preto") style "final_city_title"
                        text _("Acertos: [op_acertos]") style "final_stat_acerto"
                        text _("Erros: [op_erros]") style "final_stat_erro"
                        
                # Tiradentes Card
                frame:
                    style "final_city_card"
                    vbox:
                        xalign 0.5
                        spacing 5
                        text _("Tiradentes") style "final_city_title"
                        text _("Acertos: [td_acertos]") style "final_stat_acerto"
                        text _("Erros: [td_erros]") style "final_stat_erro"
                        
                # Mariana Card
                frame:
                    style "final_city_card"
                    vbox:
                        xalign 0.5
                        spacing 5
                        text _("Mariana") style "final_city_title"
                        text _("Acertos: [ma_acertos]") style "final_stat_acerto"
                        text _("Erros: [ma_erros]") style "final_stat_erro"
            
            # Items Row
            vbox:
                xalign 0.5
                spacing 4
                text _("ITENS COLETADOS:") style "final_items_label"
                hbox:
                    xalign 0.5
                    spacing 30
                    for slot in range(inventory.slot_count):
                        vbox:
                            spacing 5
                            xalign 0.5
                            frame:
                                xysize (60, 60)
                                xalign 0.5
                                if inventory.is_slot_unlocked(slot):
                                    background Transform("components/inventory_system/images/gui/slot_bg.png", xysize=(60, 60))
                                    if inventory.slots[slot]:
                                        for item, quantity in inventory.slots[slot].items():
                                            imagebutton:
                                                idle Transform(
                                                    Image(f"components/inventory_system/images/icons/{item}.png"),
                                                    xysize=(40, 40)
                                                )
                                                hover Transform(
                                                    Image(f"components/inventory_system/images/icons/{item}.png"),
                                                    xysize=(40, 40)
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
                                                xsize 40
                                                ysize 40
                                    else:
                                        pass
                                else:
                                    background Transform("components/inventory_system/images/gui/locked_slot_bg.png", xysize=(60, 60))
                            
                            # Item Name Label below the slot
                            if inventory.is_slot_unlocked(slot) and inventory.slots[slot]:
                                for item in inventory.slots[slot]:
                                    $ item_display_name = item.replace('_', ' ').title()
                                    text "[item_display_name]" style "final_item_name_text"
                            else:
                                text _("Vazio") style "final_item_name_text_empty"
            
            # Mineiro Type Card
            frame:
                style "final_profile_card"
                vbox:
                    xalign 0.5
                    spacing 4
                    text _("SEU PERFIL MINEIRO:") style "final_profile_label"
                    text "[perfil_titulo]" style "final_profile_title"
                    text "[perfil_desc]" style "final_profile_desc"
            
            # Actions
            textbutton _("Voltar ao Menu Principal"):
                xalign 0.5
                action MainMenu()
                style "final_menu_button"
                
    if tracking_tooltip:
        timer 0.03 repeat True action SetVariable("tooltip_pos", [p + o for p, o in zip(renpy.get_mouse_pos(), (20, -10))])
    use tooltip

# Define styles for the final screen
style final_title:
    font "fonts/Jersey25-Regular.otf"
    size 42
    color "#ffd700"
    outlines [(2, "#000000", 0, 0)]
    xalign 0.5
    text_align 0.5

style final_city_card is frame:
    background Solid("#E8D5B7")
    xsize 240
    ysize 115
    padding (15, 8)
    xalign 0.5
    yalign 0.5

style final_city_title:
    font "fonts/Quicksand-Medium.ttf"
    size 22
    bold True
    color "#A04724"
    xalign 0.5

style final_stat_acerto:
    font "fonts/Quicksand-Medium.ttf"
    size 18
    color "#3B8E1D"
    xalign 0.5

style final_stat_erro:
    font "fonts/Quicksand-Medium.ttf"
    size 18
    color "#bc3808"
    xalign 0.5

style final_profile_card is frame:
    background Solid("#2b16129c")
    xsize 890
    ysize 135
    padding (25, 10)
    xalign 0.5

style final_profile_label:
    font "fonts/Quicksand-Medium.ttf"
    size 15
    bold True
    color "#E6CEA8"
    xalign 0.5

style final_profile_title:
    font "fonts/Jersey25-Regular.otf"
    size 32
    color "#ffd700"
    outlines [(1, "#000000", 0, 0)]
    xalign 0.5

style final_profile_desc:
    font "fonts/Quicksand-Medium.ttf"
    size 16
    color "#E6CEA8"
    xalign 0.5
    text_align 0.5

style final_menu_button is button:
    background Solid("#ffd700")
    hover_background Solid("#ffea75")
    padding (24, 8)
    xalign 0.5

style final_menu_button_text is text:
    font "fonts/Quicksand-Medium.ttf"
    size 18
    bold True
    color "#120c1f"

style final_items_label:
    font "fonts/Quicksand-Medium.ttf"
    size 14
    bold True
    color "#E6CEA8"
    xalign 0.5

style final_item_name_text:
    font "fonts/Quicksand-Medium.ttf"
    size 13
    bold True
    color "#E6CEA8"
    xalign 0.5
    text_align 0.5

style final_item_name_text_empty:
    font "fonts/Quicksand-Medium.ttf"
    size 13
    color "#bda798"
    xalign 0.5
    text_align 0.5
