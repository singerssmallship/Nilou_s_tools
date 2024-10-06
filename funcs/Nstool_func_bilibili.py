import tkinter as tk
import os
from PIL import Image, ImageTk
import requests
import re
import json


class ClassFunc:

    def replace_special_chars(self,s):
        '''
        :param s: 传入一个字符串，函数将里面的一些怪怪的字符 转化为下划线
        :return:
        '''
        special_chars = '『』/\\|?:;“'
        for char in special_chars:
            s = s.replace(char, '_')
        return s


    def function_reptile_bilibili_audio(self,url, path, headers):
        # url是bilibili视频的url地址，path是下载完音频保存的地址，headers是headers
        #path最后要带\
        # 开始拿到了源代码保存为response
        response = requests.get(url, headers=headers)
        response = response.text
        #print(response)
        # 开始拿到标题
        title_0 = re.findall('<h1 data-title="(.*?)" title=".*?" class="video-title', response)[0]
        # 开始拿到音频所在字典
        audio_info_2 = re.findall('<script>window.__playinfo__=(.*?)</script>', response)[0]
        # 开始处理完成音频字典
        audio_info_1 = json.loads(audio_info_2)
        # 开始拿到音频地址
        audio_address_0 = audio_info_1['data']['dash']['audio'][0]['baseUrl']
        # 开始将返回数据保存进变量
        response_audio = requests.get(audio_address_0, headers=headers).content
        # 将变量里的二进制文件保存在path里
        title_0 = self.replace_special_chars(title_0)
        with open(path + title_0 + '.mp3', mode='wb') as audio:
            audio.write(response_audio)
        return title_0

    def __init__(self,x_=None,y_=None):
        root = tk.Tk()
        # ---------------------------------------------------窗口位置,默认居中
        if x_ is None and y_ is None:
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width - 360) // 2
            y = (screen_height - 360) // 2
            root.geometry('360x360+%d+%d' % (x, y))
        else:
            root.geometry('360x360+%d+%d' % (x_, y_))
        # ---------------------------------------------------窗口颜色
        root['background'] = "#cc9966"
        # ---------------------------------------------------限制窗口被调整大小
        root.resizable(False, False)

        # ---------------------------------------------------输入框
        entry1 = tk.Entry(root,fg='blue',bd=3,relief='flat',width=10,font=('Arial', 20))
        entry1.place(x=180, y=100)
        # ---------------------------------------------------按钮2开始
        def fuc_but_1():
            url = entry1.get()
            with open('..\\necessary\\settings.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()[0][9::].replace('\n', '') + 'bilibili\\原音频\\'
            # 接收url
            path = lines
            headers = {
                'Cookie': 'buvid3=ED712BF7-25E7-22A9-C75F-837A3F1FE5B674658infoc; b_nut=1705717574; i-wanna-go-back=-1; b_ut=7; b_lsid=C14968E3_18D24B0AAB6; bsource=search_baidu; _uuid=D2FFDD104-A115-869C-C49A-F9E105FA7B107D74331infoc; buvid4=2D9B4FC6-E127-EDA9-259F-A43A140583B275021-024012002-99qpwlwnMRioweU8cPePFULdCQpjAwnFdv0T2p3ShTSkyPYj2%2Fk0dByUUYLAA09R; enable_web_push=DISABLE; home_feed_column=5; browser_resolution=1872-966; header_theme_version=CLOSE; CURRENT_FNVAL=4048; SESSDATA=ff4c9cea%2C1721269662%2Cdad8c%2A11CjDuhqBmjZ7A2sTZPuJbN30NXOIybGl5CVLCGhDKoqDGVntrD4tMHU6b7T3Qncm-vEgSVnJJdXNzcXQ0NXR0bjJKS09OQXliNGZVMFhqUXJkVEtIZFNRaVRKM2NoTVhzNUZfeHVMX2F2UDNJc2h6T3hsVy1XQ053WUJlUDQxU2lETDdfQ294eHRRIIEC; bili_jct=fbdff1488baca8bbd553433aa08266f1; DedeUserID=1467171633; DedeUserID__ckMd5=4d0cdac928d6212a; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDU5NzY4ODAsImlhdCI6MTcwNTcxNzYyMCwicGx0IjotMX0.3oT6Ax0J456-bxNNUkAxpbz6su20H6hUE0cXJFkQyeY; bili_ticket_expires=1705976820; rpdid=0zbfVGePi8|150HtIpsC|3A|3w1Rr15J; sid=5kj3946u; PVID=2; fingerprint=efbb9697164dc970eee8716176509eec; buvid_fp_plain=undefined; bp_video_offset_1467171633=888548044031655942; buvid_fp=efbb9697164dc970eee8716176509eec',
                'Referer': 'https://www.bilibili.com/video/BV1z341187Y9/?spm_id_from=333.999.0.0&vd_source=71d8f7bd66f8fe36f6cf995f2d91425c',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

            self.function_reptile_bilibili_audio(url, path, headers)
            entry1.delete(0, tk.END)
        button1 = tk.Button(root,
                            text=" 开始 ",
                            command=fuc_but_1,
                            bg="#cc9966",
                            font=("Microsoft YaHei",20),
                            height=1,
                            width=8)
        button1.place(x=180, y=170)
        # ---------------------------------------------------右下角勾选框
        def check():
            if var.get() == 1:
                print("勾选框被选中")
            else:
                print("勾选框未被选中")


        var = tk.IntVar()
        checkbutton = tk.Checkbutton(root, text="选择", variable=var, onvalue=1, offvalue=0, command=check,)
        checkbutton.place(x=180, y=250)

        # ---------------------------------------------------左上角返回按钮

        # ---------------------------------------------------
        root.mainloop()





a = ClassFunc()