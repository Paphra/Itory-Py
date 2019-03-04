import tkinter as tk
from tkinter import ttk


class LogInAs:

    def __init__(self):
        self.login_as = ttk.Frame(self.note_book)
        self.mf_login_as = ttk.Frame(self.login_as)

        self.loggedin_as = tk.StringVar()
        self.f_logged = ttk.Frame(self.mf_login_as)
        self.l_loggedin = ttk.Label(self.f_logged,
                                    textvariable=self.loggedin_as)

        self.f_login = ttk.Frame(self.mf_login_as)
        self.btn_login = ttk.Button(self.f_login, text='Login')
        self.e_username = ttk.Entry(self.f_login, width=30)
        self.e_password = ttk.Entry(self.f_login, width=30)
        self.btn_cancel = ttk.Button(self.f_login, text='Log Out',
                                     state='disabled')

        self.user = 'worker'

        self.login_works()
        self.hide_from_user()

    def login_works(self):
        self.note_book.add(self.login_as, text='Login As')
        self.mf_login_as.grid(column=0, row=0, sticky='NSEW',
                              padx=230, pady=165)
        self.f_logged.grid(column=0, row=0, sticky='EW')
        sp_h = ttk.Separator(self.mf_login_as, orient='horizontal')
        sp_h.grid(column=0, row=1, sticky='EW')
        self.f_login.grid(column=0, row=2, sticky='EW')

        l_logged = ttk.Label(self.f_logged, text='Logged In As',
                             width=15)
        l_logged.grid(column=0, row=0, padx=20, pady=10)
        sp_v = ttk.Separator(self.f_logged, orient='vertical')
        sp_v.grid(column=1, row=0, sticky='NS')
        self.l_loggedin.grid(column=2, row=0, padx=20, pady=10)
        self.loggedin_as.set('Worker')

        '''login buttons and fields'''
        sp_vlogin = ttk.Separator(self.f_login, orient='vertical')
        sp_vlogin.grid(column=1, row=0, sticky='NS', rowspan=3)
        l_uname = ttk.Label(self.f_login, text='Username', width=15)
        l_uname.grid(column=0, row=0, padx=20, pady=10)
        l_upass = ttk.Label(self.f_login, text='Password', width=15)
        l_upass.grid(column=0, row=1, padx=20, pady=10)
        self.e_username.grid(column=2, row=0, padx=20, pady=10)
        self.e_password.grid(column=2, row=1, padx=20, pady=10)
        self.btn_login.grid(column=2, row=2, padx=20, pady=10)
        self.btn_cancel.grid(column=0, row=2, padx=20, pady=10)

    def hide_from_user(self):
        pass
