'''Base file for all the web elements interaction'''
import platform
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from src.driver_base import DriverBase


class WebElementsBase(DriverBase):
    """Class for selenium basic actions example: click, get_text, sendkeys,scroll etc

    Args:
        DriverBase ([class]): DriverBase class for initializing webdriver
    """

    def __init__(self, setup):
        """
        Initialise the WebElementsBase class.
        """
        super().__init__(setup)
        self.__prepare_locators()

    def __prepare_locators(self) -> None:
        """
        Function to prepare the locators dictionary for all the locators used.
        """
        self.locators_dict = dict()
        self.locators_dict["XPATH"] = By.XPATH
        self.locators_dict["ID"] = By.ID
        self.locators_dict["NAME"] = By.NAME
        self.locators_dict["TAG"] = By.TAG_NAME
        self.locators_dict["CLASS"] = By.CLASS_NAME
        self.locators_dict["CSS"] = By.CSS_SELECTOR
        self.locators_dict["LINK_TEXT"] = By.LINK_TEXT

    def __get_web_element(self,
                          locator: str,
                          locator_value: str,
                          **kwargs) -> WebElement:
        """
        Function to get the element from a webpage
        :params locator str: locator to be used to get the webelement ID, XPATH, NAME
        :params locator_value str: value of the locator which is used eg: xpath_value, id_value etc.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.
        :return webelement: The webelement specified in either xpath, name or id of an element.
        """
        timeout = kwargs.pop("timeout", 20)
        expected_condition = kwargs.pop(
            "EC", EC.presence_of_element_located)
        web_element: WebElement = WebDriverWait(self.driver, timeout).until(expected_condition((
            self.locators_dict[locator], locator_value)))
        return web_element

    def clear_text_and_sendkeys(self,
                                locator: str,
                                locator_value: str,
                                text_value: str,
                                **kwargs) -> None:
        """
        Function to clear text and send the text value to a web element.

        Usage::
            clear_text_and_sendkeys(locator="XPATH",
                                    locator_value="//input[@data-id='field-source-name']"
                                    text_value="Test_AmazonRedshift_003"
                                    timeout=30)

        :params: locator: type of the locator
        :params: locator_value: value of the locator for the webelement.
        :params: text_value: value of the text to be updated for the webelement.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.
        """
        web_element: WebElement = self.__get_web_element(locator=locator,
                                                         locator_value=locator_value,
                                                         **kwargs)
        if platform.system() == "Darwin":
            web_element.send_keys(Keys.COMMAND + "a")
        else:
            web_element.send_keys(Keys.CONTROL + "a")

        web_element.send_keys(Keys.DELETE)
        sleep(1)
        web_element.send_keys(text_value)

    def clear_text(self,
                   locator: str,
                   locator_value: str,
                   **kwargs) -> None:
        """
        Function to clear text and send the text value to a web element.

        Usage::
            clear_text( locator="XPATH",
                        locator_value="//input[@data-id='field-source-name']"
                        timeout=30)

        :params: locator: type of the locator
        :params: locator_value: value of the locator for the webelement.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.
        """
        web_element: WebElement = self.__get_web_element(locator=locator,
                                                         locator_value=locator_value,
                                                         **kwargs)

        if platform.system() == "Darwin":
            web_element.send_keys(Keys.COMMAND + "a")
        else:
            web_element.send_keys(Keys.CONTROL + "a")
        web_element.send_keys(Keys.DELETE)

    def sendkeys(self,
                 locator: str,
                 locator_value: str,
                 text_value: str,
                 **kwargs) -> None:
        """
        Function to clear text and send the text value to a web element.

        Usage::
            sendkeys(locator="XPATH",
                                    locator_value="//input[@data-id='field-source-name']"
                                    text_value="Test_AmazonRedshift_003"
                                    timeout=30)

        :params: locator: type of the locator
        :params: locator_value: value of the locator for the webelement.
        :params: text_value: value of the text to be updated for the webelement.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.
        """
        web_element: WebElement = self.__get_web_element(locator=locator,
                                                         locator_value=locator_value,
                                                         **kwargs)
        web_element.send_keys(text_value)

    def click_element(self,
                      locator: str,
                      locator_value: str,
                      **kwargs) -> None:
        '''
        Function to click a button at a given xpath.
        Usage::
            click_element(locator="ID",
                         locator_value="severity-filter"
                         timeout=30)

        :params: locator: type of the locator
        :params: locator_value: value of the locator for the webelement.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.
        '''

        button_to_click: WebElement = self.__get_web_element(
            locator, locator_value, **kwargs)
        try:
            webelement = button_to_click.click()
        except Exception:
            webelement = self.driver.execute_script(
                "arguments[0].click();", button_to_click)
        return webelement

    def get_text(self,
                 locator: str,
                 locator_value: str,
                 **kwargs) -> str:
        '''
        Function to get the text value of a webelement
        Usage::
            get_text(locator="NAME",
                     locator_value="frequency"
                     timeout=30)
        :params: locator: type of the locator
        :params: locator_value: value of the locator for the webelement.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.

        Returns the text value of a webelement.
        '''

        web_element: WebElement = self.__get_web_element(
            locator, locator_value, **kwargs)
        return web_element.text

    def get_attribute_web_element(self,
                                  locator: str,
                                  locator_value: str,
                                  attribute_name: str,
                                  **kwargs) -> str:
        '''
        Function to get the attribute value of a web element.

        Usage::
            get_attribute_web_element(locator="NAME",
                                      locator_value="frequency",
                                      attribute_name="attribute1",
                                      timeout=30)
        :param locator: type of the locator
        :param locator_value: value of the locator for the webelement.
        :param attribute_name: name of the attribute of the webelement
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.

        Returns the attribute value of a webelement
        '''

        web_element: WebElement = self.__get_web_element(
            locator, locator_value, **kwargs)
        return web_element.get_attribute(attribute_name)

    def scroll_till_element(self,
                            locator: str,
                            locator_value: str,
                            **kwargs) -> None:
        '''
        Function to get the attribute value of a web element.

        Usage::
            get_attribute_web_element(locator="NAME",
                                      locator_value="frequency",
                                      attribute_name="attribute1",
                                      timeout=30)
        :param locator: type of the locator
        :param locator_value: value of the locator for the webelement.
        :param attribute_name: name of the attribute of the webelement
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.

        Returns the attribute value of a webelement
        '''
        web_element: WebElement = self.__get_web_element(
            locator, locator_value, **kwargs)
        actions = ActionChains(self.driver)
        actions.move_to_element(web_element).perform()

    def wait_until_element_visible(self,
                                   locator: str,
                                   locator_value: str,
                                   **kwargs) -> WebElement:
        '''
        Function to wait untill element is visible.

        Usage::
            wait_until_element_visible(locator="NAME",
                                      locator_value="frequency",
                                      timeout=30)
        :param locator: type of the locator
        :param locator_value: value of the locator for the webelement.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.

        Returns the attribute value of a webelement
        '''
        web_element: WebElement = self.__get_web_element(
            locator, locator_value, **kwargs)
        return web_element

    def read_toggle_state(self,
                          locator: str,
                          **kwargs) -> WebElement:
        '''
        Function to get state of toggle element.

        Usage::
            wait_until_element_visible(locator="NAME",
                                      locator_value="frequency",
                                      timeout=30)
        :param locator: type of the locator
        :param locator_value: value of the locator for the webelement.
        :params kwargs: keyword arguments
            key timeout int: timeout in seconds.

        Returns the state of a webelement:True/False
        '''
        web_element: WebElement = self.__get_web_element(
            locator, **kwargs)
        return web_element.is_selected()

    def browser_back(self):
        """Function to navigate the browser back"""
        self.driver.back()

    def refresh_page(self):
        """Function to refresh the Page"""
        self.driver.refresh()
