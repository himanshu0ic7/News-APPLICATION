import requests
from tkinter import *
from urllib.request import urlopen
from PIL import Image,ImageTk
import io
import webbrowser
class NewsAPP:
    def __init__(self):
        self.data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=e08778747f0a44c89da569d1c81bd7e0").json()
        #Loading Initial GUI
        self.load_gui()
        self.load_news_item(0)
    def load_gui(self):
        self.root=Tk()
        self.root.geometry('350x650')
        self.root.title("News App")
        self.root.label=Label(self.root,text="News App",font=("Arial",20,"bold"))
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_item(self,index):
        self.clear() #Clearing the screen for this news item
        #Loading image
        try:
            img_url=self.data['articles'][index]['urlToImage']
            rawdata=urlopen(img_url).read()
            img=Image.open(io.BytesIO(rawdata)).resize((350,250))
            photo=ImageTk.PhotoImage(img)
            label=Label(self.root,image=photo)
            label.pack()
        except:
            img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd8LWlb8l34MXvr3BonwEYsd11lw1QKQVEiQ&s"
            rawdata=urlopen(img_url).read()
            img=Image.open(io.BytesIO(rawdata)).resize((350,250))
            photo=ImageTk.PhotoImage(img)
            label=Label(self.root,image=photo)
            label.pack()

        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',
                      wraplength=350,justify='center')
        heading.pack(pady=10)
        heading.config(font=('verdana',15))

        description=Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',
                      wraplength=350,justify='center')
        description.pack(pady=10)
        description.config(font=('verdana',15))

        frame=Frame(self.root,bg='black')
        frame.pack(pady=10,expand=True,fill=BOTH)

        if index!=0:
            prev_button=Button(frame,text="Previous",command=lambda:self.load_news_item(index-1),width=16,height=3)
            prev_button.pack(side='left')

        read_button=Button(frame,text="Read More",command=lambda:self.open_link(self.data['articles'][index]['url']),width=16,height=3)
        read_button.pack(side='left')

        if index!=len(self.data['articles'])-1:
            for_button=Button(frame,text="Forward",command=lambda:self.load_news_item(index+1),width=16,height=3)
            for_button.pack(side='left')

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)



obj=NewsAPP()
