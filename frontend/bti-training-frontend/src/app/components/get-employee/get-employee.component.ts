import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-get-employee',
  templateUrl: './get-employee.component.html',
  styleUrls: ['./get-employee.component.scss']
})
export class GetEmployeeComponent implements OnInit {

  constructor(private route: ActivatedRoute,
              private employeeService: EmployeeService) { }

  ngOnInit(): void {this.route.paramMap.subscribe((paramMap) => console.log(paramMap))
  }

}
