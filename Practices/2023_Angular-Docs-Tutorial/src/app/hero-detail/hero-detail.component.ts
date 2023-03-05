import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { Location } from "@angular/common"

import { HeroInterface } from "../heroes/hero-interface";

import { HeroService } from "../common/services/heroService/hero.service"
import { MessageService } from "../common/services/messages/message.service"

@Component({
  selector: 'app-hero-detail',
  templateUrl: './hero-detail.component.html',
  styleUrls: ['./hero-detail.component.css']
})
export class HeroDetailComponent implements OnInit {

  hero?: HeroInterface;

  constructor(
      private messageService: MessageService,
      private heroService: HeroService,
      private location: Location,
      private activatedRoute: ActivatedRoute
    ){}

  ngOnInit(): void{
    this.getHero()
  }

  getHero(): void{
    const id = Number(this.activatedRoute.snapshot.paramMap.get("id"))
    this.heroService.getHero(id)
      .subscribe( (hero) => this.hero = hero)
  }

  save(): void{
    if(this.hero){
      this.heroService.updateHero(this.hero)
        .subscribe(() => this.goBack())
    }
  }

  goBack(): void{
    this.location.back()
  }
}
