import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {EmployeeListComponent} from "./components/employee-list/employee-list.component";
import {CreateEmployeeComponent} from "./components/create-employee/create-employee.component";
import {DeleteEmployeeComponent} from "./components/delete-employee/delete-employee.component";
//import {EmployeePutComponent} from "./components/employee-put/employee-put.component";


const routes: Routes = [{path:"employee-list", component:EmployeeListComponent},
  {path: 'employee-list',
  children: [
  {path: "", component: EmployeeListComponent},
  {path: ":employeeId", component: GetEmployeeComponent}
  ]
},
  {path:"create-employee",component:CreateEmployeeComponent},
  {path:"delete-employee",component:DeleteEmployeeComponent},
  //{path:"employee-put", component:EmployeePutComponent},
  { path: '', redirectTo: 'employee-list', pathMatch: 'full' }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
