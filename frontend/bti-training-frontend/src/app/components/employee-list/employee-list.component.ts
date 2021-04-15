import { Component, OnInit } from '@angular/core';
import {EmployeeService} from "../../services/bti-training-api";

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent implements OnInit {

  constructor(private employeeService:EmployeeService) { }

  ngOnInit(): void {
    this.employeeService.getEmployees().subscribe(this.logToConsole)
  }
 logToConsole(v) {
    console.log(v)
}
}
