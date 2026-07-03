from playwright.sync_api import sync_playwright
class BrowserController:
    def __init__(self):
        self.playwright=sync_playwright().start()
        self.browser=self.playwright.chromium.launch(headless=False)
        self.page=self.browser.new_page()
      
    def close(self)   : 
        input("press enter to close....")
        self.page.close()
        self.browser.close()
        self.playwright.stop()
    
    def goto(self,url):
        self.page.goto(url)
    def screenshot(self,file):
        self.page.screenshot(path=file)   
    def get_all(self,selector):
        locates=self.page.locator(selector).all()
        s=[]
        for locate in locates:
            s.append(locate.text_content())
        return s    
         
    def title(self):
        
        return self.page.title() 
    
    def current_url(self)  :
        return self.page.url
    def click_link(self,selector):
        self.page.click(selector)
    def type(self,selector,text):
        self.page.type(selector,text)
    def press(self,selector,key):
        self.page.press(selector,key)
    def get_text(self,selector):
        return self.page.text_content(selector)
if __name__=="__main__":
    controller=BrowserController()
    controller.goto("https://example.com")
    #controller.screenshot("screenshot.png")
    title=controller.title()
    #controller.click_link("a")
    #controller.type("#APjFqb","Olivia Rodrigo")
    #controller.press("#APjFqb","Enter")
    text=controller.get_text("h1")
    print(text)

    controller.close()
    