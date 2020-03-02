from task.models import *
from main.models import *

cats = {
    '1': 'Технические вопросы',
    '2': 'Доработки функционала',
    '3': 'Заказать услугу',
    '4': 'Locotrade',
    '5': 'Общие вопросы'
}

cats2 = {
    '1': 'Технические проблемы',
    '2': 'Предложение к улучшению',
    '3': 'Заказать услугу',
    '4': 'Прочие вопросы'
}



subcats = {
    '1': {
        '1': 'Домен',
        '2': 'Хостинг',
        '3': 'Почта',
        '4': 'Модули и сайты',
        '5': 'Антивирусная защита',
        '6': 'Резервные копии',
        '7': 'Заказать пакет ТП',
        '8': 'Заказать мониторинг сайта',
    },
    '2': {
        '9': 'Заказать доработку сайта',
        '10': 'Заказать оптимизацию',
        '11': 'Заказать просчет доработок',
    }
}



def load_cat2():
    print ('Loading categories...')
    cnt = Category.objects.all().delete()
    for k,v in cats2.items():
        c = Category()
        c.title = cats2[k]
        c.id = int(k)
        c.save()
        print(cats2[k])


def load_cat():
    print ('Loading categories...')
    cnt = Category.objects.all().count()
    if cnt==0:
        for k,v in cats.items():
            c = Category()
            c.title = cats[k]
            c.id = int(k)
            c.save()
            print(cats[k])

def load_subcat():
    print ('Loading SUBcategories...')
    cnt = SubCategory.objects.all().count()
    if cnt==0:
        for k,v in subcats.items():
            for kk, vv in subcats[k].items():
                c = SubCategory()
                c.title = subcats[k][kk]
                c.category_id = int(k)
                c.id = int(kk)
                c.save()
                print(cats[k])

def load_test_task():
    print('Load test task')
    cnt = Task.objects.all().count()
    if cnt==0:

        t = Task()
        t.category_id = 1
        t.subcategory_id = 1
        t.title = 'Test task title 1.'
        t.content = 'Test task content.'
        t.save()

        t = Task()
        t.category_id = 2
        t.subcategory_id = 9
        t.title = 'Test task title 2.'
        t.content = 'Test task content.'
        t.status = 'в работе'
        t.save()

        t = Task()
        t.category_id = 2
        t.subcategory_id = 10
        t.title = 'Test task title 3.'
        t.content = 'Test task content.'
        t.status = 'выполнен'
        t.save()



def load_setting():
    print('Load setting')
    try:
        s = Setting.objects.get(alias='worksection_key')
    except:
        s = Setting()
        s.alias = 'worksection_key'
        s.value = '882b65ad36d2260a1bc94a6be912dc21'
        s.save()
        print('Load setting worksection_key')

    try:
        s = Setting.objects.get(alias='telegramm_bot_key')
    except:
        s = Setting()
        s.alias = 'telegramm_bot_key'
        s.value = '613923056:AAFSLF0otI2ZXQ2nRIYXVdPk_Es40jdlnr0'
        s.save()
        print('Load setting worksection_key')        




