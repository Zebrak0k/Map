import sys
import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt


class Map(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.lon = 37.530887
        self.lat = 55.703118
        self.delta = 0.005
        self.z = 8

        self.btn_Up.clicked.connect(self.locate)
        self.btn_Down.clicked.connect(self.locate)
        self.btn_Right.clicked.connect(self.locate)
        self.btn_Left.clicked.connect(self.locate)

        self.refresh_map()

    def locate(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp or event.key() == Qt.Key_W and self.z + 1 <= 100:
            self.z += 1
        if event.key() == Qt.Key_PageDown or event.key() == Qt.Key_S and self.z - 1 >= 1:
            self.z -= 1
        self.refresh_map()

    def refresh_map(self):
        self.api_server = "https://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join([str(self.lon), str(self.lat)]),
            "z": f"{self.z}",
            "l": "map"
        }
        response = requests.get(self.api_server, params=params)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

        self.pixmap = QPixmap(map_file)
        self.Map.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec_())