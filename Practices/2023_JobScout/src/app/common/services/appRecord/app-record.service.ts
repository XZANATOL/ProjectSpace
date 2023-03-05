import { Injectable } from '@angular/core';
import PocketBase from 'pocketbase';
import { Router } from '@angular/router';

import { AuthRefreshService } from '../auth-refresh/authrefresh.service'

@Injectable({
  providedIn: 'root'
})
export class AppRecordService extends AuthRefreshService {

  constructor(
      private routerAppRecord: Router
    ){
    super(routerAppRecord)
  }

  async retrieve(id: string): Promise<any>{
    let cookie = localStorage.getItem("pocketbase_auth")!
    this.pb.authStore.loadFromCookie(cookie)
    
    const res = await this.pb.collection("job_scout").getOne(id)

    localStorage.setItem("pocketbase_auth", cookie)
    return res
  }

  async submit(form: any, id: string | null): Promise<boolean>{
    const session = await this.check()

    if(session){
      let cookie = localStorage.getItem("pocketbase_auth")!
      this.pb.authStore.loadFromCookie(cookie)

      if(id == null){

        const res = await this.pb.collection("job_scout").create({
          title: form.title,
          user: this.pb.authStore.model!["id"],
          job_url: form.url,
          stage: form.stage,
          cv: form.cv_file,
          questions: form.questions,
          notes: form.notes
        })

      }else{
        let data = {
          title: form.title,
          user: this.pb.authStore.model!["id"],
          job_url: form.url,
          stage: form.stage,
          cv: form.cv_file,
          questions: form.questions,
          notes: form.notes
        }
        if (form.cv == ""){
          delete(data.cv)
        }

        const res = await this.pb.collection("job_scout").update(id, data)

      }
      
      localStorage.setItem("pocketbase_auth", cookie)
      this.routerAppRecord.navigateByUrl("/dashboard")
      return true
    }

    return false
  }
}
