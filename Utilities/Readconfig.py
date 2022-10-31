import configparser

config_path = "C:\\Users\\Bhanu\\PycharmProjects\\Mystore\\Configuration\\config1.ini"
config = configparser.RawConfigParser()
config.read(config_path)


class Readconfig:

    @staticmethod
    def geturl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def geturl1():
        url = config.get('common info', 'baseURL1')
        return url

    @staticmethod
    def geturl2():
        url = config.get('common info', 'baseURL2')
        return url

    @staticmethod
    def getregaccount1():
        reg_account = config.get('common info', 'reg1_account')
        return reg_account

    @staticmethod
    def getregaccount2():
        reg_account = config.get('common info', 'reg2_account')
        return reg_account

    @staticmethod
    def getregaccount3():
        reg_account = config.get('common info', 'reg3_account')
        return reg_account

    @staticmethod
    def getregaccount4():
        reg_account = config.get('common info', 'reg4_account')
        return reg_account

    @staticmethod
    def getregtext1():
        text = config.get('common info', 'actualregtext1')
        return text

    @staticmethod
    def getregtext2():
        text = config.get('common info', 'actualregtext2')
        return text

    @staticmethod
    def firstname1():
        first_name = config.get('common info', 'first_name1')
        return first_name

    @staticmethod
    def lastname1():
        lastname = config.get('common info', 'last_name1')
        return lastname

    @staticmethod
    def getpassword1():
        password = config.get('common info', 'password1')
        return password

    @staticmethod
    def getpassword2():
        password = config.get('common info', 'password2')
        return password

    @staticmethod
    def getaddress1():
        address = config.get('common info', 'address1')
        return address

    @staticmethod
    def getcity1():
        city = config.get('common info', 'city1')
        return city

    @staticmethod
    def getpcode1():
        pcode = config.get('common info', 'pcode')
        return pcode

    @staticmethod
    def getmobile1():
        mobile = config.get('common info', 'mobile1')
        return mobile

    @staticmethod
    def getrefer1():
        refer = config.get('common info', 'refer1')
        return refer

    @staticmethod
    def getftext1():
        ftext = config.get('common info', 'ftext')
        return ftext

    @staticmethod
    def addedproducttext1():
        ftext = config.get('common info', 'productadddedtext1')
        return ftext

