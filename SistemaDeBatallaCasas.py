import os, random
os.system("cls")

BONO_STARK = 2
BONO_LANNISTER = -3
BONO_TARGARYEN = 5
BONO_BARATHEON = 0
PODER_MIN = 1
PODER_MAX = 20

try:
    nombre = input("Ingrese su Nombre\n").title()
    edad = int(input("Ingrese su Edad\n"))
    casa = input("Ingrese casa a la que Pertenece (S-L-B-T)\n").upper()
    
    if casa == 'S' or casa == "L" or casa == "B" or casa == "T":
        poder_base = random.randint(PODER_MIN, PODER_MAX)
        
        if casa == "S":
            casa_str = "Stark"
            poder_total = poder_base + BONO_STARK
        elif casa == "L":
            casa_str = "Lannister"
            poder_total = poder_base + BONO_LANNISTER
        elif casa == "B":
            casa_str = "Baratheon"
            poder_total = poder_base + BONO_BARATHEON
        else:
            casa_str = "Targaryen"
            poder_total = poder_base + BONO_TARGARYEN

        if poder_total >= 20:
            batalla = "Victoria Epica"
        elif poder_total > 10 and poder_total < 20:
            batalla = "Victoria Ajustada"
        else:
            batalla = "Derrota"
        
        os.system("cls")
        print(f''' 
            ---------- \n
            Nombre: {nombre}\n
            Edad: {edad}\n
            Casa: {casa_str}\n
            Poder Base: {poder_base}\n
            Poder Final: {poder_total}\n
            Resultado de la Batalla: {batalla}\n
            ---------- ''')
    else:
        print("La casa ingresada no pertenece al contexto, intenta nuevamente.")
except:
    print("Valor ingresado debe ser numerico.")
    