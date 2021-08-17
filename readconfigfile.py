# 读取配置文件信息
from configparser import ConfigParser
class ReadConfigFile(object):
    cp = ConfigParser()
    cp.read("config.ini")
    logLevel = cp.get('LogParam', 'logLevel')
    logOutType = cp.get('LogParam', 'logOutType')
    logPath = cp.get('LogParam', 'logPath')
    logFileName = cp.get('LogParam', 'logFileName')
    logMaxFileNum = cp.get('LogParam', 'logMaxFileNum')
    logMaxFileSize = cp.get('LogParam', 'logMaxFileSize')

    def getlogLevel(self):
        return ReadConfigFile.logLevel

    def getlogOutType(self):
        return ReadConfigFile.logOutType

    def getlogPath(self):
        return ReadConfigFile.logPath

    def getlogFileName(self):
        return ReadConfigFile.logFileName

    def getlogMaxFileNum(self):
        return int(ReadConfigFile.logMaxFileNum)

    def getlogMaxFileSize(self):
        return int(ReadConfigFile.logMaxFileSize)
