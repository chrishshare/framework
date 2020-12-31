# -*- coding:utf8 -*-

import win32gui
import win32con
import operator


def upload_file(file_path, browser='chrome'):
    # 一级窗口
    top = None
    if operator.eq(browser, 'chrome') or operator.eq(browser, 'edger'):
        top = win32gui.FindWindow("#32770", "打开")
    elif operator.eq(browser, 'ie'):
        top = win32gui.FindWindow("#32770", "选择要加载的文件")
    elif operator.eq(browser, 'firefox'):
        top = win32gui.FindWindow("#32770", "文件上传")

    # 二级窗口，4个参数：父级；从父级的第几个儿子开始检索，0表示第一个；自身类名；文本内容，没有则None
    combo_box_ex32 = win32gui.FindWindowEx(top, 0, "ComboBoxEx32", None)

    # 3级窗口
    combo_box = win32gui.FindWindowEx(combo_box_ex32, 0, "ComboBox", None)

    # 4级窗口
    edit = win32gui.FindWindowEx(combo_box, 0, "Edit", None)

    # 二级打开按钮
    button = win32gui.FindWindowEx(top, 0, "Button", "打开(&O)")

    # 输入文件地址
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)

    # 点击打开按钮 提交文件
    win32gui.SendMessage(top, win32con.WM_COMMAND, 1, button)


upload_file("C:\\1\\nihao.7z", 'firefox')
