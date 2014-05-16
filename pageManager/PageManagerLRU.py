from pageManager.PageManager import PageManager
class PageManagerLRU(PageManager):
    """ Implémentation d'un Manager de Page de type LRU
        On utilise un octet pour symboliser l'age d'une page
        - si defaut de page : on remplace la page la plus ancienne
        - sinon : on augmente l'age de page
    """

    def manage(self):
        for p in self.pageToManage:
            # Si le slot n'est pas rempli, on ajoute la page
            if len(self.slot) < self.nbSlot:
                self.slot.append(p)
                self.nbDefaultPage += 1
            # Si la page n'est pas dans le slot, on applique l'algorithme
            elif p not in self.slot:
                self.slot.replaceOldestPage(p)
                self.nbDefaultPage += 1
            # Si la page est dans le slot, on augmente l'age de toute les pages
            else:
                self.slot.increaseAgePage(p)

            self.displaySlotContent()

        self.displayNbDefaultPage()

    def displaySlotContent (self):
        buf = ""
        for e in self.slot:
            buf += str(e.id) + " " + "(" + str(e.age) + ") "
        print(buf)