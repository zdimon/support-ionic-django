import { Component, OnInit } from '@angular/core';
import { TaskService } from './task.service';
import {Router, ActivatedRoute, NavigationEnd} from '@angular/router';

@Component({
  selector: 'app-task-list',
  templateUrl: './task.list.component.html',
  styleUrls: ['./task.component.scss'],
})
export class TaskListComponent implements OnInit {
  items: any[] = [];
  filter: string;
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

    this.filter = this.route.snapshot.paramMap.get('filter');
    this.refresh();
    console.log('onInit');

  }

  refresh = () => {
    this.task_service.getTaskList(this.filter).subscribe((data: any) => {
      this.items = data['tasks'];
      this.filter = this.route.snapshot.paramMap.get('filter');
    });
  }

  setFilter = (status) => {
     this.router.navigate(['/task/list/'+status]);
  };

}
