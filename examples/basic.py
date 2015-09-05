#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPIClientError
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPIInternalServerError

access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'

linkedin = PyLinkedinAPI(access_token)
print(linkedin.get_basic_profile())
print(linkedin.get_companies()) 
linkedin.publish_profile('This is my first package in Python')
linkedin.publish_comapny(5470551, 'This is my first package in Python')
