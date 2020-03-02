import { API_URL } from './../globals';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonHttpClient } from './../http.service';

@Injectable()
export class TaskService {
  task_list: any;
  constructor(private http: CommonHttpClient) { }


  getTaskList(filter: string) {
    return this.http.get(API_URL + '/mobile_api/task_list/' + filter);
  }

  saveTask(data: any) {
    return this.http.post(API_URL + '/mobile_api/save_task', data );
  }


}
