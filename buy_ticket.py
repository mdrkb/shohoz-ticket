import requests
from bs4 import BeautifulSoup
import playsound
import time


url = 'https://www.shohoz.com/booking/bus/search/results/0/NzYxNQ=='
cookie = 'gIS_SoyCs-vYtBe8D--5lGE0ZjAzMWVlMWE3MjA5OTcSLv1=1558034986778; FJuWOYPHRbh49l8qXPG6pGY3ZGNjYmU4YWUxNTk1YmESLv1=1558038094329; _ga=GA1.2.345490640.1558030320; _gid=GA1.2.787299828.1558030320; gIS_SoyCs-vYtBe8D--5lGE0ZjAzMWVlMWE3MjA5OTcSLv1=1558030321035; WZRK_G=aa487ef1d2ce434a8be8d72570816933; __tawkuuid=e::shohoz.com::Fl1gmGGstPO6bBbFYZc4ucIKmWxdnhKqTDzubHUZbfvvPRFKNSYr3e4ySDCrEPtg::2; _gat=1; TawkConnectionTime=0; wwwu=eyJpdiI6IlRvTm5HcHpEWEp3T1graCtZV2wyU0xjZnBqY3RTRTU1eXZiVnhRWjRneFE9IiwidmFsdWUiOiIzYitGUmVnVDJZTmlTMEVnbG5tNFdmZjFha3hjK015d0J5MWRiU3o3dk5ua1BjZXRlMEpwejVMRnhZK0thNm9GeEJ0cm1jenJ5SVZvZXFlYzhGSWJaUT09IiwibWFjIjoiMGNjNDQ4NWVkMWJlYjM2ZjZiYWMxMjU4YjUxNmNlNjgxYzI3NmIwMDAxMzY2ODc2MTU0MjcwNGY1N2YyNTliOSJ9; laravel_session=eyJpdiI6IjFqeHJ5RlwveTMwMWlrc1RFMVg4bVB6dHdRa2FKN0dDTXJ0MFpGbWdcLzJKQT0iLCJ2YWx1ZSI6IlJ4YkJ6d0NPMTlYUENzclBIMmhpZ3BcL3FMd0pKbzY0Q0Y3NHRYdWsrSmJEd3BZNW5EajhGK2NBTDRxb0c3bE9jMU41T3E4RlJxNGJJdHNWMHlQWDFSZz09IiwibWFjIjoiYTkyYWFkYjc5NTNkMDRjYmQwZDFmOGExMmZhNTgxMWJlNjdlMTUwODNkZWZkMjM2YzUyMzdiMDQ1ZWNhYTcyMyJ9; WZRK_S_485-K65-RR5Z=%7B%22p%22%3A2%2C%22s%22%3A1558038089%2C%22t%22%3A1558038094%7D'
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

                if any({*const_op_name} & {*op_name}) and any({*const_bus_type} & {*bus_type}):
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
