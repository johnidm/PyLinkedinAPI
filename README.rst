===============================
Python Linkedin API
===============================

.. image:: https://img.shields.io/travis/johnidm/PyLinkedinAPI.svg
        :target: https://travis-ci.org/johnidm/PyLinkedinAPI

.. image:: https://img.shields.io/pypi/v/PyLinkedinAPI.svg
        :target: https://pypi.python.org/pypi/PyLinkedinAPI


Python library to access Linkedin API

* Free software: BSD license
* Documentation: https://PyLinkedinAPI.readthedocs.org.

Features
--------

* Basic Use

    from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    

    access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
    linkedin = PyLinkedinAPI(access_token)
    
    print(linkedin.get_basic_profile())
    
    print(linkedin.get_companies()) specify fields
    
    linkedin.publish_profile('This is my first package in Python')
    
    linkedin.publish_comapny(5470551, 'This is my first package in Python')







