# MFA Login
This repo uses Page Object Model design principal to implement browser automation testing on MFA authentication using python, [Playwright](https://playwright.dev/python/) and pytest.
It is running automation tests against [demo website](https://seleniumbase.io/realworld/login) 


# Getting Started
Clone the project
```
 git clone git@github.com:bhanuyadav022/mfa-login-pytest-playwright.git
 cd mfa-login-pytest-playwright
```
# Running Tests
1. Run inside container 
-   Build docker image
```docker
 docker build -t <docker-images> .
```
  -   Run Test

```docker
    docker run -it -v $(pwd)/results:/app/* <docker-images>  pytest --html=reports.html tests/login_tests.py
```
2. Run Locally
- Install Dependencies
  - [playwright-pytest](https://playwright.dev/python/docs/intro#installing-playwright-pytest)
  - [pytest-html](https://pytest-html.readthedocs.io/en/latest/installing.html#installing-pytest-html)

- Run command 
```shell
pytest --html=report.html tests/login_tests.py
```
