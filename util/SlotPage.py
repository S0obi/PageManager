class SlotPage (list):
    """ Implémentation d'un Slot pour Page Manager
    """
    def __contains__(self, item):
        for e in self:
            if e.id == item.id:
                return True
        return False

    def __str__(self):
        buf = ""
        for e in self:
            buf += str(e.id) + " " + "(Age: " + str(e.age) + ", R: " + str(e.refByte) + ") "
        return buf

    def replaceOldestPage(self, pageToAdd):
        minAge = min(p.age for p in self)
        for i, p in enumerate(self):
            if p.age == minAge:
                self[i] = pageToAdd
                break

    def increaseAgePage(self, page):
        for p in self:
            if page.id == p.id:
                p.increaseAge()
                break