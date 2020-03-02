$( document ).ready(function() {
    l = function(msg){
        console.log(msg);
    }

    if(document.domain.indexOf('local') != -1){
        var api_url = 'http://support.org';
        //var api_url = 'https://support.webmonstr.com'
    } else {
        var api_url = 'https://support.wezom.agency'
    }

    /*
    $.ajaxSetup({
        headers: {
            'Access-Control-Allow-Origin': 'http://locotrade.localyy'
        }
    });
    */

    support_app = {
        'document': $('body'),
        'location': window.location.href,
        'api_url': api_url,
        'mobile_url': "{{ mobile_url }}",
        'client_sign': "{{ client_sign }}" ,
        'site_name': "{{ site }}",
        'language': '{{ lang }}',
        'content_block': $('.content-wrapper').find('.content'),
        'start_loading': function(){
            $('#sup_spinner').modal('show');
        },
        'stop_loading': function(){
            $('#sup_spinner').modal('hide');
        },
        'hide_table': function(){
            $('#sup_task_table').hide();
        },
        'show_table': function(){
            $('#sup_task_table').show();
        },
        'add_marker': function(){
            $('#support_link').append('<div id="sup_cnt_marker" class="treeview-menu__label">1</div>');
        },
        'remove_marker': function(){
            $('#sup_cnt_marker').remove();
        },
        'check_routing': function(){
            //console.log(window.location.href);
            if(window.location.href.indexOf("#Support") > -1) {
                return true;
            } else {
                return false;
            }
        },
        'ws_connect': function(){
            self = this;
            var ws_server = api_url.replace('http://','').replace('https://','');
            var ws = new WebSocket("ws://"+ws_server+":8888/socket");

            ws.onopen = function() {
                //ws.send("Hello, world");
            };

            ws.onmessage = function (evt) {
                var data = JSON.parse(evt.data);
                console.log(data);
                if (data.action == 'update_task'){
                    if(self.check_routing())
                    {
                       self.show_task(data.message, function(){
                           self.popup_message('Был добавлен комментарий.');
                       });
                    }
                    self.add_marker();
                }

                if (data.action == 'update_list'){
                    if(self.check_routing())
                    {
                        self.get_task_list('all', function(){
                            self.popup_message('Была добавлена новая задача.');
                        });
                    }
                    self.add_marker();
                }
               
            };
        },
        'init': function(){
            /// add link to the end of panel
            var self = this;
            //l(self);
            var menu = $('.sidebar-menu');
            //l(menu);
            self.ws_connect();
            menu.append('<li class="treeview"><a id="support_link" href="http://locotrade.local/admin/catalog/features"><i class="fa fa-life-ring"></i><span>Служба поддержки</span></a></li>');
            menu.append('<li class="treeview"><a id="digest_link" href="http://locotrade.local/admin/catalog/features"><i class="fa fa-bullhorn"></i><span>Дайджест новостей</span><div class="treeview-menu__label">1</div></a></li>');
            // spinner
            self.document.append('<div id="sup_spinner" class="modal fade"><div class="sup_loader"></div></div>');

            // bind the funk
            $('#support_link').on('click',function(){self.start()});
            $('#digest_link').on('click',function(){self.digest()});

            $(document).on('click', '.show_task_link', function(e){
                var id = $(this).attr("data-id");
                self.hide_table();
                self.show_task(id);
            })


            $(document).on('click', '.del_task_link', function(e){
                e.preventDefault();
                $('#btn-close-task').attr('data-id',$(e.target).attr('data-id'));

            })


            $(document).on('click', '.direct-chat-text img', function(){
                $(this).toggleClass('full-show');
            })

            // routing
            self.routing();

            // window.onpopstate = function(){
            //     self.routing();
            // }

        },

        'popup_message': function(msg){
            self = this;
            $('#sup_popup_message').show();
            $('#sup_popup_message_content').html(msg);
            setTimeout(function(){
                $('#sup_popup_message').hide();
            },10000);
        },

        'digest': function(){
            let self = this;
            self.clear_content();
            self.set_url_location('SupportDigest');
            var h = self.document.find('h1');
            h.html('Дайджест новостей');
            $.get( api_url+"/task/getDigest/locotrade/ru", function(data){
                self.content_block.html(data);
            });
        },
        'start': function(clb){
            let self = this;
            self.remove_marker();
            self.start_loading();
            self.clear_content();
            self.set_url_location('SupportList');
            self.get_task_list('all');
            if(clb!==undefined){
                clb();
            }
            self.stop_loading();
        },

        'set_url_location': function(prefix){
            window.location.hash = prefix;
        },

        'routing': function(){
            let self = this;
            var url = window.location.href;
            if(window.location.href.indexOf("#SupportList") > -1) {
               self.start();
            }
            if(window.location.href.indexOf("#SupportShow") > -1) {
                var sub = url.substring(url.indexOf('#SupportShow-')+13,url.length);
                self.clear_content();
                self.get_task_list('all',function(){self.show_task(sub)});
                //setTimeout(self.show_task(sub),5000);
            }
            //console.log(window.location.search(''));
        },

        'get_task_list': function(status='all',clb){
            let self = this;
            let url = self.api_url+'/task/getTaskList/'+self.site_name+'/'+self.language+'/'+status;
            $.get( url, function( data ) {
                self.content_block.html(data);
                if(clb!==undefined){
                    self.get_task_form(clb);
                } else {
                    self.get_task_form();
                }
              });
        },

        'get_task_form': function(clb){
            let self = this;
            let url = self.api_url+'/task/getTaskForm/'+self.site_name+'/'+self.language;
            $.get( url, function( data ) {
                self.content_block.prepend($(data));
                if(clb!==undefined){
                    clb();
                }
            });
        },

        'save_task': function(){
            let self = this;
        },


        'clear_content': function(){
            let self = this;
            var content = $('.box-body');
            var top_menu = $('.content-header').find('div');
            self.content_block.empty();
            top_menu.empty();
            var h = self.document.find('h1');
            h.html('Служба поддержки <a target=_blank href="'+self.mobile_url+'/settings/login/'+self.client_sign+'/client">Мобильная версия</a>');
            var crum = $('.breadcrumb');
            crum.find('.active').html('Служба поддержки');
            self.document.find('.breacrumb').find('.active').html('Служба поддержки');
            self.document.find('.box-info').empty();

        },

        'remove_form': function(){
            $('#sup_form').remove();
        },

        'show_task': function(id,clb){
            let self = this;
            let url = self.api_url+'/task/getTask/'+self.site_name+'/'+self.language+'/'+id;
            $.get( url, function( data ) {
                //l($(data));
                //self.remove_form()
                $('#sup_task_show').remove();
                $('#sup_form').hide();
                $('#sup_task_table').hide();
                $('#sup_header').prepend(data);
                self.set_url_location('#SupportShow-'+id);
                    if(clb!==undefined){
                        clb();
                    }
              });

        },

        'bind_actions': function(){
            let self = this;

        }

    }

    support_app.init();


});


