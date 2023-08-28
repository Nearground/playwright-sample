from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto('https://chat.openai.com/auth/login')
        age.locator("Log In:).wait_for()
        page.get_by_text("Log In").click()
   
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()