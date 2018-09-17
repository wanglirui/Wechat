from tkinter import *
import time


class RandomName(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.name_list = []
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        #  定义标签栏
        l = Label(self, textvariable=self.timestr, font=("Arial, 35"))
        self.set_name(self._elapsedtime)
        l.pack(side=TOP)

    def update(self):
        # 更新显示内容
        self._elapsedtime = time.time() - self._start
        self.set_name(self._elapsedtime)  # 设置显示内容
        self._timer = self.after(50, self.update)  # 刷新界面

    def set_name(self, elap):
        # 随机产生姓名
        cur = int(elap * 100 % 30)
        name_list = ['王生安', '李鑫灏', '薛佛世', '蔡壮保', '钱勤堃', '潘恩依', '陈国柏', '魏皑虎',
                     '周卓浩', '汤辟邦', '张顺谷', '张悌斯', '张灶冲', '易江维', '孙来笙', '饶展林',
                     '岳列洋', '时党舒', '周迟蒲', '廉梦容', '张淮森', '夏劲釜', '王好隐', '刘昼星',
                     '池荣弈', '邹包幼', '王施峪', '武慎萌', '范千皋', '潘佩焱']
        self.timestr.set(name_list[cur])

    def Start(self):
        # 开始
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self.update()
            self._running = True

    def Stop(self):
        # 暂停
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self.set_name(self._elapsedtime)
            self._running = False

    def name_label(self):
        # 显示窗口
        self.pack(side=TOP)
        Button(self, text='start', command=self.Start, width=10, height=2).pack(side=LEFT)
        Button(self, text='stop', command=self.Stop, width=10, height=2).pack(side=LEFT)


if __name__ == '__main__':
    root = Tk()
    root.title("Aloe")
    root.geometry('600x600')
    sw = RandomName(root)
    sw.name_label()
    root.mainloop()