import tkinter as tk
from tkinter import ttk as ttk

if __name__ == '__main__':
    root = tk.Tk()

    style = ttk.Style()
    style.configure('deepskyblue.TFrame',background="deepskyblue")
# ------------------------------------------------------------
# Window作成
# ------------------------------------------------------------
    root.title('ボタン押下 ラベル変化')
    root.geometry('300x300')
    root.resizable(False,False)

# ------------------------------------------------------------
# Frame作成
# ------------------------------------------------------------
    frame = tk.Frame(root,bg='deepskyblue')
    frame.pack(expand=1,fill=tk.BOTH)
  
    """
    frame = ttk.Frame(root, relief='groove',style ='deepskyblue.TFrame',padding=5)
    frame.pack()
    """
# ------------------------------------------------------------
# ボタン挙動
# ------------------------------------------------------------
    text = tk.StringVar(frame)
    text.set("ボタンを押すと変更します")

    def change():
        text.set("変更しました") 

# ------------------------------------------------------------
# ウィジェット作成
# ------------------------------------------------------------
    label_name  = ttk.Label(frame,textvariable=text,background="deepskyblue",compound="center")
    button1 = ttk.Button(frame,text="押下",compound="center",command=change)
    
    label_name.pack(anchor="center",padx=0)
    button1.pack(anchor="center",padx=0)
    root.mainloop()
    
"""
■反省
フレームの中にラベルとか入れたら、フレームが小さくなった
原因:フレームをttkで作ろうとしていたから

作って思ったこと、ウィンドウ、フレームはtkの方が作りやすい
ttkで作ると情報がないから無理に難しくなる
tkとttkの違いはウィジェットのデザインなどの違いだから影響はない
"""
