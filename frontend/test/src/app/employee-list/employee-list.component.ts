import { Component, OnInit } from '@angular/core';
import * as http from "http";

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent implements OnInit {
  test:string;
  constructor() {this.test = "" }

  ngOnInit(): void {
    this.test = "strange"
    http.get("http://0.0.0.0:8080/impulse-apps-training/employees").subscribe((v: any) => console.log(v));
  }

}
