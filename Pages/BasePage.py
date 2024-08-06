from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver


    def ClearInputTextElement(self, locator):
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(locator)).find_element(*locator).clear()

    def GetAtributeElement(self, locator, atribute):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator)).find_element().get_attribute(atribute)

    def FindElementsCustom(self, locator):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator)).find_elements(*locator)

    def FindElementCustom(self, locator):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator)).find_element(*locator)

    def FindElementTagCustom(self, tag_name):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(tag_name)).find_element(tag_name)


    def TypeTextAction(self, element, text):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).send_keys(text)

    def ClickActionClicable(self, element):
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(element)).find_element(*element).click()


    def ClickActionClicable2(self, element):
        self.driver.find_elements(*element)[-1].click()

    def ClickActionLocated(self, element):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(element)).find_element(*element).click()

    def ClickActionVisibility(self, element):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).find_element(*element).click()

    def GetElementText(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).text

    def ElementEnabledStatus(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).is_enabled()

    def ElementDisabledStatus(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).is_displayed()

    def GetPageTitle(self):
        return self.driver.title



