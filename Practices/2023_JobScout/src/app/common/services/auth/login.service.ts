import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import PocketBase from 'pocketbase';

import { environment } from '../../../../environments/environment'

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  pb = new PocketBase(environment.Db_URL);

  constructor(
      private router: Router
    ){}

  async check(): Promise<void>{
    let cookie = localStorage.getItem("pocketbase_auth")!
    this.pb.authStore.loadFromCookie(cookie)
    if(this.pb.authStore.isValid){ // If user's already logged-in
      localStorage.setItem("pocketbase_auth", cookie)
      this.forward()
    }
  }

  async login(identity: string, password: string): Promise<boolean>{
    try{
      await this.pb.collection('users').authWithPassword(identity,password)
      let cookie = this.pb.authStore.exportToCookie({}, "pb_auth")
      localStorage.setItem("pocketbase_auth", cookie)
      this.forward()
      return true
    }catch{
      return false
    }
  }

  private forward(): void{
    this.router.navigateByUrl("/dashboard")
  }

}
