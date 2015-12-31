#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import httpretty
import json

from sure import expect

from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPIClientError


class TestPyLinkedin(unittest.TestCase):

    URL_GET_BASIC_PROFILE = "https://api.linkedin.com/v1/people/~?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json"

    URL_GET_COMPANIES = "https://api.linkedin.com/v1/companies:(id,name,logo-url,company-type)?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json&is-company-admin=true"

    GET_PROFILE_ERROR_403 = "https://api.linkedin.com/v1/people/~?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json"

    GET_PROFILE_FIELDS = 'https://api.linkedin.com/v1/people/~:(id,num-connections,picture-url,email-address)?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json'

    GET_PROFILE_FIELD_NOT_FOUND = 'https://api.linkedin.com/v1/people/~:(id,num-connections,data-profile)?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json'

    POST_COMMENT_PROFILE = 'https://api.linkedin.com/v1/people/~/shares?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json'

    POST_COMMENT_COMPANY = 'https://api.linkedin.com/v1/companies/536454/shares?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json'

    POST_COMMENT_COMPANY_ERROR_403 = POST_COMMENT_COMPANY

    def setUp(self):
        access_token = 'AQVaE34QblVhvPlUn-6zWh3YLgHjx...'
        self.linkedin = PyLinkedinAPI(access_token)

    @httpretty.activate
    def test_get_basic_profile(self):

        data = '''
            {
                "id": "RzvdfgdfgGT",
                "firstName": "Johni",
                "lastName": "Douglas Marangon",
                "headline": "Senior Software Engineer",
                "siteStandardProfileRequest":  {
                    "url": "https://www.linkedin.com/profile/v..."
                }
            }
        '''

        httpretty.register_uri(httpretty.GET,
                               TestPyLinkedin.URL_GET_BASIC_PROFILE,
                               body=data,
                               content_type="application/json")

        basic_profile = self.linkedin.get_basic_profile()
        data = json.loads(data)
        expect(basic_profile).to.equal(data)

    @httpretty.activate
    def test_get_companies(self):
        data = '''
            {
              "_total": 1,
              "values":  [
                 {
                  "companyType":  {
                    "code": "O",
                    "name": "Self Owned"
                  },
                  "id": 5470551,
                  "logoUrl": "https://media.licdn.com/mpr/mpr/e34...Po.png",
                  "name": "Johni Corp"
                }
              ]
            }
        '''

        httpretty.register_uri(httpretty.GET,
                               TestPyLinkedin.URL_GET_COMPANIES,
                               body=data,
                               content_type="application/json")

        basic_profile = self.linkedin.get_companies()
        data = json.loads(data)
        expect(basic_profile).to.equal(data)

    @httpretty.activate
    def test_get_profile_error_403(self):
        data = '''
        {
              "errorCode": 0,
              "message": "Member XXXX does not have permission to get company 9898",
              "requestId": "YYYY",
              "status": 403,
              "timestamp": 1441470368132
            }
        '''

        httpretty.register_uri(httpretty.GET,
                               TestPyLinkedin.GET_PROFILE_ERROR_403,
                               body=data,
                               status=403,
                               content_type="application/json")

        with self.assertRaises(PyLinkedinAPIClientError) as ex:
            self.linkedin.get_basic_profile()

        expect(str(ex.exception)).to.equal(
            'Member XXXX does not have permission to get company 9898')

    @httpretty.activate
    def test_get_profile_fields(self):
        data = '''
            {
                "id": "RdfgsgfGT",
                "numConnections": 194,
                "pictureUrl": "https://media.licdn.com/mpr/mprx/0_v0z...jQx",
                "emailAddress": "johni@johni.com"
            }
        '''
        httpretty.register_uri(httpretty.GET,
                               TestPyLinkedin.GET_PROFILE_FIELDS,
                               body=data,
                               status=200,
                               content_type="application/json")

        basic_profile = self.linkedin.get_profile(
            ['id', 'num-connections', 'picture-url', 'email-address'])
        data = json.loads(data)
        expect(basic_profile).to.equal(data)

    @httpretty.activate
    def test_get_profile_field_not_found(self):
        data = '''
            {
              "errorCode": 0,
              "message": "Unknown field {data-profile} in resource {Person}",
              "requestId": "YUUYSSII",
              "status": 400,
              "timestamp": 1444524410254
            }
        '''

        httpretty.register_uri(httpretty.GET,
                               TestPyLinkedin.GET_PROFILE_FIELD_NOT_FOUND,
                               body=data,
                               status=400,
                               content_type="application/json")

        with self.assertRaises(PyLinkedinAPIClientError) as ex:
            self.linkedin.get_profile(
                ['id', 'num-connections', 'data-profile'])

        expect(str(ex.exception)).to.equal(
            'Unknown field {data-profile} in resource {Person}')

    @httpretty.activate
    def test_publish_comment_on_profile(self):
        response_body = '''{
            "updateKey": "UPDATE-234454664-64564654646464634502",
            "updateUrl": "https://www.linkedin.com/updates?discuss=&scope=2344546642&stype=M&topic=6456465464646463450&type=U&a=1gON"
        }'''

        httpretty.register_uri(httpretty.POST,
                               TestPyLinkedin.POST_COMMENT_PROFILE,
                               body=response_body,
                               status=201,
                               content_type="application/json")

        comment = 'A laugh a day keeps the doctor away'
        response = self.linkedin.publish_profile_comment(comment)
        actual = json.loads(response_body)
        expect(actual).to.equal(response)

    @httpretty.activate
    def test_publish_comment_on_company(self):
        response_body = '''{
            "updateKey": "UPDATE-234454664-64564654646464634502",
            "updateUrl": "https://www.linkedin.com/updates?discuss=&scope=2344546642&stype=M&topic=6456465464646463450&type=U&a=1gON"
        }'''

        httpretty.register_uri(httpretty.POST,
                               TestPyLinkedin.POST_COMMENT_COMPANY,
                               body=response_body,
                               status=201,
                               content_type="application/json")

        comment = 'Have You Tried Turning It Off And On Again?'
        response = self.linkedin.publish_company_comment(536454, comment)
        actual = json.loads(response_body)
        expect(actual).to.equal(response)

    @httpretty.activate
    def test_publish_comment_on_company_error_403(self):
        response_body = '''{
              "errorCode": 0,
              "message": "Unauthorized request",
              "requestId": "2B5UXDUSL2",
              "status": 403,
              "timestamp": 1451574899170
            }'''

        httpretty.register_uri(httpretty.POST,
                               TestPyLinkedin.POST_COMMENT_COMPANY_ERROR_403,
                               body=response_body,
                               status=403,
                               content_type="application/json")

        with self.assertRaises(PyLinkedinAPIClientError) as ex:
            comment = 'Have You Tried Turning It Off And On Again?'
            self.linkedin.publish_company_comment(536454, comment)

        expect(str(ex.exception)).to.equal(
            'Unauthorized request')

    @httpretty.activate
    def test_publish_profile(self):
        pass

    @httpretty.activate
    def test_publish_company(self):
        pass
