import logging
import os
from configparser import ConfigParser
import logging.handlers
class ReadConfigFile(object):
    cp = ConfigParser()
    cp.read("config.ini")
    logLevel =cp.get('LogParam', 'logLevel')
    logOutType=cp.get('LogParam', 'logOutType')
    logPath = cp.get('LogParam', 'logPath')
    logFileName= cp.get('LogParam', 'logFileName')
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



class Log(object):
    def __init__(self):
        self.logger=logging.getLogger("")
        logLevel=ReadConfigFile.getlogLevel(self)
        logOutType=ReadConfigFile.getlogOutType(self)
        formatter = logging.Formatter('%(asctime)s  %(filename)s[%(lineno)d]  [%(levelname)s]  %(message)s')
        logPath=ReadConfigFile.getlogPath(self)
        if os.path.exists(logPath) and os.path.isdir(logPath):
            pass
        else:
            os.mkdir(logPath)
        logFileName=ReadConfigFile.getlogFileName(self)
        logFilePath=os.path.join(logPath,logFileName)  # 路径拼接
        handler1=logging.handlers.RotatingFileHandler(filename=logFilePath,  # 文件路径+名字
                                                      maxBytes=ReadConfigFile.getlogMaxFileNum(self),  # 每个日志文件的最大字节数，单位为M，超过这个大小自动新生成一个日志文件
                                                      backupCount=ReadConfigFile.getlogMaxFileSize(self))  # 最大的日志文件个数，超过这个值，最早的日志文件自动被删除

        handler2=logging.StreamHandler()
        self.logger.setLevel(logLevel)
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        if logOutType=='all':
            self.logger.addHandler(handler1)
            self.logger.addHandler(handler2)
        elif logOutType=='file':
            self.logger.addHandler(handler2)
        elif logOutType=='terminal':
            self.logger.addHandler(handler2)


    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)




logger=Log()
logger.info('Start print log')
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
