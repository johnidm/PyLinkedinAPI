# Python Linkedin API



### Features
--------

* Get data profile

```
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)
    
profile = linkedin.get_basic_profile()

print(profile)
```

* Get data companies

```
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)

companies = linkedin.get_companies()

print(companies)
```

* Publish comment on profile

```    
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)

linkedin.publish_profile_comment('This is my first package in Python')
```

* Publish comment on company 


```
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)

linkedin.publish_company_comment(5470551, 'This is my first package in Python')
```

Publush Content/Comment on profile

```

from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)

linkedin.publish_profile(comment,
                         title=title,
                         description=description,
                         submitted_url='http://www.johnidouglas.com.br/',
                         submitted_image_url='http://www.johnidouglas.com.br/logo.jpeg')
```

Publush Content/Comment on company

```
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)

linkedin.publish_company(5470551,
                         comment,
                         title=title,
                         description=description,
                         submitted_url='http://www.johnidouglas.com.br/',
                         submitted_image_url='http://www.johnidouglas.com.br/logo.jpeg)

```


### Utils
--------

* REST Console
	
	https://developer.linkedin.com/rest-console





