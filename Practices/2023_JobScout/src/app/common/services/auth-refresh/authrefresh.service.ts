import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import PocketBase from 'pocketbase';

import { environment } from '../../../../environments/environment'

@Injectable({
  providedIn: 'root'
})
export class AuthRefreshService {
  pb = new PocketBase(environment.Db_URL)

  constructor(
      private router: Router
    ){ }


  public async check(): Promise<boolean>{
    let cookie = localStorage.getItem("pocketbase_auth")!
    
    this.pb.authStore.loadFromCookie(cookie)
    if(this.pb.authStore.isValid){ // If user's logged-in
      localStorage.setItem("pocketbase_auth", cookie)
      return true
    }

    if(this.pb.authStore.model != null){ // Case localStorage was manually deleted
      await this.pb.collection('users').authRefresh()
      if(this.pb.authStore.isValid){ // Recheck refreshed token
        cookie = this.pb.authStore.exportToCookie({}, "pb_auth")
        localStorage.setItem("pocketbase_auth", cookie)
        return true
      }
    }

    this.router.navigateByUrl("/")
    return false
  }

  public goToLogin(){
    this.router.navigateByUrl("/")
  }

}
