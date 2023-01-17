import json

from pytest import fixture
from selenium import webdriver

data_path = 'test_data.json'

@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def bowser(request):
	driver = request.param
	drvr = driver()
	yield drvr
	drvr.quit()


def load_test_data(path):
	with open(path) as data_file:
		data = json.load(data_file)
		return data

@fixture(params=load_test_data(data_path))
def test_data(request):
	data = request.param
	return data