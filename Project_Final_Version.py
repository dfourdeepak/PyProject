
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import random
import tkinter.messagebox as tmsg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
df=pd.read_csv('Top 100 most Streamed - Sheet1.csv')


# year vs Popular songs
def yearwisesongs():
    root=Tk()
    f=plt.Figure(figsize=(7,6),dpi=100)
    a=f.add_subplot(111)
    
    g=df.groupby('year').size()
    g.plot(kind='bar',ax=a)
    a.set_ylabel('Number of Popular Songs')
    a.set_xlabel('Year')
    a.set_title('Yearwise Songs')
    
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=TOP,fill=BOTH)
    root.title('Top Streamed Songs By Year')
    #root.geometry('800x500')
    root.mainloop()

clean_df=df[df['year']>2010]
g=clean_df.groupby('top genre').size()
sorted_g=g[g.values>1]
sorted_g=sorted_g.rename({'canadian contemporary r&b':0,'canadian hip hop':1,'canadian pop':2,'dance pop':3,'dfw rap':4,'electropop':5,'emo rap':6,'folk-pop':7,'latin':8,'melodic rap':9,'modern rock':10,'pop':11,'rap':12})

# year vs Genre
def topgenre():
    root=Tk()
    f=plt.Figure(figsize=(8,5),dpi=100)
    a=f.add_subplot(111)
    
    sorted_g.plot(kind='bar',ax=a,color=['red','orange','blue','green','purple','gray','black','cyan','pink','magenta',"#f8f",'#75e1eb','#3786be'])
    a.set_xlabel('--Genres--')
    a.set_ylabel('--Number of Songs--')
    a.set_title('Top Genre from Popular Songs')
    
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=TOP,fill=BOTH)
    
    Label(root,text="0 - Canadian Contemporary r&b",fg='red',bg='white',font=('Calibri 12 bold')).place(x=480,y=65)
    Label(root,text="1 - Canadian Hip Hop",fg='orange',bg='white',font=('Calibri 12 bold')).place(x=480,y=85)
    Label(root,text="2 - Canadian Pop",fg='blue',bg='white',font=('Calibri 12 bold')).place(x=480,y=105)
    Label(root,text="3 - Dance Pop",fg='green',bg='white',font=('Calibri 12 bold')).place(x=480,y=125)
    Label(root,text="4 - DFW Rap",fg='purple',bg='white',font=('Calibri 12 bold')).place(x=480,y=145)
    Label(root,text="5 - ElectroPOP",fg='gray',bg='white',font=('Calibri 12 bold')).place(x=480,y=165)
    Label(root,text="6 - EMO Rap",fg='black',bg='white',font=('Calibri 12 bold')).place(x=480,y=185)
    Label(root,text="7 - Folk Pop",fg='cyan',bg='white',font=('Calibri 12 bold')).place(x=480,y=205)
    Label(root,text="8 - Latin",fg='pink',bg='white',font=('Calibri 12 bold')).place(x=480,y=225)
    Label(root,text="9 - Melodic Rap",fg='magenta',bg='white',font=('Calibri 12 bold')).place(x=480,y=245)
    Label(root,text="10 - Modern Rock",fg='#f8f',bg='white',font=('Calibri 12 bold')).place(x=480,y=265)
    Label(root,text="11 - Pop",fg='#75e1eb',bg='white',font=('Calibri 12 bold')).place(x=480,y=285)
    Label(root,text="12 - Rap",fg='#3786be',bg='white',font=('Calibri 12 bold')).place(x=480,y=305)
    root.title('Genrewise Analysis')
    root.geometry('800x500')
    root.mainloop()

artist=df.groupby('artist').size()
t=artist[artist.values>2].rename({})
t=t.rename({'Billie Eilish':0,'Ed Sheeran':1,'Imagine Dragons':2,'Justin Bieber':3,'Maroon 5':4,'Post Malone':5,'Shawn Mendes':6,'The Chainsmokers':7,'The Weeknd':8})

def songbyartist():
    root=Tk()
    f=plt.Figure(figsize=(8,5),dpi=100)
    a=f.add_subplot(111)
    
    artist=df.groupby('artist').size()
    
    t.plot(kind='bar',ax=a,color=['red','orange','blue','green','purple','gray','black','cyan','pink'])

    a.set_xlabel('Artists')
    
    a.set_ylabel('Number of Popular Songs')
    a.set_title('Pupular Songs vs Artists')
    
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=TOP,fill=BOTH)
    
    Label(root,text="0-Billie Eilish",fg='red',bg='white',font=('Calibri 12 bold')).place(x=560,y=65)
    Label(root,text="1-Ed Sheeran",fg='orange',bg='white',font=('Calibri 12 bold')).place(x=560,y=85)
    Label(root,text="2-Imagine Dragons",fg='blue',bg='white',font=('Calibri 12 bold')).place(x=560,y=105)
    Label(root,text="3-Justin Bieber",fg='green',bg='white',font=('Calibri 12 bold')).place(x=560,y=125)
    Label(root,text="4-Maroon 5",fg='purple',bg='white',font=('Calibri 12 bold')).place(x=560,y=145)
    Label(root,text="5-Post Malone",fg='gray',bg='white',font=('Calibri 12 bold')).place(x=560,y=165)
    Label(root,text="6-Shawn Mendes",fg='black',bg='white',font=('Calibri 12 bold')).place(x=560,y=185)
    Label(root,text="7-The Chainsmokers",fg='cyan',bg='white',font=('Calibri 12 bold')).place(x=560,y=205)
    Label(root,text="8-The Weeknd",fg='pink',bg='white',font=('Calibri 12 bold')).place(x=560,y=225)
    root.title('Top Artists')
    root.geometry('800x500')
    root.mainloop()


artist=df.copy()
selected_ar=artist.artist.to_list()
artist1=artist.drop(['valance','liveness','length','acousticness','speechiness'],axis=1)
artist1.set_index('artist',inplace=True)

postmalone=[el for el in selected_ar if el!='Post Malone']
edsheeran=[el for el in selected_ar if el!='Ed Sheeran']


def EDSHEERAN():
    root=Tk()
    f=plt.Figure(figsize=(6,6),dpi=100)
    a=f.add_subplot(111)
    
    sortlisted=artist1.drop(edsheeran)
    years=sortlisted.year
    sortlisted1=sortlisted.drop(['year','loudness.dB'],axis=1)
    sortlisted1['artists']=sortlisted1.index

    lst=[x for x in range(0,5)]
    sortlisted1['indexes']=lst

    sortlisted1.set_index('indexes',inplace=True)

    final=sortlisted1.drop(['top genre','title','artists'],axis=1)
    final1=final.rename(columns={'beats.per.minute':'BPM','energy':'Energy','danceability':'Danceability','popularity':'Popularity'})
    final1['titles']=[0,1,2,3,4]
    final1.set_index('titles', inplace=True)

    final1.plot(kind='bar',grid=True,title='Ed Sheeran',legend=True,ax=a)
    a.set_xlabel('Songs')
    a.set_ylabel('Attributes')

    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().place(x=200,y=0)
    
    Label(root,text='0-Perfect',font=('calibri 12 bold')).place(x=2,y=160)
    Label(root,text='1-Shape of Your',font=('calibri 12 bold')).place(x=2,y=190)
    Label(root,text='2-Photograph',font=('calibri 12 bold')).place(x=2,y=220)
    Label(root,text='3-Thinking out Loud',font=('calibri 12 bold')).place(x=2,y=250)
    Label(root,text="4-I Don't Care(ft. Justin Bieber)",font=('calibri 12 bold')).place(x=2,y=280)
    root.title('Ed Sheeran')
    root.geometry('800x600')
    root.mainloop()


# Post Malone
def POSTMALONE():
    root=Tk()
    f=plt.Figure(figsize=(6,6),dpi=100)
    a=f.add_subplot(111)
    
    sortlisted=artist1.drop(postmalone)
    sortlisted1=sortlisted.drop(['year','loudness.dB'],axis=1)
    sortlisted1['artists']=sortlisted1.index
    lst=[x for x in range(0,7)]
    sortlisted1['indexes']=lst
    sortlisted1.set_index('indexes',inplace=True)
    final=sortlisted1.drop(['top genre','title','artists'],axis=1)
    final1=final.rename(columns={'beats.per.minute':'BPM','energy':'Energy','danceability':'Danceability','popularity':'Popularity'})
    final1['titles']=[0,1,2,3,4,5,6]
    final1.set_index('titles', inplace=True)

    final1.plot(kind='bar',grid=True,title='Post Malone',ax=a)
    a.set_xlabel('Songs')
    a.set_ylabel('Attributes')
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().place(x=200,y=0)
    
    Label(root,text='0-Circles',font=('calibri 12 bold')).place(x=2,y=160)
    Label(root,text='1-Rockstar(feat. 21 Savage)',font=('calibri 12 bold')).place(x=2,y=190)
    Label(root,text='2-Sunflower-Spider-Man',font=('calibri 12 bold')).place(x=2,y=220)
    Label(root,text='3-Congratulations',font=('calibri 12 bold')).place(x=2,y=250)
    Label(root,text='4-Better Now',font=('calibri 12 bold')).place(x=2,y=280)
    Label(root,text='5-I Fall Apart',font=('calibri 12 bold')).place(x=2,y=310)
    root.title('Post Malone')
    root.geometry('800x600')
    root.mainloop()


# Top 5 pie of Popularity
def topPopular():
    root=Tk()
    f=plt.Figure(figsize=(7,5),dpi=100)
    a=f.add_subplot(111)
    
    
    popularity=df.loc[:,['year','popularity']]
    popularityv1=popularity.head()
    popularityv1
    songs='Blinding Lights','Watermelon Sugar',"Mood (feat. iann dior)",'Someone You Loved','Perfect'
    a.pie(popularityv1.popularity.to_list(),labels=songs,shadow=True,explode = (0.2,0.05,0.06,0.02,0.1),autopct='%.3f%%')
    a.set_title('Popularity Check')
#     a.set_axis('equal')
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH)
    root.title('Popularity of Top 5 Songs')
    root.geometry('800x500')
    root.mainloop()


# BPM vs Year
def BPMvsYEAR():
    root=Tk()
    f=plt.Figure(figsize=(10,5),dpi=100)
    a=f.add_subplot(111)
    
    df_selected=df[df['year']>2010]
    df_selectedv1=df_selected.loc[:,['year','beats.per.minute']]
    df_selectedv1
    a.bar(df_selectedv1.year,df_selectedv1['beats.per.minute'])
    a.set_xticks([2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])
    a.set_title('BPM vs Year')
    a.set_xlabel('Years')
    a.set_ylabel('BPM')
    
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=True)
    root.title('BPM during Years')
    root.mainloop()


def lenVSyear():
    root=Tk()
    f=plt.Figure(figsize=(10,5),dpi=100)
    a=f.add_subplot(111)
    
    df_selected=df[df['year']>2010]
    df_selectedv1=df_selected.loc[:,['year','length']]
    df_selectedv1
    a.bar(df_selectedv1.year,df_selectedv1['length']/60,color='#002D62')
    a.set_xticks([2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])
    a.set_title('Duration vs Year')
    a.set_xlabel('Years')
    a.set_ylabel('Duration in Minutes')
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=True)
    root.geometry('700x500')
    root.title('Length vs Year')
    root.mainloop()


# ED and PM vs Energy
def sheeranvsmalone():
    root=Tk()
    f=plt.Figure(figsize=(5,4),dpi=100)
    
    dfv1=df.copy()
    dfv1.set_index('artist',inplace=True)
    dfv2=dfv1.drop(edsheeran)
    es=dfv2.energy.to_list()
    es.sort()

    dfv3=dfv1.drop(postmalone)
    pm=dfv3.energy.to_list()
    pm.sort()
    a=f.add_subplot(1,2,1)
    a.plot([x for x in range(len(pm))],pm,'o-')
    a.set_title('Post Malone')
    
    
    a1=f.add_subplot(1,2,2)
    a1.plot([x for x in range(len(es))],es,'o-',color='r')
    a1.set_title('Ed Sheeran')

    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH)
    Label(root,text='Energy Level in Top 2 Artists Songs',font=('Calibri 12 bold'),bg='white').place(x=130,y=5)
    
    root.title('Energy in Top 2 Artists Songs')
    root.geometry('500x410')
    root.mainloop()
    

# Loudness Level

def loudness():
    root=Tk()
    
    f=plt.Figure(figsize=(5,5),dpi=100)
    a=f.add_subplot(111)
    dffnl=df[df.year>2010]
    a.bar(dffnl.year,dffnl['loudness.dB'])
    a.set_ylabel('Loudness in dB')
    a.set_xlabel('Years')
    a.set_title('Loudness with the Years')
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH)
    
    root.title('Loudness Level During Years')
    root.geometry('500x410')
    root.mainloop()
    

topsngs=df.head()
topsngs


#  top 5 most streamed songs in the world

def topsongs():
    root=Tk()
    
    f=plt.Figure(figsize=(5,4),dpi=100)
    
    a=f.add_subplot(111)
    topsngs.loc[:,['title','danceability']]
    a.bar([1,2,3,4,5],topsngs.popularity,width=0.5,color=['r','orange','b','g','y'],edgecolor='black')
    a.set_xlabel('Songs')
    a.set_ylabel('Danceability')
    a.set_title('Danceability lavel of Top 5 Songs')
    
    
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack(side=TOP,fill=BOTH)
    Label(root,text='1 - Blinding Lights',fg='red',bg='white',font=('calibri 12 bold')).place(x=15,y=420,width=160)
    Label(root,text='2 - Watermelon Sugar',fg='orange',bg='white',font=('calibri 12 bold')).place(x=15,y=460,width=160)
    Label(root,text='3 - Mood (feat. iann dior)',fg='blue',bg='white',font=('calibri 12 bold')).place(x=195,y=420,width=180)
    Label(root,text='4 - Someone You Loved',fg='green',bg='white',font=('calibri 12 bold')).place(x=195,y=460,width=180)
    Label(root,text='5 - Perfect',fg='#979946',bg='white',font=('calibri 12 bold')).place(x=400,y=420,width=180)
    Label(root,text='',fg='green',bg='white',font=('calibri 12 bold')).place(x=400,y=460,width=180)
    root.title('Most Streamed Songs')
    root.geometry('600x500')
    root.mainloop()
#     plt.legend(True)



df.head()



df.describe()



df.dtypes



def others():
    root=Tk()
    
    topframe=Frame(root,borderwidth=2,relief='ridge',bg='#fff')
    Button(topframe,bg='#1ed760',fg='#191414',command=lenVSyear,borderwidth=0,text='Tap here to view Duration of songs vary from year to year                         ',font=('Calibri 11 italic')).place(x=10,y=10,width=440,height=40)
    Button(topframe,bg='#1ed760',fg='#191414',command=sheeranvsmalone,borderwidth=0,text='Tap here to view energy level in Ed Sheeran and Post Malone Hit songs',font=('Calibri 11 italic')).place(x=10,y=55,width=440,height=40)
    Button(topframe,bg='#1ed760',fg='#191414',command=loudness,borderwidth=0,text='Tap here to view Loudness level of songs                                                              ',font=('Calibri 11 italic')).place(x=10,y=100,width=440,height=40)
    Button(topframe,bg='#1ed760',fg='#191414',command=topsongs,borderwidth=0,text='Tap here to view Top 5 most Streamed songs in the world                           ',font=('Calibri 11 italic')).place(x=10,y=145,width=440,height=40)
    topframe.place(x=5,y=5,width=460,height='200')

    root.title("Top Streamed Songs")
    root.geometry('470x210')
#     root.configure(bg='#1db954')
    mainloop()




def mpopular():
    root=Tk()
    
    f=Frame(root,borderwidth=2,relief='ridge',bg='#fff')
    popular=df.loc[0,:]
    Label(f,text='Song Name: '+popular.title,bg='#fff',font=("cambria 12 bold")).place(x=10,y=10)
    Label(f,text='Artist: '+popular.artist,bg='#fff',font=("cambria 12 bold")).place(x=10,y=30)
    Label(f,text='Genre: '+popular['top genre'],bg='#fff',font=("cambria 12 bold")).place(x=10,y=50)
    Label(f,text='Release Year: '+str(popular.year),bg='#fff',font=("cambria 12 bold")).place(x=10,y=70)
    Label(f,text='BPM Level: '+str(popular['beats.per.minute']),bg='#fff',font=("cambria 12 bold")).place(x=10,y=90)
    Label(f,text='Energy Level: '+str(popular['energy']),bg='#fff',font=("cambria 12 bold")).place(x=10,y=110)
    Label(f,text='Danceability: '+str(popular.danceability),bg='#fff',font=("cambria 12 bold")).place(x=10,y=130)
    Label(f,text='Length: '+str(round(popular.length/60,4))+' Minutes',bg='#fff',font=("cambria 12 bold")).place(x=10,y=150)
    Label(f,text='Acousticness: '+str(popular.acousticness),bg='#fff',font=("cambria 12 bold")).place(x=10,y=170)
    Label(f,text='Popularity: '+str(popular.popularity),bg='#fff',font=("cambria 12 bold")).place(x=10,y=190)
    Label(f,text='Speechiness: '+str(popular.speechiness),bg='#fff',font=("cambria 12 bold")).place(x=10,y=210)
    f.place(x=5,y=5,width=290,height=245)

    root.title("Top Streamed Songs")
    root.geometry('300x255')
#     root.configure(bg='#1db954')
    mainloop()




def abt():
    tmsg.showinfo("About!","This Project is made by Deepak kumar. In this Project you can view various visualizations and analysis of data provided by Spotify as world's top 100 most streamed songs of all time.")




def further():

    root=Tk()

    mainmenu=Menu(root)
    m=Menu(mainmenu,tearoff=0)
    m.add_command(label="Get CSV File")
    m.add_separator()
    m.add_command(label="Exit",command=root.destroy)

    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="File",menu=m)
    
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="About",command=abt)

    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Help",menu=m1)


    topframe=Frame(root,borderwidth=2,relief='ridge',bg='#fff')
    #   
    topframe.place(width=790,height=100,x=5,y=5)

    namedisp=Label(topframe,text='Hello '+str(name.get())+'!',font=('futura 26 bold'),background='#fff',fg='#191414').pack(padx=230,pady=20)


    bottomframe=Frame(root,bg='#1db954')
    bottomframe.place(width=790,height=475,x=5,y=110)


    leftframe=Frame(bottomframe,borderwidth=2,relief='ridge',bg='#fff')

    subframe1=Frame(leftframe,borderwidth=2,relief='ridge',bg='#fff')
    title=Label(leftframe,text='About Dataset',font=('arial 14 bold'),fg='#191414',bg='#fff')
    title.place(x=30,y=17)

    txt=Label(subframe1,font=('calibri 12'),
            text='Top 100 most streamed songs on spotify in the',bg='#fff')
    txt.place(x=8,y=10)
    txt=Label(subframe1,font=('calibri 12'),
            text='world. This  file  contains   several  columns',bg='#fff')
    txt.place(x=8,y=30)
    txt=Label(subframe1,font=('calibri 12'),
            text='on  popularity  and other features of the songs.',bg='#fff')
    txt.place(x=8,y=50)
    txt=Label(subframe1,font=('calibri 12'),
            text='Source:- https://www.kaggle.com',bg='#fff')
    txt.place(x=8,y=70)

    subframe1.place(width=340,height=105,x=12,y=30)

    subframe2=Frame(leftframe,borderwidth=2,relief='ridge',bg='#fff')
    title2=Label(leftframe,text='About Project',font=('arial 14 bold'),fg='#191414',bg='#fff')

    txt=Label(subframe2,font=('calibri 12'),
            text='This Project is intended  to analyze and visualize',bg='#fff')
    txt.place(x=8,y=20)
    txt=Label(subframe2,font=('calibri 12'),
            text="the data of World's top 100 most streamed",bg='#fff')
    txt.place(x=8,y=40)
    txt=Label(subframe2,font=('calibri 12'),
            text='songs. Click on the links to view analysis.',bg='#fff')
    txt.place(x=8,y=60)

    title2.place(x=30,y=182)

    subframe2.place(width=340,height=105,x=10,y=195)

    subframe3=Frame(leftframe,borderwidth=2,relief='ridge',bg='#fff')
    title3=Label(leftframe,text='About Author',font=('arial 14 bold'),fg='#191414',bg='#fff')
    txt=Label(subframe3,text='Name: Deepak Kumar',font=('calibri 12'),bg='#fff')
    txt.place(x=8,y=20)
    txt=Label(subframe3,text='Branch: BCA',font=('calibri 12'),bg='#fff')
    txt.place(x=8,y=40)
    title3.place(x=30,y=350)
    subframe3.place(width=340,height=90,x=10,y=365)

    leftframe.place(width=370,height=475,x=0,y=0)



    rightframe=Frame(bottomframe,borderwidth=2,relief='ridge',bg='#fff')

    title_main=Label(rightframe,text='Analysis and Visualizations-',font=('arial 14 bold'),fg='#191414',bg='#fff')
    title_main.place(x=5,y=15)
    Button(rightframe,bg='#1ed760',fg='#191414',command=yearwisesongs,borderwidth=0,text='Tap here to view the number of famous songs by year',font=('Calibri 11 italic')).place(x=35,y=50,width=340,height=40)
    Button(rightframe,bg='#1ed760',fg='#191414',command=topgenre,borderwidth=0,text='Tap here to view the Famous Genre by Year                       ',font=('Calibri 11 italic')).place(x=35,y=95,width=340,height=40)
    Button(rightframe,bg='#1ed760',fg='#191414',command=songbyartist,borderwidth=0,text='Tap here to view number of famous song Artist wise      ',font=('Calibri 11 italic')).place(x=35,y=140,width=340,height=40)
    Button(rightframe,bg='#1ed760',fg='#191414',command=POSTMALONE,borderwidth=0,text='Tap here to visualize the attributes of Top Artist               ',font=('Calibri 11 italic')).place(x=35,y=185,width=340,height=40)
    Button(rightframe,bg='#1ed760',fg='#191414',command=EDSHEERAN,borderwidth=0,text='Tap here to visualize the attributes of Second Top Artist',font=('Calibri 11 italic')).place(x=35,y=230,width=340,height=40) #post malone
    Button(rightframe,bg='#1ed760',fg='#191414',command=mpopular,borderwidth=0,text='Tap here to view Most Popular Song in the world            ',font=('Calibri 11 italic')).place(x=35,y=275,width=340,height=40) #ed sheeran
    Button(rightframe,bg='#1ed760',fg='#191414',command=topPopular,borderwidth=0,text='Tap here to analyse the Popularity of Top 5 songs          ',font=('Calibri 11 italic')).place(x=35,y=320,width=340,height=40)
    Button(rightframe,bg='#1ed760',fg='#191414',command=BPMvsYEAR,borderwidth=0,text='Tap here to visualize BPM level of songs year wise         ',font=('Calibri 11 italic')).place(x=35,y=365,width=340,height=40)
    Button(rightframe,bg='#1ed760',fg='#191414',borderwidth=0,command=others,text='Others                                                                                                 ',font=('Calibri 11 italic')).place(x=35,y=410,width=340,height=40)
    rightframe.place(width=415,height=475,x=375,y=0)


    root.geometry('800x600')
    root.maxsize(800,590)
    root.minsize(800,590)
    root.title("Top Streamed Songs")
    root.configure(bg='#1db954')
    mainloop()
    


root=Tk()

name=StringVar()

def para():
    if not name.get():
        tmsg.showinfo('Oops!','Enter your Name first!')
    else:
        further()


lbl1=Label(root,text='Hey There!',font=('futura 26')).pack()
msg=Label(root,text='Welcome to this Mélodieuse Project')
msg.place(x=50,y=45)
lbl2=Label(root, text='Enter Your First Name to Continue:',font=('calibri 10'))
lbl2.place(x=18,y=80)
input1=Entry(root,textvariable=name,font=('arial 11 bold'), background="#fff",borderwidth=1,relief=SUNKEN)
input1.place(x=20,y=110,width=255,height=25)
btn=Button(root,border=2,relief=SUNKEN,text='Proceed Further',bg="#1ed760",command=para,padx=5,font='calibri 11 bold')
btn.place(x=70,y=145,width=150,height=30)

root.geometry("300x190")
# root.configure(bg="#e3fffd")
root.maxsize(300,190)
root.minsize(300,190)
root.title("Top Streamed Songs")
root.mainloop()






