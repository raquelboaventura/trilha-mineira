## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "stats/images/UI/stats_idle.png"
        action ShowMenu("StatsUI")

screen StatsUI:
    tag menu

    frame:
        background Frame("stats/images/UI/bg peach.png", 50, 50)
        xalign 0.5
        yalign 0.5
        xpadding 80
        ypadding 60

        vbox:
            spacing 30
            xalign 0.5

            text "Perfil do Mineiro" size 60 xalign 0.5
            text "[player_name]" size 56 xalign 0.5

            # Vbox para as duas seções uma acima da outra
            vbox:
                spacing 40
                xalign 0.5

                # VBox para Itens coletados (acima)
                vbox:
                    spacing 20
                    xalign 0.5

                    text "Itens coletados" size 45 xalign 0.5

                    python:
                        items = []
                        for slot in inventory.slots:
                            if slot:
                                pair = list(slot.items())[0]
                                items.append(pair)

                    if items:
                        hbox:
                            spacing 20
                            for item, qty in items:
                                vbox:
                                    spacing 5
                                    xalign 0.5
                                    hbox:
                                        spacing 10
                                        xalign 0.5
                                        add Transform(Image(f"components/inventory_system/images/icons/{item}.png"), xysize=(30, 30))
                                        text str(qty) size 30
                                    text item size 34
                    else:
                        text "Nenhum item coletado." size 34 xalign 0.5

                # Hbox para Status e Questões lado a lado
                hbox:
                    spacing 40
                    xalign 0.5

                    # VBox para Status
                    vbox:
                        spacing 20
                        xalign 0.5

                        text "Status" size 45 xalign 0.5

                        frame:
                            xpadding 20
                            ypadding 20
                            xsize 360

                            vbox:
                                spacing 18

                                for label, value in [
                                    ("engraçado", engraçado),
                                    ("grosso", grosso),
                                    ("fofo", fofo)
                                ]:
                                    hbox:
                                        spacing 18
                                        text label size 36
                                        text str(value) size 36 xalign 1.0

                    # VBox para Questões
                    vbox:
                        spacing 20
                        xalign 0.5

                        text "Questões" size 45 xalign 0.5

                        frame:
                            xpadding 20
                            ypadding 20
                            xsize 360

                            vbox:
                                spacing 18

                                text "Acertos: 10" size 36
                                text "Erros: 5" size 36

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "stats/images/UI/return_%s.png"
        action Return()
