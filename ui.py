# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QAUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(958, 726)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalFrame_2 = QtGui.QFrame(self.frame)
        self.horizontalFrame_2.setObjectName(_fromUtf8("horizontalFrame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.horizontalFrame_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.question_label = QtGui.QLabel(self.horizontalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_label.sizePolicy().hasHeightForWidth())
        self.question_label.setSizePolicy(sizePolicy)
        self.question_label.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(17)
        self.question_label.setFont(font)
        self.question_label.setObjectName(_fromUtf8("question_label"))
        self.verticalLayout_4.addWidget(self.question_label, QtCore.Qt.AlignHCenter)
        self.textEdit = QtGui.QTextEdit(self.horizontalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(800, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_4.addWidget(self.textEdit, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.horizontalFrame_2, QtCore.Qt.AlignTop)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(918, 340))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(27)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton = QtGui.QRadioButton(self.frame_2)
        self.radioButton.setText(_fromUtf8(""))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.label_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.alineEdit = QtGui.QLineEdit(self.frame_2)
        self.alineEdit.setMinimumSize(QtCore.QSize(510, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(15)
        self.alineEdit.setFont(font)
        self.alineEdit.setObjectName(_fromUtf8("alineEdit"))
        self.horizontalLayout_5.addWidget(self.alineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.radioButton_5 = QtGui.QRadioButton(self.frame_2)
        self.radioButton_5.setText(_fromUtf8(""))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.horizontalLayout_6.addWidget(self.radioButton_5, QtCore.Qt.AlignLeft)
        self.bLabel_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bLabel_2.setFont(font)
        self.bLabel_2.setObjectName(_fromUtf8("bLabel_2"))
        self.horizontalLayout_6.addWidget(self.bLabel_2, QtCore.Qt.AlignLeft)
        self.bLineEdit_2 = QtGui.QLineEdit(self.frame_2)
        self.bLineEdit_2.setMinimumSize(QtCore.QSize(510, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(15)
        self.bLineEdit_2.setFont(font)
        self.bLineEdit_2.setObjectName(_fromUtf8("bLineEdit_2"))
        self.horizontalLayout_6.addWidget(self.bLineEdit_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.radioButton_3 = QtGui.QRadioButton(self.frame_2)
        self.radioButton_3.setText(_fromUtf8(""))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_7.addWidget(self.radioButton_3)
        self.cLabel = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cLabel.setFont(font)
        self.cLabel.setObjectName(_fromUtf8("cLabel"))
        self.horizontalLayout_7.addWidget(self.cLabel)
        self.cLineEdit = QtGui.QLineEdit(self.frame_2)
        self.cLineEdit.setMinimumSize(QtCore.QSize(510, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(15)
        self.cLineEdit.setFont(font)
        self.cLineEdit.setObjectName(_fromUtf8("cLineEdit"))
        self.horizontalLayout_7.addWidget(self.cLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.radioButton_4 = QtGui.QRadioButton(self.frame_2)
        self.radioButton_4.setText(_fromUtf8(""))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_8.addWidget(self.radioButton_4)
        self.dLabel = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dLabel.setFont(font)
        self.dLabel.setObjectName(_fromUtf8("dLabel"))
        self.horizontalLayout_8.addWidget(self.dLabel)
        self.dLineEdit = QtGui.QLineEdit(self.frame_2)
        self.dLineEdit.setMinimumSize(QtCore.QSize(510, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(15)
        self.dLineEdit.setFont(font)
        self.dLineEdit.setObjectName(_fromUtf8("dLineEdit"))
        self.horizontalLayout_8.addWidget(self.dLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout.addWidget(self.frame_2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_3 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(822, 0))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.textEdit_2 = QtGui.QTextEdit(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(15)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_5.addWidget(self.textEdit_2)
        self.verticalLayout.addWidget(self.frame_3, QtCore.Qt.AlignHCenter)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(160, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Longdon Decorative"))
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.label_2.setBuddy(self.alineEdit)
        self.bLabel_2.setBuddy(self.bLineEdit_2)
        self.cLabel.setBuddy(self.cLineEdit)
        self.dLabel.setBuddy(self.dLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textEdit, self.alineEdit)
        Dialog.setTabOrder(self.alineEdit, self.bLineEdit_2)
        Dialog.setTabOrder(self.bLineEdit_2, self.cLineEdit)
        Dialog.setTabOrder(self.cLineEdit, self.dLineEdit)
        Dialog.setTabOrder(self.dLineEdit, self.textEdit_2)
        Dialog.setTabOrder(self.textEdit_2, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.radioButton)
        Dialog.setTabOrder(self.radioButton, self.radioButton_5)
        Dialog.setTabOrder(self.radioButton_5, self.radioButton_3)
        Dialog.setTabOrder(self.radioButton_3, self.radioButton_4)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Decoders", None))
        self.question_label.setText(_translate("Dialog", "Question", None))
        self.label_2.setText(_translate("Dialog", "A )", None))
        self.bLabel_2.setText(_translate("Dialog", "B )", None))
        self.cLabel.setText(_translate("Dialog", "C )", None))
        self.dLabel.setText(_translate("Dialog", "D )", None))
        self.pushButton.setText(_translate("Dialog", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
