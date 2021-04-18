import { Component, OnInit } from '@angular/core';
import {Employee, EmployeePostRequestBody, EmployeeService} from "../services/bti-training-api";
import {FormBuilder} from "@angular/forms";



@Component({
  selector: 'app-delete-employee',
  templateUrl: './delete-employee.component.html',
  styleUrls: ['./delete-employee.component.scss']
})
export class DeleteEmployeeComponent  {

    employees: Employee[];
    checkoutForm = this.formBuilder.group({
    employeeId: '',
  });

  constructor(
    private employeeService: EmployeeService,
    private formBuilder: FormBuilder,
  ) { }
  onSubmit(): void{
    // @ts-ignore
    const request :string  = this.checkoutForm.value.employeeId

    this.employeeService.deleteEmployee(request).subscribe();
    this.checkoutForm.reset();
    console.warn("aaaa");
  }
}
