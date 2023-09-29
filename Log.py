import logging

# 设置日志级别
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

### 打印日志
# @param str 内容
def formatPrint(str):
    logging.info(str)