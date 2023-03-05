import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators'

import { HeroInterface } from "../../../heroes/hero-interface"
import { HEROES } from "../../../heroes/heroes-mock"
import { MessageService } from "../messages/message.service"

@Injectable({
  providedIn: 'root'
})
export class HeroService {
  heroesURL = "api/heroes"
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
      private messageService: MessageService,
      private http: HttpClient
    ) { }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  log(message: string){
    this.messageService.add(message)
  }

  getHeroes(): Observable<HeroInterface[]>{
    const heroes = this.http.get<HeroInterface[]>(this.heroesURL)
      .pipe(
          tap(_ => this.log("HeroService: fetched heroes")),
          catchError(this.handleError<HeroInterface[]>("getHeroes", []))
        )
    return heroes
  }

  getHero(id: number): Observable<HeroInterface>{
    const url = `${this.heroesURL}/${id}`
    const hero = this.http.get<HeroInterface>(url)
      .pipe(
          tap(_ => this.log(`HeroService: fetched hero of id=${id}`)),
          catchError(this.handleError<HeroInterface>(`getHero id=${id}`))
        )
    return hero
  }

  searchHero(name: string): Observable<HeroInterface[]>{
    let nameValidate = name.trim().split(" ")
    if(!nameValidate.length || name == ""){
      return of([])
    }
    const hero = this.http.get<HeroInterface[]>(`${this.heroesURL}/?name=${nameValidate[0]}`)
      .pipe(
          tap(x => x.length ? // <- if condition
              this.log(`Found heroes "${nameValidate[0]}"`) :
              this.log(`Found no matchings for "${nameValidate[0]}"`)
            ),
          catchError(this.handleError<HeroInterface[]>("searchHero", []))
        )
    return hero
  }

  updateHero(hero: HeroInterface): Observable<any>{
    const h = this.http.put(this.heroesURL, hero, this.httpOptions)
      .pipe(
          tap(_ => this.log(`Updated hero id=${hero.id}`)),
          catchError(this.handleError<any>("Update hero"))
        )
    return h
  }
}
