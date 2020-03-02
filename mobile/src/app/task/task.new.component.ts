import { Component, OnInit } from '@angular/core';
import { TaskService } from './task.service';
import {Router, ActivatedRoute, NavigationEnd} from '@angular/router';

@Component({
  selector: 'app-task-new',
  templateUrl: './task.new.component.html',
  styleUrls: ['./task.component.scss'],
})
export class TaskNewComponent implements OnInit {
  description: string;
  constructor( private task_service: TaskService,
               public route: ActivatedRoute,
               public router: Router ) { 

    router.events.subscribe(event => {
        if (event instanceof NavigationEnd) {
          this.ngOnInit();
        }
      });
  }

  ngOnInit() {

    console.log('onInit new');

  }

  submitForm = () => {
     const data = { 'content': this.description };
     this.task_service.saveTask(data).subscribe((rez) => {
        
        console.log(rez);
        this.router.navigate(['/task/show/' + rez['task_id']]);
     });
     this.description = '';
  }

}
