import aircv as ac
import os

#Adb 操作类
class AdbDevice:
    def __init__(self, id, adbPath):
        self.id = id
        self.adbPath = adbPath

    # 搜索返回图片位置
    def search_location(self, imsrc, imsch, threshold=0.95):
        imsrc = ac.imread(imsrc)
        imsch = ac.imread(imsch)
        result = ac.find_template(imsrc, imsch, threshold=threshold)
        if not result:
            return result
        return result

    # 返回
    def back(self):
        os.system(self.adbPath + 'adb -s ' + self.id + ' shell input keyevent 4 >> NUL')

    # 滑动
    def swipe(self, startX, startY, endX, endY):
        os.system(
            self.adbPath + 'adb -s ' + self.id + ' shell input swipe ' + startX + ' ' + startY + ' ' + endX + ' ' + endY + ' 200 >> NUL')

    # 截图
    def screen_cap(self, name):
        os.system(self.adbPath + 'adb -s ' + self.id + ' shell screencap -p /sdcard/' + name + " >> NUL")
        os.system(self.adbPath + 'adb -s ' + self.id + '  pull /sdcard/' + name + " >> NUL")

    def pic_in_screen(self, search_img, donotclick=False):
        if not donotclick:
            self.screen_cap()
        result = self.search_location(self.id + '.png', search_img)
        if not result:
            return False
        return result['result']

    # 点击
    def click(self, pos):
        os.system(
            self.adbPath + 'adb -s ' + self.id + ' shell input  tap ' + str(pos[0]) + ' ' + str(pos[1]) + " >> NUL")

    # 点击图片
    def click_pic(self, path, donotclick=False):
        if not donotclick:
            self.screen_cap()
        result = self.search_location(self.id + '.png', path)
        if not result:
            return False
        self.click(result['result'])
        return True
