import { Component, OnInit, Input, ViewChild } from '@angular/core';
import {Router, ActivatedRoute, NavigationEnd} from '@angular/router';
import { AppConfigService } from './../app.service';


@Component({
  selector: 'app-show-task',
  templateUrl: './task.show.component.html',
  styleUrls: ['./task.component.scss']
})
export class TaskShowComponent implements OnInit {
  @Input() task: any = {};
  @ViewChild('content') content: any;
  constructor(
    public route: ActivatedRoute,
    public router: Router,
    public AppConfigService: AppConfigService) { 

      router.events.subscribe(event => {
        if (event instanceof NavigationEnd) {
          this.ngOnInit();
        }
      });

    }

  ngOnInit() {
    this.AppConfigService.getTaskById(parseInt(this.route.snapshot.paramMap.get('taskId'), 10)).subscribe((data) => {
      this.task = data['task'];
    });
  }

  commentAddedEmmited(data) {
    this.AppConfigService.getTaskById(parseInt(this.route.snapshot.paramMap.get('taskId'), 10)).subscribe(( data ) => {
      this.task = data['task'];
      //this.content.scrollToBottom(300);
    });
  }

  setStatus = (task_id, status) => {
    this.AppConfigService.changeStatus(task_id,status).subscribe((rez) => {
       console.log(rez);
    });
  }


}
