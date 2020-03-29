import json
import tkinter as tk
from tkinter import filedialog
from json import JSONDecodeError
from tkinter import messagebox
import datetime
import os.path as p
import os
import subprocess
import sys

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title('Flash')
        self.sourcefileName = tk.StringVar()
        self.resultFileName = tk.StringVar()
        self.mainframe = tk.Frame(self)
        self.mainframe.grid(row=0, column=0)
        self.frm_selectFile = tk.LabelFrame(self.mainframe, text='Select Your File')
        self.frm_selectFile.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.frm_selectFile.columnconfigure(0, weight=1)
        self.btn_browser = tk.Button(self.frm_selectFile, text='Choose File', command=self.callback_choose_file)
        tk.Label(self.frm_selectFile, text='Please Select a File: ').grid(row=0, column=0, sticky=tk.NW)
        self.btn_browser.grid(row=0, column=1, sticky=tk.NW)
        tk.Label(self.frm_selectFile, text='File Selected: ').grid(row=1, column=0, sticky=tk.NW)

        tk.Label(self.frm_selectFile, textvariable=self.sourcefileName).grid(row=1, column=1)

        self.frm_ParseFile = tk.LabelFrame(self.mainframe, text='Parse File')
        self.frm_ParseFile.columnconfigure(0, weight=1)
        self.frm_ParseFile.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.btn_parseLogs = tk.Button(self.frm_ParseFile, text='Get Unique Logs', command=self.cmd_parse_file)
        self.btn_parseLogs.grid(row=0, column=0, sticky=tk.NW)
        tk.Label(self.frm_ParseFile, text='Result File Path: ').grid(row=1, column=0, sticky=tk.NW)
        tk.Label(self.frm_ParseFile, textvariable=self.resultFileName).grid(row=1, column=1, sticky=tk.NW)
        self.btn_show_file = tk.Button(self.frm_ParseFile, text= 'View File', command=self.cmd_view_file)
        self.btn_show_file.grid(row=2, column=0, sticky=tk.NW)

    def callback_choose_file(self):
        self.sourcefileName.set(filedialog.askopenfilename())

    def cmd_parse_file(self):
        data_dic = {}
        if self.sourcefileName.get():
            with open(self.sourcefileName.get(), 'r') as fp:
                for line_num, line in enumerate(fp):
                    try:
                        js = json.loads(line)
                        error_name = js.get('@mt', None)
                        if error_name not in data_dic and error_name:
                            data_dic[error_name] = js
                    except JSONDecodeError as e:
                        messagebox.showwarning('Warning!!!!',
                                               'Invalid Json at line No {}. This line will be skipped from the filtering'.format(line_num))
            # with open('/Users/mandeepdhiman/Downloads/result.clef','w') as fp2:
            #     fp2.write(json.dumps(data_dic))
            home = p.expanduser("~")
            proj_path = p.join(home, 'Flash_parser')
            if not p.exists(proj_path):
                os.mkdir(proj_path)
            suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")+'.clef'
            result_filename = "_".join(['result', suffix])
            result_file =p.join(proj_path, result_filename)
            with open(result_file, 'w') as log:
                for value in data_dic.values():
                    log.write('{}\n'.format(value))
            messagebox.showinfo('Finished!!', 'Parsing has been Completed. File Name:{}'.format(result_filename))
            self.resultFileName.set(result_file)
        else:
            messagebox.showerror('Source Not Found!', 'Please select a file.')

    def cmd_view_file(self):
        if self.resultFileName.get():
            if sys.platform == 'win32':
                subprocess.Popen('explorer"{}"'.format(p.dirname(self.resultFileName)))
            else:
                subprocess.call(["open", p.dirname(self.resultFileName.get())])