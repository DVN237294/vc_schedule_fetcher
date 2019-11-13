# openapi_client.ScheduleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_schedule_add_room_room_name_post**](ScheduleApi.md#api_schedule_add_room_room_name_post) | **POST** /api/Schedule/AddRoom/{roomName} | 
[**api_schedule_room_name_get**](ScheduleApi.md#api_schedule_room_name_get) | **GET** /api/Schedule/{roomName} | 
[**api_schedule_room_name_post**](ScheduleApi.md#api_schedule_room_name_post) | **POST** /api/Schedule/{roomName} | 


# **api_schedule_add_room_room_name_post**
> api_schedule_add_room_room_name_post(room_name)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (JWT): bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = openapi_client.ScheduleApi(openapi_client.ApiClient(configuration))
room_name = 'room_name_example' # str | 

try:
    api_instance.api_schedule_add_room_room_name_post(room_name)
except ApiException as e:
    print("Exception when calling ScheduleApi->api_schedule_add_room_room_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_schedule_room_name_get**
> RoomRecordingSchedule api_schedule_room_name_get(room_name)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (JWT): bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = openapi_client.ScheduleApi(openapi_client.ApiClient(configuration))
room_name = 'room_name_example' # str | 

try:
    api_response = api_instance.api_schedule_room_name_get(room_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->api_schedule_room_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  | 

### Return type

[**RoomRecordingSchedule**](RoomRecordingSchedule.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_schedule_room_name_post**
> api_schedule_room_name_post(room_name, scheduled_session=scheduled_session)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (JWT): bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = openapi_client.ScheduleApi(openapi_client.ApiClient(configuration))
room_name = 'room_name_example' # str | 
scheduled_session = [openapi_client.ScheduledSession()] # list[ScheduledSession] |  (optional)

try:
    api_instance.api_schedule_room_name_post(room_name, scheduled_session=scheduled_session)
except ApiException as e:
    print("Exception when calling ScheduleApi->api_schedule_room_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  | 
 **scheduled_session** | [**list[ScheduledSession]**](ScheduledSession.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

