from readconfigfile import ReadConfigFile
import logging
import os
import logging.handlers


class Log(object):
    def __init__(self):
        self.logger = logging.getLogger("")
        # 获取日志配置文件信息
        logLevel = ReadConfigFile.getlogLevel(self)
        logOutType = ReadConfigFile.getlogOutType(self)
        formatter = logging.Formatter('%(asctime)s  %(filename)s[%(lineno)d]  [%(levelname)s]  %(message)s')  # 设置日志格式
        # 判断文件路径是否存在，不存在则创建一个
        logPath = ReadConfigFile.getlogPath(self)
        if os.path.exists(logPath) and os.path.isdir(logPath):
            pass
        else:
            os.mkdir(logPath)
        logFileName = ReadConfigFile.getlogFileName(self)
        logFilePath = os.path.join(logPath, logFileName)  # 路径拼接
        handler1 = logging.handlers.RotatingFileHandler(filename=logFilePath,  # 文件路径+名字
                                                        maxBytes=ReadConfigFile.getlogMaxFileNum(self),
                                                        # 每个日志文件的最大字节数，单位为M，超过这个大小自动新生成一个日志文件
                                                        backupCount=ReadConfigFile.getlogMaxFileSize(
                                                            self))  # 最大的日志文件个数，超过这个值，最早的日志文件自动被删除

        handler2 = logging.StreamHandler()  # 控制台输出
        self.logger.setLevel(logLevel)  # 日志等级
        handler1.setFormatter(formatter)  # 日志格式
        handler2.setFormatter(formatter)
        # 日志输出设置
        if logOutType == 'all':
            self.logger.addHandler(handler1)
            self.logger.addHandler(handler2)
        elif logOutType == 'file':
            self.logger.addHandler(handler2)
        elif logOutType == 'terminal':
            self.logger.addHandler(handler2)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
