import { TaskNewComponent } from './task.new.component';
import { PhotoComponent } from './../photo/photo.component';
import { TaskListComponent } from './task.list.component';
import { TaskComponent } from './task.component';
import { FormCommentComponent } from './form.comment';
import { TaskShowComponent } from './task.show.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { FormsModule }   from '@angular/forms';




@NgModule({
  declarations: [
    TaskComponent,
    TaskListComponent,
    FormCommentComponent,
    PhotoComponent,
    TaskNewComponent,
    TaskShowComponent],
  imports: [
    CommonModule,
    IonicModule,
    FormsModule,
    RouterModule.forChild([
      {
        path: 'show/:taskId',
        component: TaskComponent
      },
      {
        path: 'list/:filter',
        component: TaskListComponent
      },
      {
        path: 'new',
        component: TaskNewComponent
      },
      {
        path: 'photo/:taskId',
        component: PhotoComponent
      }
    ])
  ]
})
export class TaskModule { }
