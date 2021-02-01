'''
subprocess.call()
os.system(命令行命令):不能收集返回值，只是运行命令 启动服务就可以了
'''

import os
os.system('adb logcat')