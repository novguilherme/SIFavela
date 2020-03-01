#Personagens
##Honoka
define hon = Character("Honoka")
###Honoka Uniforme Inverno
image iHon UI3 = "images/chara/honoka/honoka_01_03.png"
image iHon UI4 = "images/chara/honoka/honoka_01_04.png"
##Umi
define umi = Character("Umi")
###Umi Uniforme Inverno
image iUmi UI4 = "images/chara/umi/umi_01_04.png"
##Kotori
define kot = Character("Kotori")
###Kotori Uniforme Inverno
image iKot UI4 = "images/chara/kotori/kotori_01_04.png"

#Cenários
##Cenários Padrões
##Cenários únicos
image c01s001 = "images/scenes/01/bg001.png"

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
transform posN:
    zoom zN
    yalign yN
transform posAtv:
    zoom zAtv
    yalign yN
##Dissolves
define slowDis = Dissolve(1)
define nDis = Dissolve(.5)

# Inicio do jogo
label start:
    scene c01s001
    with slowDis

    pause 1

    show iKot UI4 at posN:
        xalign 1.1
    show iHon UI3 at posC
    show iUmi UI4 at posN:
        xalign -0.08
    with slowDis

    show iHon at posAtv

    hon "Ô, na moral memo, alguém ae sabe ler japonês pra dizer o que está escrito?"

    show iHon at posN
    show iUmi at posAtv:
        xalign -0.12

    umi "Bom, só tá dizendo que o Criança Esperança vai parar de sustentar a escola"

    show iHon UI4

    umi "E ela vai fechar"

    # Fim do jogo
    return
