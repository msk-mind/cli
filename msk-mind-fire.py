import fire
import openapi_client
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration

class MskMind(object):
	"""MSK-MIND CLI.

	ex)
	msk-mind business get_metadata "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'" --host=http://localhost:8080
	msk-mind business get_metadata_file_url "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'"
	msk-mind operation get_files '{ "dmpIds": ["P-0039384"], "createTime": "2020-03-01", "fileType": "IMAGE_HNE"}'
	msk-mind operation get_file_url '{ "dmpIds": ["P-0039384"], "createTime": "2020-03-01", "fileType": "IMAGE_HNE"}'
	"""
	def __init__(self, host="http://localhost:8080"):
		# setup api client
		config = Configuration(host=host)
		self.client = ApiClient(configuration=config)
		self.business = openapi_client.BusinessApi(self.client)
		self.operation = openapi_client.OperationApi(self.client)

	def metadata(self, text_node, **kwargs):
		"""Get metadata 

		Custom docstring for get_metadata

		ex)
		msk-mind metadata "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'"

		:param TextNode text_node: SQL string to query business data (required)
		"""
		return self.business.get_metadata(text_node, **kwargs)



if __name__ == '__main__':
	fire.Fire(MskMind)
