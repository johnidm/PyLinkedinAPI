# Python Linkedin API

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

### Created instance

```python
>>>>>>> Add get profile based in fields
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)
```

### Features
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





