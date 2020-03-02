import { AppConfigService } from './app.service';
import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';


@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {
  public appPages = [
    {
      title: 'Заявки',
      url: '',
      icon: 'home'
    },
    {
      title: 'На рассмотрении',
      url: '/task/list/new',
      icon: 'paper-plane'
    },
    {
      title: 'В работе',
      url: '/task/list/inprocess',
      icon: 'build'
    },
    {
      title: 'Выполнено',
      url: '/task/list/done',
      icon: 'boat'
    },
    {
      title: 'Архив',
      url: '/task/list/deleted',
      icon: 'close-circle'
    },
    {
      title: 'Настройки',
      url: '/settings',
      icon: 'construct'
    }
  ];

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private appConfigService: AppConfigService
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
      //this.appConfigService.getConfig().subscribe((data: any) => {
      //    this.appConfigService.setAppConfig(data);
      //    console.log(this.appConfigService.getAppConfig());
      //});


    });
  } 
}
