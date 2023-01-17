from pytest import fixture

from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
	browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
	return browser