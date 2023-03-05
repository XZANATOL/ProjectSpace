import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import PocketBase from 'pocketbase';

import { AuthRefreshService } from '../auth-refresh/authrefresh.service'

@Injectable({
  providedIn: 'root'
})
export class DashboardService extends AuthRefreshService {

  async retrieve(): Promise<Array<Object>>{
    let cookie = localStorage.getItem("pocketbase_auth")!
    this.pb.authStore.loadFromCookie(cookie)
    
    const submitted = await this.pb.collection("job_scout").getList(1, 100, {
      filter: `user = '${this.pb.authStore.model!.id}' && stage = 'Submitted'`,
      sort: 'updated'
    })
    const accepted = await this.pb.collection("job_scout").getList(1, 100, {
      filter: `user = '${this.pb.authStore.model!.id}' && stage = 'Accepted'`,
      sort: 'updated'
    })
    const rejected = await this.pb.collection("job_scout").getList(1, 100, {
      filter: `user = '${this.pb.authStore.model!.id}' && stage = 'Rejected'`,
      sort: 'updated'
    })

    localStorage.setItem("pocketbase_auth", cookie)
    return [submitted, accepted, rejected]
  }


  async user(): Promise<string>{
    let cookie = localStorage.getItem("pocketbase_auth")!
    this.pb.authStore.loadFromCookie(cookie)

    let name = this.pb.authStore.model!['name']

    localStorage.setItem("pocketbase_auth", cookie)
    return name
  }


  async deleteRecord(id: string): Promise<boolean>{
    const session = await this.check()

    if(session){
      let cookie = localStorage.getItem("pocketbase_auth")!
      this.pb.authStore.loadFromCookie(cookie)

      let t = await this.pb.collection('job_scout').delete(id)
      localStorage.setItem("pocketbase_auth", cookie)
      return true
    }

    return false
  }


  logout(){
    this.pb.authStore.clear()
    this.goToLogin()
  }

}
