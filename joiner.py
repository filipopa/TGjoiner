import gui
import time
from telethon.sync import TelegramClient
import sys
from PyQt5 import QtWidgets
from telethon.tl.functions.channels import JoinChannelRequest

groups_path = ""
logoutput_path = ""
Groups = []
phone = ""
api_id = ""
hash_id = ""
count=0
class ExampleApp(QtWidgets.QMainWindow, gui.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле final.py
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.start_func)
        self.filechoose2.clicked.connect(self.logs_path_func)
        self.filechoose1.clicked.connect(self.groups_path_func)
        self.load.clicked.connect(self.load_func)

    def groups_path_func(self):
        global groups_path
        groups_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Кому капец?', None, 'Че зыришь?(*.txt;*.json)')[0]
        self.directory1.setText(groups_path)

    def logs_path_func(self):
        global logoutput_path
        logoutput_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.directory2.setText(logoutput_path)
        logoutput_path = f'{logoutput_path}/logs-' + time.asctime().replace(' ', '-').replace(':', '-').lower() + '.txt'

    def load_func(self):
        global Groups
        logs = open(logoutput_path, 'w')
        try:
            datasetup = open(str(sys.argv[0])[:-9] + 'config.txt', 'r')
            global phone, api_id, hash_id
            rawdata = datasetup.read().split()
            api_id = int(rawdata[0])
            hash_id = rawdata[1]
            phone = rawdata[2]
            datasetup.close()
        except FileNotFoundError:
            status = '[FATAL ERROR] No file config.txt found in directory' + str(sys.argv[0])[:-9] + 'config.txt ' + time.asctime().replace(' ', '-').replace(':', '-').lower()
            logs.write(status + '\n')
            status = time.asctime().replace(' ', '-').replace(':', '-').lower() + f'-run-setup.py-first'
            logs.write(status + '\n')
            sys.exit()
        status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-opening-groups-file'
        logs.write(status + '\n')
        f = open(groups_path, 'r')
        Groups = f.read().split()
        f.close()
        status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-load-complete'
        logs.write(status + '\n')
        logs.close()

    def start_func(self):
        logs = open(logoutput_path, 'a')
        global count
        with TelegramClient(phone, api_id, hash_id) as client:
            for a in Groups:
                count+=1
                status = time.asctime().replace(' ', '-').replace(':','-').lower() + f'-trying-to-join-{a}'
                print(status)
                logs.write(status + '\n')
                try:
                    client(JoinChannelRequest(a))
                    status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-success'
                    logs.write(status + '\n')
                    print(status)
                except Exception as e:
                    status = "[!] Error:" + str(e)
                    logs.write(status + '\n')
                    print(status)
                    status = f"[!] Stopped while trying to join {a}"
                    print(status)
                    logs.write(status + '\n')
                    if count % 5 == 0:
                        status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-waiting-500-seconds'
                        print(status)
                        logs.write(status + '\n')
                        time.sleep(500)
                    continue
                if count%5==0:
                    status = time.asctime().replace(' ', '-').replace(':','-').lower() + '-waiting-500-seconds'
                    print(status)
                    logs.write(status + '\n')
                    time.sleep(500)
        status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-im-done'
        logs.write(status + '\n')
        logs.close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()