(window.webpackJsonp=window.webpackJsonp||[]).push([[17],{ygjv:function(l,n,u){"use strict";u.r(n);var t=u("CcnG"),o=function(){return function(){}}(),e=u("pMnS"),i=["ion-label[_ngcontent-%COMP%]{padding-left:20px;padding-bottom:10px}h2[_ngcontent-%COMP%]{padding-left:40px}.img[_ngcontent-%COMP%] > img[_ngcontent-%COMP%]{height:100%;width:100%;-o-object-fit:cover;object-fit:cover}ion-text[_ngcontent-%COMP%]{padding:10px}ion-row[_ngcontent-%COMP%]   ion-textarea[_ngcontent-%COMP%]{border:1px solid silver;height:60px;border-radius:5px;padding-left:10px}"],b=u("oBZk"),a=u("ZZ/e"),r=u("ZYCi"),c=u("Ip0R"),s=u("gIcY"),p=u("F11b"),d=u("xa+l"),g=function(){function l(l){var n=this;this.http=l,this.commentAdded=new t.m,this.commentForm=function(){n.http.post(d.a+"/mobile_api/save_comment",{task_id:n.taskId,content:n.content}).subscribe(function(l){n.content="",n.commentAdded.emit(n.taskId)})}}return l.prototype.ngOnInit=function(){},l}(),h=t.nb({encapsulation:0,styles:[i],data:{}});function k(l){return t.Fb(0,[(l()(),t.pb(0,0,null,null,1,"h2",[],null,null,null,null,null)),(l()(),t.Eb(-1,null,["\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439"])),(l()(),t.pb(2,0,null,null,18,"form",[["class","ion-padding"],["novalidate",""]],[[2,"ng-untouched",null],[2,"ng-touched",null],[2,"ng-pristine",null],[2,"ng-dirty",null],[2,"ng-valid",null],[2,"ng-invalid",null],[2,"ng-pending",null]],[[null,"ngSubmit"],[null,"submit"],[null,"reset"]],function(l,n,u){var o=!0,e=l.component;return"submit"===n&&(o=!1!==t.zb(l,4).onSubmit(u)&&o),"reset"===n&&(o=!1!==t.zb(l,4).onReset()&&o),"ngSubmit"===n&&(o=!1!==e.commentForm()&&o),o},null,null)),t.ob(3,16384,null,0,s.j,[],null,null),t.ob(4,4210688,null,0,s.g,[[8,null],[8,null]],null,{ngSubmit:"ngSubmit"}),t.Bb(2048,null,s.a,null,[s.g]),t.ob(6,16384,null,0,s.f,[[4,s.a]],null,null),(l()(),t.pb(7,0,null,null,4,"ion-row",[],null,null,null,b.G,b.m)),t.ob(8,49152,null,0,a.fb,[t.h,t.k],null,null),(l()(),t.pb(9,0,null,0,2,"ion-button",[["color","danger"],["type","submit"]],null,null,null,b.v,b.b)),t.ob(10,49152,null,0,a.h,[t.h,t.k],{color:[0,"color"],type:[1,"type"]},null),(l()(),t.Eb(-1,0,["\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"])),(l()(),t.pb(12,0,null,null,8,"ion-row",[],null,null,null,b.G,b.m)),t.ob(13,49152,null,0,a.fb,[t.h,t.k],null,null),(l()(),t.pb(14,0,null,0,6,"ion-textarea",[["name","description"]],[[2,"ng-untouched",null],[2,"ng-touched",null],[2,"ng-pristine",null],[2,"ng-dirty",null],[2,"ng-valid",null],[2,"ng-invalid",null],[2,"ng-pending",null]],[[null,"ngModelChange"],[null,"ionBlur"],[null,"ionChange"]],function(l,n,u){var o=!0,e=l.component;return"ionBlur"===n&&(o=!1!==t.zb(l,16)._handleBlurEvent()&&o),"ionChange"===n&&(o=!1!==t.zb(l,16)._handleInputEvent(u.target.value)&&o),"ngModelChange"===n&&(o=!1!==(e.content=u)&&o),o},b.L,b.r)),t.ob(15,49152,null,0,a.ub,[t.h,t.k],{name:[0,"name"]},null),t.ob(16,16384,null,0,a.Ib,[t.k],null,null),t.Bb(1024,null,s.c,function(l){return[l]},[a.Ib]),t.ob(18,671744,null,0,s.h,[[2,s.a],[8,null],[8,null],[6,s.c]],{name:[0,"name"],model:[1,"model"]},{update:"ngModelChange"}),t.Bb(2048,null,s.d,null,[s.h]),t.ob(20,16384,null,0,s.e,[[4,s.d]],null,null)],function(l,n){var u=n.component;l(n,10,0,"danger","submit"),l(n,15,0,"description"),l(n,18,0,"description",u.content)},function(l,n){l(n,2,0,t.zb(n,6).ngClassUntouched,t.zb(n,6).ngClassTouched,t.zb(n,6).ngClassPristine,t.zb(n,6).ngClassDirty,t.zb(n,6).ngClassValid,t.zb(n,6).ngClassInvalid,t.zb(n,6).ngClassPending),l(n,14,0,t.zb(n,20).ngClassUntouched,t.zb(n,20).ngClassTouched,t.zb(n,20).ngClassPristine,t.zb(n,20).ngClassDirty,t.zb(n,20).ngClassValid,t.zb(n,20).ngClassInvalid,t.zb(n,20).ngClassPending)})}var m=u("F5nt"),f=function(){function l(l,n){var u=this;this.route=l,this.AppConfigService=n,this.task={},this.setStatus=function(l,n){u.AppConfigService.changeStatus(l,n).subscribe(function(l){console.log(l)})}}return l.prototype.ngOnInit=function(){var l=this;this.AppConfigService.getTaskById(parseInt(this.route.snapshot.paramMap.get("taskId"),10)).subscribe(function(n){l.task=n.task})},l.prototype.commentAddedEmmited=function(l){var n=this;this.AppConfigService.getTaskById(parseInt(this.route.snapshot.paramMap.get("taskId"),10)).subscribe(function(l){n.task=l.task,n.content.scrollToBottom(300)})},l}(),v=t.nb({encapsulation:0,styles:[i],data:{}});function C(l){return t.Fb(0,[(l()(),t.pb(0,0,null,null,6,"ion-item",[],null,null,null,b.A,b.g)),t.ob(1,49152,null,0,a.E,[t.h,t.k],null,null),(l()(),t.pb(2,0,null,0,1,"ion-text",[["color","dark"]],[[8,"innerHTML",1]],null,null,b.K,b.q)),t.ob(3,49152,null,0,a.tb,[t.h,t.k],{color:[0,"color"]},null),(l()(),t.pb(4,0,null,0,2,"div",[["class","img"]],null,null,null,null,null)),(l()(),t.pb(5,0,null,null,1,"ion-text",[["color","dark"]],[[8,"innerHTML",1]],null,null,b.K,b.q)),t.ob(6,49152,null,0,a.tb,[t.h,t.k],{color:[0,"color"]},null)],function(l,n){l(n,3,0,"dark"),l(n,6,0,"dark")},function(l,n){l(n,2,0,n.context.$implicit.content),l(n,5,0,n.context.$implicit.link)})}function x(l){return t.Fb(0,[t.Cb(402653184,1,{content:0}),(l()(),t.pb(1,0,null,null,18,"ion-header",[],null,null,null,b.y,b.e)),t.ob(2,49152,null,0,a.y,[t.h,t.k],null,null),(l()(),t.pb(3,0,null,0,16,"ion-toolbar",[],null,null,null,b.N,b.t)),t.ob(4,49152,null,0,a.yb,[t.h,t.k],null,null),(l()(),t.pb(5,0,null,0,3,"ion-buttons",[["slot","start"]],null,null,null,b.w,b.c)),t.ob(6,49152,null,0,a.i,[t.h,t.k],null,null),(l()(),t.pb(7,0,null,0,1,"ion-menu-button",[],null,null,null,b.D,b.k)),t.ob(8,49152,null,0,a.O,[t.h,t.k],null,null),(l()(),t.pb(9,0,null,0,2,"ion-title",[],null,null,null,b.M,b.s)),t.ob(10,49152,null,0,a.wb,[t.h,t.k],null,null),(l()(),t.Eb(11,0,["\u0417\u0430\u0434\u0430\u0447\u0430 #",""])),(l()(),t.pb(12,0,null,0,7,"ion-title",[["slot","end"]],null,null,null,b.M,b.s)),t.ob(13,49152,null,0,a.wb,[t.h,t.k],null,null),(l()(),t.pb(14,0,null,0,5,"ion-button",[["color","primary"]],null,[[null,"click"]],function(l,n,u){var o=!0;return"click"===n&&(o=!1!==t.zb(l,16).onClick()&&o),"click"===n&&(o=!1!==t.zb(l,18).onClick(u)&&o),o},b.v,b.b)),t.ob(15,49152,null,0,a.h,[t.h,t.k],{color:[0,"color"]},null),t.ob(16,16384,null,0,r.n,[r.m,r.a,[8,null],t.D,t.k],{routerLink:[0,"routerLink"]},null),t.Ab(17,1),t.ob(18,737280,null,0,a.Gb,[c.g,a.Db,t.k,r.m,[2,r.n]],null,null),(l()(),t.Eb(-1,0,["\u0412\u0441\u0435 \u0437\u0430\u044f\u0432\u043a\u0438"])),(l()(),t.pb(20,0,null,null,3,"ion-row",[],null,null,null,b.G,b.m)),t.ob(21,49152,null,0,a.fb,[t.h,t.k],null,null),(l()(),t.pb(22,0,null,0,1,"ion-text",[["color","dark"]],[[8,"innerHTML",1]],null,null,b.K,b.q)),t.ob(23,49152,null,0,a.tb,[t.h,t.k],{color:[0,"color"]},null),(l()(),t.pb(24,0,null,null,4,"ion-row",[],null,null,null,b.G,b.m)),t.ob(25,49152,null,0,a.fb,[t.h,t.k],null,null),(l()(),t.pb(26,0,null,0,2,"ion-label",[["color","dark"]],null,null,null,b.B,b.h)),t.ob(27,49152,null,0,a.K,[t.h,t.k],{color:[0,"color"]},null),(l()(),t.Eb(28,0,["\u0410\u0432\u0442\u043e\u0440: ",""])),(l()(),t.pb(29,0,null,null,16,"ion-item",[],null,null,null,b.A,b.g)),t.ob(30,49152,null,0,a.E,[t.h,t.k],null,null),(l()(),t.pb(31,0,null,0,1,"div",[["slot","start"]],null,null,null,null,null)),(l()(),t.Eb(-1,null,["\u0421\u0442\u0430\u0442\u0443\u0441:"])),(l()(),t.pb(33,0,null,0,12,"ion-select",[["cancelText","\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c"],["okText","\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"],["slot","start"]],null,[[null,"ionChange"],[null,"ionBlur"]],function(l,n,u){var o=!0,e=l.component;return"ionBlur"===n&&(o=!1!==t.zb(l,36)._handleBlurEvent()&&o),"ionChange"===n&&(o=!1!==t.zb(l,36)._handleChangeEvent(u.target.value)&&o),"ionChange"===n&&(o=!1!==e.setStatus(e.task.id,t.zb(l,35).value)&&o),o},b.I,b.n)),t.Bb(5120,null,s.c,function(l){return[l]},[a.Hb]),t.ob(35,49152,[["sel",4]],0,a.jb,[t.h,t.k],{cancelText:[0,"cancelText"],okText:[1,"okText"],value:[2,"value"]},null),t.ob(36,16384,null,0,a.Hb,[t.k],null,null),(l()(),t.pb(37,0,null,0,2,"ion-select-option",[["value","paper-plane"]],null,null,null,b.H,b.o)),t.ob(38,49152,null,0,a.kb,[t.h,t.k],{value:[0,"value"]},null),(l()(),t.Eb(-1,0,["\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435 \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u0438\u044f"])),(l()(),t.pb(40,0,null,0,2,"ion-select-option",[["value","build"]],null,null,null,b.H,b.o)),t.ob(41,49152,null,0,a.kb,[t.h,t.k],{value:[0,"value"]},null),(l()(),t.Eb(-1,0,["\u0412 \u0440\u0430\u0431\u043e\u0442\u0435"])),(l()(),t.pb(43,0,null,0,2,"ion-select-option",[["value","boat"]],null,null,null,b.H,b.o)),t.ob(44,49152,null,0,a.kb,[t.h,t.k],{value:[0,"value"]},null),(l()(),t.Eb(-1,0,["\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d"])),(l()(),t.pb(46,0,null,null,3,"ion-row",[],null,null,null,b.G,b.m)),t.ob(47,49152,null,0,a.fb,[t.h,t.k],null,null),(l()(),t.pb(48,0,null,0,1,"h2",[["clas","ion-padding"]],null,null,null,null,null)),(l()(),t.Eb(-1,null,["\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438"])),(l()(),t.pb(50,0,null,null,3,"ion-list",[],null,null,null,b.C,b.i)),t.ob(51,49152,null,0,a.L,[t.h,t.k],null,null),(l()(),t.gb(16777216,null,0,1,null,C)),t.ob(53,278528,null,0,c.h,[t.O,t.L,t.s],{ngForOf:[0,"ngForOf"]},null),(l()(),t.pb(54,0,null,null,1,"app-form-comment",[],null,[[null,"commentAdded"]],function(l,n,u){var t=!0;return"commentAdded"===n&&(t=!1!==l.component.commentAddedEmmited(u)&&t),t},k,h)),t.ob(55,114688,null,0,g,[p.a],{taskId:[0,"taskId"]},{commentAdded:"commentAdded"})],function(l,n){var u=n.component;l(n,15,0,"primary");var o=l(n,17,0,"/home");l(n,16,0,o),l(n,18,0),l(n,23,0,"dark"),l(n,27,0,"dark"),l(n,35,0,"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c","\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c",t.rb(1,"",u.task.status_icon,"")),l(n,38,0,"paper-plane"),l(n,41,0,"build"),l(n,44,0,"boat"),l(n,53,0,u.task.comments),l(n,55,0,u.task.id)},function(l,n){var u=n.component;l(n,11,0,u.task.id),l(n,22,0,u.task.content),l(n,28,0,u.task.author)})}var z=function(){function l(){this.task={}}return l.prototype.ngOnInit=function(){},l}(),y=t.nb({encapsulation:0,styles:[i],data:{}});function I(l){return t.Fb(0,[(l()(),t.pb(0,0,null,null,3,"ion-content",[],null,null,null,b.x,b.d)),t.ob(1,49152,[["content",4]],0,a.r,[t.h,t.k],null,null),(l()(),t.pb(2,0,null,0,1,"app-show-task",[],null,null,null,x,v)),t.ob(3,114688,null,0,f,[r.a,m.a],null,null)],function(l,n){l(n,3,0)},null)}function w(l){return t.Fb(0,[(l()(),t.pb(0,0,null,null,1,"app-task",[],null,null,null,I,y)),t.ob(1,114688,null,0,z,[],null,null)],function(l,n){l(n,1,0)},null)}var M=t.lb("app-task",z,w,{},{},[]);u.d(n,"TaskModuleNgFactory",function(){return E});var E=t.mb(o,[],function(l){return t.wb([t.xb(512,t.j,t.bb,[[8,[e.a,M]],[3,t.j],t.x]),t.xb(4608,c.j,c.i,[t.u,[2,c.p]]),t.xb(4608,a.a,a.a,[t.z,t.g]),t.xb(4608,a.Cb,a.Cb,[a.a,t.j,t.q,c.c]),t.xb(4608,a.Fb,a.Fb,[a.a,t.j,t.q,c.c]),t.xb(4608,s.k,s.k,[]),t.xb(1073742336,c.b,c.b,[]),t.xb(1073742336,a.Ab,a.Ab,[]),t.xb(1073742336,s.i,s.i,[]),t.xb(1073742336,s.b,s.b,[]),t.xb(1073742336,r.o,r.o,[[2,r.u],[2,r.m]]),t.xb(1073742336,o,o,[]),t.xb(1024,r.k,function(){return[[{path:"show/:taskId",component:z}]]},[])])})}}]);