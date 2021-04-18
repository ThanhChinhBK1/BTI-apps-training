import { Component, OnInit } from '@angular/core';
import {Employee, EmployeePostRequestBody, EmployeeService} from "../services/bti-training-api";
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-create-employee',
  templateUrl: './create-employee.component.html',
  styleUrls: ['./create-employee.component.scss']
})
export class CreateEmployeeComponent
{
    employees: Employee[];
    checkoutForm = this.formBuilder.group({
    name: '',
    description: ''
  });

  constructor(
    private employeeService: EmployeeService,
    private formBuilder: FormBuilder,
  ) { }
  onSubmit(): void{
       const request:EmployeePostRequestBody = {
         name :this.checkoutForm.value.name,
         description :this.checkoutForm.value.description
       }


    // @ts-ignore
    this.employeeService.postEmployees(request).subscribe();
    this.checkoutForm.reset();
    console.warn("aaaa");
  }

  ngOnInit(): void {
  }

}
