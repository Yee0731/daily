import logging
import os
import logging.handlers


class Log(object):
    def __init__(self, log_path, log_file_name, log_out_type='all',
                 log_level='INFO', log_max_file_size=10240,log_max_file_num=30):
        # 内部变量前加两下划线
        self.__logger = logging.getLogger("")
        self.__log_max_file_size = int(log_max_file_size) * 1024
        self.__log_max_file_num = int(log_max_file_num)
        self.__log_out_type = log_out_type

        formatter = logging.Formatter('%(asctime)s  %(filename)s[%(lineno)d]  [%(levelname)s]  %(message)s')  # 设置日志格式
        # 判断文件路径是否存在，不存在则创建一个
        if os.path.exists(log_path) and os.path.isdir(log_path):
            pass
        else:
            os.mkdir(log_path)

        self.__log_path = os.path.join(log_path, log_file_name)  # 路径拼接
        log_file_handler = logging.handlers.RotatingFileHandler(filename=self.__log_path  # 文件路径+名字
                                                                , maxBytes=int(log_max_file_size)
                                                                # 每个日志文件的最大字节数，单位为M，超过这个大小自动新生成一个日志文件
                                                                , backupCount=int(log_max_file_num))  # 最大的日志文件个数，超过这个值，最早的日志文件自动被删除

        log_stream_handler = logging.StreamHandler()  # 控制台输出
        self.__logger.setLevel(log_level.upper())  # 日志等级
        log_file_handler.setFormatter(formatter)  # 日志格式
        log_stream_handler.setFormatter(formatter)
        # 日志输出设置
        if log_out_type.lower() == 'all':
            self.__logger.addHandler(log_file_handler)
            self.__logger.addHandler(log_stream_handler)
        elif log_out_type.lower() == 'file':
            self.__logger.addHandler(log_file_handler)
        elif log_out_type.lower() == 'terminal':
            self.__logger.addHandler(log_stream_handler)

    def info(self, message):
        self.__logger.info(message)

    def debug(self, message):
        self.__logger.debug(message)

    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)

