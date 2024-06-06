class Bankomat:
    def __init__(self, poczatkowe_saldo=0):
        self.saldo = poczatkowe_saldo

    def wplata(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            print(f"Wpłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN")
        else:
            print("Kwota wpłaty musi byc większa od zera")

    def wyplata(self, kwota):
        if kwota > 0:
            if self.saldo >= kwota:
                self.saldo -= kwota
                print(f"Wypłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN")
            else:
                print("Niewystarczające środki na koncie")
        else:
            print("Kwota wypłaty musi być więszka od zera")

    def sprawdz_saldo(self):
        print(f"Aktualne saldo: {self.saldo} PLN")
        return self.saldo
