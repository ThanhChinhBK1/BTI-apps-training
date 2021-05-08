import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import {EmployeePostRequestBody, EmployeeService} from "../../services/bti-training-api";
import {any} from "codelyzer/util/function";
import {Employee} from "../../services/bti-training-api";


@Component({
  selector: 'app-create-employee',
  templateUrl: './create-employee.component.html',
  styleUrls: ['./create-employee.component.scss']
})
export class CreateEmployeeComponent implements OnInit {
  employees : Employee[];
  employee : any;
  location : Location;

  items = this.employeeService.postEmployees();
  checkoutForm = this.formBuilder.group({
    name: '',
    department: '',
    omitted: '',
    participate: '',
    team: ''
  });

  constructor(private employeeService:EmployeeService,
              private formBuilder: FormBuilder,) { }

  ngOnInit(): void {}

  onSubmit(){
    const request:EmployeePostRequestBody = {
      name: this.checkoutForm.value.name,
      description: this.checkoutForm.value.description
    }
    this.employeeService.postEmployees(request).subscribe((employee)=>
    {
      location.reload()
    });
  }
  onClick(){
    console.log("harenohi")
  }
}

