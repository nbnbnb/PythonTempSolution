import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

# 把 WindowsFormApp 的生成输出目录设置到当前文件夹中
# 一定要将源代码格式设置为 UTF8+BOM，否则无法输入中文

# 需要将控件的 Modify 设置为 Pubulic
# 这样才能在 Python 中进行访问
clr.AddReferenceToFile('WindowsFormApp.exe') 
#clr.AddReference('WindowsFormApp')

from System import *
from System.Drawing import *
from System.Windows.Forms import *
from WindowsFormApp import MainForm


class TemplateMainForm(MainForm): 
    def __init__(self):
        # Create child controls and initialize form
        # self.buttonAddToList.Click+= self.addTime
        self.buttonAddToList.Click+= lambda sender,event : self.listBoxTimes.Items.Add(DateTime.Now.ToString())
        self.listBoxTimes.Click+=self.showItem
    def addTime(self,target,event):
        self.listBoxTimes.Items.Add(DateTime.Now.ToString())
        self.log('addTime')

    def showItem(self,target,event):
        if self.listBoxTimes.SelectedItem:
            MessageBox.Show(self.listBoxTimes.SelectedItem.ToString())
            self.log('showItem')

    def log(self,message):
        # TODO：两种方式在 VS 调试器中都无法输出
        Console.WriteLine(message)
        print(message)



Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = TemplateMainForm()
Application.Run(form)
