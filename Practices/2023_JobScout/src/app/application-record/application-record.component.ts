import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { FormGroup, FormControl, Validators } from '@angular/forms';

import { AppRecordService } from "../common/services/appRecord/app-record.service"
import { fileType } from "../common/formValidators/fileType"

@Component({
  selector: 'app-application-record',
  templateUrl: './application-record.component.html',
  styleUrls: ['./application-record.component.css']
})
export class ApplicationRecordComponent implements OnInit, OnDestroy {
  private subscription: any;
  isNewRecord: boolean = false
  private recordId: string = ""
  inputFileName?: string // If there's an existing record

  form = new FormGroup({
    title: new FormControl("", [Validators.required]),
    url: new FormControl("", [Validators.required, Validators.pattern("^https?://.+")]),
    stage: new FormControl("", [Validators.required]),
    cv: new FormControl("", [fileType(["pdf"])]),
    cv_file: new FormControl(""),
    questions: new FormControl(""),
    notes: new FormControl(""),
  })

  onFileChange(event: any){
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.patchValue({
        cv_file: file
      });
    }
  }
  clearCV(){
    this.form.patchValue({
      cv: ""
    })
  }


  submit(){
    if(this.isNewRecord){
      this.appRecService.submit(this.form.value, null)
    }else{
      this.appRecService.submit(this.form.value, this.recordId)
    }
  }


  constructor(
      private route: ActivatedRoute,
      private appRecService: AppRecordService
    ){}
  ngOnInit(){
    this.subscription =  this.route.params.subscribe( (params) => {
      if(params["id"] != undefined){

        this.appRecService.retrieve(params["id"]).then((res) => {
          this.form.patchValue({
            title: res.title,
            stage: res.stage,
            url: res.job_url,
            questions: res.questions,
            notes: res.notes
          })
          this.inputFileName = res.cv
          this.recordId = params["id"]
        })
        
      }else{
        this.isNewRecord = true
      }
    });
  }
  ngOnDestroy(){
    this.subscription.unsubscribe();
  }

  test(){
    console.log(this.form)
  }
}
