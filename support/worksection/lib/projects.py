import requests
url = 'https://wezom.worksection.com/project/166584/new/'
data = {
"return_to" : 1,
"single": 1,
"id_comment_copy": '',
"name": 'From script',
"important": 1,
"id_user_to": 360829,
"tags": 149135,
"datelen2": 1,
"datelen": 1,
"datelen_we": 1,
"relate_id": 0,
"id_project": 166584,
"is_term": 0,
"datestart": "25.02.2019",
"datestart_def": "25.02.2019",
"dateend": "25.02.2019",
"timeend": '',
"is_repeat": 0,
"rep_type":  0,
"rep_num": 1,
"rep_numrepeat": 1,
"rep_wday": 1,
"rep_day": 0,
"is_nocopy": 0,
"is_subtask": 0,
"rep_name": 0,
"sv_relate": 0,
"sn_relate": 0,
"max_time": 0,
"descr": 'test from script',
"ufile[]": 0,
"presave": 0,
"is_file_edit": 0,
"limit": '1487936443|0|0|1|1|0',
"is_hidden": 0,
"save_invite": 0,
"save_user[]": [360829,101419],
"action": 'save',
"mda": '2e423e0d3a5ff120de413d3c10cfcf33'
}

txt = requests.post(url,data=data)

print(txt.text)








