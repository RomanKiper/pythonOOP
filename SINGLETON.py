class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с ДБ: {self.user}, {self.psw}, {self.port}")

    def Close(self):
        print("Закрытие соединения с ДБ")

    def Read(self):
        return "данные из ДБ"

    def Write(self, data):
        print(f"запись в ДБ {data}")

db = DataBase("root", "1234", 80)
db2 = DataBase("root2", "5678", 40)
print(id(db), id(db2))
