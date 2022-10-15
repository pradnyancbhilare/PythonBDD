"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""
import time

from selenium import webdriver
from BDDCommon.CommonConfigs import urlconfig

def go_to(context, page):
    """
    Function to start instance of the specified browser and navigate to the specified url.

    :param url: the url to navigate to
    :param browser_type: the type of browser to start (Default is Firefox)

    :return: driver: browser instance
    """

    url = urlconfig.URLCONFIG.get(page)
    print("Navigating to the site: {}".format(url))

    browser_type = context.config.userdata.get('browser')

    if not browser_type:
        # create instance of Firefox driver the browser type is not specified
        conext.driver = webdriver.Firefox()
    elif browser_type.lower() == 'chrome':
        # create instance of the Chrome driver
        context.driver = webdriver.Chrome()
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    #context.driver = driver
    # clean the url and go to the url
    url = url.strip()
    context.driver.get(url)
    time.sleep(5)

    return context.driver


def assert_page_title(context, expected_title):
    """
    Function to assert title of current page.
    :param expected_title:
    :param context:
    """

    actual_title = context.driver.title

    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)
    print("The page title is as expected.")


def assert_current_url(context, expected_url):
    """
    Function to get the current url and assert it is same as the expected url.
    :param context:
    :param expected_url:
    """

    # get the current url
    current_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url, "The current url is not as expected." \
                                        " Actual: {}, Expected: {}".format(current_url, expected_url)

    print("The page url is as expected.")

#======================================================================================#
def find_element(context, locator_attribute, locator_text):
    """
    Finds an element and returns the element object.
    :param context:
    :param locator_attribute: what to use to locate (example, id, class, xpath,....)
    :param locator_text: the locator text (ex. the id, the class, the name,...)
    """

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)
    try:
        time.sleep(1)
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)
#======================================================================================#
def is_element_visible(element):
    '''
    Checks if element is visible and returns True or False
    '''

    if element.is_displayed():
        return True
    else:
        return False
#======================================================================================#
def assert_element_visible(element):
    '''
    Function to check if the passed in element is visible.
    Raises and exception if it is not exception.
    '''

    if not element.is_displayed():
        raise AssertionError('The element is not displayed')