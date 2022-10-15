from behave import step
from tests.backend.greenroomLogin.test_rules_logic import greenroom_login_api

@step("check the apps for the producer")
def check_apps_for_the_produer(context):
    data = {"email":"pradnyan.bhilare@brandlive.com"}
    greenroom_login_api_instance = greenroom_login_api.GreenroomLoginApi()
    response = greenroom_login_api_instance.post_producer_app_check(data)

    assert response['events_legacy_producer'] == True, "Event legacy producer is not true"
    assert response['events_producer'] == True, "Event producer is not true"
    assert response['standalone_producer'] == True, "Standalone producer is not true"

@step("login to Greenroom successfully")
def login_to_Greenroom_successfully(context):
    data = {"email":"pradnyan.bhilare@brandlive.com","password":"Pbhilare123!","app":"events","storedTwoFactorEvents":""}
    greenroom_login_api_instance = greenroom_login_api.GreenroomLoginApi()
    response = greenroom_login_api_instance.post_producer_login(data)

    assert len(response['events_channels']) > 0, "There are no channels associated with this profile"

@step("get the Greenroom channels for the profile")
def get_the_Greenroom_channels_for_the_profile(context):

    greenroom_login_api_instance = greenroom_login_api.GreenroomLoginApi()
    response = greenroom_login_api_instance.get_producer_profile_channel()

    assert len(response['events_channels']) > 0, "There are no channels associated with this profile"