(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["task-task-module"],{

/***/ "./src/app/photo/photo.component.html":
/*!********************************************!*\
  !*** ./src/app/photo/photo.component.html ***!
  \********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<ion-header>\n  <ion-toolbar>\n    <ion-buttons slot=\"start\">\n      <ion-menu-button></ion-menu-button>\n    </ion-buttons>\n    <ion-title>\n      Сделать фото\n    </ion-title>\n  </ion-toolbar>\n</ion-header>\n\n<ion-content>\n\n    <ion-row>\n\n        <ion-col>\n            <ion-button (click)=\"photoEventHandler(e)\"  color=\"danger\" expand=\"full\">Сделать фото</ion-button>    \n        </ion-col>\n        \n      </ion-row>\n\n  <ion-row>\n    <video #videoElement id=\"video\" autoplay=\"autoplay\"></video>\n  </ion-row>\n  <ion-row>\n    <canvas #canvas width=\"800\" height=\"600\"> </canvas>\n  </ion-row>\n\n</ion-content>\n"

/***/ }),

/***/ "./src/app/photo/photo.component.scss":
/*!********************************************!*\
  !*** ./src/app/photo/photo.component.scss ***!
  \********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "video {\n  border: 1px solid silver; }\n\ncanvas {\n  display: none; }\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3pkaW1vbi9zdG9yYWdlMS93d3cvc3VwcG9ydC9tb2JpbGUvc3JjL2FwcC9waG90by9waG90by5jb21wb25lbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtFQUNJLHdCQUF3QixFQUFBOztBQUc1QjtFQUVJLGFBQWEsRUFBQSIsImZpbGUiOiJzcmMvYXBwL3Bob3RvL3Bob3RvLmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsidmlkZW8ge1xuICAgIGJvcmRlcjogMXB4IHNvbGlkIHNpbHZlcjtcbn1cblxuY2FudmFzIHtcblxuICAgIGRpc3BsYXk6IG5vbmU7XG5cbn0iXX0= */"

/***/ }),

/***/ "./src/app/photo/photo.component.ts":
/*!******************************************!*\
  !*** ./src/app/photo/photo.component.ts ***!
  \******************************************/
/*! exports provided: PhotoComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "PhotoComponent", function() { return PhotoComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./../http.service */ "./src/app/http.service.ts");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./../globals */ "./src/app/globals.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");





var PhotoComponent = /** @class */ (function () {
    function PhotoComponent(route, http, router) {
        var _this = this;
        this.route = route;
        this.http = http;
        this.router = router;
        this.browser = navigator;
        this.getActiveCam = function () {
            return new Promise(function (resolve, reject) {
                _this.browser.mediaDevices.enumerateDevices()
                    .then(function (devices) {
                    console.log(devices);
                    var arrayLength = devices.length;
                    for (var i = 0; i < arrayLength; i++) {
                        if (devices[i].label.indexOf('Camera') !== -1 || devices[i].label.indexOf('back') !== -1) {
                            _this.cameraId = devices[i].deviceId;
                            console.log(devices[i]);
                        }
                    }
                    resolve();
                });
            });
        };
        this.photoEventHandler = function (e) {
            var context = _this.canvas.getContext('2d');
            context.drawImage(_this.video, 0, 0, 800, 600);
            var dataURL = _this.canvas.toDataURL();
            var data = { imgBase64: dataURL, task_id: _this.route.snapshot.paramMap.get('taskId') };
            _this.http.post(_globals__WEBPACK_IMPORTED_MODULE_3__["API_URL"] + '/mobile_api/photo', data).subscribe(function (rez) {
                _this.router.navigate(['/task/show/' + _this.route.snapshot.paramMap.get('taskId')]);
                //this.video.srcObject = false;
                //this.stream.stop();
            });
            console.log(_this.innerHeight);
        };
    }
    PhotoComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.innerWidth = window.innerWidth;
        this.innerHeight = window.innerHeight;
        this.video = this.videoElement.nativeElement;
        this.canvas = this.canvas.nativeElement;
        var streamTrack = MediaStreamTrack;
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
        this.browser.mediaDevices.getUserMedia({ audio: false, video: { facingMode: 'environment', width: 800, height: 600 } }).then(function (stream) {
            _this.stream = stream;
            _this.video.srcObject = _this.stream;
        }, function (e) { alert(e); });
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
    };
    tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ViewChild"])('videoElement'),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:type", Object)
    ], PhotoComponent.prototype, "videoElement", void 0);
    tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ViewChild"])('canvas'),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:type", Object)
    ], PhotoComponent.prototype, "canvas", void 0);
    PhotoComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-photo',
            template: __webpack_require__(/*! ./photo.component.html */ "./src/app/photo/photo.component.html"),
            styles: [__webpack_require__(/*! ./photo.component.scss */ "./src/app/photo/photo.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_4__["ActivatedRoute"],
            _http_service__WEBPACK_IMPORTED_MODULE_2__["CommonHttpClient"],
            _angular_router__WEBPACK_IMPORTED_MODULE_4__["Router"]])
    ], PhotoComponent);
    return PhotoComponent;
}());



/***/ }),

/***/ "./src/app/task/form.comment.html":
/*!****************************************!*\
  !*** ./src/app/task/form.comment.html ***!
  \****************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n<form (ngSubmit)=\"commentForm()\" class=\"ion-padding\">\n\n  <ion-row>\n    <ion-col>\n        <ion-button type=\"submit\" color=\"danger\" expand=\"full\">Сохранить</ion-button>    \n    </ion-col>\n    <ion-col>\n      <ion-button [routerLink]=\"['/task/photo/'+taskId]\" color=\"primary\" expand=\"full\">Добавить фото</ion-button>    \n  </ion-col>\n  </ion-row>\n\n  <ion-row>\n    <ion-textarea [(ngModel)]=\"content\" name=\"description\"></ion-textarea>\n  </ion-row>\n\n  \n</form>"

/***/ }),

/***/ "./src/app/task/form.comment.ts":
/*!**************************************!*\
  !*** ./src/app/task/form.comment.ts ***!
  \**************************************/
/*! exports provided: FormCommentComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FormCommentComponent", function() { return FormCommentComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./../http.service */ "./src/app/http.service.ts");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../globals */ "./src/app/globals.ts");




var FormCommentComponent = /** @class */ (function () {
    function FormCommentComponent(http) {
        var _this = this;
        this.http = http;
        this.commentAdded = new _angular_core__WEBPACK_IMPORTED_MODULE_2__["EventEmitter"]();
        this.commentForm = function () {
            var data = {
                task_id: _this.taskId,
                content: _this.content
            };
            _this.http.post(_globals__WEBPACK_IMPORTED_MODULE_3__["API_URL"] + '/mobile_api/save_comment', data).subscribe(function (data) {
                _this.content = '';
                _this.commentAdded.emit(_this.taskId);
            });
        };
    }
    FormCommentComponent.prototype.ngOnInit = function () { };
    tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"])(),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:type", Number)
    ], FormCommentComponent.prototype, "taskId", void 0);
    tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["Output"])(),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:type", Object)
    ], FormCommentComponent.prototype, "commentAdded", void 0);
    FormCommentComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["Component"])({
            selector: 'app-form-comment',
            template: __webpack_require__(/*! ./form.comment.html */ "./src/app/task/form.comment.html"),
            styles: [__webpack_require__(/*! ./task.component.scss */ "./src/app/task/task.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_http_service__WEBPACK_IMPORTED_MODULE_1__["CommonHttpClient"]])
    ], FormCommentComponent);
    return FormCommentComponent;
}());



/***/ }),

/***/ "./src/app/task/task.component.html":
/*!******************************************!*\
  !*** ./src/app/task/task.component.html ***!
  \******************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<ion-content #content>\n \n    <app-show-task></app-show-task>\n\n</ion-content>\n\n"

/***/ }),

/***/ "./src/app/task/task.component.scss":
/*!******************************************!*\
  !*** ./src/app/task/task.component.scss ***!
  \******************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "ion-label {\n  padding-left: 20px;\n  padding-bottom: 10px; }\n\nh2 {\n  padding-left: 40px; }\n\n.img > img {\n  height: 100%;\n  width: 100%;\n  -o-object-fit: cover;\n     object-fit: cover; }\n\nion-text {\n  padding: 10px; }\n\nion-row ion-textarea {\n  border: solid 1px silver;\n  height: 60px;\n  border-radius: 5px;\n  padding-left: 10px; }\n\n.border-bottom {\n  border-bottom: 1px solid silver; }\n\n.line-breaker {\n  white-space: pre-line; }\n\nion-select {\n  border: 1px solid #488aff;\n  border-radius: 5px; }\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3pkaW1vbi9zdG9yYWdlMS93d3cvc3VwcG9ydC9tb2JpbGUvc3JjL2FwcC90YXNrL3Rhc2suY29tcG9uZW50LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFDSSxrQkFBa0I7RUFDbEIsb0JBQW9CLEVBQUE7O0FBR3hCO0VBQ0ksa0JBQWtCLEVBQUE7O0FBR3RCO0VBQ0ksWUFBWTtFQUNaLFdBQVc7RUFDWCxvQkFBaUI7S0FBakIsaUJBQWlCLEVBQUE7O0FBR3JCO0VBQ0ksYUFBYSxFQUFBOztBQUdqQjtFQUVPLHdCQUF3QjtFQUN4QixZQUFZO0VBQ1osa0JBQWtCO0VBQ2xCLGtCQUFrQixFQUFBOztBQUt4QjtFQUNJLCtCQUErQixFQUFBOztBQUduQztFQUNHLHFCQUFxQixFQUFBOztBQUd6QjtFQUVJLHlCQUF5QjtFQUN6QixrQkFBa0IsRUFBQSIsImZpbGUiOiJzcmMvYXBwL3Rhc2svdGFzay5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbImlvbi1sYWJlbCB7XG4gICAgcGFkZGluZy1sZWZ0OiAyMHB4O1xuICAgIHBhZGRpbmctYm90dG9tOiAxMHB4O1xufVxuXG5oMiB7XG4gICAgcGFkZGluZy1sZWZ0OiA0MHB4O1xufVxuXG4uaW1nID4gaW1nIHtcbiAgICBoZWlnaHQ6IDEwMCU7XG4gICAgd2lkdGg6IDEwMCU7XG4gICAgb2JqZWN0LWZpdDogY292ZXI7XG59XG5cbmlvbi10ZXh0IHtcbiAgICBwYWRkaW5nOiAxMHB4O1xufVxuXG5pb24tcm93e1xuICAgIGlvbi10ZXh0YXJlYXtcbiAgICAgICBib3JkZXI6IHNvbGlkIDFweCBzaWx2ZXI7XG4gICAgICAgaGVpZ2h0OiA2MHB4O1xuICAgICAgIGJvcmRlci1yYWRpdXM6IDVweDtcbiAgICAgICBwYWRkaW5nLWxlZnQ6IDEwcHg7XG4gICAgfVxuIH1cblxuXG4gLmJvcmRlci1ib3R0b20ge1xuICAgICBib3JkZXItYm90dG9tOiAxcHggc29saWQgc2lsdmVyO1xuIH1cblxuIC5saW5lLWJyZWFrZXIge1xuICAgIHdoaXRlLXNwYWNlOiBwcmUtbGluZTtcbiAgfVxuXG5pb24tc2VsZWN0IHtcbiAgICBcbiAgICBib3JkZXI6IDFweCBzb2xpZCAjNDg4YWZmO1xuICAgIGJvcmRlci1yYWRpdXM6IDVweDtcbn0iXX0= */"

/***/ }),

/***/ "./src/app/task/task.component.ts":
/*!****************************************!*\
  !*** ./src/app/task/task.component.ts ***!
  \****************************************/
/*! exports provided: TaskComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TaskComponent", function() { return TaskComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var TaskComponent = /** @class */ (function () {
    function TaskComponent() {
        this.task = {};
    }
    TaskComponent.prototype.ngOnInit = function () {
    };
    TaskComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-task',
            template: __webpack_require__(/*! ./task.component.html */ "./src/app/task/task.component.html"),
            styles: [__webpack_require__(/*! ./task.component.scss */ "./src/app/task/task.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], TaskComponent);
    return TaskComponent;
}());



/***/ }),

/***/ "./src/app/task/task.list.component.html":
/*!***********************************************!*\
  !*** ./src/app/task/task.list.component.html ***!
  \***********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<ion-header>\n    <ion-toolbar>\n      <ion-buttons slot=\"start\">\n        <ion-menu-button></ion-menu-button>\n      </ion-buttons>\n      <ion-title>\n        Заявки\n      </ion-title>\n          <ion-select #sel (ionChange)=\"setFilter(sel.value)\" interface=\"popover\" slot=\"end\" [(ngModel)]=\"filter\" okText=\"Сохранить\" cancelText=\"Отменить\">\n            <ion-select-option [value]='\"new\"'>В процессе рассмотрения</ion-select-option>\n            <ion-select-option [value]='\"inprocess\"'>В работе</ion-select-option>\n            <ion-select-option [value]='\"done\"'>Выполнен</ion-select-option>\n            <ion-select-option [value]='\"all\"'>Все заявки</ion-select-option>\n            <ion-select-option [value]='\"deleted\"'>Архив</ion-select-option>\n          </ion-select>\n          <ion-buttons slot=\"start\">\n            <ion-icon name=\"refresh\" slot=\"end\" (click)=\"refresh()\" ></ion-icon>\n          </ion-buttons>\n          <ion-buttons slot=\"end\">\n            \n          </ion-buttons>\n          <ion-title slot=\"end\">\n            <ion-button [routerLink]=\"['/task/new']\" color=\"primary\">\n              <ion-icon name=\"add-circle-outline\"></ion-icon>Новая заявка\n            </ion-button>\n          </ion-title>\n\n\n    </ion-toolbar>\n  </ion-header>\n  \n  <ion-content>\n        <ion-list>\n          <ion-item\n                    [routerLink]=\"['/task','show',item.id]\" \n                    *ngFor=\"let item of items\">\n            <ion-icon slot=\"start\" color=\"medium\" name=\"{{ item.status_icon }}\"></ion-icon>\n            {{ item.title }}   \n            <div class=\"item-note\" slot=\"end\">\n                #{{ item.id }}\n            </div> \n          </ion-item>\n      </ion-list>\n  </ion-content>\n  "

/***/ }),

/***/ "./src/app/task/task.list.component.ts":
/*!*********************************************!*\
  !*** ./src/app/task/task.list.component.ts ***!
  \*********************************************/
/*! exports provided: TaskListComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TaskListComponent", function() { return TaskListComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _task_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./task.service */ "./src/app/task/task.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");




var TaskListComponent = /** @class */ (function () {
    function TaskListComponent(task_service, route, router) {
        var _this = this;
        this.task_service = task_service;
        this.route = route;
        this.router = router;
        this.items = [];
        this.refresh = function () {
            _this.task_service.getTaskList(_this.filter).subscribe(function (data) {
                _this.items = data['tasks'];
                _this.filter = _this.route.snapshot.paramMap.get('filter');
            });
        };
        this.setFilter = function (status) {
            _this.router.navigate(['/task/list/' + status]);
        };
        router.events.subscribe(function (event) {
            if (event instanceof _angular_router__WEBPACK_IMPORTED_MODULE_3__["NavigationEnd"]) {
                _this.ngOnInit();
            }
        });
    }
    TaskListComponent.prototype.ngOnInit = function () {
        this.filter = this.route.snapshot.paramMap.get('filter');
        this.refresh();
        console.log('onInit');
    };
    TaskListComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-task-list',
            template: __webpack_require__(/*! ./task.list.component.html */ "./src/app/task/task.list.component.html"),
            styles: [__webpack_require__(/*! ./task.component.scss */ "./src/app/task/task.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_task_service__WEBPACK_IMPORTED_MODULE_2__["TaskService"],
            _angular_router__WEBPACK_IMPORTED_MODULE_3__["ActivatedRoute"],
            _angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"]])
    ], TaskListComponent);
    return TaskListComponent;
}());



/***/ }),

/***/ "./src/app/task/task.module.ts":
/*!*************************************!*\
  !*** ./src/app/task/task.module.ts ***!
  \*************************************/
/*! exports provided: TaskModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TaskModule", function() { return TaskModule; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _task_new_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./task.new.component */ "./src/app/task/task.new.component.ts");
/* harmony import */ var _photo_photo_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./../photo/photo.component */ "./src/app/photo/photo.component.ts");
/* harmony import */ var _task_list_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./task.list.component */ "./src/app/task/task.list.component.ts");
/* harmony import */ var _task_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./task.component */ "./src/app/task/task.component.ts");
/* harmony import */ var _form_comment__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./form.comment */ "./src/app/task/form.comment.ts");
/* harmony import */ var _task_show_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./task.show.component */ "./src/app/task/task.show.component.ts");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _ionic_angular__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @ionic/angular */ "./node_modules/@ionic/angular/dist/fesm5.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");












var TaskModule = /** @class */ (function () {
    function TaskModule() {
    }
    TaskModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_7__["NgModule"])({
            declarations: [
                _task_component__WEBPACK_IMPORTED_MODULE_4__["TaskComponent"],
                _task_list_component__WEBPACK_IMPORTED_MODULE_3__["TaskListComponent"],
                _form_comment__WEBPACK_IMPORTED_MODULE_5__["FormCommentComponent"],
                _photo_photo_component__WEBPACK_IMPORTED_MODULE_2__["PhotoComponent"],
                _task_new_component__WEBPACK_IMPORTED_MODULE_1__["TaskNewComponent"],
                _task_show_component__WEBPACK_IMPORTED_MODULE_6__["TaskShowComponent"]
            ],
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_8__["CommonModule"],
                _ionic_angular__WEBPACK_IMPORTED_MODULE_10__["IonicModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_11__["FormsModule"],
                _angular_router__WEBPACK_IMPORTED_MODULE_9__["RouterModule"].forChild([
                    {
                        path: 'show/:taskId',
                        component: _task_component__WEBPACK_IMPORTED_MODULE_4__["TaskComponent"]
                    },
                    {
                        path: 'list/:filter',
                        component: _task_list_component__WEBPACK_IMPORTED_MODULE_3__["TaskListComponent"]
                    },
                    {
                        path: 'new',
                        component: _task_new_component__WEBPACK_IMPORTED_MODULE_1__["TaskNewComponent"]
                    },
                    {
                        path: 'photo/:taskId',
                        component: _photo_photo_component__WEBPACK_IMPORTED_MODULE_2__["PhotoComponent"]
                    }
                ])
            ]
        })
    ], TaskModule);
    return TaskModule;
}());



/***/ }),

/***/ "./src/app/task/task.new.component.html":
/*!**********************************************!*\
  !*** ./src/app/task/task.new.component.html ***!
  \**********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<ion-header>\n    <ion-toolbar>\n      <ion-buttons slot=\"start\">\n        <ion-menu-button></ion-menu-button>\n      </ion-buttons>\n      <ion-title>\n        Новая заявка\n      </ion-title>\n    </ion-toolbar>\n</ion-header>\n  \n<ion-content>\n  <form (ngSubmit)=\"submitForm()\">\n    <ion-row>\n      <ion-col>\n        <ion-label>Описание</ion-label>\n        <ion-textarea [(ngModel)]=\"description\" name=\"description\"></ion-textarea>\n      </ion-col>\n    </ion-row>\n    <ion-row>\n      <ion-col>\n        <ion-button type=\"submit\" color=\"primary\" expand=\"full\">Сохранить</ion-button>    \n    </ion-col>\n    </ion-row>\n\n    \n  </form>\n</ion-content>\n  "

/***/ }),

/***/ "./src/app/task/task.new.component.ts":
/*!********************************************!*\
  !*** ./src/app/task/task.new.component.ts ***!
  \********************************************/
/*! exports provided: TaskNewComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TaskNewComponent", function() { return TaskNewComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _task_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./task.service */ "./src/app/task/task.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");




var TaskNewComponent = /** @class */ (function () {
    function TaskNewComponent(task_service, route, router) {
        var _this = this;
        this.task_service = task_service;
        this.route = route;
        this.router = router;
        this.submitForm = function () {
            var data = { 'content': _this.description };
            _this.task_service.saveTask(data).subscribe(function (rez) {
                console.log(rez);
                _this.router.navigate(['/task/show/' + rez['task_id']]);
            });
            _this.description = '';
        };
        router.events.subscribe(function (event) {
            if (event instanceof _angular_router__WEBPACK_IMPORTED_MODULE_3__["NavigationEnd"]) {
                _this.ngOnInit();
            }
        });
    }
    TaskNewComponent.prototype.ngOnInit = function () {
        console.log('onInit new');
    };
    TaskNewComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-task-new',
            template: __webpack_require__(/*! ./task.new.component.html */ "./src/app/task/task.new.component.html"),
            styles: [__webpack_require__(/*! ./task.component.scss */ "./src/app/task/task.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_task_service__WEBPACK_IMPORTED_MODULE_2__["TaskService"],
            _angular_router__WEBPACK_IMPORTED_MODULE_3__["ActivatedRoute"],
            _angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"]])
    ], TaskNewComponent);
    return TaskNewComponent;
}());



/***/ }),

/***/ "./src/app/task/task.show.component.html":
/*!***********************************************!*\
  !*** ./src/app/task/task.show.component.html ***!
  \***********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<ion-header>\n    <ion-toolbar>\n      <ion-buttons slot=\"start\">\n        <ion-menu-button></ion-menu-button>\n      </ion-buttons>\n      <ion-title>Задача #{{ task.id }}</ion-title>\n      <ion-title slot=\"end\">\n          <ion-button [routerLink]=\"['/task/list/all']\" color=\"primary\">Все заявки</ion-button>\n      </ion-title>\n    </ion-toolbar>\n</ion-header>\n\n\n      \n      <ion-card class=\"ion-padding\">\n          <ion-grid>\n            <ion-row>\n              <ion-col size=\"8\"> \n                <ion-text color=\"dark\" [innerHTML]=\"task.content\" ion-padding></ion-text> \n              </ion-col>\n              <ion-col size=\"4\"><ion-label color=\"dark\">\n                Автор: {{ task.author }}</ion-label>\n              </ion-col>\n            </ion-row>\n          </ion-grid>\n          \n      </ion-card>\n\n\n          \n\n\n      \n      <ion-row>\n        \n        <ion-col>\n            <ion-select #sel (ionChange)=\"setStatus(task.id,sel.value)\" value=\"{{ task.status }}\" okText=\"Сохранить\" cancelText=\"Отменить\">\n              <ion-select-option value=\"new\">В процессе рассмотрения</ion-select-option>\n              <ion-select-option value=\"inprocess\">В работе</ion-select-option>\n              <ion-select-option value=\"done\">Выполнен</ion-select-option>\n            </ion-select>\n        \n        </ion-col>\n      </ion-row>\n\n        \n      \n\n\n      <ion-title slot=\"end\">\n        <h4 clas=\"ion-padding\">Коментарии</h4>\n      </ion-title>\n\n      \n          <ion-row *ngFor=\"let item of task.comments\" class=\"ion-padding border-bottom\">\n            <ion-col size=\"9\">\n                <div class=\"item-note line-breaker\"  [innerHTML]=\"item.content\"></div>\n                <div class=\"item-note\"  [innerHTML]=\"item.link\"></div>\n            </ion-col>\n            <ion-col size=\"3\">\n                {{ item.user }}\n            </ion-col>\n\n              \n          </ion-row>\n     \n\n  <app-form-comment  [taskId]=\"task.id\" (commentAdded)=\"commentAddedEmmited($event)\"></app-form-comment>\n"

/***/ }),

/***/ "./src/app/task/task.show.component.ts":
/*!*********************************************!*\
  !*** ./src/app/task/task.show.component.ts ***!
  \*********************************************/
/*! exports provided: TaskShowComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TaskShowComponent", function() { return TaskShowComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _app_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./../app.service */ "./src/app/app.service.ts");




var TaskShowComponent = /** @class */ (function () {
    function TaskShowComponent(route, router, AppConfigService) {
        var _this = this;
        this.route = route;
        this.router = router;
        this.AppConfigService = AppConfigService;
        this.task = {};
        this.setStatus = function (task_id, status) {
            _this.AppConfigService.changeStatus(task_id, status).subscribe(function (rez) {
                console.log(rez);
            });
        };
        router.events.subscribe(function (event) {
            if (event instanceof _angular_router__WEBPACK_IMPORTED_MODULE_2__["NavigationEnd"]) {
                _this.ngOnInit();
            }
        });
    }
    TaskShowComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.AppConfigService.getTaskById(parseInt(this.route.snapshot.paramMap.get('taskId'), 10)).subscribe(function (data) {
            _this.task = data['task'];
        });
    };
    TaskShowComponent.prototype.commentAddedEmmited = function (data) {
        var _this = this;
        this.AppConfigService.getTaskById(parseInt(this.route.snapshot.paramMap.get('taskId'), 10)).subscribe(function (data) {
            _this.task = data['task'];
            //this.content.scrollToBottom(300);
        });
    };
    tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"])(),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:type", Object)
    ], TaskShowComponent.prototype, "task", void 0);
    tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ViewChild"])('content'),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:type", Object)
    ], TaskShowComponent.prototype, "content", void 0);
    TaskShowComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-show-task',
            template: __webpack_require__(/*! ./task.show.component.html */ "./src/app/task/task.show.component.html"),
            styles: [__webpack_require__(/*! ./task.component.scss */ "./src/app/task/task.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_2__["ActivatedRoute"],
            _angular_router__WEBPACK_IMPORTED_MODULE_2__["Router"],
            _app_service__WEBPACK_IMPORTED_MODULE_3__["AppConfigService"]])
    ], TaskShowComponent);
    return TaskShowComponent;
}());



/***/ })

}]);
//# sourceMappingURL=task-task-module.js.map