============
Contributing
============

Contributions are welcome, you can contribute in many ways:

Types of Contributions
----------------------

Report Bugs, Fix Bugs and Implement Features
~~~~~~~~~~~

Look through the GitHub issues, https://github.com/johnidm/PyLinkedinAPI/issues, for bugs and improvements.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Python Linkedin API could always use more documentation, whether as part of the
official Python Linkedin API docs, in docstrings, or even on the web in blog posts,
articles, and such.

Get Started!
------------

Ready to contribute? Here's how to set up `PyLinkedinAPI` for local development.

1. Fork the `PyLinkedinAPI` repo on GitHub.
2. Clone your fork locally::

    $ git clone https://github.com/johnidm/PyLinkedinAPI.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ pyenv virtualenv venv-PyLinkedinAPI
    $ pyenv activate venv-PyLinkedinAPI
    $ cd PyLinkedinAPI/
    $ python setup.py develop

4. You need to generate temporary access token for basic tests::

- Acces the https://developer.linkedin.com/rest-console
- On then Authentication menu select OAuth2
- After you need to login and authorization to access some information from your LinkedIn profile
- Send anywhere request URL, for example https://api.linkedin.com/v1/people/~?format=json, and copy field access token 

5. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8 PyLinkedinAPI tests
    $ python setup.py test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, and 3.4, and for PyPy. Check
   https://travis-ci.org/johnidm/PyLinkedinAPI/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ python -m unittest tests.test_PyLinkedinAPI
