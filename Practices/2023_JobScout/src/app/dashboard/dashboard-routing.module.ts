import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';

import { authGuard } from '../common/guards/authGuard';

const routes: Routes = [{ path: '', component: DashboardComponent, canActivate: [authGuard] }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
