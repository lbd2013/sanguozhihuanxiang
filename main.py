import configparser
import os
import sys
import time
import Log
from AdbDevice import AdbDevice
from Sanhuan import Sanhuan
from Tool import Tool


def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)            #没打包前的py目录

# adb工具目录
adbPath = app_path() + '\\adb_tools\\'
print(adbPath)

# 获取 adb 已连接的设备
def get_drive_list(conf):
	# 连接手机模拟器，重复执行无影响
	os.popen(adbPath + 'adb connect 127.0.0.1:'+conf['adbPort']+' >> NUL') #5555是蓝叠模拟器的端口，不同模拟器不同
	os.popen(adbPath + 'adb logcat -d >> NUL') # 关闭adb 执行日志
	time.sleep(2)
	# 查看當前設備
	devices = os.popen(adbPath + 'adb devices')
	str_list = devices.read().split('\n')
	drive_list = []
	for i in str_list:
		if '\t' in i:
			drive_list.append(i.split('\t')[0])
	return drive_list


# 入口
def main(adbDeviceObj, conf):
	control = conf["control"]
	sanhuanObj = Sanhuan(adbDeviceObj)
	# 0. 领红包
	if control["linghongbao"] == "1":
		sanhuanObj.linghongbao()
		Log.formatPrint("领红包完成\n\n\n")
	# 1.文姬助手一键执行功能
	if control["wenjizhushou"] == "1":
		sanhuanObj.wenjizhushou()
		Log.formatPrint("文姬助手一键执行完成\n\n\n")
	# 2.群雄
	if control["qunxiong"] == "1":
		sanhuanObj.yanwu("qunxiongzhulu", conf['qunxiongSec'])
		Log.formatPrint("群雄逐鹿完成\n\n\n")
	# 3.天下会武
	if control["tianxia"] == "1":
		sanhuanObj.yanwu("tianxiahuiwu", conf['tianxiaSec'])
		Log.formatPrint("天下会武完成\n\n\n")
	# 4.黑龙
	if control["heilong"] == "1":
		sanhuanObj.heilong()
		Log.formatPrint("黑龙完成\n\n\n")
	# 5.扫荡体力
	if control["saodangtili"] == "1":
		sanhuanObj.saodangtili()
		Log.formatPrint("扫荡体力完成\n\n\n")
	# 6.远古剑冢
	if control["yuangujianzhong"] == "1":
		sanhuanObj.yuangujianzhong()
		Log.formatPrint("远古剑冢完成\n\n\n")
	# 7.乾坤幻境
	if control["qiankunhuanjing"] == "1":
		sanhuanObj.qiankunhuanjing()
		Log.formatPrint("乾坤幻境完成\n\n\n")
	# 8.山河领取奖励
	if control["shanhejiangli"] == "1":
		sanhuanObj.shanheJiangli()
		Log.formatPrint("山河领取奖励完成\n\n\n")
	# 9.领取每日任务奖励
	if control["meirirenwu"] == "1":
		sanhuanObj.meirirenwu()
		Log.formatPrint("领取每日任务奖励完成\n\n\n")

	# todo 10.山河自动过图

	Log.formatPrint("所有任务完成")

#读取配置文件参数
def readConf():
	con = configparser.ConfigParser()
	con.read('conf.ini', encoding='utf-8')
	# 开关控制器
	control = adbPort = dict(con.items('control'))
	# 手机模拟器端口
	adbPort = dict(con.items('adbPort'))["val"]
	# 群雄逐鹿时间
	qunxiongSec = dict(con.items('qunxiong'))["val"]
	# 天下会武时间
	tianxiaSec = dict(con.items('tianxia'))["val"]
	return {"adbPort":adbPort,"qunxiongSec":qunxiongSec,"tianxiaSec":tianxiaSec, "control":control}

conf = readConf()

# 获取adb已连接设备
drive_list = get_drive_list(conf)
if len(drive_list) == 0:
	Log.formatPrint("adb 连接失败")
	exit()

#初始化 adb 处理类，包括截图，图片查找，点击等
adbDeviceObj = AdbDevice(drive_list[0], adbPath)
#初始化工具類，包括查找图片跟点击图片
tool = Tool(adbDeviceObj)
#一键长草
main(adbDeviceObj,conf)

input("输入任意键结束")