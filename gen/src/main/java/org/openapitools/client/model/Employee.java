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
public class Employee {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_DEPARTMENT = "department";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT)
  private String department;

  public static final String SERIALIZED_NAME_TEAM = "team";
  @SerializedName(SERIALIZED_NAME_TEAM)
  private String team;

  public static final String SERIALIZED_NAME_OMITTED = "omitted";
  @SerializedName(SERIALIZED_NAME_OMITTED)
  private Boolean omitted;

  public static final String SERIALIZED_NAME_PARTICIPATE = "participate";
  @SerializedName(SERIALIZED_NAME_PARTICIPATE)
  private Boolean participate;


  public Employee name(String name) {
    
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getName() {
    return name;
  }


  public void setName(String name) {
    this.name = name;
  }


  public Employee department(String department) {
    
    this.department = department;
    return this;
  }

   /**
   * Get department
   * @return department
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDepartment() {
    return department;
  }


  public void setDepartment(String department) {
    this.department = department;
  }


  public Employee team(String team) {
    
    this.team = team;
    return this;
  }

   /**
   * Get team
   * @return team
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTeam() {
    return team;
  }


  public void setTeam(String team) {
    this.team = team;
  }


  public Employee omitted(Boolean omitted) {
    
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


  public Employee participate(Boolean participate) {
    
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
    Employee employee = (Employee) o;
    return Objects.equals(this.name, employee.name) &&
        Objects.equals(this.department, employee.department) &&
        Objects.equals(this.team, employee.team) &&
        Objects.equals(this.omitted, employee.omitted) &&
        Objects.equals(this.participate, employee.participate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, department, team, omitted, participate);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Employee {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    department: ").append(toIndentedString(department)).append("\n");
    sb.append("    team: ").append(toIndentedString(team)).append("\n");
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
