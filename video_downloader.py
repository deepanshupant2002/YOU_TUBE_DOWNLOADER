from pytube import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0
def progress(stream=None,chunk=None,file_handle=None,remaining=0):
                    
                    # GETS THE %AGE OF THE FILE THAT HAS BEEN DOWNLOADED

    file_downloaded=(file_size-remaining)
    per = (file_downloaded//file_size)*100
    btm.config(text=f"{per}% downloaded")

def startDownload():
    global file_size 
    try:
        url =urlField.get()
        print(url)
                    #  CHANGING BUTTON TEXT
        btm.config(text="Please wait.......")
        btm.config(state=DISABLED)
        path_to_save = askdirectory()
        print(path_to_save)                    #path must be same as the directory in which you are working 

        if path_to_save is None:
            return

                         # CREATING YOU TUBE OBJECT WITH URL

        ob= YouTube(url,on_progress_callback=progress)




        # strms=ob.streams.all()          for checking all streams
        # for i in strms:
        #     print(i)

        strm=ob.streams.first()
        file_size=strm.filesize
        print(file_size)

        # print(strm.filesize)          for determining video size
        # print(strm.title)             for determining  video title
        # print(ob.title)               for determining video title using ob object
        # print(ob.description)         for checking description

                            #    FOR DOWNLOADING THE VIDEO 

        strm.download(path_to_save)
        print('Done.....')
        btm.config(text="Start Download") 
        btm.config(state=NORMAL)
        showinfo("Download Finished","Downloaded Successfully")
        urlField.delete(0,END)

    except Exception as e:
        print(e)
        print("error !!!")


def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()



                                # STARTING GUI MAKING

root=Tk()
root.title("Video Downloader")

                                    # SETTING ICON

root.iconbitmap("youtube.ico")
root.geometry('500x600')
file=PhotoImage(file='download.png')
headingicon=ttk.Label(root,image=file)
headingicon.pack(side=TOP)

                                # URL TEXTFIELD

urlField=ttk.Entry(root,font=("verdana",15),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)
                                 

                        #  CREATING BUTTON


btm = Button(root,text="Start Download",font=("verdana",15),relief='ridge',command=startDownloadThread)
btm.pack(side=TOP,pady=10)



root.mainloop()