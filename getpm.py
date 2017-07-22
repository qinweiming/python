import  urllib.request
import  threading
from time import ctime
from  bs4  import BeautifulSoup
def getPM25(cityname):
    site="http://www.pm25.com/"+cityname+".html"
    html=urllib.request.urlopen(site)
    soup=BeautifulSoup(html)
    city=soup.find(class_="bi_loaction_city")
    aqi=soup.find("a",{"class","bi_aqiarea_num"})
    quality=soup.select(".bi_aqiarea_right span")
    result=soup.find("div",class_='bi_aqiarea_bottom')
    print(city.text+"aqizhihsu"+aqi.text+"zhiliang"+quality[0].text+result.text)
    print("*"*20+ctime()+"*"*20)
def  one_thread():
    print("one threaf start"+ctime()+"\n")
    getPM25("hefei")
    getPM25("shanghai")
def  two_thread():
    print("two"+ctime()+"\n")
    threads=[]
    t1=threading.Thread(target=getPM25,args="hefei")
    threads.append(t1)
    t2=threading.Thread(target=getPM25,args="shanghai")
    threads.append(t2)
    for  t in threads:
        t.start()
if __name__=="__main__":
    one_thread()
    print("----------------")
    two_thread()
