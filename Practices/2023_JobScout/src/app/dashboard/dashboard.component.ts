import { Component, OnInit } from '@angular/core';
import PocketBase from 'pocketbase';

import { AuthRefreshService } from '../common/services/auth-refresh/authrefresh.service';
import { DashboardService } from '../common/services/dashboard/dashboard.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  user?: string
  submitted?: any
  accepted?: any
  rejected?: any

  constructor(
      private dashboardService: DashboardService
    ){}

  ngOnInit(){
    this.loadData()
  }


  private loadData(){
    this.dashboardService.retrieve().then(
      (data) => {
        if(data){
          [this.submitted, this.accepted, this.rejected] = data
        }
    }).then(() => {
      this.dashboardService.user().then((name) => {
        this.user = name
      })
    })
  }


  async deleteRecord(id: string){
    let res = await this.dashboardService.deleteRecord(id)
    if(res){
      this.submitted.items.forEach((element: any, index: number) => {
        if(element.id == id){
          this.submitted.items.splice(index, 1)
        }
      })

      this.accepted.items.forEach((element: any, index: number) => {
        if(element.id == id){
          this.accepted.items.splice(index, 1)
        }
      })

      this.rejected.items.forEach((element: any, index: number) => {
        if(element.id == id){
          this.rejected.items.splice(index, 1)
        }
      })
    }
  }


  logout(){
    this.dashboardService.logout()
  }

}
