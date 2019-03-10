import tkinter as tk
from tkinter import ttk


class LogInAs:

    def __init__(self):

        self.main_ntb = self.tabs_inst['main']
        self.tabs = self.main_ntb.tabs()

        self.login_as = ttk.Frame(self.note_book)
        self.mf_login_as = ttk.Frame(self.login_as)

        self.loggedin_as = tk.StringVar()
        self.v_username = tk.StringVar()
        self.v_password = tk.StringVar()
        self.v_wrong_pass = tk.StringVar()
        self.v_wrong_ch = tk.StringVar()
        self.f_logged = ttk.Frame(self.mf_login_as)
        self.l_loggedin = ttk.Label(self.f_logged,
                                    textvariable=self.loggedin_as)

        self.f_login = ttk.Frame(self.mf_login_as)
        self.e_username = ttk.Entry(self.f_login, width=30,
                                    textvariable=self.v_username)
        self.e_password = ttk.Entry(self.f_login, width=30, show='*',
                                    textvariable=self.v_password)
        self.l_wrong = ttk.Label(self.f_login, textvariable=self.v_wrong_pass,
                                 width=30, foreground='red')
        self.btn_login = ttk.Button(self.f_login, text='Login')

        # change Password
        self.f_ch_p = ttk.Frame(self.mf_login_as)
        self.l_wrong_ch = ttk.Label(self.f_ch_p, textvariable=self.v_wrong_ch,
                                    width=30, foreground='red')
        self.v_old_p = tk.StringVar()
        self.v_new_p = tk.StringVar()
        self.v_new_pc = tk.StringVar()
        self.b_ch_prompt = ttk.Button(self.f_login, text='Change Password',
                                      command=self.show_ch)
        self.b_ch_pass = ttk.Button(self.f_ch_p, text='Change',
                                    command=self.change)
        self.e_old_p = ttk.Entry(self.f_ch_p, textvariable=self.v_old_p,
                                 width=30, show='*')
        self.e_new_p = ttk.Entry(self.f_ch_p, textvariable=self.v_new_p,
                                 width=30, show='*')
        self.e_new_pc = ttk.Entry(self.f_ch_p, textvariable=self.v_new_pc,
                                  width=30, show='*')

        self.login_works()
        self.hide_from_user()

    def login_works(self):
        self.note_book.add(self.login_as, text='Login As')
        self.mf_login_as.grid(column=0, row=0, sticky='NSEW',
                              padx=220, pady=30)
        self.f_logged.grid(column=0, row=0, sticky='EW')
        sp_h = ttk.Separator(self.mf_login_as, orient='horizontal')
        sp_h.grid(column=0, row=1, sticky='EW')
        self.f_login.grid(column=0, row=2, sticky='EW')
        sp_h2 = ttk.Separator(self.mf_login_as, orient='horizontal')
        sp_h2.grid(column=0, row=3, stick='EW')
        self.f_ch_p.grid(column=0, row=4, sticky='EW', pady=20)

        l_logged = ttk.Label(self.f_logged, text='Logged In As',
                             width=15)
        l_logged.grid(column=0, row=0, padx=20, pady=10)
        sp_v = ttk.Separator(self.f_logged, orient='vertical')
        sp_v.grid(column=1, row=0, sticky='NS', padx=10)
        self.l_loggedin.grid(column=2, row=0, padx=20, pady=10)
        self.loggedin_as.set('Worker')

        '''login buttons and fields'''
        sp_vlogin = ttk.Separator(self.f_login, orient='vertical')
        sp_vlogin.grid(column=1, row=0, sticky='NS', rowspan=4,
                       padx=10)
        l_uname = ttk.Label(self.f_login, text='Username', width=15)
        l_uname.grid(column=0, row=0, padx=20, pady=5, sticky='E')
        l_upass = ttk.Label(self.f_login, text='Password', width=15)
        l_upass.grid(column=0, row=1, padx=20, pady=5, sticky='E')
        self.e_username.grid(column=2, row=0, padx=20, pady=5)
        self.e_password.grid(column=2, row=1, padx=20, pady=5)
        self.l_wrong.grid(column=2, row=2, padx=20, pady=5)
        self.btn_login.grid(column=2, row=3, padx=20, pady=5)

        self.btn_login.configure(command=self.login)

        self.change_password_works()

    def change_password_works(self):
        # prompt
        self.b_ch_prompt.grid(column=0, row=3, sticky='W')
        self.b_ch_prompt.configure(state='disabled')

        # change
        l_old_p = ttk.Label(self.f_ch_p, text='Old Password', width=15)
        l_new_p = ttk.Label(self.f_ch_p, text='New Password', width=15)
        l_new_pc = ttk.Label(self.f_ch_p, text='Confirm', width=15)

        l_ch_p = ttk.Label(self.f_ch_p, text='Change Password')
        l_ch_p.grid(column=2, row=0, pady=5)
        sep_h = ttk.Separator(self.f_ch_p, orient='horizontal')
        sep_h.grid(column=0, row=1, sticky='EW', columnspan=3)

        list1 = [l_old_p, l_new_p, l_new_pc]
        list2 = [self.e_old_p, self.e_new_p, self.e_new_pc]
        _i = 2
        for _l in list1:
            _l.grid(column=0, row=_i, sticky='E', padx=20, pady=5)
            list2[_i-2].grid(column=2, row=_i)
            _i = _i + 1
        sep_v2 = ttk.Separator(self.f_ch_p, orient='vertical')
        sep_v2.grid(column=1, row=2, rowspan=6, sticky='NS',
                    padx=10)
        self.l_wrong_ch.grid(column=2, row=6, padx=20, pady=5)
        sep_h2 = ttk.Separator(self.f_ch_p, orient='horizontal')
        sep_h2.grid(column=0, row=7, sticky='EW', columnspan=3)
        self.b_ch_pass.grid(column=2, row=8, padx=20, pady=5)

    def show_ch(self, event=None):
        pass

    def change(self, event=None):
        old_p = self.v_old_p.get()
        new_p = self.v_new_p.get()
        new_pc = self.v_new_pc.get()

        if new_p == new_pc:
            return None

    def hide_from_user(self):
        logged = "Worker"
        if self.user == 'manager':
            self.main_ntb.add(self.tabs[4])
            self.main_ntb.add(self.tabs[5])
            logged = 'Manager'
        else:
            self.main_ntb.hide(4)
            self.main_ntb.hide(5)

        self.loggedin_as.set(logged)
        self.sb.lb_right['text'] = 'Logged In As: ' + logged

    def login(self, event=None):
        uname = self.v_username.get()
        upass = self.v_password.get()
        if uname.lower() == 'manager' and upass == 'peitory':
            self.user = 'manager'
            self.v_username.set('')
            self.v_password.set('')
            self.v_wrong_pass.set('')
        elif uname == 'manager':
            self.v_wrong_pass.set('Invalid Password!')
            return None
        else:
            self.user = uname
            self.v_wrong_pass.set('')

        self.hide_from_user()
