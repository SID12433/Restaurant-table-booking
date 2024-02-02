import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReservationstatusComponent } from './reservationstatus.component';

describe('ReservationstatusComponent', () => {
  let component: ReservationstatusComponent;
  let fixture: ComponentFixture<ReservationstatusComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ReservationstatusComponent]
    });
    fixture = TestBed.createComponent(ReservationstatusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
