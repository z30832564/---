# -*- coding:utf-8 -*-
import wx
from sklearn.externals import joblib
clf1 = joblib.load("train_mode1.m")
clf2 = joblib.load("train_mode2.m")
def leibie(argument):
    switcher = {
        1: "机场车站",
        2: "餐厅",
        4: "宾馆",
        5: "商店",
        6: "住宅",
        7: "银行",
        8: "医院",
        9: "学校",
        10: "公司",
        11: "公园户外"
    }
    return switcher.get(argument, "nothing")
def fenlei(event):
    b = Result.GetValue().encode('utf-8')
    b = b.split()
    c = Result2.GetValue().encode('utf-8')
    c = c.split()
    if len(b)==10:
        a = clf1.predict(b)
        p = leibie(int(a[0]))
        Result1.SetValue(str(p))
    if len(c) == 2:
        d = clf2.predict(c)
        q = leibie(int(d[0]))
        Result1.SetValue(str(q))

app = wx.App()
win = wx.Frame(None, title="社交地点分类应用程序", size = (480, 400))

bkg = wx.Panel(win)
Button = wx.Button(bkg, label="分类", pos=(185,250))
Button.Bind(wx.EVT_BUTTON, fenlei)
Result = wx.TextCtrl(bkg,-1,"",size=(300,-1), pos=(100,100))
Result2 = wx.TextCtrl(bkg,-1,"",size=(300,-1), pos=(100,150))
Result1 = wx.TextCtrl(bkg, -1, "", size=(300, -1), pos=(100, 200))
tezheng = wx.StaticText(bkg, -1,"微博特征：",pos=(40, 105))
jingweidu = wx.StaticText(bkg, -1,"经纬信息：",pos=(40, 155))
jieguo = wx.StaticText(bkg, -1,"分类结果：",pos=(40, 205))
R1 = wx.StaticText(bkg, -1,"输入10维特征，以空格分隔",pos=(105, 128))
R2 = wx.StaticText(bkg, -1,"若有经纬度，先纬度后经度，以空格分隔",pos=(105, 178))
win.Show()
app.MainLoop()