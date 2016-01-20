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
- software: [MJPG-streamer](http://www.ntex.tw/wordpress/545.html)

3.motor
- software: RPi.GPIO


## 實作過程 - GPIO 配置
1.ULN2003 Driver Board (Stepper motor)
- pin 2,6,11,12,13,15
![step1](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/pipin.png)
![step2](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/pysan.JPG)

2.L293D晶片
- pin 4,7,20

![L293D](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/l293d.jpg)
- 接腳說明

接腳 | 用途 | 說明
------------ | ------------- | -------------
1| Enable 1,2|			作為左半邊IC控制用。此Pin為高電壓時，左半邊IC可作用，反之，低電壓時，左半邊IC無作用。
2| INPUT 1|			此Pin為高電壓時，電流會流出至Output 1。
3| OUTPUT 1|			此Pin要接到終端馬達的一個接腳。
4,5| GND|			接地。
6| OUTPUT 2|			此Pin要接到終端馬達的一個接腳。
7| INPUT 2|			此Pin為高電壓時，電流會流出至Output 2。
8| VC|			供給給馬達使用的電壓，如果要驅動的馬達是12V，那就要供給這個Pin 12V直流電。
9| Enable 3,4|			作為右半邊IC控制用。此Pin為高電壓時，右半邊IC可作用，反之，低電壓時，右半邊IC無作用。
10| INPUT 3|			此Pin為高電壓時，電流會流出至Output 3。
11| OUTPUT 3|			此Pin要接到終端馬達的一個接腳。
12,13| GND|			接地。
14| OUTPUT 4|			此Pin要接到終端馬達的一個接腳。
15| INPUT 4|			此Pin為高電壓時，電流會流出至Output 4。
16| Vcc|			提供給IC的電源，這個Pin要供給5V電壓。

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

## 實作過程 － Coding
```
import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 11
Motor1B = 12
Motor1E = 13
GPIO.setup(Motor1A,GPIO.OUT)

GPIO.setup(Motor1B,GPIO.OUT)

GPIO.setup(Motor1E,GPIO.OUT)
def clockwise():
    print "Turning motor on Clockwise."
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)

def counterclockwise():
    print "Turning motor on Counterclockwise."
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

def stopmotor():
    print "Stopping motor"
    GPIO.output(Motor1E,GPIO.LOW)

while True:
    cmd = raw_input("Command, q/s/w/e ")
    direction = cmd[0]
    if direction == "q":
        clockwise()
    elif direction == "s":
        stopmotor()
    elif direction == "w":
        counterclockwise()
    elif direction == "e":
        GPIO.cleanup()
        break

```

## 實際產出 - 外觀

![p2](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/002.png)

![p4](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/004.jpg)

## demo
- [豆豆先生 video](https://youtu.be/Bdxe6ts-_pI)

## 參考資料
1.網頁：
- https://github.com/NCNU-OpenSource/BT-7
- https://github.com/NCNU-OpenSource/PlayMeow
- https://www.raspberrypi.com.tw/4944/raspberry-pi-2-and-rpi-gpio/
- http://atceiling.blogspot.tw/2014/02/raspberry-pi-l293d.html#.Vp-ggvl97IU
- https://books.google.com.tw/books?id=n4XSCQAAQBAJ&pg=SA19-PA22&lpg=SA19-PA22&dq=raspberry+pi+gpio+%E8%AA%BF%E6%95%B4%E9%A6%AC%E9%81%94%E8%BD%89%E9%80%9F&source=bl&ots=I3OkQemmaR&sig=5E6Eu-SJka-G1EKytGap-6SDCq4&hl=zh-TW&sa=X&ved=0ahUKEwiNlI_U56bKAhWKmJQKHTIXAksQ6AEIITAB#v=onepage&q=raspberry%20pi%20gpio%20%E8%AA%BF%E6%95%B4%E9%A6%AC%E9%81%94%E8%BD%89%E9%80%9F&f=false


2.書籍：
- Raspberry Pi超炫專案與完全實戰 ， 柯博文 ， 碁峰 ，2014-09-26
![p7](https://raw.githubusercontent.com/NCNU-OpenSource/mr-bean/master/img/007.jpg)

## END
THANK YOU !
