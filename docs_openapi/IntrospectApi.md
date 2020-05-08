# openapi_client.IntrospectApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_columns**](IntrospectApi.md#get_columns) | **POST** /list-columns | 
[**get_databases**](IntrospectApi.md#get_databases) | **POST** /list-databases | 
[**get_tables**](IntrospectApi.md#get_tables) | **POST** /list-tables | 


# **get_columns**
> MindResponse get_columns(db, table)



List columns

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
    api_instance = openapi_client.IntrospectApi(api_client)
    db = 'db_example' # str | 
table = 'table_example' # str | 

    try:
        api_response = api_instance.get_columns(db, table)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntrospectApi->get_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**|  | 
 **table** | **str**|  | 

### Return type

[**MindResponse**](MindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases**
> MindResponse get_databases()



List databases

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
    api_instance = openapi_client.IntrospectApi(api_client)
    
    try:
        api_response = api_instance.get_databases()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntrospectApi->get_databases: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MindResponse**](MindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tables**
> MindResponse get_tables(db)



List tables

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
    api_instance = openapi_client.IntrospectApi(api_client)
    db = 'db_example' # str | 

    try:
        api_response = api_instance.get_tables(db)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntrospectApi->get_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**|  | 

### Return type

[**MindResponse**](MindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

