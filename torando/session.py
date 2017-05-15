
USER = {

}

class Session():
    def __init__(self,handler):
        self.handler = handler # 保存当前的请求对象
        if handler.__class__.__name__ == "MainHandler" and (not self.handler.random_str):
            # 这里的判断是为了防止重复获取随机字符串
            self.random_str = self.__get_random_str() # 获得随机字符串
            USER[self.random_str] = {}
        else:
            self.random_str = self.handler.random_str

    def __setitem__(self,key,value):
        # 将用户的信息保存在session中
        # 获得随机字符串
        # 将随机字符串设置为 cookie
        # 修改用户登录状态
        USER[self.random_str][key] = value

    def __getitem__(self,key):
        # 根据传入的随机字符串获得用户信息
        # 获得用户登录状态
        # 获得用户信息
        if self.handler.random_str in USER:
            return USER[self.handler.random_str][key]


    def __get_random_str(self):
        # 产生随机字符串并返回
        import hashlib
        import time

        obj = hashlib.md5() # 获取md5 对象
        obj.update(bytes("%s"%time.time() ,encoding='utf-8')) # 将时间戳进行md5加密
        return obj.hexdigest() # 获得加密后的字符串

