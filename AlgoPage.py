from pageManager.PageManagerFIFO import PageManagerFIFO
from pageManager.PageManagerClock import PageManagerClock
from pageManager.PageManagerLRU import PageManagerLRU
from util.Page import Page

page = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
#page = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

listPage = []
for p in page:
    listPage.append(Page(p))

pageManagerFIFO = PageManagerFIFO(listPage)
pageManagerFIFO.manage()

pageManagerLRU = PageManagerLRU(listPage)
pageManagerLRU.manage()

pageManagerClock = PageManagerClock(listPage)
pageManagerClock.manage()