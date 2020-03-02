import { Component, OnInit, ViewChild } from '@angular/core';
import { CommonHttpClient } from './../http.service';
import { API_URL } from './../globals';
import {Router, ActivatedRoute, NavigationEnd} from '@angular/router';

@Component({
  selector: 'app-photo',
  templateUrl: './photo.component.html',
  styleUrls: ['./photo.component.scss'],
})
export class PhotoComponent implements OnInit {
  navigator: any;
  @ViewChild('videoElement') videoElement: any;  
  @ViewChild('canvas') canvas: any;  
  public video: any;
  public innerWidth: any;
  public innerHeight: any;
  public cameraId: string;
  public stream: any;
  public browser = <any>navigator;

  constructor( public route: ActivatedRoute,
               private http: CommonHttpClient,
               public router: Router) {



                }

  getActiveCam = () => {
    return new Promise( (resolve, reject) =>  {
      
      this.browser.mediaDevices.enumerateDevices()
      .then((devices)=> {
        console.log(devices);
        var arrayLength = devices.length;
        for (var i = 0; i < arrayLength; i++) {
          if(devices[i].label.indexOf('Camera') !== -1 || devices[i].label.indexOf('back') !== -1){
            this.cameraId = devices[i].deviceId;
            console.log(devices[i]);
          }
        }
        resolve();
      })
    })
  };

  ngOnInit() {
    this.innerWidth = window.innerWidth;
    this.innerHeight = window.innerHeight;
    this.video = this.videoElement.nativeElement;
    this.canvas = this.canvas.nativeElement;
    var streamTrack = <any>MediaStreamTrack;

      var constraints = {};
      /*
      streamTrack.getSources (function(sources) {
          sources.forEach(function(info) {
              console.log(info);
              if (info.facing == "environment") {
                  constraints = {
                    video: {
                      optional: [{sourceId: info.id}]
                    }
                  };
              }
          })
      })
       */

      this.browser.getUserMedia = (this.browser.getUserMedia ||
      this.browser.webkitGetUserMedia ||
      this.browser.mozGetUserMedia ||
      this.browser.msGetUserMedia);

      
        this.browser.mediaDevices.getUserMedia({ audio: false, video: {  facingMode: 'environment' , width: 800,  height: 600 }}).then(stream => {
          this.stream = stream;
          this.video.srcObject = this.stream;
          },(e) => {alert(e)});
       

      /*
      browser.mediaDevices.enumerateDevices()
      .then((devices)=> {
        console.log(devices.length);
        console.log(devices);
        console.log(this.video);
        devices.forEach(function(device) {
          if(device.label.indexOf('Camera') !== -1){
            console.log(device);
            console.log(this.video);
            browser.mediaDevices.getUserMedia({ facingMode: { exact: device.deviceId }, audio: false, video: { width: 800,  height: 600 }}).then(stream => {
              this.video.srcObject = stream;
              },(e) => {alert(e)});
          }
          
        })
        
      });
      */


  }      

  photoEventHandler = (e) => {
    var context = this.canvas.getContext('2d');
    context.drawImage(this.video, 0, 0, 800, 600);
    var dataURL = this.canvas.toDataURL();
    var data = {imgBase64: dataURL, task_id: this.route.snapshot.paramMap.get('taskId')};
    this.http.post(API_URL + '/mobile_api/photo',data).subscribe((rez) => {
       this.router.navigate(['/task/show/'+this.route.snapshot.paramMap.get('taskId')]);
       //this.video.srcObject = false;
       //this.stream.stop();
    });
    console.log(this.innerHeight);
    
  };

}
