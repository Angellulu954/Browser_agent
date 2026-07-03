from controller import BrowserController
class QuoteScraper:
    def __init__(self):
        self.controller=BrowserController()
        self.quotes=[]
    def qoutes(self):
        self.controller.goto("https://quotes.toscrape.com/")
        self.controller.get_text(".quote")
        quote=self.controller.get_all(".text")
        author=self.controller.get_all(".author")
       
        for i in range(len(quote)):
            self.quotes.append({"quote":quote[i],
                    "author":author[i]})
            
        print(self.quotes)

        
        return self.quotes
    def FindByAuthor(self,author):
        
        print(f"{author} quotes:")
        authorquote=[]
        for a in self.quotes:
                
                
                if author in a["author"]:
                    
                    authorquote.append(a["quote"])
                    
        for b in authorquote:
            print("-",b)
        
        return authorquote
    def close (self):
        return self.controller.close()

quotest=QuoteScraper()
quotest.qoutes()
result=quotest.FindByAuthor("Albert")

quotest.close()