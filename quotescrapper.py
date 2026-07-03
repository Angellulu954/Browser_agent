from controller import BrowserController
class QuoteScraper:
    def __init__(self):
        self.controller=BrowserController()
    def qoutes(self):
        self.controller.goto("https://quotes.toscrape.com/")
        self.controller.get_text(".quote")
        quote=self.controller.get_all(".text")
        author=self.controller.get_all(".author")
        s=[]
        for i in range(len(quote)):
            s.append({"quote":quote[i],
                    "author":author[i]})
            
        print(s)
        self.controller.close()
        
        return s
    def FindByAuthor(self,author):
        self.controller.get_by_text(author,".author")
        self.controller.close()

quotest=QuoteScraper()
quotest.qoutes()
result=quotest.FindByAuthor("Albert")
print(result)