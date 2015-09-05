#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyLinkedinAPI import PyLinkedinAPI

access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'

linkedin = PyLinkedinAPI(access_token)
print(linkedin.get_basic_profile())
print(linkedin.get_companies()) specify fields
linkedin.publish_profile('This is my first package in Python')
linkedin.publish_comapny(5470551, 'This is my first package in Python')
