import requests
import json


class PyLinkedinAPIClientError(Exception):
    pass


class PyLinkedinAPIInternalServerError(Exception):
    pass


class PyLinkedinAPI():

    BASE_URI_API = 'https://api.linkedin.com/v1/'

    def __init__(self, access_token):
        self.access_token = access_token
        self.default_format = 'json'

    def __factory_session(self):
        sess = requests.Session()
        return sess

    def __headers_http(self):
        headers = {'Content-Type': 'application/json', 'x-li-format': 'json'}
        return headers

    def __deserialize(self, json):
        content = json.loads(json.decode('utf-8'))
        return content

    def __publish_data_comment(self, comment):
        data = {
            "comment": comment,
            "visibility": {
                "code": "anyone"
            }
        }

        return json.dumps(data)

    def __publish_data(self, comment, **kwargs):
        title = kwargs.get('title', '')
        description = kwargs.get('description', '')
        submitted_url = kwargs.get('submitted_url', '')
        submitted_image_url = kwargs.get('submitted_image_url', '')

        data = {
            "comment": comment,
            "content": {
                "title": title,
                "description": description,
                "submitted-url": submitted_url,
                "submitted-image-url": submitted_image_url,
            },
            "visibility": {
                "code": "anyone"
            }
        }

        return json.dumps(data)

    def __build_url_get_basic_profile(self):
        url = '{url}people/~?oauth2_access_token={access_token}&format={format}'.format(
            url=self.BASE_URI_API,
            access_token=self.access_token,
            format=self.default_format)
        return url

    def __build_url_get_companies(self):
        uri = '{url}{resource}?oauth2_access_token={access_token}&format=json&is-company-admin=true'.format(
            url=self.BASE_URI_API,
            resource="companies:(id,name,logo-url,company-type)",
            access_token=self.access_token)

        return uri

    def __build_url_publish_profile(self):
        uri = '{url}{resource}?oauth2_access_token={access_token}&format=json'.format(
            url=self.BASE_URI_API,
            resource='people/~/shares',
            access_token=self.access_token)

        return uri

    def __build_url_publish_company(self, id):
        resource = 'companies/{}/shares'.format(id)

        uri = '{url}{resource}?oauth2_access_token={access_token}&format=json'.format(
            url=self.BASE_URI_API,
            resource=resource,
            access_token=self.access_token)

        return uri

    def __build_url_get_profile(self, fields):

        uri = '{url}{resource}~:({fields})?oauth2_access_token={access_token}&format=json'.format(
            url=self.BASE_URI_API,
            resource='people/',
            fields=','.join(fields),
            access_token=self.access_token)

        return uri

    def __check_response_status_code(self, resp):
        status_code = resp.status_code

        if status_code in list(range(400, 599)):
            data = json.loads(resp.content.decode('utf-8'))
            message = data['message']

            if status_code in list(range(400, 499)):
                raise PyLinkedinAPIClientError(message)
            elif status_code in list(range(500, 599)):
                raise PyLinkedinAPIInternalServerError(message)

    def __execute_request_get(self, url):
        sess = self.__factory_session()
        resp = sess.get(url, headers=self.__headers_http())
        self.__check_response_status_code(resp)
        return json.loads(resp.content.decode('utf-8'))

    def __execute_request_post(self, url, data):
        sess = self.__factory_session()
        resp = sess.post(url, data=data, headers=self.__headers_http())
        self.__check_response_status_code(resp)
        return json.loads(resp.content.decode('utf-8'))

    def get_basic_profile(self):
        url = self.__build_url_get_basic_profile()
        content = self.__execute_request_get(url)
        return content

    def get_profile(self, fields):
        url = self.__build_url_get_profile(fields)
        content = self.__execute_request_get(url)
        return content

    def get_companies(self):
        url = self.__build_url_get_companies()
        content = self.__execute_request_get(url)
        return content

    def get_detail_company(self, id):
        # https://api.linkedin.com/v1/companies/5470551:(id,name,ticker,description)?format=json
        pass

    def publish_profile(self, comment, **kwargs):
        url = self.__build_url_publish_profile()
        data = self.__publish_data(comment, **kwargs)
        return self.__execute_request_post(url, data)

    def publish_company(self, id, comment, **kwargs):
        url = self.__build_url_publish_company(id)
        data = self.__publish_data(comment, **kwargs)
        return self.__execute_request_post(url, data)

    def publish_profile_comment(self, comment):
        url = self.__build_url_publish_profile()
        data = self.__publish_data_comment(comment)
        return self.__execute_request_post(url, data)

    def publish_company_comment(self, id, comment):
        url = self.__build_url_publish_company(id)
        data = self.__publish_data_comment(comment)
        return self.__execute_request_post(url, data)
