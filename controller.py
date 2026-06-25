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
    def title(self):
        
        return self.page.title()
           
        
controller=BrowserController()
controller.goto("https://example.com")
controller.screenshot("screenshot.png")
title=controller.title()
controller.close()
    