class Config: 
	def __init__(self, env):
		
		SUPPORTED_ENVS = ['dev', 'qa']

		if env.lower() not in SUPPORTED_ENVS:
			raise Exception(f'{env} is not a supported environment.')
	
		self.base_url = {
			'dev': 'https://dev.testing-url.com',
			'qa': 'https://qa.testing-url.com'
		}[env]

		self.app_port = {
			'dev': 8080,
			'qa': 80
		}[env]