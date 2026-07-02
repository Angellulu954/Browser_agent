from controller import BrowserController
class QuoteScrapper:
    def __init__(self):
        self.controller=BrowserController()
    def qoutes(self):
        self.controller.goto("https://quotes.toscrape.com/")
        self.controller.get_text(".quote")
        print(self.controller.get_all(".text"))
        print(self.controller.get_all(".author"))
        self.controller.close()

quotest=QuoteScrapper()
quotest.qoutes()
