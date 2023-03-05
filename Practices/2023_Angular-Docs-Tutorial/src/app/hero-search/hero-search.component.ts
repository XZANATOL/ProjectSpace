import { Component, OnInit } from '@angular/core';

import { Observable, Subject } from "rxjs";
import {debounceTime, distinctUntilChanged, switchMap } from "rxjs/operators";

import { HeroInterface } from "../heroes/hero-interface";
import { HeroService } from "../common/services/heroService/hero.service";

@Component({
  selector: 'hero-search',
  templateUrl: './hero-search.component.html',
  styleUrls: ['./hero-search.component.css']
})
export class HeroSearchComponent implements OnInit {
  heroes$!: Observable<HeroInterface[]>
  private searchTerms = new Subject<string>()

  constructor(
      private heroService: HeroService
    ){}

  search(term: string): void{
    this.searchTerms.next(term)
  }

  ngOnInit(): void{
    this.heroes$ = this.searchTerms.pipe(
        debounceTime(100),
        distinctUntilChanged(),
        switchMap((term: string) => this.heroService.searchHero(term))
      )
  }
}
