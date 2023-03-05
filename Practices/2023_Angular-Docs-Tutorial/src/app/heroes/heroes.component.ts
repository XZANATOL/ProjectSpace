import { Component, Input, OnInit } from '@angular/core';

import { MessageService } from "../common/services/messages/message.service";
import { HeroInterface } from "./hero-interface";
import { HeroService } from "../common/services/heroService/hero.service";


@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent implements OnInit {
  heroes: HeroInterface[] = []
  selectedHero?: HeroInterface

  constructor(
      private heroService: HeroService,
      private messageService: MessageService
    ){}

  ngOnInit(): void {
    this.getHeroes()
  }

  getHeroes(): void {
    this.heroService.getHeroes()
      .subscribe((heroes) => this.heroes = heroes)
  }

}
