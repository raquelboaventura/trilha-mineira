label capitulo_4_mariana:
    scene bg_mariana with fade
    play music "audio/charmes.ogg" fadein 2.0
    
    n "O clarão ofusca a visão de vocês. Quando abrem os olhos, estão em uma praça imponente. O clima aqui é diferente, mais vibrante e caótico, mas com uma beleza antiga."

    show julia seria at left with dissolve
    j "Deixe-me adivinhar... voltamos no tempo de novo. Qual o nome dessa vila?"
    hide julia seria

    m "Pelas duas grandes igrejas na mesma praça, isso aqui deve ser Mariana! A primeira vila, cidade e capital de Minas Gerais!"

    show aline feliz at left with dissolve
    s "Mariana! Que legal! Então essa é a cidade mais antiga de todas?"
    hide aline feliz

    show deusa rindo at left with dissolve
    deusa "Sim, Aline! Vocês chegaram à Primaz de Minas. Esta é a última parada antes de voltarem para casa!"
    hide deusa

    # Aparece o Charmes
    show charmes normal at left with dissolve
    c "Exatamente. A Primaz de Minas. Fundada no auge do ciclo do ouro. E, como toda riqueza desenfreada, ela trouxe grandes histórias."
    
    n "Enquanto Charmes falava, um homem com pincéis na mão e manchas de tinta na roupa se aproxima. Ele olha para as igrejas da praça com admiração."
    
    hide charmes with dissolve
    
    show mestre_ataide at left with dissolve
    $ adicionar_item()
    ataide "Bem-vindos à minha terra, jovens. Sou Manuel da Costa Ataíde, mas muitos me conhecem como Mestre Ataíde."
    hide mestre_ataide
    
    show aline feliz at left
    s "Mestre Ataíde! O grande mestre da pintura do Rococó mineiro!"
    hide aline feliz
    
    show mestre_ataide at left
    ataide "Fico honrado que meu nome e minhas cores tenham chegado ao futuro. A arte é a nossa verdadeira herança. Dei vida a anjos e santos com a alma do nosso povo colonial."
    hide mestre_ataide
    
    m "E um enorme prazer conhecê-lo. Nós viemos para aprender mais sobre a história de Mariana."
    
    show mestre_ataide at left
    ataide "Mariana é o berço de tudo nas Gerais. A primeira capital e bispado. E também a cidade que inspirou grande parte da minha pintura e da minha vida."
    hide mestre_ataide with dissolve
    
    show charmes normal at left with dissolve
    c "Belo resumo, pintor. Mas agora é hora do teste final de vocês. O último selo da Trilha Mineira."
    
    label quiz_mariana_1:
        c "Qual é o título histórico que Mariana carrega, sendo um marco pioneiro na organização de Minas Gerais?"
        hide charmes
        
        show deusa orgulhosa at left with dissolve
        deusa "Prestem muita atenção ao que Mestre Ataíde e [player_name] comentaram! Mariana é pioneira em tudo no estado: a primeira vila, a primeira cidade, a primeira capital e o primeiro bispado!"
        hide deusa

        menu:
            "A) Foi a sede administrativa definitiva da Estrada Real":
                jump quiz_errado_ma
            "B) Foi a primeira vila, cidade, capital e bispado de Minas Gerais":
                jump quiz_correto_ma
            "C) Foi a cidade onde a Inconfidência Mineira começou":
                jump quiz_errado_ma

    label quiz_correto_ma:
        $ acertos["Mariana"] += 1
        $ points += 1
        show charmes feliz at left
        c "Correto. A Cidade Primaz. O berço de Minas. Vocês finalmente provaram que não são tão ignorantes assim."
        jump segue_historia_mariana

    label quiz_errado_ma:
        $ erros["Mariana"] += 1
        show charmes chocado at left, shake
        c "Errado. Mariana foi a pioneira em tudo no estado. A primeira vila, a primeira cidade, a primeira capital e bispado. Lembrem-se disso."
        jump segue_historia_mariana

    label segue_historia_mariana:
        hide charmes
        show julia feliz at left
        j "Acho que respondemos tudo! Já podemos voltar?"
        hide julia feliz

        show charmes normal at left with dissolve
        c "Calma lá, apressadinhos. Mariana não é só a história administrativa e pioneira das Minas Gerais."
        c "Seu maior pintor também deixou sua marca nas cores desta praça. Vocês realmente compreendem a revolução da arte colonial?"
        hide charmes

        label quiz_mariana_2:
            show charmes normal at left
            c "Manuel da Costa Ataíde, o Mestre Ataíde, revolucionou a pintura do Barroco e Rococó mineiro. Qual foi a sua principal e mais marcante inovação artística nas pinturas dos tetos das igrejas?"
            hide charmes

            show deusa orgulhosa at left with dissolve
            deusa "Ele foi um verdadeiro gênio! Olhem para os anjos pintados nos tetos: as feições e cores refletem o povo da nossa própria terra!"
            hide deusa

            menu:
                "A) Representar anjos, santos e figuras sagradas com traços mestiços, feições brasileiras e cores vivas":
                    $ acertos["Mariana"] += 1
                    $ points += 1
                    show charmes feliz at left
                    c "Excelente! Ele usou a diversidade e beleza do povo de sua terra, imortalizando feições mestiças e cores vibrantes no teto das igrejas."
                    hide charmes
                    jump conclusao_mariana

                "B) Usar exclusivamente tintas importadas da Europa para garantir que as figuras fossem totalmente brancas":
                    $ erros["Mariana"] += 1
                    show charmes chocado at left, shake
                    c "Totalmente errado. A genialidade dele estava exatamente em retratar nossa gente mestiça, e não em reproduzir o eurocentrismo."
                    hide charmes
                    jump conclusao_mariana

                "C) Abandonar a pintura religiosa para focar apenas em paisagens naturais e marinhas":
                    $ erros["Mariana"] += 1
                    show charmes chocado at left, shake
                    c "Não. Toda a sua fama e maestria foram conquistadas na pintura de temas religiosos (artes sacras) nos tetos das igrejas."
                    hide charmes
                    jump conclusao_mariana

        label conclusao_mariana:
            show julia feliz at left with dissolve
            j "Agora sim, Charmes! Mostramos que aprendemos a lição de verdade!"
            hide julia feliz

            show charmes feliz at left with dissolve
            c "Vocês aprenderam sobre o ouro com Aleijadinho e Chico Rei, sobre a revolta com Tiradentes e sobre a arte com Mestre Ataíde. O selo final é de vocês."

            n "Charmes estala os dedos. Um brilho intenso envolve vocês, muito mais forte que os anteriores."

            c "Adeus, estudantes. E prestem mais atenção nas aulas da próxima vez!"
            hide charmes

            jump epilogo
