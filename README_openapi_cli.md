# openapi-client
MSK-MIND REST API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientExperimentalCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint


# Defining host is optional and default to http://localhost:8080
configuration.host = "http://localhost:8080"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BusinessApi(api_client)
    text_node_text_node = openapi_client.TextNode() # text_node.TextNode | SQL string to query business data

    try:
        api_response = api_instance.get_metadata(text_node_text_node)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BusinessApi->get_metadata: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BusinessApi* | [**get_metadata**](docs/BusinessApi.md#get_metadata) | **POST** /metadata | 
*BusinessApi* | [**get_metadata_url**](docs/BusinessApi.md#get_metadata_url) | **POST** /metadata/url | 
*OperationApi* | [**get_file_url**](docs/OperationApi.md#get_file_url) | **POST** /files/url | 
*OperationApi* | [**get_files**](docs/OperationApi.md#get_files) | **POST** /files | 


## Documentation For Models

 - [mind_error_response.MindErrorResponse](docs/MindErrorResponse.md)
 - [mind_response.MindResponse](docs/MindResponse.md)
 - [mind_success_response.MindSuccessResponse](docs/MindSuccessResponse.md)
 - [text_node.TextNode](docs/TextNode.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author



