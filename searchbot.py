from controller import BrowserController
class SearchBot:
    def __init__(self):
        self.controller=BrowserController()
    def search(self,query):
        self.controller.goto("https://google.com")
        self.controller.type("#APjFqb",query)
        self.controller.press("#APjFqb","Enter")
        self.controller.screenshot("screenshot.png")
        self.controller.close()
        