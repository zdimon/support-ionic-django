Getting a list of users: get_users
    {

        "status": "ok",
        "data": [
            {
                "id": "USER_ID",
                "email": "USER_EMAIL",
                "first_name": "USER_FIRST_NAME",
                "last_name": "USER_LAST_NAME",
                "name": "USER_NAME",
                "title": "USER_POSITION",
                "avatar": "URL",
                "company": "USER_COMPANY",
                "department": "USER_DEPARTMENT"
             }
        ]
    }


Getting the list of all account tasks: get_all_tasks

"status": "ok",
    "data": [
    {
            "name": "TITLE",
            "page": "/project/PROJECT_ID/TASK_ID/",
            "status": "done",
            "priority": "0..10",
            "user_from": {
                "email": "USER_EMAIL",
                "name": "USER_NAME"
            },
            "user_to": {
                "email": "USER_EMAIL",
                "name": "USER_NAME"
            },
            "date_added": "YYYY-MM-DD HH:II",
            "date_start": "YYYY-MM-DD",
            "date_end": "YYYY-MM-DD",
            "date_closed": "YYYY-MM-DD HH:II",
            "max_time": "50"
            "max_money": "100"
            "tags": "complete"
            "child": [
                {
                    "name": "SUBTASK_NAME",
                    "page": "/project/PROJECT_ID/TASK_ID/SUBTASK_ID/",
                    "status": "done",
                    "priority": "0..10",
                    "user_from": {
                        "email": "USER_EMAIL",
                        "name": "USER_NAME"
                    },
                    "user_to": {
                        "email": "USER_EMAIL",
                        "name": "USER_NAME"
                    },
                    "date_added": "YYYY-MM-DD HH:II",
                    "date_start": "YYYY-MM-DD",
                    "date_end": "YYYY-MM-DD",
                    "date_closed": "YYYY-MM-DD HH:II"
"max_time": "25"
			"max_money": "50"
			"tags": "complete"
                }
            ]
       }
Getting a list of time and costs : get_timemoney

            "time": "1:30",
            "money": "20.50",
            "date": " YYYY-MM-DD",
            "is_timer": false,
            
            
Вопросы.

Несколько пользователей в задаче как рулить?





            
