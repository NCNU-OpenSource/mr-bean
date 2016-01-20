# Mr.bean

104-1 LSA 期末報告 第一組-  李安正 <101213002>  謝孟剛 <101213027>  吳庭賢 <101213029>


## 題目發想緣起
- 做出趣味性的產品
- 玩家都可以依照喜好，自由改裝
- 兒時對於世X帝國二中攻城兵器的嚮往
- 構想圖

![p1](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/001.png)

[![參考影片](https://img.youtube.com/vi/CgNlPOMOps0/0.jpg)](https://www.youtube.com/watch?v=CgNlPOMOps0)




## 實作所需材料
 電子材料 | 取得來源 | 價格
------------ | ------------- | -------------
Raspberry Pi|			BlueT|			$－－
Logitech Webcam C170|		yahoo拍賣|			$549
銅線|			草屯電子材料行|			$10
杜邦線(公公)|			草屯電子材料行|			$70
10條杜邦線(公母)|			ICshop|			$35
日製12V減速馬達|			露天|			$200
電池盒(8顆一組)|			草屯電子材料行|			$20
83x55mm 麵包板|			ICshop|			$65
L293D控制晶片|			ICshop|			$95
電池8顆|			草屯電子材料行|			$80

材料 | 取得來源 | 價格
------------ | ------------- | -------------
髮夾|		書局|			$10
髮圈|	書局|			$10
木夾|		書局|			$20
吸管|			自備|			$－－
木板|			自備|		$－－
紙盒|			自備|			$－－
厚紙板|			自備|			$－－
竹筷|			自備|			$－－
棉線|			書局|			$30
背包扣環|			書局|			$15
寶特瓶|			自備|			$－－
皮帶|			自備|			$－－
AB膠|			五金行|			$140
強力膠|			自備|			$－－
雙面膠|			自備|			$－－
膠帶|			自備|			$－－
老虎鉗|			自備|			$－－
剪刀|			自備|			$－－
美工刀|			自備|			$－－





## 運用與課程內容中相關的技巧
- SSH連線

- raspberry pi的設定

## 使用的現有軟體與來源

1.Python

2.Webcam
- software: MJPG-streamer

3.motor
- software: RPi.GPIO


## 實作過程 - GPIO 配置
1.ULN2003 Driver Board (Stepper motor)
- pin 2,6,11,12,13,15
![step](https://github.com/NCNU-OpenSource/PlayMeow/raw/master/img/1032%20Practical%20Linux%20System%20Administration.png)

2.直流馬達
- pin 4,7,20
![servo](https://github.com/NCNU-OpenSource/PlayMeow/raw/master/img/1032%20Practical%20Linux%20System%20Administration%20(1).png)

## 實作過程 - webcam
![p6](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/006.jpg)

## 實作過程 - MJPG-streamer
1.Builds MJPG-streamer
```
sudo apt-get install subversion
svn co https://svn.code.sf.net/p/mjpg-streamer/code/ mjpg-streamer
sudo apt-get install libjpeg8-dev
sudo apt-get install imagemagick
sudo make
sudo ./mjpg_streamer -i "./input_uvc.so -y -r 640x480" -o "./output_http.so -w ./www"
```

## 實作過程 － Coding (servo90.php & servo90.py)

## 實際產出 - 外觀
![p2](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/002.png)
![p4](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/004.jpg)

## 參考資料
1.網頁：
- https://github.com/NCNU-OpenSource/BT-7
- https://github.com/NCNU-OpenSource/PlayMeow
- https://www.raspberrypi.com.tw/4944/raspberry-pi-2-and-rpi-gpio/
- https://books.google.com.tw/books?id=n4XSCQAAQBAJ&pg=SA19-PA22&lpg=SA19-PA22&dq=raspberry+pi+gpio+%E8%AA%BF%E6%95%B4%E9%A6%AC%E9%81%94%E8%BD%89%E9%80%9F&source=bl&ots=I3OkQemmaR&sig=5E6Eu-SJka-G1EKytGap-6SDCq4&hl=zh-TW&sa=X&ved=0ahUKEwiNlI_U56bKAhWKmJQKHTIXAksQ6AEIITAB#v=onepage&q=raspberry%20pi%20gpio%20%E8%AA%BF%E6%95%B4%E9%A6%AC%E9%81%94%E8%BD%89%E9%80%9F&f=false


2.書籍：
- Raspberry Pi超炫專案與完全實戰 ， 柯博文 ， 碁峰 ，2014-09-26

## END
THANK YOU !
