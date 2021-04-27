import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import {EmployeeService} from "../../services/bti-training-api";
import {Employee} from "../../services/bti-training-api";

@Component({
  selector: 'app-delete-employee',
  templateUrl: './delete-employee.component.html',
  styleUrls: ['./delete-employee.component.scss']
})
export class DeleteEmployeeComponent implements OnInit {
  employees : Employee[];
  employee : any;
  location : Location;

  //items = this.employeeService.deleteEmployee();
  checkoutForm = this.formBuilder.group({
    employeeId: ''
  });

  constructor(private employeeService:EmployeeService,
              private formBuilder: FormBuilder,) { }

  ngOnInit(): void {
  }

  onSubmit(){
     // const request = {
     //   id: this.checkoutForm.value.employeeId
     // }
     this.employeeService.deleteEmployee(this.checkoutForm.value.employeeId).subscribe((employee)=>
     {
       location.reload()
     });
   }
}



