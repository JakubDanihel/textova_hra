print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Vitaj na ostrove pokladov.")
print("Tvojou ulohou je najst poklad.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


cesta = input('Nachadzas sa na krizovatke. kade sa vyberies? Napis "vpravo" alebo "vlavo" pre vybratie cesty.\n').lower()


if cesta == "vlavo":
    more = input("Po chvili cestovania si prisiel k moru. V dialke vidis ostrov. Chces preplavat na ostrov alebo pockat? Napis 'cakat' alebo 'plavat': \n").lower()

    if(more == "cakat"):
        dvere = input("Po chvili cakania k tebe priplava lod. Ked na nu nastupis tak ta privedie na ostrov. \nNa ostrove najdes stenu v ktorej je trojo dveri.\nCervene, Zlte, Modre\npre vyber napis: 'cervene', 'zlte' alebo 'modre'.\n").lower()

        if(dvere == 'zlte'):
            print("Gratulujem nasiel si poklad!")
        else:
            print("Dvere sa neotvorili a po chvili prisli vlci a zozrali ta. Koniec hry.")

    else:
        print("Po chvili snahy o plavanie a zozeru zraloky. Konie hry")
else:
    print("Prepadol si sa do diery. Koniec hry.")
