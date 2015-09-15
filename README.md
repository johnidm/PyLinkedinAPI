# Python Linkedin API

### Basic use

from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
    
access_token = 'AQVaE34Qblm6uIhh3wVLXuhQPSI...'
    
linkedin = PyLinkedinAPI(access_token)


### Features
--------

* Get data profile

```    
profile = linkedin.get_basic_profile()

print(profile)
```

* Get data companies

```
companies = linkedin.get_companies()

print(companies)
```

* Publish comment on profile

```    
linkedin.publish_profile_comment('This is my first package in Python')
```

* Publish comment on company 


```
linkedin.publish_company_comment(5470551, 'This is my first package in Python')
```

Publush Content/Comment on profile

```
linkedin.publish_profile(comment,
                         title=title,
                         description=description,
                         submitted_url='http://www.johnidouglas.com.br/',
                         submitted_image_url='http://www.johnidouglas.com.br/logo.jpeg')
```

Publush Content/Comment on company

```
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





