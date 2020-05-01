# openapi_client.BusinessApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata**](BusinessApi.md#get_metadata) | **POST** /metadata | 
[**get_metadata_url**](BusinessApi.md#get_metadata_url) | **POST** /metadata/url | 


# **get_metadata**
> MindResponse get_metadata(text_node)



Get metadata that match the query

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
    api_instance = openapi_client.BusinessApi(api_client)
    text_node = openapi_client.TextNode() # TextNode | SQL string to query business data

    try:
        api_response = api_instance.get_metadata(text_node)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_node** | [**TextNode**](TextNode.md)| SQL string to query business data | 

### Return type

[**MindResponse**](MindResponse.md)

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

# **get_metadata_url**
> MindResponse get_metadata_url(text_node)



Get a URL to the metadata bundle that match the query

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
    api_instance = openapi_client.BusinessApi(api_client)
    text_node = openapi_client.TextNode() # TextNode | SQL string to query business data

    try:
        api_response = api_instance.get_metadata_url(text_node)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessApi->get_metadata_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_node** | [**TextNode**](TextNode.md)| SQL string to query business data | 

### Return type

[**MindResponse**](MindResponse.md)

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

