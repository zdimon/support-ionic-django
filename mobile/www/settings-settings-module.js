(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["settings-settings-module"],{

/***/ "./src/app/settings/login.component.ts":
/*!*********************************************!*\
  !*** ./src/app/settings/login.component.ts ***!
  \*********************************************/
/*! exports provided: LoginComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "LoginComponent", function() { return LoginComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./../http.service */ "./src/app/http.service.ts");
/* harmony import */ var _app_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./../app.service */ "./src/app/app.service.ts");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./../globals */ "./src/app/globals.ts");






/*
  http://localhost:4200/settings/login/fedda421636cd36d7bddba5eace058a4/client

  http://localhost:4200/settings/login/7843a9ded793b7ed28dc2ebc23b5813c/10/task

*/
var LoginComponent = /** @class */ (function () {
    function LoginComponent(router, route, AppConfigService, http) {
        this.router = router;
        this.route = route;
        this.AppConfigService = AppConfigService;
        this.http = http;
    }
    LoginComponent.prototype.ngOnInit = function () {
        var _this = this;
        var sign = this.route.snapshot.paramMap.get('sign');
        var taskId = this.route.snapshot.paramMap.get('taskId');
        if (sign && taskId) {
            var data = { 'sign': sign };
            this.http.post(_globals__WEBPACK_IMPORTED_MODULE_5__["API_URL"] + '/mobile_api/enter_task', data).subscribe(function (rez) {
                console.log(rez);
                if (rez.status === 1) {
                    alert(rez.message);
                }
                else {
                    localStorage.setItem('current_user_id', rez.user_id);
                    localStorage.setItem('current_user_sign', rez.user_sign);
                    _this.task_id = taskId;
                    //this.router.navigate(['/task/show/' + taskId]);
                    window.location.href = '/task/show/' + taskId;
                }
            });
        }
        // by client
        if (sign && !taskId) {
            var data = { 'sign': sign };
            this.http.post(_globals__WEBPACK_IMPORTED_MODULE_5__["API_URL"] + '/mobile_api/enter_client', data).subscribe(function (rez) {
                console.log(rez);
                if (rez.status === 1) {
                    alert(rez.message);
                }
                else {
                    localStorage.setItem('current_user_id', rez.user_id);
                    localStorage.setItem('current_user_sign', rez.user_sign);
                    _this.AppConfigService.getDatabaseFromServer().subscribe(function (data) {
                        _this.AppConfigService.setAppConfig(data);
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
    };
    LoginComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_3__["Component"])({
            selector: 'app-settings',
            template: 'wait...',
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_4__["Router"],
            _angular_router__WEBPACK_IMPORTED_MODULE_4__["ActivatedRoute"],
            _app_service__WEBPACK_IMPORTED_MODULE_2__["AppConfigService"],
            _http_service__WEBPACK_IMPORTED_MODULE_1__["CommonHttpClient"]])
    ], LoginComponent);
    return LoginComponent;
}());



/***/ }),

/***/ "./src/app/settings/settings.component.html":
/*!**************************************************!*\
  !*** ./src/app/settings/settings.component.html ***!
  \**************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<ion-header>\n  <ion-toolbar>\n    <ion-buttons slot=\"start\">\n      <ion-menu-button></ion-menu-button>\n    </ion-buttons>\n    <ion-title>\n      Настройки\n    </ion-title>\n  </ion-toolbar>\n</ion-header>\n\n<ion-content>\n  <ion-list>\n    <ion-item>\n      <ion-icon name=\"wifi\" slot=\"start\"></ion-icon>\n       test\n      <div class=\"item-note\" slot=\"end\">\n         note\n      </div>\n    </ion-item>\n  </ion-list>\n  <!--\n    <div *ngIf=\"selectedItem\" padding>\n      You navigated here from <b>{{selectedItem.title }}</b>\n    </div>\n  -->\n</ion-content>\n"

/***/ }),

/***/ "./src/app/settings/settings.component.scss":
/*!**************************************************!*\
  !*** ./src/app/settings/settings.component.scss ***!
  \**************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL3NldHRpbmdzL3NldHRpbmdzLmNvbXBvbmVudC5zY3NzIn0= */"

/***/ }),

/***/ "./src/app/settings/settings.component.ts":
/*!************************************************!*\
  !*** ./src/app/settings/settings.component.ts ***!
  \************************************************/
/*! exports provided: SettingsComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SettingsComponent", function() { return SettingsComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var SettingsComponent = /** @class */ (function () {
    function SettingsComponent() {
    }
    SettingsComponent.prototype.ngOnInit = function () { };
    SettingsComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-settings',
            template: __webpack_require__(/*! ./settings.component.html */ "./src/app/settings/settings.component.html"),
            styles: [__webpack_require__(/*! ./settings.component.scss */ "./src/app/settings/settings.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], SettingsComponent);
    return SettingsComponent;
}());



/***/ }),

/***/ "./src/app/settings/settings.module.ts":
/*!*********************************************!*\
  !*** ./src/app/settings/settings.module.ts ***!
  \*********************************************/
/*! exports provided: SettingsModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SettingsModule", function() { return SettingsModule; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _login_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./login.component */ "./src/app/settings/login.component.ts");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var _ionic_angular__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @ionic/angular */ "./node_modules/@ionic/angular/dist/fesm5.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _settings_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./settings.component */ "./src/app/settings/settings.component.ts");








/*
  http://localhost:4200/settings/login/fedda421636cd36d7bddba5eace058a4/client

  http://localhost:4200/settings/login/7843a9ded793b7ed28dc2ebc23b5813c/10/task

*/
var SettingsModule = /** @class */ (function () {
    function SettingsModule() {
    }
    SettingsModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["NgModule"])({
            declarations: [_settings_component__WEBPACK_IMPORTED_MODULE_7__["SettingsComponent"], _login_component__WEBPACK_IMPORTED_MODULE_1__["LoginComponent"]],
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_3__["CommonModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_4__["FormsModule"],
                _ionic_angular__WEBPACK_IMPORTED_MODULE_5__["IonicModule"],
                _angular_router__WEBPACK_IMPORTED_MODULE_6__["RouterModule"].forChild([
                    {
                        path: '',
                        component: _settings_component__WEBPACK_IMPORTED_MODULE_7__["SettingsComponent"]
                    },
                    {
                        path: 'login/:sign/client',
                        component: _login_component__WEBPACK_IMPORTED_MODULE_1__["LoginComponent"]
                    },
                    {
                        path: 'login/:sign/:taskId/task',
                        component: _login_component__WEBPACK_IMPORTED_MODULE_1__["LoginComponent"]
                    },
                ])
            ]
        })
    ], SettingsModule);
    return SettingsModule;
}());



/***/ })

}]);
//# sourceMappingURL=settings-settings-module.js.map