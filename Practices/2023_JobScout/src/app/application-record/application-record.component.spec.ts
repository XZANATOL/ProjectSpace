import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApplicationRecordComponent } from './application-record.component';

describe('ApplicationRecordComponent', () => {
  let component: ApplicationRecordComponent;
  let fixture: ComponentFixture<ApplicationRecordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ApplicationRecordComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ApplicationRecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
