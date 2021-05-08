import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AbsenteeComponent } from './absentee.component';

describe('AbsenteeComponent', () => {
  let component: AbsenteeComponent;
  let fixture: ComponentFixture<AbsenteeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AbsenteeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AbsenteeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
