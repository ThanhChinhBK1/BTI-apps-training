import {Component, OnInit} from '@angular/core';
import {FormControl} from '@angular/forms';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';
import {Employee} from "../../services/bti-training-api";
import {EmployeePutRequestBody, EmployeeService} from "../../services/bti-training-api";

/**
 * @title Highlight the first autocomplete option
 */
@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.scss'],
})
export class InputComponent implements OnInit {
  employees: Employee[];
  employee: any;
  public parentData: string;
  public parentData2: string;
  myControl = new FormControl();
  options: string[] = ['中澤 宣貴', '藤原 和成', '柴田 和輝', '佐々木 瞭太', '森 祐貴', '日置 健二', '熊田 純也', '栗田 尚明', '白石 多一郎', '加藤 翔', '奥山 昌紀', '田中 健一', 'Le Hau', '榎並 利晃', '柏木 正隆', '塚田 直樹', '釋迦郡 翔太', '中澤 貴明', '樋口 学', '前田 昌太朗', '吉田 香織', '安部 美希', '石本 慎太郎', '本間 由美子', '柏木 琴真', '今野 勝之', '田中 幸一', '濤川 杏子', '中西 啓太', '寺村 駿哉', '加藤 孝幸', '太田 良介', '神蔵 奈緒子', '森瀬 周', '桑原 陽子', '脇野 寛洋', '鈴木 資潤', '小林 拓哉', '濱中 佐和子', '鈴木 誠二郎', '矢羽々 豊', '三浦 剛', '岩城 圭亮', '西川 浩平', 'Le Khanh', '竹内 沙也加', 'Pham Hoang', '青木 正良', '河田 哲', '原 拓郎', '田村 太一', 'Nguyen Cuong', 'Nguyen Chinh', '林 琢磨', '沢村 敬太'];
  filteredOptions: Observable<string[]>;

  constructor(private employeeService: EmployeeService) {
  }

  ngOnInit() {
    this.filteredOptions = this.myControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value))
    );
    this.employeeService.getEmployees().subscribe((employees) => {
      this.employees = employees;
    })
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.options.filter(option => option.toLowerCase().includes(filterValue));
  }

  sanka(namae) {
    this.parentData = namae
  }

  husanka(namae) {
    this.parentData2 = namae
  }

  OnClick() {
    const request1: EmployeePutRequestBody = {
      omitted: true,
      participate: false
    }
    const request2: EmployeePutRequestBody = {
      omitted: true,
      participate: true
    }

    this.employeeService.getEmployees(true).subscribe((participant) => {
        this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
          this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
            this.employeeService.getEmployees(true).subscribe((participant) => {
              this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
                this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
                  this.employeeService.getEmployees(true).subscribe((participant) => {
                    this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
                      this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
                        this.employeeService.getEmployees(true).subscribe((participant) => {
                          this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
                            this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(()=>{
                              this.employeeService.getEmployees(true).subscribe((participant) => {
                                this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
                                  this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
                                    this.employeeService.getEmployees(true).subscribe((participant) => {
                                      this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
                                        this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe()
                                      })
                                    })
                                  })
                                })
                              })
                            })
                          })
                        })
                      })
                    })
                  })
                })
              })
            })
          })
        })
      })
    // for (let i = 0; i < 1; i++) {
    //   this.employeeService.getEmployees(true).subscribe((participant) => {
    //     this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
    //       this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
    //         this.employeeService.getEmployees(true).subscribe((participant) => {
    //           this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
    //             this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
    //               this.employeeService.getEmployees(true).subscribe((participant) => {
    //                 this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
    //                   this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
    //                     this.employeeService.getEmployees(true).subscribe((participant) => {
    //                       this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
    //                         this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe()
    //                       })
    //                     })
    //                   })
    //                 })
    //               })
    //             })
    //           })
    //         })
    //       })
    //     })
    //   })
    // }
  }
}


/**  Copyright 2020 Google LLC. All Rights Reserved.
    Use of this source code is governed by an MIT-style license that
    can be found in the LICENSE file at http://angular.io/license */
