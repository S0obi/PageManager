class Page:
    """ Implémentation d'une Page mémoire
        id  : Identifiant de la page
        age : Age de la page (LRU)
        lastMSB : Dernier bit le plus significatif (LRU)
        refByte : bit de référence (Clock)
    """

    def __init__(self, ident):
        self.id = ident
        self.age = 0
        self.lastMSB = 2**8
        self.refByte = True

    def increaseAge (self):
        if self.lastMSB == 0:
            raise OverflowError("L'age d'une page est stocké sur 8 bits")

        self.age += self.lastMSB
        self.lastMSB //= 2
