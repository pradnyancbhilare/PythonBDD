import requests
import json

class GreenroomLoginApi(object):

    tokenStr = ''

    def __init__(self):
        self.url = 'https://greenroom-api.brandlive-qa.com/v2/greenroom'

    def post_producer_app_check(self, data=None):
        self.endpoint = '/check-apps-email-is-producer-for'
        url = self.url + self.endpoint
        resp = requests.post(url, data)
        print(resp.json())
        return resp.json()

    def post_producer_login(self, data=None):
        self.endpoint = '/producer/login/'
        url = self.url + self.endpoint
        resp = requests.post(url, data)
        print(resp.json())
        GreenroomLoginApi.tokenStr = resp.json()['token']
        print(f"the token value is {GreenroomLoginApi.tokenStr}")
        return resp.json()

    def get_producer_profile_channel(self, params=None):

        headers = {"bl-token":f"{GreenroomLoginApi.tokenStr}"}
        print('Header JSON is: ', headers)

        self.endpoint = '/profile/events'
        url = self.url + self.endpoint
        resp = requests.get(url, headers=headers)
        print(resp.json())
        return resp.json()