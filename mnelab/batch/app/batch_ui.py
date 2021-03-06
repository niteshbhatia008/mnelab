# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatchDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 430)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dirButton = QtWidgets.QPushButton(Dialog)
        self.dirButton.setObjectName("dirButton")
        self.horizontalLayout_2.addWidget(self.dirButton)
        self.directory = QtWidgets.QLineEdit(Dialog)
        self.directory.setObjectName("directory")
        self.horizontalLayout_2.addWidget(self.directory)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filterBox = QtWidgets.QCheckBox(Dialog)
        self.filterBox.setObjectName("filterBox")
        self.horizontalLayout_3.addWidget(self.filterBox)
        self.low = QtWidgets.QLineEdit(Dialog)
        self.low.setObjectName("low")
        self.horizontalLayout_3.addWidget(self.low)
        self.high = QtWidgets.QLineEdit(Dialog)
        self.high.setObjectName("high")
        self.horizontalLayout_3.addWidget(self.high)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.samplingBox = QtWidgets.QCheckBox(Dialog)
        self.samplingBox.setObjectName("samplingBox")
        self.horizontalLayout_4.addWidget(self.samplingBox)
        self.sfreq = QtWidgets.QLineEdit(Dialog)
        self.sfreq.setObjectName("sfreq")
        self.horizontalLayout_4.addWidget(self.sfreq)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tfrBox = QtWidgets.QCheckBox(Dialog)
        self.tfrBox.setObjectName("tfrBox")
        self.horizontalLayout_7.addWidget(self.tfrBox)
        self.tfrParams = QtWidgets.QPushButton(Dialog)
        self.tfrParams.setObjectName("tfrParams")
        self.horizontalLayout_7.addWidget(self.tfrParams)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tfrLabel = QtWidgets.QTextEdit(Dialog)
        self.tfrLabel.setObjectName("tfrLabel")
        self.verticalLayout.addWidget(self.tfrLabel)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.psdBox = QtWidgets.QCheckBox(Dialog)
        self.psdBox.setObjectName("psdBox")
        self.horizontalLayout_8.addWidget(self.psdBox)
        self.psdParams = QtWidgets.QPushButton(Dialog)
        self.psdParams.setObjectName("psdParams")
        self.horizontalLayout_8.addWidget(self.psdParams)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.psdLabel = QtWidgets.QTextEdit(Dialog)
        self.psdLabel.setObjectName("psdLabel")
        self.verticalLayout.addWidget(self.psdLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.savePath = QtWidgets.QLineEdit(Dialog)
        self.savePath.setObjectName("savePath")
        self.horizontalLayout_6.addWidget(self.savePath)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.startBatch = QtWidgets.QPushButton(Dialog)
        self.startBatch.setObjectName("startBatch")
        self.verticalLayout.addWidget(self.startBatch)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Batch Processing"))
        self.dirButton.setText(_translate("Dialog", "Open files..."))
        self.filterBox.setText(_translate("Dialog", "Filter (min-max, Hz)"))
        self.samplingBox.setText(_translate("Dialog", "Resample (Hz)"))
        self.tfrBox.setText(_translate("Dialog", "Compute Time-Frequency"))
        self.tfrParams.setText(_translate("Dialog", "Select Parameters"))
        self.psdBox.setText(_translate("Dialog", "Compute Power-Spectrum Density"))
        self.psdParams.setText(_translate("Dialog", "Select Parameters"))
        self.pushButton.setText(_translate("Dialog", "Choose saving folder..."))
        self.startBatch.setText(_translate("Dialog", "Start batch processing..."))
