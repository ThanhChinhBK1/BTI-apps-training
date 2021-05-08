import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {Employee} from "../../services/bti-training-api";
import {EmployeePutRequestBody, EmployeeService} from "../../services/bti-training-api";

@Component({
  selector: 'app-absentee',
  templateUrl: './absentee.component.html',
  styleUrls: ['./absentee.component.scss']
})
export class AbsenteeComponent implements OnInit, OnChanges {
  employees: Employee[];
  employee: any;
  absentees: Employee[] = [];

  @Input() dataFromParent: string;

  constructor(private employeeService: EmployeeService) {
  }

  ngOnInit(): void {
    this.employeeService.getEmployees().subscribe((employees) => {
      this.employees = employees;
    })
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.hasOwnProperty("dataFromParent")&& this.employees) {
      const request1: EmployeePutRequestBody = {
        omitted: true,
        participate: false
      }
      for (let i = 0; i < this.employees.length; i++) {
        if (this.dataFromParent == this.employees[i].name) {
          this.employeeService.putEmployeeByName(this.employees[i].id, request1).subscribe(()=>{
            this.absentees = this.absentees.concat(this.employees[i]);
          })
        }

        // if (this.dataFromParent == this.employees[i].name) {
        //   this.employeeService.putEmployeeByName(this.employees[i].id, request).subscribe(()=>{
        //     this.employeeService.putEmployeeByTeam(this.employees[i].team,request2).subscribe(()=>{
        //       this.shusaisha = this.shusaisha.concat(this.employees[i]);
        //     })
        //   })
        // }
      }
    }
  }
}

