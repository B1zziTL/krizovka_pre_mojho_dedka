#naimportovanie modulu
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width="450", height="200", background="white")
canvas.pack()

#otvorenie suboru
subor = open("krizovka1-1.txt","r")

#vytvorenie prazdneho slovnika
slova = {}

def precitanie(): #funkcia na precitanie info
    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        #rozdelenie riadka na hodnoty
        riadocek = riadok.split()

        #ulozenie hodnot z riadka do slovnika
        slova[riadocek[1]] = riadocek[0]

    #vratenie vyplneneho slovnika
    return slova

def vykreslenie(): #funkcia na vykreslenie krizovky
    #zadeklarovanie zaciatocnych suradnic
    x = 5
    y = 20

    #zistenie najvyssieho poctu pismen
    naj_pismena = list(slova.keys())[0]
    
    for i in range(len(slova)): #cyklus s poctom opakovani v dlzke slovnika
        #ulozenie hodnoty a kluca do premennej
        vyznacene = list(slova.values())[i]
        pismena = list(slova.keys())[i]

        #vypocitanie posunu
        posun = len(naj_pismena) - int(vyznacene)

        #zadeklarovanie pomocnej premennej
        pocitadlo = 0

        #podmienka na vypocet posunu
        if posun != 0:
            x =  20 * posun + 10
        else:
            x += 5

        for i in pismena: #cyklus na prechadzanie pismen
            #zmena pomocnej premennej
            pocitadlo += 1

            #podmienka na vykreslenie farebneho policka
            if int(vyznacene) == pocitadlo:
                #vykreslenie farebnych policok
                canvas.create_rectangle(x,y,x+20,y+20,fill="grey")
                canvas.create_rectangle(x+200,y,x+220,y+20,fill="grey")
            else:
                #vykreslenie normalnych policok
                canvas.create_rectangle(x,y,x+20,y+20)
                canvas.create_rectangle(x+200,y,x+220,y+20)

            #vykreslenie pismena
            canvas.create_text(x+210,y+10,text=i,font="Arial 15")

            #zmena x suradnice
            x += 20

        #zmena y suradnice
        y += 20

#zavolanie funkcii
precitanie()
vykreslenie()

#zatvorenie suboru
subor.close()
