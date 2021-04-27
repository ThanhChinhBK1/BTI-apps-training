import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployeePutComponent } from './employee-put.component';

describe('EmployeePutComponent', () => {
  let component: EmployeePutComponent;
  let fixture: ComponentFixture<EmployeePutComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EmployeePutComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployeePutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
