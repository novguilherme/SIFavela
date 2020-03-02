#Personagens
##Honoka
define hon = Character("Honoka")
###Honoka Uniforme Inverno
image iHon UI1 = "images/chara/honoka/honoka_01_01.png"
image iHon UI2 = "images/chara/honoka/honoka_01_02.png"
image iHon UI3 = "images/chara/honoka/honoka_01_03.png"
image iHon UI4 = "images/chara/honoka/honoka_01_04.png"
##Umi
define umi = Character("Umi")
###Umi Uniforme Inverno
image iUmi UI1 = "images/chara/umi/umi_01_01.png"
image iUmi UI2 = "images/chara/umi/umi_01_02.png"
image iUmi UI3 = "images/chara/umi/umi_01_03.png"
image iUmi UI4 = "images/chara/umi/umi_01_04.png"
##Kotori
define kot = Character("Kotori")
###Kotori Uniforme Inverno
image iKot UI1 = "images/chara/kotori/kotori_01_01.png"
image iKot UI2 = "images/chara/kotori/kotori_01_02.png"
image iKot UI3 = "images/chara/kotori/kotori_01_03.png"
image iKot UI4 = "images/chara/kotori/kotori_01_04.png"
#Duplas
define kotUmi = Character("Kotori e Umi")

#Cenários
##Cenários Padrões
image bgClass = "images/scenes/classroom.png"
##Cenários únicos
image c01s001 = "images/scenes/01/bg001.png"
image c01s002 = "images/scenes/01/bg002.png"

#Músicas
define bgmMain = "sounds/bgm/main story.mp3"
define bgmTuto = "sounds/bgm/tutorial.mp3"

#Balões de expressões
image bubble1 = "images/bubbles/bubble1.png"
define sBubble1 = "sounds/bubbles/bubble1.mp3"
image bubble2 = "images/bubbles/bubble2.png"
define sBubble2 = "sounds/bubbles/bubble2.mp3"
image bubble3 = "images/bubbles/bubble3.png"
define sBubble3 = "sounds/bubbles/bubble3.mp3"
image bubble4 = "images/bubbles/bubble4.png"
define sBubble4 = "sounds/bubbles/bubble4.mp3"
image bubble5 = "images/bubbles/bubble5.png"
define sBubble5 = "sounds/bubbles/bubble5.mp3"
image bubble6 = "images/bubbles/bubble6.png"
define sBubble6 = "sounds/bubbles/bubble6.mp3"
image bubble7 = "images/bubbles/bubble7.png"
define sBubble7 = "sounds/bubbles/bubble7.mp3"
image bubble8 = "images/bubbles/bubble8.png"
define sBubble8 = "sounds/bubbles/bubble8.mp3"
##Aparecer Balões
transform posBubbles:
    yalign 0.2

#Efeitos
##Variaveis Zoom
define zN = 0.8
define zAtv = 0.83
##Variaveis Posicao
define yN = 0.9
define xN = 0.5

##Position
transform posC:
    zoom zN
    yalign yN
    xalign xN
transform posR:
    zoom zN
    yalign yN
    xalign 1.5
transform posL:
    zoom zN
    yalign yN
    xalign -0.5
transform posN:
    zoom zN
    yalign yN
transform posAtv:
    zoom zAtv
    yalign yN
transform posAtvL:
    zoom zAtv
    yalign yN
    xalign -0.57
transform posAtvR:
    zoom zAtv
    yalign yN
    xalign 1.57
##Dissolves
define slowDis = Dissolve(1)
define nDis = Dissolve(.5)
define fastDis = Dissolve(.2)

# Inicio do jogo
label start:
    #Pular para cena trabalhando no momento, comentar quando for publicar no git
    #jump cap01cena002

    play music bgmMain

    scene c01s001
    with slowDis

    pause 1

    show iKot UI4 at posN:
        xalign 1.1
    show iHon UI4 at posC
    show iUmi UI4 at posN:
        xalign -0.08
    with slowDis

    show iHon at posAtv

    hon "Ô, na moral memo, alguém ae sabe ler japonês pra dizer o que está escrito?"

    show iHon UI3 at posN
    show iUmi at posAtv:
        xalign -0.12

    umi "Bom, só tá dizendo que o Criança Esperança vai parar de sustentar a escola..."

    play sound sBubble6
    show bubble6 at posBubbles:
        xalign 0.4
    with fastDis

    umi "E ela vai fechar."

    hide bubble6

    pause 0

    play sound sBubble5

    hide iHon
    with zoomout

    show iKot UI3
    show iUmi UI3
    with vpunch

    kotUmi "HONOKA!"

    scene c01s002
    with fastDis

    hon "Onde eu vou vender crack agora!?"
    hon "Eu vou quebrar velho!"

label cap01cena002:
    #stop music fadeout 1.0
    #play music bgmTuto

    scene bgClass
    show iKot UI1 at posR
    show iHon UI1 at posC
    show iUmi UI1 at posL
    with fade

    show iHon at posAtv

    hon "Calma, eu tive uma idéia!"

    show iHon UI2

    hon "Agente vai salvar a escola gravando um desenho japonês!"

    show iHon at posN
    show iUmi UI2 at posAtvL

    umi "Okay, e que tipo de desenho?"

    show iUmi at posL
    show iKot UI2 at posAtvR

    kot ""

    # Fim do jogo
    return
