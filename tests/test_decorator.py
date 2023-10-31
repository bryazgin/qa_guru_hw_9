import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("Find_issue_2")
@allure.severity(Severity.NORMAL)
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может найти задачу в public репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("bryazgin/qa_guru_hw_7")
    go_to_repository("bryazgin/qa_guru_hw_7")
    open_issue_tab()
    should_see_issue_with_number("#2")


@allure.step("Открываем гитхаб")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем в поиске имя репозитория")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").press_enter()


@allure.step("Кликаем на найденный репозиторий")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Выбираем таб issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем, что есть issue с номером 2")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)
