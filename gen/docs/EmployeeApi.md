# EmployeeApi

All URIs are relative to *http://localhost/impulse-apps-training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteEmployee**](EmployeeApi.md#deleteEmployee) | **DELETE** /employees/{employeeId} | 
[**getEmployee**](EmployeeApi.md#getEmployee) | **GET** /employees/{employeeId} | 
[**getEmployees**](EmployeeApi.md#getEmployees) | **GET** /employees | 
[**postEmployees**](EmployeeApi.md#postEmployees) | **POST** /employees | 
[**putEmployeeByName**](EmployeeApi.md#putEmployeeByName) | **PUT** /employees/{employeeId} | 


<a name="deleteEmployee"></a>
# **deleteEmployee**
> Employee deleteEmployee(employeeId)



Delete a list of action recommendation by targetType and targetId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/impulse-apps-training");

    EmployeeApi apiInstance = new EmployeeApi(defaultClient);
    String employeeId = "employeeId_example"; // String | 
    try {
      Employee result = apiInstance.deleteEmployee(employeeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#deleteEmployee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employeeId** | **String**|  |

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected Error |  -  |

<a name="getEmployee"></a>
# **getEmployee**
> Employee getEmployee(employeeId)



Get a list of action recommendation by targetType and targetId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/impulse-apps-training");

    EmployeeApi apiInstance = new EmployeeApi(defaultClient);
    String employeeId = "employeeId_example"; // String | 
    try {
      Employee result = apiInstance.getEmployee(employeeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#getEmployee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employeeId** | **String**|  |

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error |  -  |

<a name="getEmployees"></a>
# **getEmployees**
> List&lt;Employee&gt; getEmployees(randomGet, participant)



get employees under several conditions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/impulse-apps-training");

    EmployeeApi apiInstance = new EmployeeApi(defaultClient);
    Boolean randomGet = true; // Boolean | 
    Boolean participant = true; // Boolean | 
    try {
      List<Employee> result = apiInstance.getEmployees(randomGet, participant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#getEmployees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **randomGet** | **Boolean**|  | [optional]
 **participant** | **Boolean**|  | [optional]

### Return type

[**List&lt;Employee&gt;**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected Error |  -  |

<a name="postEmployees"></a>
# **postEmployees**
> Employee postEmployees(employeePostRequestBody)



create a new employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/impulse-apps-training");

    EmployeeApi apiInstance = new EmployeeApi(defaultClient);
    EmployeePostRequestBody employeePostRequestBody = new EmployeePostRequestBody(); // EmployeePostRequestBody | 
    try {
      Employee result = apiInstance.postEmployees(employeePostRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#postEmployees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employeePostRequestBody** | [**EmployeePostRequestBody**](EmployeePostRequestBody.md)|  | [optional]

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**0** | Unexpected Error |  -  |

<a name="putEmployeeByName"></a>
# **putEmployeeByName**
> Employee putEmployeeByName(employeeId, employeePutRequestBody)



update omittetd and participate for the employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/impulse-apps-training");

    EmployeeApi apiInstance = new EmployeeApi(defaultClient);
    String employeeId = "employeeId_example"; // String | 
    EmployeePutRequestBody employeePutRequestBody = new EmployeePutRequestBody(); // EmployeePutRequestBody | 
    try {
      Employee result = apiInstance.putEmployeeByName(employeeId, employeePutRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#putEmployeeByName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employeeId** | **String**|  |
 **employeePutRequestBody** | [**EmployeePutRequestBody**](EmployeePutRequestBody.md)|  | [optional]

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected Error |  -  |

