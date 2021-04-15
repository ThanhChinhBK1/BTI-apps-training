import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {Configuration, ConfigurationParameters, ImpulseAppsApiModule} from "./services/bti-training-api";
import { EmployeeListComponent } from './components/employee-list/employee-list.component';
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
    EmployeeListComponent
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
