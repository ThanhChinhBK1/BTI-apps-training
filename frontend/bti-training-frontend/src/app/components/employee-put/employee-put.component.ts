import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import {EmployeePostRequestBody, EmployeePutRequestBody, EmployeeService} from "../../services/bti-training-api";
import {any} from "codelyzer/util/function";
import {Employee} from "../../services/bti-training-api";

@Component({
  selector: 'app-employee-put',
  templateUrl: './employee-put.component.html',
  styleUrls: ['./employee-put.component.scss']
})


export class CreateEmployeeComponent implements OnInit {
  employees : Employee[];
  employee : any;
  location : Location;

  checkoutForm = this.formBuilder.group({
    name: '',
    description: ''
  });

  constructor(private employeeService:EmployeeService,
              private formBuilder: FormBuilder,) { }

  ngOnInit(): void {}

  onSubmit(){
    const request:EmployeePutRequestBody = {
      description: this.checkoutForm.value.description
    }
    this.employeeService.putEmployee("1",request).subscribe((employee)=>
    {
      location.reload()
    });
  }
}

export class EmployeePutComponent {
}


export class GetEmployeeComponent implements OnInit {

  constructor(private route: ActivatedRoute,
              private employeeService: EmployeeService) { }

  ngOnInit(): void {this.route.paramMap.subscribe((paramMap) => console.log(paramMap))
  }

}
