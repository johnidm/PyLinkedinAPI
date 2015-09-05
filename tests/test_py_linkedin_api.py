#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import httpretty
import json
from sure import expect

from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPIClientError
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPIInternalServerError



class TestPyLinkedin(unittest.TestCase):

    def setUp(self):
        access_token = 'AQVaE34QblVhvPlUn-6zWh3YLgHjx...'
        self.linkedin = PyLinkedinAPI(access_token)
        
    @httpretty.activate
    def test_get_basic_profile(self):
         
         
        data = '''
            {
                "firstName": "Johni",
                "headline": "Full Stack Developer na Contentools",
                "id": "RzvS62YRGT",
                "lastName": "Douglas Marangon",
                "siteStandardProfileRequest":  {
                    "url": "https://www.linkedin.com/profile/view?id=275012757&authType=name&authToken=CdC0&trk=api*a3227641*s3301901*"
                }
            }
        '''
       
        httpretty.register_uri(httpretty.GET, 
                            "https://api.linkedin.com/v1/people/~?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json",
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
                  "logoUrl": "https://media.licdn.com/mpr/mpr/AAEtNDhkYQ.png",
                  "name": "Johni Corp"
                }
              ]
            }
        '''

        httpretty.register_uri(httpretty.GET, 
                            "https://api.linkedin.com/v1/companies:(id,name,logo-url,company-type)?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json&is-company-admin=true",
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
                            "https://api.linkedin.com/v1/people/~?oauth2_access_token=AQVaE34QblVhvPlUn-6zWh3YLgHjx...&format=json",
                            body=data,
                            status=403,
                            content_type="application/json")

        with self.assertRaises(PyLinkedinAPIClientError) as ex:
            self.linkedin.get_basic_profile()

        expect(str(ex.exception)).to.equal( 'Member XXXX does not have permission to get company 9898')

    @httpretty.activate
    def test_publish_profile(self):
        pass

    @httpretty.activate
    def test_publish_comapany(self):
        pass
