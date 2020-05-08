# openapi_client.QueryApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](QueryApi.md#download) | **POST** /download | 
[**query**](QueryApi.md#query) | **POST** /query | 


# **download**
> MindResponse download(text_node)



Download data that match the query

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
    api_instance = openapi_client.QueryApi(api_client)
    text_node = openapi_client.TextNode() # TextNode | SQL or DSL string

    try:
        api_response = api_instance.download(text_node)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_node** | [**TextNode**](TextNode.md)| SQL or DSL string | 

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

# **query**
> MindResponse query(text_node)



Get data that match the query

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
    api_instance = openapi_client.QueryApi(api_client)
    text_node = openapi_client.TextNode() # TextNode | SQL or DSL string

    try:
        api_response = api_instance.query(text_node)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_node** | [**TextNode**](TextNode.md)| SQL or DSL string | 

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

