import time

# 工具类
class Tool():
    def __init__(self, adbDeviceObj):
        self.adbDeviceObj = adbDeviceObj

    ### 查找图片
    # @param targetImg String 要查找的图片路径
    # @return None 找不到图片
    # @return 图标坐标
    #
    def findImg(self, targetImg):
        screenImgName = "tmp.png"
        self.adbDeviceObj.screen_cap(screenImgName)
        match_result = self.adbDeviceObj.search_location(screenImgName, targetImg)
        return match_result

    ### 查找图片并点击
    # @param targetImg String 要查找的图片路径
    # @param sleepNum  Int    点击完后等待的时间
    # @param sepecialPos  Int    特殊坐标，默认传0点击左上角，传3代表点击
    # @return False 找不到图片
    # @return True 找到并点击完成
    #
    def findAndClickImg(self, targetImg, sleepNum, sepecialPos=0):
        match_result = self.findImg(targetImg)
        if match_result == None:
            return False
        targetX = match_result['rectangle'][sepecialPos][0]
        targetY = match_result['rectangle'][sepecialPos][1]
        self.adbDeviceObj.click((targetX, targetY))
        if sleepNum > 0:
            time.sleep(sleepNum)  # 等待
        return True