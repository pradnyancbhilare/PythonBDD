
from behave import given, when, then, step
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig
import pdb
# start of step definitions

# @given("I go to '{page}' page")
# def go_to_the_page(context, page):
#
#     print("On the my account login page")

#==============================================================#
@step("I go to '{page}' page")
@given('I go to the site "{page}"')
def go_to_page(context, page):
    """
    Step definition to go to the specified url.
    :param context:
    :param url:
    """

    webcommon.go_to(context,page)

#========================================================================================#
@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    """
    Verifies the home page title is as expected.
    :param context:
    :param expected_title:
    :return:
    """

    webcommon.assert_page_title(context, expected_title)

#========================================================================================#
@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    """
    Verifies the current uls is as expected_url
    :param context:
    :param expected_url:
    """

    webcommon.assert_current_url(context, expected_url)