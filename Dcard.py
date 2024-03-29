# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 23:11:03 2019

@author: Relieak
"""

'''
DCARD 熱門前３０文章搜尋
純用 BeautifulSoup 寫法
'''



from bs4 import BeautifulSoup
import requests
import re

url = "https://www.dcard.tw/f/"
html = requests.get(url)
html.encoding = "utf-8"

#print(html.text)

sp = BeautifulSoup(html.text,"html.parser")

#print(sp.prettify())　#排版後更容易分析 

#data = sp.select(".PostEntry_root_V6g0rd")

data = sp.select(".PostList_entry_1rq5Lf")                                       #若要搜尋標簽中的內容 必須先搜尋上一個標籤 否則會找不到 ex : href 先<div 不能先<a
  
  
#print(data[0])

#for link in data[1].find_all("a",{"class" : "PostEntry_root_V6g0rd"}) :                                            
#    
#    #print(link)
#    
#    http = link.get("href")
#    
#    print("https://www.dcard.tw%s" %(http))

while True :
    
    try :
        
        
        number = input("～～～歡迎來到Dcard　前３０熱門文章搜尋～～～\n""\n你想看第幾則文章(離開　請按Enter)>> ")
        
        if number == "" :
            
            break
        
        
        elif 0 < int(number) <= 30 : 
        
            try :
            
                for i in range(int(number)-1,int(number)) :
                    
                   
                    data1 = data[i].find_all("h3",{"class" : "Title__Text-v196i6-0 gmfDU"})
                    
                    data2 = data[i].find_all("div",{"class" : "PostEntry_excerpt_2eHlNn"})
                
                    data3 = data[i].find_all("div",{"class" : "ActionBar__LikeCount-pwz3il-1 cGEHtj"})
                    
                    data4 = data[i].find_all("span",{"class" : "ActionBar__CommentWrapper-pwz3il-5 hkpJwJ"})
                    
                    data5 = data[i].find_all("span",{"class" : "Header__PublishedDateTime-xvcbwe-3 MDszy"})
                    
                                                                               
                    print("")
                    print("第%d則" %(int(number)))
                    print("標題 :",data1[0].text)
                    print("簡介 :",data2[0].text)
                    print("表達心情數　：",data3[0].text)
                    
                    # .strip() 方法用於移除字符串頭尾指定的字符（默認為空格或換行符）或字符序列    -->文字<--
                    print("回應數　：",data4[0].text.strip("回應"))
                    print("發表時間 ：",data5[0].text)
                    
                    # 搜尋標簽中的內容的方法 ＃href 
                    for link in data[i].find_all("a",{"class" : "PostEntry_root_V6g0rd"}) :
                        
                        http = link.get("href")
                        #print(http)
                        
                        #正規表示法
                        A = re.compile("[0-9]+")                                 #表示任意數字串
                        B = re.compile("[A-Za-z0-9\./_]+")                       #表達任意數字，任意英文字母和底線字元的組合，也可寫成 \w
                        
                        # search(string)的用法是傳回第一組符合正規表示法的字串
                        Search1 = A.search(http)
                        Search2 = B.search(http)                                 #去掉網址後面的中文字                               
                        #print(Search1)
                        #print(Search2)
                        
                        print("文章ID :",Search1.group())                        #傳回儲存在match物件中的值 group()
                        
                        print("網頁 ：https://www.dcard.tw%s" %(Search2.group()))                        
                        
                    print("")
                
                            
            except :
                
                """ 若文章簡介開頭是 "前情提要" 會搜尋不到內文 "PostEntry_excerpt_2eHlNn" 產生錯誤 須去搜尋 "PostEntry_reply_1oU-6z" """
                
                data2 = data[i].find_all("div",{"class" : "PostEntry_reply_1oU-6z"})
                
                data3 = data[i].find_all("div",{"class" : "ActionBar__LikeCount-pwz3il-1 cGEHtj"})
                    
                data4 = data[i].find_all("span",{"class" : "ActionBar__CommentWrapper-pwz3il-5 hkpJwJ"})
                
                data5 = data[i].find_all("span",{"class" : "Header__PublishedDateTime-xvcbwe-3 MDszy"})
                    
                print("簡介 :",data2[0].text)
                print("表達心情數　：",data3[0].text)
                print("回應數　：",data4[0].text.strip("回應"))
                print("發表時間 ：",data5[0].text)
                for link in data[i].find_all("a",{"class" : "PostEntry_root_V6g0rd"}) :
                                           
                    http = link.get("href")
                    
                    A = re.compile("[0-9]+")
                    B = re.compile("[A-Za-z0-9\./_]+")                                              
                    Search1 = A.search(http)
                    Search2 = B.search(http)
                    print("文章ID :",Search1.group())                      
                    
                    print("網頁 ：https://www.dcard.tw%s" %(Search2.group()))
                    
                print("")
                                              
        else :
                
            print("")
            print("只能搜尋前３０篇文章喔！！")
    
    except :
        
        print("")
        print("輸入錯誤請重新輸入！！！")
    
 





