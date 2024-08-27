import sqlite3
import tkinter as tk
from tkinter import messagebox

class Login_applicaton():
    def start_page(self,back=None):
        if back!=None:
            back.destroy()
        self.login_window = tk.Tk()
        self.login_window.title("login page")

        tk.Label(self.login_window, text="Username").pack()
        self.username_entry=tk.Entry(self.login_window)
        self.username_entry.pack()

        tk.Label(self.login_window, text="Password").pack()
        self.password_entry=tk.Entry(self.login_window,show="*")
        self.password_entry.pack()

        self.login_button= tk.Button(self.login_window, text="login",command=self.login)
        self.login_button.pack()

        self.sinup_button=tk.Button(self.login_window,text="SINUP",command=self.sinup)
        self.sinup_button.pack()

        self.login_window.mainloop()

    def __init__(self) -> None:
        self.start_page()
        conn=sqlite3.connect('user_db.db')
        courser=conn.cursor()
        courser.execute('''
            CREATE TABLE IF NOT EXISTS users (
                        USERNAME TEXT PRIMARY KEY,
                        PASSWORD TEXT NOT NULL,
                        NAME TEXT NOT NULL,
                        AGE INTEGER NOT NULL,
                        EMAIL TEXT NOT NULL)
            ''')

    def sinup(self):

        self.login_window.destroy()

        self.sinup_window=tk.Tk()
        self.sinup_window.title("sinup")

        tk.Label(self.sinup_window,text="username").pack()
        self.new_username=tk.Entry(self.sinup_window)
        self.new_username.pack()
        tk.Label(self.sinup_window,text="password").pack()
        self.new_password=tk.Entry(self.sinup_window)
        self.new_password.pack()
        tk.Label(self.sinup_window,text="name").pack()
        self.new_name=tk.Entry(self.sinup_window)
        self.new_name.pack()
        tk.Label(self.sinup_window,text="age").pack()
        self.new_age=tk.Entry(self.sinup_window)
        self.new_age.pack()
        tk.Label(self.sinup_window,text="e-mail").pack()
        self.new_email=tk.Entry(self.sinup_window)
        self.new_email.pack()

        self.submit_button=tk.Button(self.sinup_window,command=self.new_sinup,text="submit")
        self.submit_button.pack()
        
        self.sinup_window.mainloop()
    def new_sinup(self):
        
        conn=sqlite3.connect('user_db.db')
        courser=conn.cursor()

        usename=self.new_username.get()
        password=self.new_password.get()
        name=self.new_name.get()
        age=self.new_age.get()
        email=self.new_email.get()

        courser.execute('''
            INSERT INTO users (username,password,name,age,email) VALUES
                        (?,?,?,?,?)
        ''',(usename,password,name,age,email))

        conn.commit()
        conn.close()
        self.sinup_window.destroy()
        self.start_page()


        

    def login(self):
        conn= sqlite3.connect('user_db.db')
        courser=conn.cursor()

        username =self.username_entry.get()
        password= self.password_entry.get()

        courser.execute('''
SELECT * FROM users WHERE USERNAME = ? AND PASSWORD =?''',(username,password))
        user=courser.fetchone()

        if user:
            self.show_profile(user,self.login_window)
        else:
            messagebox.showerror(title="login failed",message="invalid username or password")
        conn.close()
    def show_profile(self,user,page):
        page.destroy()
        self.profile_window=tk.Tk()
        
        self.profile_window.title(f'Profile of {user[0]}')

        tk.Label(self.profile_window, text=f'Name:{user[2]}').pack()
        tk.Label(self.profile_window, text=f'Age:{user[3]}').pack()
        tk.Label(self.profile_window, text=f'E-Mail:{user[4]}').pack()
        tk.Button(self.profile_window,text="back",command=self.back_p).pack()
        self.profile_window.mainloop()
    def back_p(self):
        self.profile_window.destroy()
        self.start_page()
        
if __name__== "__main__":
    Login_applicaton()
        



