#coding:utf-8
#!/usr/bin/env python
#Filename:first_gui.py
#Author:Haro
#Date:2017.02.19 22:08
"""
GUI编程 Tkinter 简易计算器
"""
from Tkinter import *
import time

def cal(inp_cal):
    try:
        return eval(inp_cal)
    except Exception as e:   #防止计算发生错误
        return 0

class App:
    def __init__(self, master):
        frame1 = Frame(master)
        #frame1.pack_propagate(0)
        frame1.pack()
        w = Label(frame1,text="输入结果",font='Helvetica 12 bold')
        w.pack()
        self.v=StringVar()  #对变量进行跟踪修改
        self.e = Entry(frame1,textvariable=self.v,font='Helvetica 12 bold')
        self.e.pack(padx=5)
        w1 = Label(frame1,text="计算结果",font='Helvetica 12 bold')
        w1.pack()
        self.v1 = StringVar() #对变量进行跟踪修改
        e1 = Entry(frame1, textvariable=self.v1,font='Helvetica 12 bold')
        self.v1.set("")
        #v1 = v1
        e1.pack()

        frame = Frame(master)
        #frame.pack_propagate(0)
        frame.pack()

        self.input_str=[]

        Button(frame, text="1",command=lambda:self.input_cal('1'),font='Helvetica 15 bold').grid(row=0,column=0)
        Button(frame, text="2",command=lambda:self.input_cal('2'),font='Helvetica 15 bold').grid(row=0,column=1)
        Button(frame, text="3",command=lambda:self.input_cal('3'),font='Helvetica 15 bold').grid(row=0,column=2)
        Button(frame, text="4",command=lambda:self.input_cal('4'),font='Helvetica 15 bold').grid(row=1,column=0)
        Button(frame, text="5",command=lambda:self.input_cal('5'),font='Helvetica 15 bold').grid(row=1,column=1)
        Button(frame, text="6",command=lambda:self.input_cal('6'),font='Helvetica 15 bold').grid(row=1,column=2)
        Button(frame, text="7",command=lambda:self.input_cal('7'),font='Helvetica 15 bold' ).grid(row=2,column=0)
        Button(frame, text="8",command=lambda:self.input_cal('8'),font='Helvetica 15 bold').grid(row=2,column=1)
        Button(frame, text="9",command=lambda:self.input_cal('9'),font='Helvetica 15 bold').grid(row=2,column=2)
        Button(frame, text="0",command=lambda:self.input_cal('0'),font='Helvetica 15 bold' ).grid(row=3,column=0)
        Button(frame, text="+",command=lambda:self.input_cal('+'),font='Helvetica 15 bold' ).grid(row=0,column=3)
        Button(frame, text="-",command=lambda:self.input_cal('-'),font='Helvetica 15 bold' ).grid(row=1,column=3)
        Button(frame, text="x",command=lambda:self.input_cal('*'),font='Helvetica 15 bold').grid(row=2,column=3)
        Button(frame, text="/",command=lambda:self.input_cal('/'),font='Helvetica 15 bold' ).grid(row=3,column=3)
        Button(frame, text="=", command=self.show_result,font='Helvetica 15 bold').grid(row=3,column=1)
        Button(frame, text="C", command=self.empty,font='Helvetica 15 bold').grid(row=3,column=2)

    def input_cal(self,s): #更新输入列表
        self.input_str.append(s)
        self.v.set(''.join(self.input_str))
        self.v1.set('')
    def show_result(self):
        input_str1 = self.e.get()
        self.v1.set('='+'%d'% cal(input_str1))
        self.input_str=[]  #清空输入列表
    def empty(self):  #清空输入输出列表
        self.input_str=[]
        self.v.set("")
        self.v1.set("")
    def empty_out(self):
        self.v1.set('')

root = Tk()
root.geometry('280x330')
root.title('Calculator')
app = App(root)
Button(root,text='close',command=root.quit,font='Helvetica 15 bold').pack()
root.mainloop()
