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
 * Put request body to update an employee
 */
@ApiModel(description = "Put request body to update an employee")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-05-06T13:07:18.612441+09:00[Asia/Tokyo]")
public class EmployeePutRequestBody {
  public static final String SERIALIZED_NAME_OMITTED = "omitted";
  @SerializedName(SERIALIZED_NAME_OMITTED)
  private Boolean omitted;

  public static final String SERIALIZED_NAME_PARTICIPATE = "participate";
  @SerializedName(SERIALIZED_NAME_PARTICIPATE)
  private Boolean participate;


  public EmployeePutRequestBody omitted(Boolean omitted) {
    
    this.omitted = omitted;
    return this;
  }

   /**
   * Get omitted
   * @return omitted
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getOmitted() {
    return omitted;
  }


  public void setOmitted(Boolean omitted) {
    this.omitted = omitted;
  }


  public EmployeePutRequestBody participate(Boolean participate) {
    
    this.participate = participate;
    return this;
  }

   /**
   * Get participate
   * @return participate
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getParticipate() {
    return participate;
  }


  public void setParticipate(Boolean participate) {
    this.participate = participate;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EmployeePutRequestBody employeePutRequestBody = (EmployeePutRequestBody) o;
    return Objects.equals(this.omitted, employeePutRequestBody.omitted) &&
        Objects.equals(this.participate, employeePutRequestBody.participate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(omitted, participate);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EmployeePutRequestBody {\n");
    sb.append("    omitted: ").append(toIndentedString(omitted)).append("\n");
    sb.append("    participate: ").append(toIndentedString(participate)).append("\n");
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

