# openapi_client.OperationApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_url**](OperationApi.md#get_file_url) | **POST** /files/url | 
[**get_files**](OperationApi.md#get_files) | **POST** /files | 


# **get_file_url**
> MindResponseString get_file_url(text_node)



Get a URL to the zipped data that match the criteria

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OperationApi(api_client)
    text_node = openapi_client.TextNode() # TextNode | Filter criteria for operational data

    try:
        api_response = api_instance.get_file_url(text_node)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OperationApi->get_file_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_node** | [**TextNode**](TextNode.md)| Filter criteria for operational data | 

### Return type

[**MindResponseString**](MindResponseString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> MindResponseListObject get_files(text_node)



Get operational metadata

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OperationApi(api_client)
    text_node = openapi_client.TextNode() # TextNode | Filter criteria for operational data

    try:
        api_response = api_instance.get_files(text_node)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OperationApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_node** | [**TextNode**](TextNode.md)| Filter criteria for operational data | 

### Return type

[**MindResponseListObject**](MindResponseListObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

