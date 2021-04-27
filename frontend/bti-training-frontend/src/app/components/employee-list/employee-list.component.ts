import { Component, OnInit } from '@angular/core';
import {EmployeeService} from "../../services/bti-training-api";
import {any} from "codelyzer/util/function";
import {Employee} from "../../services/bti-training-api";

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent implements OnInit {
  employees : Employee[];
  employee : any;
  constructor(private employeeService:EmployeeService) { }

  ngOnInit(): void {
    this.employeeService.getEmployees().subscribe((employees) => {
      this.employees = employees;
    })
  }

}
