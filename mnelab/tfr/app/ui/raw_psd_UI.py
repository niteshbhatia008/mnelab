# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_psd-ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RawPSDWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 800)
        Dialog.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("b")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.figureLayout = QtWidgets.QVBoxLayout()
        self.figureLayout.setObjectName("figureLayout")
        self.verticalLayout_3.addLayout(self.figureLayout)
        self.lowerWindowLayout = QtWidgets.QVBoxLayout()
        self.lowerWindowLayout.setContentsMargins(300, 20, 300, -1)
        self.lowerWindowLayout.setSpacing(6)
        self.lowerWindowLayout.setObjectName("lowerWindowLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.frame.setMaximumHeight(180)
        self.ParametersLayout = QtWidgets.QHBoxLayout(self.frame)
        self.ParametersLayout.setSpacing(6)
        self.ParametersLayout.setObjectName("ParametersLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectPlotLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(160)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.selectPlotLabel.sizePolicy().hasHeightForWidth())
        self.selectPlotLabel.setSizePolicy(sizePolicy)
        self.selectPlotLabel.setMaximumSize(QtCore.QSize(300, 25))
        self.selectPlotLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selectPlotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectPlotLabel.setObjectName("selectPlotLabel")
        self.horizontalLayout.addWidget(self.selectPlotLabel)
        self.selectPlotType = QtWidgets.QComboBox(self.frame)
        self.selectPlotType.setObjectName("selectPlotType")
        self.horizontalLayout.addWidget(self.selectPlotType)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frequencyLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(160)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.frequencyLabel.sizePolicy().hasHeightForWidth())
        self.frequencyLabel.setSizePolicy(sizePolicy)
        self.frequencyLabel.setMaximumSize(QtCore.QSize(300, 25))
        self.frequencyLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frequencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.horizontalLayout_2.addWidget(self.frequencyLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fmin = QtWidgets.QLineEdit(self.frame)
        self.fmin.setObjectName("fmin")
        self.horizontalLayout_5.addWidget(self.fmin)
        self.fmax = QtWidgets.QLineEdit(self.frame)
        self.fmax.setObjectName("fmax")
        self.horizontalLayout_5.addWidget(self.fmax)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frequencySlider = QtWidgets.QSlider(self.frame)
        self.frequencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.frequencySlider.setObjectName("frequencySlider")
        self.horizontalLayout_4.addWidget(self.frequencySlider)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vmaxLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(160)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.vmaxLabel.sizePolicy().hasHeightForWidth())
        self.vmaxLabel.setSizePolicy(sizePolicy)
        self.vmaxLabel.setMaximumSize(QtCore.QSize(300, 25))
        self.vmaxLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vmaxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.vmaxLabel.setObjectName("vmaxLabel")
        self.horizontalLayout_3.addWidget(self.vmaxLabel)
        self.vmin = QtWidgets.QLineEdit(self.frame)
        self.vmin.setObjectName("vmin")
        self.horizontalLayout_3.addWidget(self.vmin)
        self.vmax = QtWidgets.QLineEdit(self.frame)
        self.vmax.setObjectName("vmax")
        self.horizontalLayout_3.addWidget(self.vmax)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.displayLog = QtWidgets.QCheckBox(self.frame)
        self.displayLog.setMaximumSize(QtCore.QSize(300, 25))
        self.displayLog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayLog.setObjectName("displayLog")
        self.horizontalLayout_6.addWidget(self.displayLog, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.ParametersLayout.addLayout(self.verticalLayout)
        self.ParametersLayout.setStretch(0, 1)
        self.lowerWindowLayout.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.lowerWindowLayout)
        self.recapLabel = QtWidgets.QLabel(Dialog)
        self.recapLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.recapLabel.setText("")
        self.recapLabel.setObjectName("recapLabel")
        self.verticalLayout_3.addWidget(self.recapLabel)
        self.verticalLayout_3.setStretch(0, 15)
        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PSD Visualizer"))
        self.selectPlotLabel.setText(_translate("Dialog", "Select Plot Type  "))
        self.frequencyLabel.setText(_translate("Dialog", "Frequency Range Display (min - max)"))
        self.vmaxLabel.setText(_translate("Dialog", "Scaling (min - max)"))
        self.displayLog.setText(_translate("Dialog", "Log Scale"))
