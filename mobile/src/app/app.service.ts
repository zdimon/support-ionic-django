import { CommonHttpClient } from './http.service';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './globals';
//import { map } from 'rxjs/operators';
//import { Observable } from 'rxjs/Observable';

@Injectable()
export class AppConfigService {
  appConfig;
  appDb;

  constructor(private http: CommonHttpClient) { }

  getConfig(): Promise<any> {

      return new Promise( (resolve, reject) =>  {

         
        if (this.getDatabaseFromServer()) {
          this.getDatabaseFromServer().subscribe((data) => {
            this.setDb(data);
            console.log(this.getDb());
            localStorage.setItem('filter',data['filter']);
            resolve();
          });
        }
        
        resolve();
        /**
        this.http.get(API_URL + '/mobile_api/settings').subscribe(( data ) => {
            this.appConfig = data;
            resolve();
        });
        **/

      });
  }

  getDatabaseFromServer(): any{
    //if (localStorage.getItem('current_user_id')) {
      return this.http.get(API_URL + '/mobile_api/task_list/'+localStorage.getItem('filter'));
    //} else {
    //  return false;
    //}
  }

  getDb() {
    return this.appDb;
  }
  setDb(db: any) {
    this.appDb = db;
  }

  getTaskById(id: number): any{
// tslint:disable-next-line: forin
/*
    for (const i in Object.keys(this.getDb()['tasks'])){
      if (this.getDb()['tasks'][i]['id'] === id) {
        return this.getDb()['tasks'][i];
      }
    }
*/
    return this.http.get(API_URL + '/mobile_api/show_task/' + id);
  }

  setAppConfig(val: any) {
    this.appConfig = val;
  }

  getAppConfig() {
    return this.appConfig;
  }

  changeStatus(task_id,status): any{
      const data = {'task_id': task_id, 'status': status}
      return this.http.post(API_URL + '/mobile_api/set_status', data);
  }

}
