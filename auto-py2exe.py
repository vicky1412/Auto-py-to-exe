import tkinter
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import scrolledtext
import subprocess
import os
import threading
import time
import sys

old_stdout = sys.stdout


class StdoutRedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.update_idletasks()
        self.text_area.insert(tkinter.END, str)
        self.text_area.see(tkinter.END)

class autopy2exe:

    def __init__(self):
        self.main_window()
        self.command = ['pyinstaller', '--onedir', '--console']
        self.test1 = ""
        self.test2 = ""
        self.test3 = ""
        self.one = "--onedir"
        self.two = "--console"
        self.frame()
        self.logo()
        self.icon()
        self.label()
        self.tk_button()


    def main_window(self):
        self.window = tkinter.Tk()
        self.window.configure(background='white')
        self.window.title('Auto-Py-to-Exe')
        self.window.geometry('610x650+400+30')
        self.canvas = tkinter.Canvas(self.window, bg='red')
        self.scroll = tkinter.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.main_frame = tkinter.Frame(self.canvas, width=610)
        self.canvas.create_window(0, 0, anchor='nw', window=self.main_frame)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'),yscrollcommand=self.scroll.set)
        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll.pack(fill='y', side='right')


    def hide_widget(self,widget):
        widget.pack_forget()

    def show_widget(self,widget):
        widget.pack(after=self.bttn6)

    def logo(self):
        self.image1 = Image.open("favicon.png")
        self.image1 = self.image1.resize((70, 70))
        self.image1 = ImageTk. PhotoImage(self.image1)
        tkinter.Label(self.frame1,bg='white',image=self.image1).place(x=10,y=20)

    def icon(self):
        p1 = tkinter.PhotoImage(file='C:\\Users\\vignesh\\Documents\\PycharmProjects\\vicky\\auto-py-to-exe\\favicon.png')
        self.window.iconphoto(False, p1)

    def process(self):
        sys.stdout = StdoutRedirector(self.label6)
        print("\n")
        #subprocess.call(self.total_command,shell=True, cwd="C:\\Users\\vignesh\\Documents\\PycharmProjects\\vicky",stderr=sys.stdout)

        self.p = subprocess.Popen(self.total_command, shell=True, cwd="C:\\Users\\vignesh\\Documents\\PycharmProjects\\vicky",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.output, self.errors = self.p.communicate()

        print(self.errors)

        # delete the build and spec file
        try:
            print('entered')
            xx = self.file.split('/')
            location1 = '/'.join(xx[0:-1])
            yy = self.filename1.split('/')
            location2 = location1 + "/"+ yy[-1].replace('.py','.txt')
            location2 = location2.strip('"')
            os.remove(location2)
            dir = "build"
            path = location1.strip('"') + '/'+ dir
            os.rmdir(path)
        except Exception:
            print("passed")
            pass

    def current_cmd_update(self):
        self.label5.delete("1.0","end")
        for x in self.command:
            self.label5.insert(tkinter.END,x + " ")

    def label(self):
        tkinter.Label(self.frame1, text="Auto Py to Exe", bg='white', font=("Arial", 20),padx=2,pady=2).place(x=90, y=35)
        tkinter.Label(self.frame2, text="Script Loacation", bg='white',font=("Arial", 15),padx=2,pady=2).place(x=10, y=10)
        tkinter.Label(self.frame3, text="Onefile",bg='white', font=("Arial", 15), padx=2, pady=2).place(x=10, y=5)
        tkinter.Label(self.frame3, text="(--onedir / --onefile)",bg='white', font=("TkTextFont", 10), padx=2, pady=2).place(x=80, y=10)
        tkinter.Label(self.frame4, text="Console Window", bg='white', font=("Arial", 15), padx=2, pady=2).place(x=10, y=2)
        tkinter.Label(self.frame4, text="(--console / --windowed)", bg='white', font=("TkTextFont", 10), padx=2,pady=2).place(x=170, y=7)
        tkinter.Label(self.frame5, text="Icon", bg='white', font=("Arial", 15), padx=2, pady=2).place(x=50,y=2)
        tkinter.Label(self.frame5, text="(--icon)", bg='white', font=("TkTextFont", 10), padx=2,pady=2).place(x=95, y=7)
        tkinter.Label(self.frame7, text='Manual Argument',bg='white', font=("Arial", 15), padx=2, pady=2).place(x=50,y=3)
        tkinter.Label(self.frame8, text='Manual Argument : ', bg='white', font=("TkTextFont", 12), padx=2, pady=2).place(x=30,y=3)
        tkinter.Label(self.frame9, text='Output', bg='white', font=("Arial", 15), padx=2, pady=2).place(x=50,y=3)
        tkinter.Label(self.frame10, text='Output Directory : ', bg='white', font=("TkTextFont", 12), padx=2,pady=2).place(x=30, y=3)
        tkinter.Label(self.frame11, text="Current Command", bg='white', font=("Arial", 15), padx=2, pady=2).place(x=17,y=5)

        # file browse label
        self.label_border1 = tkinter.Frame(self.frame2, highlightbackground="blue", highlightthickness=1, bd=0)
        self.label1 = tkinter.Label(self.label_border1, text="select the file", relief="solid", fg='#2b2d2e', width='60', bg="White",borderwidth='0', anchor='w', padx=5, pady=4)
        self.label1.pack()
        self.label_border1.pack()
        self.label_border1.place(x=15, y=50)

        # icon browse label
        self.label_border2 = tkinter.Frame(self.frame6, highlightbackground="blue", highlightthickness=1, bd=0)
        self.label2 = tkinter.Label(self.label_border2, text="select the file", relief="solid", fg='#2b2d2e',width='58', bg="White", borderwidth='0', anchor='w', padx=5, pady=4)
        self.label2.pack()
        self.label_border2.pack()
        self.label_border2.place(x=30, y=2)

        # manual argument input
        self.label_border3 = tkinter.Frame(self.frame8, highlightbackground="blue", highlightthickness=1, bd=0)
        self.label3 = tkinter.Text(self.label_border3, relief="solid", fg='#2b2d2e',width='33',height='1', bg="White", borderwidth='0', padx=5, pady=4)
        self.label3.pack()
        self.label_border3.pack()
        self.label_border3.place(x=170, y=2)

        # output directory browse label
        self.label_border4 = tkinter.Frame(self.frame10, highlightbackground="blue", highlightthickness=1, bd=0)
        self.label4 = tkinter.Label(self.label_border4, text="select folder", relief="solid", fg='#2b2d2e',
                                    width='39', bg="White", borderwidth='0', anchor='w', padx=5, pady=4)
        self.label4.pack()
        self.label_border4.pack()
        self.label_border4.place(x=160, y=3)

        # current command
        self.label5 = tkinter.Text(self.frame12, relief="solid", fg='#2b2d2e', width='68', height='2', yscrollcommand='yes', bg="White", borderwidth='1', padx=5, pady=4)
        self.label5.pack()
        self.label5.place(x=17,y=5)

        self.label5.insert(tkinter.END,self.command)

        self.label6 = scrolledtext.ScrolledText(self.frame14,width=68,height=20)
        self.label6.pack()
        self.label6.place(x=17,y=5)

    def frame(self):
        self.frame1 = tkinter.LabelFrame(self.main_frame,width=600,height=110,bg='white', borderwidth='0')
        self.frame1.pack()
        self.frame2 = tkinter.LabelFrame(self.main_frame,width=600,height=85,bg='white', borderwidth='0')
        self.frame2.pack(after=self.frame1)
        self.frame3 = tkinter.LabelFrame(self.main_frame, width=600, height=91, bg='white', borderwidth='0')
        self.frame3.pack(after=self.frame2)
        self.frame4 = tkinter.LabelFrame(self.main_frame, width=600, height=95, bg='white', borderwidth='0')
        self.frame4.pack(after=self.frame3)
        self.frame5 = tkinter.LabelFrame(self.main_frame, width=600, height=38, bg='white', borderwidth='0')
        self.frame5.pack(after=self.frame4)
        self.frame6 = tkinter.LabelFrame(self.main_frame, width=600, height=35, bg='white', borderwidth='0')
        self.frame6.pack_forget()
        self.frame7 = tkinter.LabelFrame(self.main_frame, width=600, height=42, bg='white', borderwidth='0')
        self.frame7.pack(after=self.frame5)
        self.frame8 = tkinter.LabelFrame(self.main_frame, width=600, height=35, bg='white', borderwidth='0')
        self.frame8.pack_forget()
        self.frame9 = tkinter.LabelFrame(self.main_frame, width=600, height=42, bg='white', borderwidth='0')
        self.frame9.pack(after=self.frame7)
        self.frame10 = tkinter.LabelFrame(self.main_frame, width=600, height=35, bg='white', borderwidth='0')
        self.frame10.pack_forget()
        self.frame11 = tkinter.LabelFrame(self.main_frame, width=600, height=38, bg='white', borderwidth='0')
        self.frame11.pack(after=self.frame9)
        self.frame12 = tkinter.LabelFrame(self.main_frame, width=600, height=52, bg='white', borderwidth='0')
        self.frame12.pack(after=self.frame11)
        self.frame13 = tkinter.LabelFrame(self.main_frame, width=600, height=53, bg='white', borderwidth='0')
        self.frame13.pack(after=self.frame12)
        self.frame14 = tkinter.LabelFrame(self.main_frame, width=600, height=150, bg='yellow', borderwidth='0')
        self.frame14.pack_forget()

    def command_text(self):
        self.frame12.pack_forget()
        self.frame14.pack(after=self.frame11)

    def browsefunc1(self):
        self.filename1= '"' + filedialog.askopenfilename() + '"'
        if self.filename1 == "":
            self.label_border1.config(highlightbackground="red")
        else:
            self.label_border1.config(highlightbackground="blue")
            self.label1.config(text=self.filename1)
            if self.test1 in self.command:
                self.command.remove(self.test1)
                self.command.append(self.filename1)
                self.test1 = self.filename1
            else:
                self.test1 = self.filename1
                self.command.append(self.filename1)
        self.current_cmd_update()

    def browsefunc2(self):
        self.filename2 = '--icon "' +filedialog.askopenfilename() + '"'
        if self.filename2 == "":
            self.label_border2.config(highlightbackground="red")
        else:
            self.label_border2.config(highlightbackground="blue")
            self.label2.config(text=self.filename2)
            if self.test2 in self.command:
                self.command.remove(self.test2)
                self.command.append(self.filename2)
                self.test2 = self.filename2
            else:
                self.test2 = self.filename2
                self.command.append(self.filename2)
        self.current_cmd_update()

    def browsefunc3(self):
        self.file = '"' +filedialog.askdirectory()+ '"'
        self.filename3 = '--distpath ' +self.file
        if self.filename3 == "":
            self.label_border4.config(highlightbackground="red")
        else:
            self.label_border4.config(highlightbackground="blue")
            self.label4.config(text=self.filename3)
            if self.test3 in self.command:
                self.command.remove(self.test3)
                self.command.append(self.filename3)
                self.test3 = self.filename3
            else:
                self.test3 = self.filename3
                self.command.append(self.filename3)
        self.current_cmd_update()

    def onedirectoryfunc(self):
        self.button_border2.config(highlightbackground='blue')
        self.button_border3.config(highlightbackground="gray")
        if self.one == '--onedir':
            pass
        elif self.one in self.command:
            self.command.remove((self.one))
            self.one = '--onedir'
            self.command.append(self.one)
        self.current_cmd_update()

    def onefilefunc(self):
        self.button_border3.config(highlightbackground="blue")
        self.button_border2.config(highlightbackground='grey')
        if self.one == '--onedir':
            self.command.remove(self.one)
            self.one = '--onefile'
            self.command.append(self.one)
        self.current_cmd_update()

    def consolefunc(self):
        self.button_border4.config(highlightbackground="blue")
        self.button_border5.config(highlightbackground='grey')
        if self.two == '--console':
            pass
        elif self.two in self.command:
            self.command.remove((self.two))
            self.two = '--Windowed'
            self.command.append(self.two)
        self.current_cmd_update()

    def windowedfunc(self):
        self.button_border5.config(highlightbackground="blue")
        self.button_border4.config(highlightbackground='grey')
        if self.two == '--console':
            self.command.remove(self.two)
            self.two = '--windowed'
            self.command.append(self.two)
        self.current_cmd_update()

    def addfcn(self):
        self.ARGUMENTS = self.label3.get("1.0", "end-1c")
        self.command.append(self.ARGUMENTS)
        self.label3.delete("1.0", "end-1c")
        self.ARGUMENTS = ""
        self.current_cmd_update()

    def converbtnfunc(self):
        self.total_command = self.label5.get("1.0", "end-1c")
        self.command_text()
        self.process()

    def changeOnHover(self,button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def tk_button(self):
        # file browse button
        button_border1 = tkinter.Frame(self.frame2, highlightbackground="blue",highlightthickness=2, bd=0)
        bttn1 = tkinter.Button(button_border1, text="Browse", relief="solid", bg="White", borderwidth='0', padx=45, pady=1,command=self.browsefunc1)
        bttn1.pack()
        button_border1.pack()
        button_border1.place(x=453,y=50)
        self.changeOnHover(bttn1, "#dde5eb", "white")

        # icon browse button
        self.button_border7 = tkinter.Frame(self.frame6, highlightbackground="blue", highlightthickness=2, bd=0)
        self.bttn7 = tkinter.Button(self.button_border7, text="Browse", relief="solid", bg="White", borderwidth='0', padx=45,pady=1, command=self.browsefunc2)
        self.bttn7.pack()
        self.button_border7.pack()
        self.button_border7.place(x=453, y=2)
        self.changeOnHover(self.bttn7, "#dde5eb", "white")

        # manual args add button
        button_border8 = tkinter.Frame(self.frame8, highlightbackground="blue", highlightthickness=2, bd=0)
        bttn8 = tkinter.Button(button_border8, text="Add", relief="solid", bg="White", borderwidth='0',padx=20,pady=1,command=self.addfcn)
        bttn8.pack()
        button_border8.pack()
        button_border8.place(x=453, y=2)
        self.changeOnHover(bttn8, "#dde5eb", "white")

        # output directory browse button
        self.button_border10 = tkinter.Frame(self.frame10, highlightbackground="blue", highlightthickness=2, bd=0)
        self.bttn10 = tkinter.Button(self.button_border10, text="Browse", relief="solid", bg="White", borderwidth='0',padx=45, pady=1, command=self.browsefunc3)
        self.bttn10.pack()
        self.button_border10.pack()
        self.button_border10.place(x=453, y=2)
        self.changeOnHover(self.bttn10, "#dde5eb", "white")

        # convert button
        bttn11 = tkinter.Button(self.frame13, text="CONVERT .PY TO .EXE", font=('Arial',12), relief="solid", bg="blue",fg='white', borderwidth='0', padx=190, pady=10,command=self.converbtnfunc)
        bttn11.pack()
        bttn11.place(x=17, y=3)
        self.changeOnHover(bttn11, "#094385", "blue")

        # one directory button
        self.button_border2 = tkinter.Frame(self.frame3, highlightbackground="blue",highlightthickness=2, bd=0)
        bttn2 = tkinter.Button(self.button_border2, text="One Directory",relief="solid",bg="White",borderwidth='0',pady=8,command=self.onedirectoryfunc)
        bttn2.pack()
        self.button_border2.pack()
        self.button_border2.place(x=17,y=45)
        self.changeOnHover(bttn2, "#dde5eb", "white")

        # one file button
        self.button_border3 = tkinter.Frame(self.frame3, highlightbackground="grey",highlightthickness=2, bd=0)
        bttn3 = tkinter.Button(self.button_border3, text="One File",relief="solid",bg="White",borderwidth='0',pady=8,command=self.onefilefunc)#.place(x=105,y=250)
        bttn3.pack()
        self.button_border3.pack()
        self.button_border3.place(x=108,y=45)
        self.changeOnHover(bttn3, "#dde5eb", "white")

        # console based button
        self.button_border4 = tkinter.Frame(self.frame4, highlightbackground="blue", highlightthickness=2, bd=0)
        bttn4 = tkinter.Button(self.button_border4, text="Console Based", relief="solid", bg="White", borderwidth='0',pady=8,command=self.consolefunc)
        bttn4.pack()
        self.button_border4.pack()
        self.button_border4.place(x=17, y=40)
        self.changeOnHover(bttn4, "#dde5eb", "white")

        # window based buttton
        self.button_border5 = tkinter.Frame(self.frame4, highlightbackground="grey", highlightthickness=2, bd=0)
        bttn5 = tkinter.Button(self.button_border5, text="Window Based(hide the console)", relief="solid", bg="White", borderwidth='0',pady=8,command=self.windowedfunc)
        bttn5.pack()
        self.button_border5.pack()
        self.button_border5.place(x=111, y=40)
        self.changeOnHover(bttn5, "#dde5eb", "white")

        # read image
        self.photo = Image.open("bttnimage.png")
        self.photo = self.photo.resize((30,30))
        self.photo = ImageTk.PhotoImage(self.photo)

        self.s1 = self.photo
        self.s2 = self.photo
        self.s3 = self.photo

        # icon button 1
        self.bttn6 = tkinter.Button(self.frame5,bg='white',image = self.s1,borderwidth='0',relief='solid',command=self.selct_icon1)
        self.bttn6.place(x=17,y=2)
        self.changeOnHover(self.bttn6, "white", "white")

        # icon button 2
        self.bttn8 = tkinter.Button(self.frame7, bg='white', image=self.s2, borderwidth='0', relief='solid',command=self.selct_icon2)
        self.bttn8.place(x=17, y=3)
        self.changeOnHover(self.bttn8, "white", "white")

        # icon button 3
        self.bttn9 = tkinter.Button(self.frame9, bg='white', image=self.s2, borderwidth='0', relief='solid',command=self.selct_icon3)
        self.bttn9.place(x=17, y=3)
        self.changeOnHover(self.bttn9, "white", "white")

    def selct_icon1(self):
        if self.s1 == self.photo:
            self.photo1 = Image.open("bttnimage.png")
            self.photo1 = self.photo1.resize((30, 30))
            self.photo1 = self.photo1.rotate(180)
            self.photo1 = ImageTk.PhotoImage(self.photo1)
            self.s1=self.photo1
            self.bttn6.config(image=self.photo1)

            self.frame6.pack(after=self.frame5)
        else:
            self.bttn6.config(image=self.photo)
            self.s1 = self.photo
            self.frame6.pack_forget()

    def selct_icon2(self):
        if self.s2 == self.photo:
            self.photo2 = Image.open("bttnimage.png")
            self.photo2 = self.photo2.resize((30, 30))
            self.photo2 = self.photo2.rotate(180)
            self.photo2 = ImageTk.PhotoImage(self.photo2)
            self.s2=self.photo2
            self.bttn8.config(image=self.photo2)

            self.frame8.pack(after=self.frame7)
        else:
            self.bttn8.config(image=self.photo)
            self.s2 = self.photo
            self.frame8.pack_forget()

    def selct_icon3(self):
        if self.s3 == self.photo:
            self.photo3 = Image.open("bttnimage.png")
            self.photo3 = self.photo3.resize((30, 30))
            self.photo3 = self.photo3.rotate(180)
            self.photo3 = ImageTk.PhotoImage(self.photo3)
            self.s3=self.photo3
            self.bttn9.config(image=self.photo3)

            self.frame10.pack(after=self.frame9)
        else:
            self.bttn9.config(image=self.photo)
            self.s3 = self.photo
            self.frame10.pack_forget()

    def loop_window(self):
        self.window.mainloop()


X = autopy2exe()
X.loop_window()

sys.stdout = old_stdout
