label capitulo_4_mariana:
    scene bg_mariana with fade
    play music audio.suspense fadein 2.0
    
    n "O clarão ofusca a visão de vocês. Quando abrem os olhos, estão em uma praça imponente. O clima aqui é diferente, mais vibrante e caótico, mas com uma beleza antiga."

    show julia seria at center with dissolve
    j "Deixe-me adivinhar... voltamos no tempo de novo. Qual o nome dessa vila?"

    m "Pelas duas grandes igrejas na mesma praça, isso aqui deve ser Mariana! A primeira vila, cidade e capital de Minas Gerais!"

    show aline feliz at left with dissolve
    s "Mariana! Que legal! Então essa é a cidade mais antiga de todas?"

    # Aparece o Charmes
    show charme_normal at right with dissolve
    c "Exatamente. A Primaz de Minas. Fundada no auge do ciclo do ouro. E, como toda riqueza desenfreada, ela trouxe grandes histórias."
    
    n "Enquanto Charmes falava, um homem forte, com roupas simples mas carregando um ar de realeza e um colar marcante, caminha pela praça. Ele sorri para vocês."
    
    hide charme_normal with dissolve
    
    show chicorei at right with dissolve
    chico "Bem-vindos à minha terra. Sou Francisco, mas muitos me conhecem como Chico Rei."
    
    s "Chico Rei! O rei africano que comprou a própria liberdade e a de seu povo com o ouro das minas!"
    
    chico "Isso mesmo, pequena. A liberdade é a nossa verdadeira riqueza. Trabalhamos duro na mina da Encardideira, e lá, o ouro em pó se transformou em alforria."
    
    m "É uma honra conhecê-lo. Nós viemos aprender sobre Mariana."
    
    chico "Mariana foi o centro de tudo. O primeiro bispado. Foi aqui que a engrenagem do ouro de Minas Gerais começou a girar com toda a sua força, para o bem e para o mal."
    
    hide chicorei with dissolve
    
    show charme_normal at right with dissolve
    c "Belo resumo, majestade. Mas agora é hora do teste final de vocês. O último selo da Trilha Mineira."
    
    label quiz_mariana_1:
        c "Qual é o título histórico que Mariana carrega, sendo um marco pioneiro na organização de Minas Gerais?"

        menu:
            "A) Foi a capital do Império do Brasil.":
                jump quiz_errado_ma
            "B) Foi a primeira vila, cidade, capital e bispado de Minas Gerais.":
                jump quiz_correto_ma
            "C) Foi a cidade onde a Inconfidência Mineira começou.":
                jump quiz_errado_ma

    label quiz_correto_ma:
        $ points += 1
        show charme_normal at right, bounce
        c "Correto. A Cidade Primaz. O berço de Minas. Vocês finalmente provaram que não são tão ignorantes assim."
        jump segue_historia_mariana

    label quiz_errado_ma:
        show charme_normal at right, shake
        c "Errado. Mariana foi a pioneira em tudo no estado. A primeira vila, a primeira cidade, a primeira capital e bispado. Lembrem-se disso."
        jump segue_historia_mariana

    label segue_historia_mariana:
        show julia feliz at center
        j "Ganhamos? Acabou a recuperação?"
        
        c "Vocês aprenderam sobre o ouro com Aleijadinho, sobre a revolta com Tiradentes e sobre os pioneiros com Chico Rei. O selo final é de vocês."
        
        n "Charmes estala os dedos. Um brilho intenso envolve vocês, muito mais forte que os anteriores."
        
        c "Adeus, estudantes. E prestem mais atenção nas aulas da próxima vez!"
        
        jump epilogo
