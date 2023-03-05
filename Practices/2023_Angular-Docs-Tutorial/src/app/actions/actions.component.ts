import { Component } from '@angular/core';

import { ActionInterface } from "./action-interface"
import { ACTIONS } from "./action-mock"

@Component({
  selector: 'app-actions',
  templateUrl: './actions.component.html',
  styleUrls: ['./actions.component.css']
})
export class ActionsComponent {
  actions: ActionInterface[] = ACTIONS
}
