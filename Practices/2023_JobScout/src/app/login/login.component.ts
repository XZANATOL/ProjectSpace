import { Component, OnInit } from '@angular/core';

import { LoginService } from '../common/services/auth/login.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  email?: string;
  password?: string;
  clicked: boolean = false;
  validationFail: boolean = false;

  constructor(
      private loginService: LoginService
    ){}

  async ngOnInit(){
    this.loginService.check()
  }

  async submit(): Promise<void>{
    if(this.email && this.password){
      this.clicked = true
      let validation: boolean = await this.loginService.login(this.email, this.password)
      if(!validation){
        this.validationFail = true
        this.clicked = false
      }
    }   
  }
}
