# Ülesanne 1
def joonista_puud(n):
    puu = [
        "   /V\\    ",
        "  / V \\   ",
        " / V V \\  ",
        "/VV V VV\\ "
    ]
    for _ in range(n):
        for rida in puu:
            print(rida, end=" ")
        print()

# Ülesanne 2
def korruta_paaritud_arvud(R):
    tulemus = 1
    for i in range(1, R+1, 2):
        tulemus *= i
    return tulemus

# Ülesanne 3
def leia_positiivsete_arvude_arv(arvud):
    arv = sum(1 for num in arvud if num > 0)
    return arv

# Ülesanne 4
def loe_paaris_paaritud_numbrid(number):
    paaritu_arv = 0
    paaritu_arv = 0
    for number in str(number):
        if int(number) % 2 == 0:
            paaritu_arv += 1
        else:
            paaritu_arv += 1
    return paaritu_arv, paaritu_arv

# Ülesanne 5
def arvude_summa(A, B):
    return sum(range(A, B+1))

# Kasutamise näide:
n = int(input("Sisestage puude arv vahemikus 1 kuni 9: "))
joonista_puud(n)

R = int(input("Sisestage arv R ülesande 2 jaoks: "))
print("Paaritute arvude korrutis kuni", R, ":", korruta_paaritud_arvud(R))

N = int(input("Sisestage arv N ülesande 3 jaoks: "))
arvud = [int(input("Sisestage arv: ")) for _ in range(N)]
print("Positiivsete arvude arv sisestatud hulgas:", leia_positiivsete_arvude_arv(arvud))

number = int(input("Sisestage looduslik arv ülesande 4 jaoks: "))
paaris_arv, paaritu_arv = loe_paaris_paaritud_numbrid(number)
print("Paarsete numbrite arv:", paaris_arv)
print("Paaritute numbrite arv:", paaritu_arv)

A = int(input("Sisestage algarv ülesande 5 jaoks: "))
B = int(input("Sisestage lõpparv ülesande 5 jaoks: "))
print("Arvude rida summa", A, "kuni", B, ":", arvude_summa(A, B))

