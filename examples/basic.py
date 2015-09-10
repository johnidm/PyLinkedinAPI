#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
# from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPIClientError
# from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPIInternalServerError

access_token = 'AQU7mB9mL8MnEmy_xqkToeSwdCNJBYb0qxw_DGaJnGU2HP3zkKIlWR2mMbPwmGk_qyyjsHsmYh2iPgPwJwC7xAcnONM53GTUXPSv0xtaBrZ_w0FG5ImNmrflOHwzTe2Vx540aCWhw9v7fEL4dpgrIaXXv5PxxYCFeqmcCMOwBHZm0O-RUiA'


comment = "Hey, Do you want beer"
title = "I want beer"
description = "I want to make beer on my house"
site = "http://www.johnidouglas.com.br/"
image = "http://pngimg.com/upload/beer_PNG2383.png"


import pdb; pdb.set_trace()

# print(linkedin.get_basic_profile())
# print(linkedin.get_companies())

linkedin = PyLinkedinAPI(access_token)

json = linkedin.publish_company(5470551,
                                comment,
                                title=title,
                                description=description,
                                submitted_url=site,
                                submitted_image_url=image)

print(json)

linkedin = PyLinkedinAPI(access_token)

json = linkedin.publish_profile(comment,
                                title=title,
                                description=description,
                                submitted_url=site,
                                submitted_image_url=image)

print(json)



"""

linkedin.publish_profile('This is my first package in Python')
linkedin.publish_comapny(5470551, 'This is my first package in Python')
"""
