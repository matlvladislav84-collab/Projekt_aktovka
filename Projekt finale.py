class Aktovka:
    def __init__(self):
        self.Pouzdro = []
        self.KomoraKnihy = []
        self.KomoraSesity = []
        self.KomoraVoda = []
        self.KomoraSvacina = []


# Část pro pouzdro
try:
    class Pouzdro:
        def __init__(self, objem: float, vaha: float):
            self.objem = objem
            self.vaha = vaha

    from dataclasses import dataclass

# Seznam předmětů co se můžou vložit do části Pouzdro.
    @dataclass
    class Tuzky:
        nazev: str
        objem: float
        vaha: float

    @dataclass
    class Ostatni:
        nazev: str
        objem: float
        vaha: float

except TypeError as e:
    print(e)
    print("Překontoluj třídu Pouzdro: nazev: str, objem: float, vaha: float")
except Exception as e:
    print(e)


# Komora pro vložení knih
try:
    class KomoraKnihy:
        def __init__(self, objem: float, vaha: float):
            self.objem = objem
            self.vaha = vaha

    from dataclasses import dataclass

# Seznam knih co se můžou vložit do KomoraKnihy.
    @dataclass
    class VelkeKnihy:
        nazev: str
        objem: float
        vaha: float

    @dataclass
    class MaleKnihy:
        nazev: str
        objem: float
        vaha: float

except TypeError as e:
    print(e)
    print("Překontoluj třídu Pouzdro: nazev: str, objem: float, vaha: float")
except Exception as e:
    print(e)

# Komora pro vložení sešitů
try:
    class KomoraSesity:
        def __init__(self, objem: float, vaha: float):
            self.objem = objem
            self.vaha = vaha

    from dataclasses import dataclass

# Seznam sešitů co se můžou vložit do KomoraSesity.
    @dataclass
    class VelkeSesity:
        nazev: str
        objem: float
        vaha: float

    @dataclass
    class MaleSesity:
        nazev: str
        objem: float
        vaha: float

except TypeError as e:
    print(e)
    print("Překontoluj třídu Pouzdro: nazev: str, objem: float, vaha: float")
except Exception as e:
    print(e)

# Prostor pro vodu.
try:
    class KomoraVoda:
        def __init__(self):
            self.Voda = []


except TypeError as e:
    print(e)
    print("Překontoluj třídu Pouzdro: nazev: str, objem: float, vaha: float")
except Exception as e:
    print(e)


# Prostor pro svačinu.
try:
    class KomoraSvacina:
        def __init__(self):
            self.vahy = []
            self.objemy = []
            # zadat limity přímo sem mě nenapadlo :)
            self.limitVahy = 0.5
            self.limitObjemu = 1.0

        def pridani_svacina(self, objem: float, vaha: float) -> bool:
            # pokud jsem to dobře pochopil tak se bude procházet seznam a splní se podmínka limitů tak se na základě True povolí přídání sváči?
            muzu_pridat_svacinu = True

            # do proměnné hodnoty ,,vaha_v_seznamu,, mohu načítat z externího souboru typu excel? nebo musím z listu?
            # na výběr ze seznamu svacin budou cca 3 druhy, vkladat se bude pouze 1
            # potom bych to napsal pouze takto:
            svacina_vaha = 0
            for vaha_v_seznamu in self.vahy:
                svacina_vaha = vaha_v_seznamu

            # no a teď bych jenom dal podmínky jestli splním limit váhy a objemu
            if svacina_vaha <= self.limitVahy:
                print("Svačina se váhově vejde do aktovky")
            else:
                muzu_pridat_svacinu = False
                print("Svacina se vahove nevejde do aktovky")

            # objem vložených svačin bude vždy nula aktovka je prazdná, nemá žadnou sváču
            svacina_objem = 0
            for objem_v_seznamu in self.objemy:
                svacina_objem = objem_v_seznamu

            if svacina_objem <= self.limitObjemu:
                print("Svačina se objemove vejde do komory")
            else:
                muzu_pridat_svacinu = False
                print("Svačina se objemove nevejde do komory")

            if muzu_pridat_svacinu:
                # tady to na zakladě podmínek True a False buď přidá nebo nepřidá
                self.objemy.append(objem)
                self.vahy.append(vaha)

            return muzu_pridat_svacinu
except TypeError as e:
    print(e)
    print("Překontoluj třídu Pouzdro: nazev: str, objem: float, vaha: float")
except Exception as e:
    print(e)