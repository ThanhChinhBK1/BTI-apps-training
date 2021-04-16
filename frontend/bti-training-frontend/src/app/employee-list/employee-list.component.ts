import { Component, OnInit } from '@angular/core';
import {EmployeeService} from "../services/bti-training-api/api/employee.service";
import {Observable} from "rxjs";
import {any} from "codelyzer/util/function";
import {Employee} from "../services/bti-training-api";
import {CreateEmployeeComponent} from "../create-employee/create-employee.component";
import {Router} from "@angular/router";


@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  //template:'<input type="button" value="新規作成画面" (click)="Onclick_create()"/>',
  styleUrls: ['./employee-list.component.scss']
})

export class EmployeeListComponent implements OnInit {
  employees: Employee[];
  employee: any;
  router: Router;
  location: Location;
  next_url: String;
  create_employee: CreateEmployeeComponent;
  constructor(private employeeService: EmployeeService) {}


  ngOnInit(): void {
     //this.employee_list = this.employeeService.getEmployees().subscribe();
     //this.employee_list.pipe().subscribe((v)=>console.log(v));
    this.employeeService.getEmployees().subscribe((employees) =>
    {
      this.employees = employees ;
    }
    );
  }
  onClick(action:string): void {
    //this.router.navigate(['create-employee']);
  }

}
