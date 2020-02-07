from behave import *
import assertpy

@given("I go to my login form")
def user_on_login_page(context):
    context.browser.get("http://the-internet.herokuapp.com/login")
    assert context.browser.title == "The Internet"


@when("I enter correct login information")
def user_enters_information(context):
    context.browser.find_element_by_id("username").send_keys("tomsmith")
    context.browser.find_element_by_id("password").send_keys("SuperSecretPassword!")
    context.browser.find_element_by_css_selector("#login > button > i").click()


@then("I should be logged in")
def taken_to_correct_page(context):
    assert context.browser.current_url == "http://the-internet.herokuapp.com/secure"
