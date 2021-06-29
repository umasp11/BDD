from behave import *
from selenium import webdriver


@given('Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")

@When('open orangeHRM homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@When('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

@When('click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()

@Then('user must login to dashboard page')
def step_impl(context):
    try:
        text=context.driver.find_element_by_xpath('//*[@id="divLogo"]/img').text()
    except:
        context.driver.close()
        assert False, 'TEst failed'
    if text== "Dashboard":
        context.driver.close()
        assert True, 'Test passed'


#raise NotImplementedError(u'STEP: Then close browser')
# To execute this go to terminal and execute  c:\....\behave Features\orange.feature








