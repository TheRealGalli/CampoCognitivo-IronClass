# Core autosufficiente: nessuna dipendenza da INTELLECTUS o Iron-Class

def funzione_pubblica(x):
    """Esempio di funzione indipendente."""
    return x ** 2 + 1

class ModuloCore:
    def __init__(self, valore):
        self.valore = valore

    def elabora(self):
        return funzione_pubblica(self.valore)