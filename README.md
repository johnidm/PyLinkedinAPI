Python Linkedin API
======

[![Travis CI](https://travis-ci.org/johnidm/PyLinkedinAPI.svg)](https://travis-ci.org/johnidm/PyLinkedinAPI)
[![PyPI](https://img.shields.io/pypi/v/PyLinkedinAPI.svg)](https://pypi.python.org/pypi/PyLinkedinAPI)
[![Coverage Status](https://coveralls.io/repos/johnidm/PyLinkedinAPI/badge.svg?branch=master&service=github)](https://coveralls.io/github/johnidm/PyLinkedinAPI?branch=master)

The Python Linkedin provides a easy interface to the Linkedin API.

We are in development, if you want to help, please see [CONTRIBUTING](https://github.com/johnidm/PyLinkedinAPI/blob/master/CONTRIBUTING.rst)

### Installation

You can to install through pip.

```python
pip install PyLinkedinAPI
```

### Generate Access Token

If you don't have a access token I recommend to use the [requests-oauthlib](https://github.com/requests/requests-oauthlib)

### Examples

See examples [here](https://github.com/johnidm/PyLinkedinAPI/blob/master/examples/basic.py)

You need to generate temporary access token for basic tests:

* Acces the https://developer.linkedin.com/rest-console
* On then Authentication menu select OAuth2
* After you need to login and authorization to access some information from your LinkedIn profile
* Send anywhere request URL, for example https://api.linkedin.com/v1/people/~?format=json, and copy field access token

Run `python examples/basic.py` and insert the access token

### Created an instance

```python
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI

access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'

linkedin = PyLinkedinAPI(access_token)
```

#### Features
--------

Get data profile

```python
profile = linkedin.get_basic_profile()

print(profile)
```

Get data companies

```python
companies = linkedin.get_companies()

print(companies)
```

Publish comment on profile

```python
linkedin.publish_profile_comment('This is my first package in Python')
```

Publish comment on company


```python
linkedin.publish_company_comment(5470551, 'This is my first package in Python')
```

Publush Content/Comment on profile

```python
linkedin.publish_profile(comment,
                         title=title, description=description,
                         submitted_url='http://www.johnidouglas.com.br/',
                         submitted_image_url='http://www.johnidouglas.com.br/logo.jpeg')
```

Publush Content/Comment on company

```python
linkedin.publish_company(5470551,
                         comment,
                         title=title, description=description,
                         submitted_url='http://www.johnidouglas.com.br/',
                         submitted_image_url='http://www.johnidouglas.com.br/logo.jpeg)

```


### Utils
--------

* REST Console

	https://developer.linkedin.com/rest-console





