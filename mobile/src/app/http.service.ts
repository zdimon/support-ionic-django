import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Injectable()
export class CommonHttpClient {
  headers: any;

  constructor (private http: HttpClient) {
    
    
    this.headers = new HttpHeaders()
    .set('Content-Type', 'application/json; text/html; application/x-www-form-urlencoded; charset=UTF-8')
    .set('Authorization', 'Token ' + localStorage.getItem('current_user_sign'))
    .set('Access-Control-Allow-Headers', '*');
    
  }

  public get(url: string): any {

    return this.http
    .get(url, { headers: this.headers })

  }

  public post(url: string, data: any): any {
    //console.log('getttttttttt');
    //console.log(this.headers);
    return this.http
    .post(url, data, { headers: this.headers })

  }


}