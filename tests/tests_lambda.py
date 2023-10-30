import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_find_issue():
    allure.dynamic.tag("Find_issue")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь может найти задачу в public репозитории")
    allure.dynamic.link("https://github.com", name="Testing")

    with allure.step("Открываем гитхаб"):
        browser.open("https://github.com")

    with allure.step("Ищем в поиске имя репозитория"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("bryazgin/qa_guru_hw_7")
        s("#query-builder-test").press_enter()

    with allure.step("Кликаем на найденный репозиторий"):
        s(by.link_text("bryazgin/qa_guru_hw_7")).click()

    with allure.step("Выбираем таб issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем, что есть issue с номером 2"):
        s(by.partial_text("#2")).should(be.visible)