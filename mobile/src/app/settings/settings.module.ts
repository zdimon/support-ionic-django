import { LoginComponent } from './login.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';

import { SettingsComponent } from './settings.component';

/*
  http://localhost:4200/settings/login/fedda421636cd36d7bddba5eace058a4/client

  http://localhost:4200/settings/login/7843a9ded793b7ed28dc2ebc23b5813c/10/task

*/

@NgModule({
  declarations: [SettingsComponent, LoginComponent],
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild([
      {
        path: '',
        component: SettingsComponent
      },
      {
        path: 'login/:sign/client',
        component: LoginComponent
      },
      {
        path: 'login/:sign/:taskId/task',
        component: LoginComponent
      },
    ])
  ]
})
export class SettingsModule { }
