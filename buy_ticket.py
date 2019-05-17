import requests
from bs4 import BeautifulSoup
import playsound
import time


url = 'https://www.shohoz.com/booking/bus/search/results/0/NzYxNQ=='
cookie = 'gIS_SoyCs-vYtBe8D--5lGE0ZjAzMWVlMWE3MjA5OTcSLv1=1558060279904; FJuWOYPHRbh49l8qXPG6pGY3ZGNjYmU4YWUxNTk1YmESLv1=1558060280467; _ga=GA1.2.345490640.1558030320; _gid=GA1.2.787299828.1558030320; gIS_SoyCs-vYtBe8D--5lGE0ZjAzMWVlMWE3MjA5OTcSLv1=1558030321035; WZRK_G=aa487ef1d2ce434a8be8d72570816933; __tawkuuid=e::shohoz.com::Fl1gmGGstPO6bBbFYZc4ucIKmWxdnhKqTDzubHUZbfvvPRFKNSYr3e4ySDCrEPtg::2; TawkConnectionTime=0; wwwu=eyJpdiI6IkpEeXlvU3I2eGUyY3U1c3lnMVZjU2VQZmdiSWpuTHp3RVRWeVdFaWZNMnM9IiwidmFsdWUiOiJlRVo2U21YVGZIQ0RVN2VwS1ZCN3lVQXVycGhmVm00b1JiYnBWNCtNTVl1VzRhN0ZjNDVOVzRkNmQrVUdTbmU3RlVFb2pcL2licTUxR3dsZ3NwWnNEN2c9PSIsIm1hYyI6ImY2MTc3MTIzMDk5MTI4NGVkMzIzZDkxYmYwN2Y5MTg5OTkyNzg2ODg0NmI2ZDU3MThmMDAzMzU0OTM0MzhhNDcifQ%3D%3D; laravel_session=eyJpdiI6ImVyalZrVFRIN0NtSjBUYUozblBJaEhyY3hFWjAwaUs4WkF2amJRd0xsdzQ9IiwidmFsdWUiOiJpOEI0Q2JUb1UrMElXK3ZpRks2OHFUbmFiT2dCZnVWbkNGTktRNUdvRjIxSXVORHRUNHFkbmk2S2hiQzhsWmdsU2hIZlRhK2ZTZVh2UnRWdDZLK1RUdz09IiwibWFjIjoiNWJhZGJmNDk0NjljZjZmNWU2MGYwMWIwOWQwN2VjNjkyZjNkMTI0NzJkYzU0ZGFmNDY4ZjJiM2VjOWIxMDIxNiJ9; WZRK_S_485-K65-RR5Z=%7B%22p%22%3A4%2C%22s%22%3A1558060227%2C%22t%22%3A1558060280%7D'
const_op_name = ['Nabil', 'S.R', 'Hanif', 'Shyamoli']
const_bus_type = ['Hyundai', 'Scania', 'VOLVO']


def find_ticket():
    try:
        response = requests.get(url, headers={'Cookie': cookie})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            trips = soup.find(id='trips').find('tbody').find_all('tr', {'class': 'trip-row'})
            for trip in trips:
                columns = trip.find_all('td')
                operator_details = columns[0].find('ul').find_all('li')
                op_name = operator_details[0].text.split()
                bus_type = operator_details[1].text.split()
                seats_available = int(columns[3].text)

                if any({*const_op_name} & {*op_name}) and any({*const_bus_type} & {*bus_type}) and seats_available > 0:
                    return True
            return False
        else:
            print('API error occured: {}'.format(response.status_code))
            return False
    except Exception as ex:
        print('Error occured: {}'.format(str(ex)))
        return False


def play_alarm():
    print('Ticket Found!')
    playsound.playsound('./alarm.mp3', True)


if __name__ == "__main__":
    while not find_ticket():
        print('Ticket not found.')
        time.sleep(30)
    
    while True:
        play_alarm()
        time.sleep(5)
