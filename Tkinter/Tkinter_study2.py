import tkinter as tk
from tkinter import ttk as ttk
from tkinter import StringVar

if __name__ == '__main__':
    root = tk.Tk()

# ------------------------------------------------------------
# インスタンス化、変数宣言
# ------------------------------------------------------------
msg_out = ''
msg_in = tk.StringVar(value="")
msg_out= tk.StringVar(value="")


# buttonを押下時の動作
def name_output():
    print("ボタンを押下")
    msg_out.set(msg_in.get())
    
    
# ------------------------------------------------------------
# Window作成・配置
# ------------------------------------------------------------
root.title('名前入出力')
root.geometry('320x320')
root.resizable(False,False)

# ------------------------------------------------------------
# Frame作成・配置
# ------------------------------------------------------------
frame = tk.Frame(root)
frame.pack(expand=1,fill=tk.BOTH)

# ------------------------------------------------------------
# ウィジェット作成・配置
# ------------------------------------------------------------
name = ttk.Label(frame,text='姓  名')
text = ttk.Entry(frame,width= 20,textvariable=msg_in)
button = ttk.Button(frame,text='決 定',command=name_output)
output_name = ttk.Label(frame,textvariable=msg_out,background="MediumSpringGreen")

name.grid(row=0, column= 0,ipadx= 10)
text.grid(row=0,column=1 ,padx= 5)
button.grid(row=0,column=2 ,ipadx= 5)
output_name.grid(row=1,column=0,sticky=tk.E+tk.W,columnspan=3)



root.mainloop()

"""
メモ
textvariableを使用しているから
テキスト入力時がイベントの為、
入力しているときにラベルの出力欄にそのまま出力出来るからボタンを押下するイベント自体不要


"""