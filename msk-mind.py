import fire
import openapi_client
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration

class MskMind(object):

	def __init__(self, host="http://localhost:8080"):
		# setup api client
		config = Configuration(host=host)
		self.client = ApiClient(configuration=config)
		self.business = openapi_client.BusinessApi(self.client)
		self.operation = openapi_client.OperationApi(self.client)


if __name__ == '__main__':
	fire.Fire(MskMind)
