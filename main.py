from PyQt5.QtWidgets import *
from main_window import Window
import pyrebase
import sys


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

    # setting app storage
    storage = firebase.storage()

    app = QApplication(sys.argv)
    window = Window(storage)
    window.show()
    sys.exit(app.exec_())
