
  @greenroom_login_api
  Feature: Greenroom Login APIs

    Scenario: Test Greenroom Login APIs

      Given check the apps for the producer
      When login to Greenroom successfully
      Then get the Greenroom channels for the profile