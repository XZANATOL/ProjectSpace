import { TestBed } from '@angular/core/testing';

import { AppRecordService } from './app-record.service';

describe('AppRecordService', () => {
  let service: AppRecordService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AppRecordService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
