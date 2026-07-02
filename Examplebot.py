from controller import BrowserController
class PracticeBot:
    def __init__(self):
        self.controller=BrowserController()
    def checkpage(self,selector):
        self.controller.goto("https://example.com")
        text=self.controller.get_text(selector)
        if text=="Example Domain":
            print("Success")
        else:
            print("Failed")
        title=self.controller.title()
        print("title",title)
        self.controller.close()
        


search=PracticeBot()
search.checkpage("h1")
