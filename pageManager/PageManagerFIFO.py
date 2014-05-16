from pageManager.PageManager import PageManager

class PageManagerFIFO(PageManager):
    """ Implémentation d'un Manager de Page de type FIFO
        On remplace simplement la plus vielle page
    """

    def manage(self):
        index = 0

        for p in self.pageToManage:
            # Si le slot n'est pas rempli, on ajoute la page
            if len(self.slot) < self.nbSlot:
                self.slot.append(p)
                self.nbDefaultPage += 1
            # Si la page n'est pas dans les slots, on applique l'algorithme
            elif p not in self.slot:
                self.slot[index] = p
                index = (index + 1) % self.nbSlot
                self.nbDefaultPage += 1

            self.displaySlotContent()

        self.displayNbDefaultPage()

    def displaySlotContent (self):
        buf = ""
        for e in self.slot:
            buf += str(e.id) + "\t"
        print(buf)