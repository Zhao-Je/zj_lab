import logging.handlers

class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            #获取日志器
            cls.logger = logging.getLogger()
            #设置日志级别
            cls.logger.setLevel(logging.INFO)
            #获取处理器 文件-时间分割
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/log.log", when="m", interval=1, backupCount=3, encoding="utf-8")
            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            th.setFormatter(fm)
            cls.logger.addHandler(th)

        return cls.logger