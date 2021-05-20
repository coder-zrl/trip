import requests

def get_weather(place):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+place
    res = requests.get(url).json()
    return res



if __name__ == '__main__':
    print(get_weather('武汉'))