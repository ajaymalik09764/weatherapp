import requests
import json
import time
class base1():
    def __init__(self):
        self.__apikey="YOUR API KEY"
        self.baseurl="http://api.openweathermap.org/data/2.5/weather?"+"appid="+self.__apikey
    def cityname(self,city):   #get data with cityname--
        self.cityname1=city
        self.__complate_url=self.baseurl+"&q="+self.cityname1+"&units=metric"
        self.response=requests.get(self.__complate_url)
        self.x=self.response.json()
        if self.response!='[404]':
            self.ax="Current Time:"+'\t'+str(time.strftime("%I:%M:%S  %p"))
            self.bx="Date:"+'\t'+str(time.strftime("%x"))
            self.cx="Name:"+'\t'+str(self.x['name'])
            self.dx="Temp:"+'\t'+str(self.x['main']['temp'])+' C'
            self.ex="Humidity:"+'\t'+str(self.x['main']['humidity'])+' %'
            self.fx="Visibility:"+'\t'+str(self.x['visibility'])
            self.gx="Weather:"+'\t'+str(self.x['weather'][0]['main'])
            self.hx="Wind:"+'\t'+str(self.x['wind']['speed'])+" m\s"
    def get_laco(self): #get lat and loc with the help of ipinfo api
        self.req=requests.get("https://ipinfo.io/")
        self.loc=self.req.json()
        if self.req.ok:
            self.city=self.loc['city']
            self.region=self.loc['region']
            self.lat_lon=self.loc['loc'].split(',')
    def lat_lon_f(self): #get data with lat and loc from openweather api
        self.get_laco()
        self.complateurl=self.baseurl+'&'+'lat='+self.lat_lon[0]+'&'+'lon='+self.lat_lon[1]+"&units=metric"
        self.response1=requests.get(self.complateurl)
        self.y=self.response1.json()
        if self.response1!='[404]':
            self.ay="Current Time"+'\t'+str(time.strftime("%I:%M:%S  %p"))
            self.by='Date'+'\t'+str(time.strftime("%x"))
            self.cy='Name'+'\t'+str(self.y['name'])
            self.dy='Temp'+'\t'+str(self.y['main']['temp'])+' C'
            self.ey='Humidity'+'\t'+str(self.y['main']['humidity'])+' %'
            self.fy='Visibility'+'\t'+str(self.y['visibility'])
            self.gy='Weather:'+'\t'+str(self.y['weather'][0]['main'])
            self.hy='Wind:'+'\t'+str(self.y['wind']['speed'])+' m\s'
