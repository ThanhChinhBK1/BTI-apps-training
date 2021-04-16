import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {EmployeeListComponent} from "./employee-list/employee-list.component";
import {CreateEmployeeComponent} from "./create-employee/create-employee.component";
import {DeleteEmployeeComponent} from "./delete-employee/delete-employee.component";



const routes: Routes = [{ path: 'employee-list', component: EmployeeListComponent},
  { path: '', redirectTo: 'employee-list', pathMatch: 'full' },{path:'create-employee',component:CreateEmployeeComponent},{path:'delete-employee',component:DeleteEmployeeComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
