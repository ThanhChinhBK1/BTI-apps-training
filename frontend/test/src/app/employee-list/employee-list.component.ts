import { Component, OnInit } from '@angular/core';
import * as http from 'http';

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent implements OnInit {

  test : string;
  constructor() { this.test = "";}

  ngOnInit(): void
  {
    this.test = "難しすぎる";
    http.get("http://0.0.0.0:8080/impulse-apps-training/employee/BR2").subscribe((v :any)=>console.log(v));
  }

}
