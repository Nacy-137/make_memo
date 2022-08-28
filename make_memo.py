import tkinter as tk
from tkinter import messagebox

class Menu_Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("メニュー")
        self.root.geometry("250x120")
        
        self.button1 = tk.Button(self.root, text="メモを記録する", command = self.create_write_win)
        self.button1.pack()
        self.button2 = tk.Button(self.root, text="メモを確認する", command = self.create_check_win)
        self.button2.pack()
        self.button3 = tk.Button(self.root, text="メモを削除する", command = self.delete_list)
        self.button3.pack()
        self.button4 = tk.Button(self.root, text="終了する", command = self.quit)
        self.button4.pack()
        
        self.root.mainloop()
        
    def create_write_win(self):
        self.write_win = Write_Window()
        
    def create_check_win(self):
        self.check_win = Check_Window()
        
    def delete_list(self):
        delete_memo()
        
    def quit(self):
        self.root.destroy()

class Write_Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("メモ作成")
        self.root.geometry("500x400")
        
        self.text = tk.Text(self.root)
        self.text.pack()
        
        self.button1 = tk.Button(self.root, text="記録する", command = self.write)
        self.button1.place(x=100,y=330,width=100,height=50)
        self.button2 = tk.Button(self.root, text="閉じる", command = self.quit)
        self.button2.place(x=300,y=330,width=100,height=50)
        
        self.root.mainloop()
        
    def write(self):
        data = self.text.get("1.0", "end")
        textWrite(self,data)
    
    def quit(self):
        self.root.destroy()

class Check_Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("メモ確認")
        self.root.geometry("500x400")
        
        self.text = tk.Text(self.root)
        self.text.pack()
        textRead(self)
        
        self.button = tk.Button(self.root, text="閉じる", command = self.quit)
        self.button.place(x=200,y=330,width=100,height=50)
        self.root.mainloop()

    def quit(self):
        self.root.destroy()
    
def textWrite(address,data):
    f = open('memo.txt','a', encoding="utf-8")
    memo_data = data.split('/n')
    f.writelines(memo_data)
    f.close()
    
    address.quit()
    messagebox.showinfo("記録完了","記録しました")
    

def textRead(address):
    f = open('memo.txt', 'r', encoding="utf-8")
    filedata = f.read().split('/n')
    i = 1
    for text in filedata:
        address.text.insert("{0}.0".format(i),text)
        i += 1
    f.close()
    
def delete_memo():
    f = open('memo.txt', 'w', encoding="utf-8")
    f.close()
    messagebox.showinfo("削除完了","削除しました")
    
if __name__ == '__main__':
    start_win = Menu_Window()
