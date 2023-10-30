from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("bryazgin/qa_guru_hw_7")
    s("#query-builder-test").press_enter()

    s(by.link_text("bryazgin/qa_guru_hw_7")).click()

    s("#issues-tab").click()

    s(by.partial_text("#2")).should(be.visible)