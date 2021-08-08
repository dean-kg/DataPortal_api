import requests


class portal:
    def __init__(self, servicekey=None, endpoint_url=None):
        '''
        servicekey는 
        '''
        self.servicekey = servicekey
        self.endpoint_url = endpoint_url

    def get_data(self, **params):
        '''
        kwags는 파라미터 인자를 받아야한다. 
        '''

        params['serviceKey'] = self.servicekey
        response = requests.get(self.endpoint_url, params=params)
        if response.status_code != 200:
            print('에러')
            return

        return response
