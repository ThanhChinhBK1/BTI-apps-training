/*
 * apps-training RESTful API
 * OpenAPI definition file for impulse-apps
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * Basic response with application status code
 */
@ApiModel(description = "Basic response with application status code")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-04-26T16:53:18.375008+09:00[Asia/Tokyo]")
public class BasicResponse {
  public static final String SERIALIZED_NAME_APP_STATUS_CODE = "appStatusCode";
  @SerializedName(SERIALIZED_NAME_APP_STATUS_CODE)
  private Integer appStatusCode;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;


  public BasicResponse appStatusCode(Integer appStatusCode) {
    
    this.appStatusCode = appStatusCode;
    return this;
  }

   /**
   * Get appStatusCode
   * @return appStatusCode
  **/
  @ApiModelProperty(required = true, value = "")

  public Integer getAppStatusCode() {
    return appStatusCode;
  }


  public void setAppStatusCode(Integer appStatusCode) {
    this.appStatusCode = appStatusCode;
  }


  public BasicResponse description(String description) {
    
    this.description = description;
    return this;
  }

   /**
   * Get description
   * @return description
  **/
  @ApiModelProperty(required = true, value = "")

  public String getDescription() {
    return description;
  }


  public void setDescription(String description) {
    this.description = description;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BasicResponse basicResponse = (BasicResponse) o;
    return Objects.equals(this.appStatusCode, basicResponse.appStatusCode) &&
        Objects.equals(this.description, basicResponse.description);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appStatusCode, description);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BasicResponse {\n");
    sb.append("    appStatusCode: ").append(toIndentedString(appStatusCode)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
