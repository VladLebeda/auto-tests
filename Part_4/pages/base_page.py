from selenium.webdriver import Remote as RemoteWebDriver


class BasePage():
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (имя исключения):
            return False
        return True