import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { EmployeeListComponent } from './employee-list/employee-list.component';
import {HttpClientModule} from "@angular/common/http";
import {Configuration, ConfigurationParameters, ImpulseAppsApiModule} from "./services/bti-training-api";
import { CreateEmployeeComponent } from './create-employee/create-employee.component';
import { DeleteEmployeeComponent } from './delete-employee/delete-employee.component';
import {Routes} from "@angular/router";

const ROUTE_TABLE: Routes = [
  { path: '', component: EmployeeListComponent },
  { path: 'employee-list', component: EmployeeListComponent },
  { path: 'create-employee', component: CreateEmployeeComponent },
  { path: 'delete-employee', component: DeleteEmployeeComponent }
];
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
    DeleteEmployeeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ImpulseAppsApiModule.forRoot(impulseAppsApiConfigFactory)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
