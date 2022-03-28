from PyQt5.QtWidgets import *
from main_window import Window
import pyrebase
import sys
import os


if __name__ == "__main__":
    firebase = pyrebase.initialize_app({
        "apiKey": "AIzaSyDc1dnrvTzR7Y5uDWJzDRtfACferheZgI4",
        "authDomain": "cpc-graphs.firebaseapp.com",
        "projectId": "cpc-graphs",
        "storageBucket": "cpc-graphs.appspot.com",
        "messagingSenderId": "344220732549",
        "appId": "1:344220732549:web:e9f58e10540bfa6e45edec",
        "measurementId": "G-XQ625HPKBH",
        "databaseURL": "https://cpc-graphs-default-rtdb.firebaseio.com"
    })
    storage = firebase.storage()

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

    for file in os.listdir('C:\\Users\\Kate\\PycharmProjects\\CPC_Graphs'):
        if file.endswith('.jpeg'):
            storage.child(file).put(file)

    sys.exit()
