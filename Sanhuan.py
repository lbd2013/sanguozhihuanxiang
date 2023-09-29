import os
import time
import Log
from datetime import datetime
from Tool import Tool

class Sanhuan():
	def __init__(self, adbDeviceObj):
		self.adbDeviceObj = adbDeviceObj
		self.tool = Tool(adbDeviceObj)

	### 领取红包
	def linghongbao(self):
		self.goToIndex(0, 10)

		# 进入(军团)
		Log.formatPrint("进入(军团)")
		self.tool.findAndClickImg('images/hongbao/1.png', 2)

		# 进入(红包)页
		Log.formatPrint("进入(红包)页")
		self.tool.findAndClickImg('images/hongbao/2.png', 2)

		# 一键领取红包
		Log.formatPrint("一键领取红包")
		rs = self.tool.findAndClickImg('images/hongbao/3.png', 2)
		if rs == False:
			Log.formatPrint("没有可领取的红包")
		else:
			while True:
				Log.formatPrint("检查一键领取红包是否已结束")
				match_result = self.tool.findImg('images/hongbao/4.png')
				if match_result == None:
					Log.formatPrint("未结束，等待")
					time.sleep(1) #等待
				else:
					Log.formatPrint("一键领取红包结束")
					break
		Log.formatPrint("完成")

	# 山河领取奖励
	def shanheJiangli(self):
		self.goToIndex(0, 10)

		# 进入(山河)
		Log.formatPrint("进入(山河)")
		self.tool.findAndClickImg('images/shanhe/1.png', 2)

		# 打开领取奖励界面
		Log.formatPrint("打开(领取奖励)界面")
		while True:
			match_result = self.tool.findImg('images/shanhe/2.png')
			if match_result != None:
				Log.formatPrint("已处于山河界面，进入（领取奖励界面）")
				self.adbDeviceObj.click((200,980))
				time.sleep(2) #等待

				Log.formatPrint("已进入（领取奖励界面），点击（领取按钮）")
				rs = self.tool.findAndClickImg('images/shanhe/3.png', 2)
				if rs == True:
					Log.formatPrint("山河奖励领取完成")
					break
			else:
				Log.formatPrint("还没进入山河界面，等待...")
				time.sleep(1) #等待
		Log.formatPrint("完成")

	#乾坤幻境领取奖励
	def qiankunhuanjing(self):
		self.goToIndex(0, 10)

		# 进入(征战)
		Log.formatPrint("进入(征战)")
		self.tool.findAndClickImg('images/qiankunhuanjing/1.png', 2)

		# 进入(乾坤幻境)
		Log.formatPrint("进入(乾坤幻境)")
		while True:
			match_result = self.tool.findImg('images/qiankunhuanjing/2.png')
			if match_result != None:
				Log.formatPrint("找到（乾坤幻境），进入")
				targetX = match_result['rectangle'][0][0]
				targetY = match_result['rectangle'][0][1]
				self.adbDeviceObj.click((targetX,targetY))
				time.sleep(2) #等待
				break
			else:
				Log.formatPrint("找不到乾坤幻境，往左拖动屏幕")
				self.adbDeviceObj.swipe("700", "200", "550", "300")

		#进入聚灵台
		Log.formatPrint("进入(聚灵台)")
		self.tool.findAndClickImg('images/qiankunhuanjing/3.png', 2)

		# 点击领取
		Log.formatPrint("点击(领取)按钮")
		rs = self.tool.findAndClickImg('images/qiankunhuanjing/4.png', 2)
		if rs:
			#跳过（恭喜获得）遮罩
			Log.formatPrint("跳过（恭喜获得）遮罩")
			self.tool.findAndClickImg('images/qiankunhuanjing/6.png', 2)

		# 点击快速收益
		Log.formatPrint("点击(快速收益)按钮")
		self.tool.findAndClickImg('images/qiankunhuanjing/5.png', 2)

		#点击免费挂机
		Log.formatPrint("点击(免费挂机)按钮")
		rs = self.tool.findAndClickImg('images/qiankunhuanjing/7.png', 2)
		if rs:
			#跳过（恭喜获得）遮罩
			Log.formatPrint("跳过（恭喜获得）遮罩")
			self.tool.findAndClickImg('images/qiankunhuanjing/8.png', 2)
		else:
			Log.formatPrint("已经领取过（免费挂机），结束")

		Log.formatPrint("完成")

	### 远古剑冢
	def yuangujianzhong(self):
		self.goToIndex(0, 10)

		# 进入(征战)
		Log.formatPrint("进入(征战)")
		self.tool.findAndClickImg('images/yuangujianzhong/1.png', 2)

		# 进入(征战)
		Log.formatPrint("进入(远古剑冢)")
		while True:
			match_result = self.tool.findImg('images/yuangujianzhong/2.png')
			if match_result != None:
				Log.formatPrint("找到远古剑冢，进入")
				targetX = match_result['rectangle'][0][0]
				targetY = match_result['rectangle'][0][1]
				self.adbDeviceObj.click((targetX,targetY))
				time.sleep(2) #等待
				break
			else:
				Log.formatPrint("找不到远古剑冢，往左拖动屏幕")
				self.adbDeviceObj.swipe("700", "200", "550", "300")

		# 自动打特殊士兵
		self.yuangujianzhongDetail("teshu")

		# 自动打寻宝士兵
		self.yuangujianzhongDetail("xunbao")

		Log.formatPrint("完成")

	###远古剑冢打怪逻辑
	# @param type 用来标记是打寻宝怪还是特殊怪
	def yuangujianzhongDetail(self, type):
		if type == "xunbao":
			name = "寻宝"
			findFile = "3.png"
			targetFile = "4.png"
		else:
			name = "特殊"
			findFile = "5.png"
			targetFile = "6.png"

		# 自动打寻宝士兵
		while True:
			Log.formatPrint("检查有没有（"+name+"士兵）")
			targetImg = 'images/yuangujianzhong/'+findFile
			match_result = self.tool.findImg(targetImg)
			if match_result == None:
				Log.formatPrint("找不到"+name+"士兵，结束")
				break
			else:
				Log.formatPrint("找到（"+name+"士兵），跳转到对应位置")
				targetX = match_result['rectangle'][0][0]
				targetY = match_result['rectangle'][0][1]
				self.adbDeviceObj.click((targetX,targetY))
				time.sleep(2) #等待

			Log.formatPrint("进入布阵页")
			targetImg = 'images/yuangujianzhong/'+targetFile
			self.tool.findAndClickImg(targetImg, 2)

			Log.formatPrint("开始战斗")
			targetImg = 'images/yuangujianzhong/7.png'
			self.tool.findAndClickImg(targetImg, 2)

			Log.formatPrint("点击跳过战斗")
			while True:
				# 光亮场景的跳过按钮
				targetImg = 'images/yuangujianzhong/8.png'
				rs = self.tool.findAndClickImg(targetImg, 2)
				if rs:
					#等待战斗胜利的遮罩层出现
					while True:
						targetImg = 'images/yuangujianzhong/10.png'
						rs = self.tool.findAndClickImg(targetImg, 2)
						if rs == False:
							#等待战斗胜利的遮罩层出现
							Log.formatPrint("等待战斗胜利的遮罩层出现..")
						else:
							break

						# 处理特殊情况：有时候战斗结束后不出现战斗胜利的遮罩，直接跳到远古剑冢的主页，这种也是战斗结束
						match_result = self.tool.findImg('images/yuangujianzhong/2.png')
						if match_result != None:
							break

						#等待
						time.sleep(1)
					#结束
					break

	# 扫荡体力
	def saodangtili(self):
		self.goToIndex(0, 10)

		#进入神木页面
		Log.formatPrint("进入(神木新篇章)")
		self.tool.findAndClickImg('images/saodangtili/1.png', 2)

		#扫荡体力
		Log.formatPrint("点击(扫荡体力)")
		self.tool.findAndClickImg('images/saodangtili/2.png', 2)

		Log.formatPrint("完成")

	# 组队征伐 - 黑龙幻境
	def heilong(self):
		self.goToIndex(0, 10)
		# 进入(征战)
		Log.formatPrint("进入(征战)")
		self.tool.findAndClickImg('images/zhengzhan/1.png', 2)

		# 进入(征战)
		Log.formatPrint("进入(组队讨伐)")
		while True:
			match_result = self.tool.findImg('images/zhengzhan/2.png')
			if match_result != None:
				Log.formatPrint("点击进入组队讨伐")
				targetX = match_result['rectangle'][0][0]
				targetY = match_result['rectangle'][0][1]
				self.adbDeviceObj.click((targetX,targetY))
				time.sleep(2) #等待
				break
			else:
				Log.formatPrint("找不到组队征伐，往左拖动屏幕")
				self.adbDeviceObj.swipe("700", "200", "550", "200")
				time.sleep(3) #等待

		# 进入(黑龙幻境)
		Log.formatPrint("进入(黑龙幻境)")
		rs = self.tool.findAndClickImg('images/zhengzhan/3.png', 2)
		if rs == False:
			Log.formatPrint("进入黑龙幻境失败")
			return False

		# 进入(创建队伍_1)
		Log.formatPrint("点击(创建队伍_1)")
		self.tool.findAndClickImg('images/zhengzhan/4.png', 2)
		if rs == False:
			Log.formatPrint("点击(创建队伍_1)失败")
			return False

		# 队伍权限设置为仅邀请
		Log.formatPrint("检查(队伍权限)设置")
		rs = self.tool.findAndClickImg('images/zhengzhan/6.png', 2)
		if rs:
			Log.formatPrint("(队伍权限)设置为所有人，修改为仅邀请")
		else:
			Log.formatPrint("(队伍权限)设置为仅邀请，无需修改")
		time.sleep(2) #等待

		# 点击(创建队伍_2)
		Log.formatPrint("点击(创建队伍_2)")
		self.tool.findAndClickImg('images/zhengzhan/5.png', 2)

		# 点击(开始战斗)
		while True:
			Log.formatPrint("检查是否精力不足")
			match_result_1 = self.tool.findImg('images/zhengzhan/10.png')
			match_result_2 = self.tool.findImg('images/zhengzhan/11.png')
			match_result_3 = self.tool.findImg('images/zhengzhan/12.png')
			if match_result_1 != None or match_result_2 != None or match_result_3 != None:
				Log.formatPrint("精力不足,黑龙完成")
				break
			else:
				Log.formatPrint("精力足够或仍处于战斗中")
				time.sleep(2)

			#点击开始战斗
			Log.formatPrint("点击(开始战斗)")
			self.tool.findAndClickImg('images/zhengzhan/8.png', 2)

			#点击提示不满三人的确定
			Log.formatPrint("点击(点击提示不满三人的确定)")
			self.tool.findAndClickImg('images/zhengzhan/9.png', 5, 3)


	### 群雄逐鹿+天下会武
	# @param type 标志是群雄还是会武
	def yanwu(self, type, doTime):
		if type == "qunxiongzhulu":
			name = "群雄逐鹿"
			typeFile = "2.png"
			startFile = "8.png"
			passFile = "6.png"
		else:
			name = "天下会武"
			typeFile = "3.png"
			startFile = "9.png"
			passFile = "7.png"

		self.goToIndex(0, 10)
		# 进入(演武)
		Log.formatPrint("进入(演武页面)")
		self.tool.findAndClickImg('images/yanwu/1.png', 2)

		# 进入群雄逐鹿、天下会武
		Log.formatPrint("进入("+ name +")")
		targetImg = 'images/yanwu/'+typeFile
		self.tool.findAndClickImg(targetImg, 2)

		# 处理群雄逐鹿变更为赛区问题
		Log.formatPrint("检查变更为赛区遮罩")
		rs = self.tool.findAndClickImg('images/yanwu/10.png', 2)
		if rs == False:
			Log.formatPrint("不存在变更为赛区遮罩")

		# 左上角点几下，处理战绩排名遮罩问题
		Log.formatPrint("检查积分变动遮罩")
		rs = self.tool.findAndClickImg('images/yanwu/4.png', 2)
		if rs == False:
			Log.formatPrint("不存在积分变动遮罩")

		# 勾选(跳过战斗)
		Log.formatPrint("勾选(跳过战斗)按钮")
		rs = self.tool.findAndClickImg('images/yanwu/6.png', 2)
		if rs == False:
			Log.formatPrint("原本已勾选")

		# 开始匹配
		Log.formatPrint("开始匹配，持续时间: "+doTime+" 秒")
		targetImg = 'images/yanwu/'+startFile
		screenImgName = "tmp.png"
		self.adbDeviceObj.screen_cap(screenImgName)
		match_result = self.adbDeviceObj.search_location(screenImgName, targetImg)
		targetX = int(match_result['rectangle'][0][0] + (match_result['rectangle'][3][0] - match_result['rectangle'][0][0]) / 2)
		targetY = int(match_result['rectangle'][0][1] + (match_result['rectangle'][3][1] - match_result['rectangle'][0][1]) / 2)
		startTime = datetime.now()
		while True:
			#连点
			if (datetime.now() - startTime).seconds > int(doTime):
				Log.formatPrint(name+"执行完成")
				break
			self.adbDeviceObj.click((targetX,targetY))

	#领取每日任务奖励
	def meirirenwu(self):
		self.goToIndex(0, 10)
		# 打开每日任务
		Log.formatPrint("打开每日任务")
		self.tool.findAndClickImg('images/meirirenwu/1.png', 2)

		# 点击全部领取按钮
		Log.formatPrint("查看是否有(全部领取)按钮")
		self.tool.findAndClickImg('images/meirirenwu/2.png', 2)

	#文姬一键助手
	def wenjizhushou(self):
		self.goToIndex(0, 10)
		# 打开文姬助手
		Log.formatPrint("打开文姬助手")
		self.tool.findAndClickImg('images/wenjizhushou/wen_ji_zhu_shou.png', 2)

		#点击一键执行
		Log.formatPrint("点击一键执行")
		self.tool.findAndClickImg('images/wenjizhushou/yi_jian.png', 2)

		while True:
			time.sleep(1)
			#检查是否出现完成按钮
			Log.formatPrint("检查是否出现完成按钮")
			match_result = self.tool.findImg('images/wenjizhushou/finish_1.png')
			if match_result != None:
				Log.formatPrint("出现完成按钮，一键执行完成")
				targetX = int(match_result['rectangle'][0][0] + (match_result['rectangle'][3][0] - match_result['rectangle'][0][0]) / 2)
				targetY = int(match_result['rectangle'][0][1] + (match_result['rectangle'][3][1] - match_result['rectangle'][0][1]) / 2)
				self.adbDeviceObj.click((targetX,targetY))
				break

			#检查是否出现【当前无可快速完成内容】提示
			Log.formatPrint("检查是否出现(当前无可快速完成内容)提示")
			match_result = self.tool.findImg('images/wenjizhushou/finish_2.png')
			if match_result != None:
				Log.formatPrint("出现(当前无可快速完成内容)提示，一键执行完成")
				targetX = int(match_result['rectangle'][0][0] + (match_result['rectangle'][3][0] - match_result['rectangle'][0][0]) / 2)
				targetY = int(match_result['rectangle'][0][1] + (match_result['rectangle'][3][1] - match_result['rectangle'][0][1]) / 2)
				self.adbDeviceObj.click((targetX,targetY))
				break

			Log.formatPrint("一键执行未完成，等待1s...")



	# 回到首页，为减少操作错误，所有操作都以首页为起点
	def goToIndex(self, tryNum, maxTryNum):
		tryNum += 1

		# 超过次数还没回到首页, 退出
		if tryNum > maxTryNum:
			Log.formatPrint("超过次数还没回到首页, 退出")
			return False

		#判断是否已经在首页
		match_result = self.tool.findImg('images/wenjizhushou/wen_ji_zhu_shou.png')
		if match_result == None:
			Log.formatPrint("找不到文姬助手按钮，不是首页，开始返回首页")
		else:
			Log.formatPrint("找到文姬助手按钮，是首页")
			return True

		# images 中的back文件夹中，放了所有的后退按钮
		# 逐个后退按钮找一下，退到首页
		filePath = 'images/back/'
		fileList = os.listdir(filePath)
		notFind  = True
		for fileName in fileList:
			targetImg = filePath + fileName
			rs = self.tool.findAndClickImg(targetImg, 2)
			if rs != False:
				notFind = False
				Log.formatPrint("找到后退按钮, 点击")
				return self.goToIndex(tryNum, maxTryNum) # 递归检查

		#一个按钮图片都找不到，有可能被遮罩，随便点一个地方
		if notFind:
			Log.formatPrint("一个按钮图片都找不到，被遮罩，随便点一个地方")
			self.adbDeviceObj.click((1,1))
			return self.goToIndex(tryNum, maxTryNum) # 递归检查
