import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { EmployeeListComponent } from './employee-list/employee-list.component';
import {HttpClientModule} from "@angular/common/http";
import {Configuration, ConfigurationParameters, ImpulseAppsApiModule} from "./services/bti-training-api";

export function impulseAppsApiConfigFactory(): Configuration {
    const params: ConfigurationParameters = {
        // set configuration parameters here.
        // basePath: "/impulse-apps-api"
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
