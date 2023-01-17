def test_environment_is_qa(app_config):
	base_url = app_config.base_url
	port = app_config.app_port
	assert base_url == 'https://qa.testing-url.com'
	assert port == 80

def test_environment_is_dev(app_config):
	base_url = app_config.base_url
	port = app_config.app_port
	assert base_url == 'https://dev.testing-url.com'
	assert port == 8080