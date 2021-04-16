import { Component, OnInit } from '@angular/core';
import {Employee} from "../services/bti-training-api";

@Component({
  selector: 'app-create-employee',
  templateUrl: './create-employee.component.html',
  styleUrls: ['./create-employee.component.scss']
})
export class CreateEmployeeComponent implements OnInit {
  employees: Employee[]

  constructor() { }

  ngOnInit(): void {

  }

}
