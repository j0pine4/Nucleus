import sys
from PyQt5 import QtWidgets
from wordsAPI import wordsAPI, wordsList
from googleSheets import sheetsUpload
from googleData import risingQueries, topQueries, risingQueriesVAR, topQueriesVAR
from googleData import risingTopics, topTopics, cityData, regionData, metroData, trendingTopics, currentTrends
from youtubeData import yt_risingQueries, yt_topQueries, youtube_api
from youtubeData import topQueriesVAR, risingQueriesVAR
from fileManager import fileManager, FILE_LIST


class window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Generate')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        self.setLayout(v_box)
        self.setWindowTitle('Lead Generator')

        self.b1.clicked.connect(self.btn_click)
        self.b2.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):

        keyword = self.le.text()
        suggestions = [keyword]

        sender = self.sender()

        if sender.text() == "Generate":
            #Turn this user input into a usable variable calls userText
            userText = self.le.text()

            #Run the words API on user input
            wordsAPI(userText)
            trendingTopics(wordsList, 'Word_Association_Trends.csv')

            #Find the rising queries based on Keyword
            risingQueries(userText)

            #Find the top queries based on Keyword
            topQueries(userText)

            # Find the rising topics based on Keyword
            risingTopics(userText)

            # Find the rising topics based on Keyword
            topTopics(userText)

            # Append all to the same list with the original Keyword
            suggestions = suggestions + risingQueriesVAR + topQueriesVAR
            print(suggestions)

            #Find the best locations based on user input
            cityData(userText)
            metroData(userText)
            regionData(userText)

            #Find Current Trends
            currentTrends()

            #Find the rising Youtube queries based on Keyword
            yt_risingQueries(userText)

            #Find the top Youtube queries based on Keyword
            yt_topQueries(userText)

            # Find the rising Youtube topics based on Keyword
            youtube_api(userText)

            #Upload everything to google sheets
            fileManager()

            for item in FILE_LIST:
                print('Uploading %s to DataBase' % (item))
                sheetsUpload(item, item)

            print('Report Created')

        else:
            self.le.clear()
            suggestions.clear()


app = QtWidgets.QApplication(sys.argv)
a_window = window()
sys.exit(app.exec_())
