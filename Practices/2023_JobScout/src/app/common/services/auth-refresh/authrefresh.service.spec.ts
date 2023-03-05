import { TestBed } from '@angular/core/testing';

import { AuthRefreshService } from './authrefresh.service';

describe('AuthRefreshService', () => {
  let service: AuthRefreshService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AuthRefreshService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
