import { NgModule } from '@angular/core';
import { RouterModule, Routes, UrlSegment } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { ApplicationRecordComponent } from './application-record/application-record.component';

import { authGuard } from './common/guards/authGuard';

const routes: Routes = [
  { path: "", component: LoginComponent },
  { path: 'dashboard', loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
  { path: "appRecord", canActivate: [authGuard],
    children: [
      { path: "new", component: ApplicationRecordComponent },

      { matcher: (url) => {
          if (url.length === 1 && url[0].path.match(/^\S{15}$/gi)){
            return {
              consumed: url,
              posParams: {
                id: new UrlSegment(url[0].path, {})
              }
            }
          }
          return null
        },

        component: ApplicationRecordComponent
      },

      { path: "**", redirectTo: "/dashboard" }
    ]
  },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
