import { Component, OnInit } from '@angular/core';
import {EmployeeService} from "../services/bti-training-api/api/employee.service";
import {Employee} from "../services/bti-training-api/model/employee";

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent {


  employees: Employee[];
  constructor(private employeeService: EmployeeService) { }

  ngOnInit(): void {
    this.employeeService.getEmployees().subscribe((employees) => { this.employees = employees.filter((employee)=>employee.name !== "aaa") });
  }


}
