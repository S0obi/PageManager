from util import SlotPage

class PageManager:
    """ Implémentation d'un Manager de Page """

    def __init__(self, listPageToManager, nbSlot=3):
        self.slot = SlotPage.SlotPage()
        self.pageToManage = listPageToManager
        self.nbSlot = nbSlot
        self.nbDefaultPage = 0

    def displayNbDefaultPage (self):
        print ("\nnbDefaultPage = " + str(self.nbDefaultPage)
               + " (" + str((self.nbDefaultPage/len(self.pageToManage)*100)) + "%)\n")

    def displaySlotContent (self):
        raise NotImplementedError

    def manage(self):
        raise NotImplementedError