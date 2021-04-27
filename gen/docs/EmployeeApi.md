# EmployeeApi

All URIs are relative to *http://localhost/impulse-apps-training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteEmployee**](EmployeeApi.md#deleteEmployee) | **DELETE** /employees/{name} | 
[**getEmployee**](EmployeeApi.md#getEmployee) | **GET** /employees/{name} | 
[**getEmployeeAtRandom**](EmployeeApi.md#getEmployeeAtRandom) | **GET** /employees/getAtRandom | 
[**getEmployees**](EmployeeApi.md#getEmployees) | **GET** /employees | 
[**getParticipants**](EmployeeApi.md#getParticipants) | **GET** /employees/getParticipants | 
[**postEmployees**](EmployeeApi.md#postEmployees) | **POST** /employees | 
[**putEmployeeByName**](EmployeeApi.md#putEmployeeByName) | **PUT** /employees/{name} | 
[**putEmployeesByTeam**](EmployeeApi.md#putEmployeesByTeam) | **PUT** /employees | 


<a name="deleteEmployee"></a>
# **deleteEmployee**
> Employee deleteEmployee(name)



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
    String name = "name_example"; // String | 
    try {
      Employee result = apiInstance.deleteEmployee(name);
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
 **name** | **String**|  |

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
> Employee getEmployee(name)



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
    String name = "name_example"; // String | 
    try {
      Employee result = apiInstance.getEmployee(name);
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
 **name** | **String**|  |

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

<a name="getEmployeeAtRandom"></a>
# **getEmployeeAtRandom**
> Employee getEmployeeAtRandom(omitted, random, size)



get an employee with &#39;omitted&#x3D;false&#39; at random

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
    Boolean omitted = true; // Boolean | get an employee from the list of employees with 'omitted=false'
    Boolean random = true; // Boolean | get an employee at random
    Integer size = 56; // Integer | get one employee
    try {
      Employee result = apiInstance.getEmployeeAtRandom(omitted, random, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#getEmployeeAtRandom");
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
 **omitted** | **Boolean**| get an employee from the list of employees with &#39;omitted&#x3D;false&#39; | [optional]
 **random** | **Boolean**| get an employee at random | [optional]
 **size** | **Integer**| get one employee | [optional]

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

<a name="getEmployees"></a>
# **getEmployees**
> List&lt;Employee&gt; getEmployees(team, participate, omitted)



get all employees

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
    String team = "team_example"; // String | 
    Boolean participate = true; // Boolean | whether he/she participates in the online lunch meeting
    Boolean omitted = true; // Boolean | 
    try {
      List<Employee> result = apiInstance.getEmployees(team, participate, omitted);
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
 **team** | **String**|  |
 **participate** | **Boolean**| whether he/she participates in the online lunch meeting | [optional]
 **omitted** | **Boolean**|  | [optional]

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

<a name="getParticipants"></a>
# **getParticipants**
> Employee getParticipants(participate)



get employees with &#39;participate&#x3D;true&#39;

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
    Boolean participate = true; // Boolean | whether he/she participates in the online lunch meeting
    try {
      Employee result = apiInstance.getParticipants(participate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#getParticipants");
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
 **participate** | **Boolean**| whether he/she participates in the online lunch meeting | [optional]

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
> Employee putEmployeeByName(name, employeePutRequestBody)



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
    String name = "name_example"; // String | 
    EmployeePutRequestBody employeePutRequestBody = new EmployeePutRequestBody(); // EmployeePutRequestBody | 
    try {
      Employee result = apiInstance.putEmployeeByName(name, employeePutRequestBody);
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
 **name** | **String**|  |
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

<a name="putEmployeesByTeam"></a>
# **putEmployeesByTeam**
> List&lt;Employee&gt; putEmployeesByTeam()



update the omitted value of the employees in a certain team

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
    try {
      List<Employee> result = apiInstance.putEmployeesByTeam();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeApi#putEmployeesByTeam");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

