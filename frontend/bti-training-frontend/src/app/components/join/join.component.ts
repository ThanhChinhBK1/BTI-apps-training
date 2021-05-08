import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {Employee} from "../../services/bti-training-api";
import {EmployeePutRequestBody, EmployeeService} from "../../services/bti-training-api";

@Component({
  selector: 'app-join',
  templateUrl: './join.component.html',
  styleUrls: ['./join.component.scss']
})
export class JoinComponent implements OnInit, OnChanges {
  employees: Employee[];
  employee: any;
  shusaisha: Employee[] = [];
  num: number;
  location : Location;

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
      const request2: EmployeePutRequestBody = {
        omitted: true,
        participate: true
      }
      for (let i = 0; i < this.employees.length; i++) {
        if (this.dataFromParent == this.employees[i].name) {
          this.employeeService.putEmployeeByTeam(this.employees[i].team, request1).subscribe(()=>{
            this.employeeService.putEmployeeByName(this.employees[i].id,request2).subscribe(()=>{
              this.shusaisha = this.shusaisha.concat(this.employees[i]);
              this.num = this.shusaisha.length;
            })
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

  OnClick() {
    const request1: EmployeePutRequestBody = {
      omitted: true,
      participate: false
    }
    const request2: EmployeePutRequestBody = {
      omitted: true,
      participate: true
    }

    if (this.num==0) {
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
    }

    else if (this.num==1) {
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
                              location.reload();
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
    }

    else if (this.num==2) {
      this.employeeService.getEmployees(true).subscribe((participant) => {
        this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
          this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
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
    }

    else if (this.num==3) {
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
    }

    else if (this.num==4) {
      this.employeeService.getEmployees(true).subscribe((participant) => {
        this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
          this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe()
        })
      })
    }




    // this.employeeService.getEmployees(true).subscribe((participant) => {
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
    //                         this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(()=>{
    //                           this.employeeService.getEmployees(true).subscribe((participant) => {
    //                             this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
    //                               this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe(() => {
    //                                 this.employeeService.getEmployees(true).subscribe((participant) => {
    //                                   this.employeeService.putEmployeeByTeam(participant[0].team, request1).subscribe(() => {
    //                                     this.employeeService.putEmployeeByName(participant[0].id, request2).subscribe()
    //                                   })
    //                                 })
    //                               })
    //                             })
    //                           })
    //                         })
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
