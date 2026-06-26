from playwright.sync_api import sync_playwright
print("Starting Playwright")
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://example.com")
    print("Browser Opened Succesfully")
    input("Press Enter to close... ")
    browser.close()
    