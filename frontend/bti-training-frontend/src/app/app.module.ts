import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {Configuration, ConfigurationParameters, ImpulseAppsApiModule} from "./services/bti-training-api";
import { EmployeeListComponent } from './components/employee-list/employee-list.component';
import { CreateEmployeeComponent } from './components/create-employee/create-employee.component';
import { DeleteEmployeeComponent } from './components/delete-employee/delete-employee.component';
import {ReactiveFormsModule} from "@angular/forms";
import { GetEmployeeComponent } from './components/get-employee/get-employee.component';
//import { EmployeePutComponent } from './components/employee-put/employee-put.component';
export function impulseAppsApiConfigFactory(): Configuration {
    const params: ConfigurationParameters = {
        // set configuration parameters here.
        basePath: "/impulse-apps-training"
    };
    return new Configuration(params);
}
@NgModule({
  declarations: [
    AppComponent,
    EmployeeListComponent,
    CreateEmployeeComponent,
    DeleteEmployeeComponent,
    GetEmployeeComponent,
    //EmployeePutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ImpulseAppsApiModule.forRoot(impulseAppsApiConfigFactory),
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
