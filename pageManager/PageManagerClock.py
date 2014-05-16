from pageManager.PageManager import PageManager

class PageManagerClock(PageManager):
    """ Implémentation d'un Manager de Page de type Clock (approximation de LRU)
        Avant de retirer une page, on lui donne une 2eme chance :
        - si bit R=0, on remplace la page
        - si bit R=1, on met le bit R=0 et on passe à la page suivante
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
                terminee = False
                while not terminee:
                    if self.slot[index].refByte == False:
                        self.slot[index] = p
                        terminee = True
                    else:
                        self.slot[index].refByte = False
                    index = (index + 1) % self.nbSlot

                self.nbDefaultPage += 1
            # Si la page est dans le slot, on met son RefByte a True
            else:
                for pageUsed in self.slot:
                    if pageUsed.id == p.id:
                        pageUsed.refByte = True
                        break

            self.displaySlotContent()

        self.displayNbDefaultPage()

    def displaySlotContent (self):
        buf = ""
        for e in self.slot:
            buf += str(e.id) + " " + "(" + str(e.refByte) + ") "
        print(buf)