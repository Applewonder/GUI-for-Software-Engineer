# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
import difflib
import pandas as pd
import csv
import subprocess
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox
from PyQt5.QtCore import QUrl, QFileInfo


class MainDialog(QMainWindow):

    count_file = 1

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tips.triggered.connect(self.show_child)
        self.ui.Equal.clicked.connect(self.connect_inform)
        self.ui.Inequal.clicked.connect(self.connect_inform)
        self.ui.Save.clicked.connect(self.connect_inform)

    def connect_inform(self):
        child_window = Inform_unimport()

    def show_child(self):
        if self.find_folder() == 0:
            child_window = Success()
            os.system("./auto_judging")
            self.load_file()
            #hello, this is my gui!
        else:
            child_window = Failure()

    def load_file(self):
        self.ui.Equal.clicked.disconnect()
        self.ui.Inequal.clicked.disconnect()
        self.ui.Save.clicked.disconnect()
        self.ui.Equal.clicked.connect(self.equal)
        self.ui.Inequal.clicked.connect(self.inequal)
        self.ui.Save.clicked.connect(self.save_output)
        self.show_diff()

    def compare(self, file_1, file_2):
        fd_1 = open("../" + file_1, "r")
        text_1 = fd_1.read().splitlines()
        fd_2 = open("../" + file_2, "r")
        text_2 = fd_2.read().splitlines()
        diff = difflib.HtmlDiff()
        result = diff.make_file(text_1, text_2)
        with open("./diff.html", "w") as file:
            file.write(result)

    def show_diff(self):
        with open("../output/equal.csv", 'r') as f:
            reader = csv.reader(f)
            result = list(reader)
            if self.count_file >= len(result):
                msg_box = QMessageBox()
                msg_box.setText("恭喜，已完成所有判断，结果自动保存在../output文件夹内")
                msg_box.exec_()
                exit(0)
                return
            prog_pair = result[self.count_file]
            file_1 = prog_pair[0]
            file_2 = prog_pair[1]
            self.compare(file_1, file_2)
            self.ui.webEngineView.load(QUrl("file:///" + QFileInfo("./diff.html").absoluteFilePath()))


    def equal(self):
        self.count_file = self.count_file + 1
        self.show_diff()

    def inequal(self):
        with open("../output/equal.csv", 'r') as f:
            reader = csv.reader(f)
            result = list(reader)
            if self.count_file >= len(result):
                msg_box = QMessageBox()
                msg_box.setText("恭喜，已完成所有判断，结果自动保存在../output文件夹内")
                msg_box.exec_()
                exit(0)
                return
            prog_pair = result[self.count_file]
            with open("../output/inequal.csv", mode="a") as file:
                file.write(prog_pair[0]+"," +prog_pair[1]+"\n")
        data = pd.read_csv("../output/equal.csv")
        os.system("rm ../output/equal.csv")
        data = data.drop(self.count_file - 1)
        data.to_csv("../output/equal.csv", index=False, encoding="utf-8")
        self.show_diff()

    def save_output(self):
        child_window = Save_Success()

    def find_folder(self):
        command = 'ls {}'.format('../input')
        return (subprocess.call(command, shell=True))

        #os.system('cd judger')
        #os.system('g++ -std=c++17 -g main.cpp input.cpp run_code.cpp judge_diff.cpp output.cpp -o judging')

class Inform_unimport(QDialog):
    def __init__(self):
        super().__init__()
        msg_box = QMessageBox()
        msg_box.setText("请先传入input文件夹")
        msg_box.exec_()

class Save_Success(QDialog):
    def __init__(self):
        super().__init__()
        msg_box = QMessageBox()
        msg_box.setText("保存成功")
        msg_box.exec_()

class Failure(QDialog):
    def __init__(self):
        super().__init__()
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '导入文件失败，请将input文件夹放在本程序所在文件夹里')
        msg_box.exec_()

class Success(QDialog):
    def __init__(self):
        super().__init__()
        msg_box = QMessageBox()
        msg_box.setText("导入成功")
        msg_box.exec_()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
