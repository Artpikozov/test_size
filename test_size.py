from selene import browser, be, have

def test(setting_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('тестирование ПО').press_enter()
    browser.element('html').should(have.text('Теория тестирования ПО просто и понятно / Хабр'))
def test_1(setting_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('ea23451213grhgshv234shvrtvh43532nhstnns3245tr').press_enter()
    browser.element('html').should(have.text('привет'))