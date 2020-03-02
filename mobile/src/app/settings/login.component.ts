import { CommonHttpClient } from './../http.service';
import { AppConfigService } from './../app.service';
import { Component, OnInit } from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './../globals';



/*
  http://localhost:4200/settings/login/fedda421636cd36d7bddba5eace058a4/client

  http://localhost:4200/settings/login/7843a9ded793b7ed28dc2ebc23b5813c/10/task

*/

@Component({
  selector: 'app-settings',
  template: 'wait...',
})
export class LoginComponent implements OnInit {
  task_id: string;
  constructor( private router: Router,
               private route: ActivatedRoute,
               private AppConfigService: AppConfigService,
               private http: CommonHttpClient) { }

  ngOnInit() {
    const sign = this.route.snapshot.paramMap.get('sign');
    const taskId = this.route.snapshot.paramMap.get('taskId');


    if (sign && taskId ) {
      const data = {'sign': sign};
      this.http.post(API_URL + '/mobile_api/enter_task', data).subscribe((rez: any) => {
        console.log(rez);
        if (rez.status === 1) {
            alert(rez.message);
        } else {
            localStorage.setItem('current_user_id', rez.user_id);
            localStorage.setItem('current_user_sign', rez.user_sign);
            this.task_id = taskId;
            //this.router.navigate(['/task/show/' + taskId]);
            window.location.href = '/task/show/' + taskId;
        }
      });
    }
    // by client
    if (sign && !taskId) {
      const data = {'sign': sign};
      this.http.post(API_URL + '/mobile_api/enter_client', data).subscribe((rez: any) => {
        console.log(rez);
        if (rez.status === 1) {
            alert(rez.message);
        } else {
            localStorage.setItem('current_user_id', rez.user_id);
            localStorage.setItem('current_user_sign', rez.user_sign);
            this.AppConfigService.getDatabaseFromServer().subscribe((data) => {
              this.AppConfigService.setAppConfig(data);
            });
            alert('test');
            window.location.href = '/home';
            //this.router.navigate(['/home']);
            
        }
      });
    }



    /*
    const data = {'sign': sign};
    this.http.post(API_URL + '/mobile_api/enter', data).subscribe((rez: any) => {
      console.log(rez);
      if (rez.status === 1) {
          alert(rez.message);
      } else {
          localStorage.setItem('current_user_id', rez.user_id);
          localStorage.setItem('current_user_sign', sign);
          this.router.navigate(['/home']);
      }
    });
    */

  }

}
