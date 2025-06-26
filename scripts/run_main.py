import time
import unittest

from tools.HTMLTestRunner import HTMLTestRunner

#定义测试套件
suite = unittest.defaultTestLoader.discover("./", pattern="test*.py")
#定义报告存放路径
report_dir = "../result/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))
with open(report_dir, "wb") as f:
    HTMLTestRunner(stream=f, verbosity=2, title="去哪儿网项目自动化测试报告",description="操作系统win10").run(suite)