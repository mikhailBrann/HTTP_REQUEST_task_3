import requests,time
from datetime import timedelta, datetime

def get_stack_questions():
    upload_url = 'https://api.stackexchange.com/2.3/questions'
    responce_result = False
    # получаем текущую дату и двухдневную
    now = datetime.now()
    two_days = timedelta(2)
    two_days_ago = now - two_days
    
    # переводим полученые даты в unix формат для запроса
    now_unixtime = time.mktime(now.timetuple())
    two_days_ago_unixtime = time.mktime(two_days_ago.timetuple())
    
    params = {'order': 'desc', 'fromdate': int(two_days_ago_unixtime), 'todate': int(now_unixtime),'tagged': 'python', 'sort': 'month', 'site': 'stackoverflow'}
    response = requests.get(url=upload_url, params=params)
   
    if response.status_code == 200:
        responce_result = response.json()
        
    return responce_result    


if __name__ == '__main__':
    quest_response = get_stack_questions()
    
    if quest_response:
        for question in quest_response['items']:
            result = 'Вопрос: {0}\nСсылка на вопрос: {1}\nТеги: {2}\n'.format(question["title"], question["link"], ', '.join(question["tags"]))
            print(result)
    else:
        print('error')





