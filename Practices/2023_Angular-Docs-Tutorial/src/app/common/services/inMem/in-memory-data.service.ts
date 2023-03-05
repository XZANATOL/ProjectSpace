import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';

import { HeroInterface } from "../../../heroes/hero-interface"

@Injectable({
  providedIn: 'root'
})
export class InMemoryDataService implements InMemoryDbService {
  createDb(){
    const heroes = [
      { id: 12, name: 'XZANATOL', alias: 'Hacker Cat'},
      { id: 13, name: 'Tarek', alias: 'Chair Man' },
      { id: 14, name: 'Amr', alias: 'Shblanga Master'},
      { id: 15, name: 'Saeed', alias: 'AK Kebda' },
      { id: 16, name: 'Yehia', alias: 'Nigga Killer' },
      { id: 17, name: 'Hasan', alias: 'Gold Eagle' },
    ];
    return {heroes}
  }

  genId(heroes: HeroInterface[]): number {
    return heroes.length > 0 ? Math.max(...heroes.map(hero => hero.id)) + 1 : 11;
  }
}
