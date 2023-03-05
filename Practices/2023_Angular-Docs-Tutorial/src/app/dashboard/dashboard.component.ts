import { Component, OnInit } from '@angular/core';

import { HeroInterface } from "../heroes/hero-interface"
import { HeroService } from "../common/services/heroService/hero.service"

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  heroes: HeroInterface[] = [];

  constructor(
      private heroService: HeroService
    ){}

  ngOnInit(): void{
    this.getHeroes()
  }

  getHeroes(): void{
    this.heroService.getHeroes()
      .subscribe((heroes) => {this.heroes = heroes})
  }
}
