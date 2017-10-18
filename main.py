#author  = Natesh M Bhat
#python version = 3.5

import pymysql
from ui import Ui_Dialog ;
from time import sleep
from threading import Thread;

from PyQt5 import QtCore , QtGui , QtWidgets

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



class datahandler(object):
    def __init__(self):
        ui.submit_PushButton.mouseReleaseEvent = self.connecttosql ;

    def replace(self , mystring ):
        mystring = mystring.replace("&" , "&amp;");
        mystring = mystring.replace("'" , "&apos;");
        mystring = mystring.replace('"' , "&quot;");
        mystring = mystring.replace("<" , "&lt;");
        mystring = mystring.replace(">" , "&gt;");
        return mystring ;

    def showtooltip(self, text):
        tt = QtWidgets.QToolTip ;
        myfont = QtGui.QFont() ;
        myfont.setFamily("caladea")
        myfont.setBold(True)
        myfont.setPointSize(20)
        tt.setFont(myfont)
        mywin = Dialog.frameGeometry() ;
        pos = mywin.center()
        pos.setX(pos.x() - 6.5 * len(text));
        pos.setY(mywin.y()-20)
        tt.showText(pos, text, Dialog ) ;


    def connecttosql(self , event):

        question = self.replace(ui.question_textedit.toPlainText()) ;
        if not question:
            QtWidgets.QMessageBox.warning(Dialog , "Empty Question field" , "Make sure that the question field is not Empty ! " , QtWidgets.QMessageBox.Ok) ;
            return ;

        opa = self.replace(ui.alineEdit.text()) ;
        opb = self.replace(ui.bLineEdit.text() ) ;
        opc = self.replace(ui.cLineEdit.text()  ) ;
        opd = self.replace(ui.cLineEdit.text() )  ;
        rightop = 'A' if ui.aradioButton.isChecked() else 'B' if ui.bradioButton.isChecked() else 'C' if ui.cradioButton.isChecked() else 'D' ;
        codesnippet = self.replace(ui.codesnippet_textedit.toPlainText()) ;


        try:
            con = pymysql.connect(host='localhost',
                                  user='root',
                                  password='toor',
                                  db='mydatabase',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor);
            cur = con.cursor();

            command = """insert into tablename (Question , optiona , optionb , optionc , optiond , correct , codesnippet) values (%s, %s , %s, %s , %s , %s , %s ) """ ;
            strings = (
                question ,
                opa ,
                opb ,
                opc ,
                opd,
                rightop,
                codesnippet
            );

            cur.execute(command , strings);
            con.commit();
            for i in ui.frame.findChildren((QtWidgets.QTextEdit , QtWidgets.QLineEdit)):
                i.clear() ;

            self.showtooltip("Added to Database");
        except Exception as e:
            self.showtooltip("Failed Adding to Database") ;
            print(e) ;


        finally:
            con.close();



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) ;
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    datahandler() ;
    Dialog.show()
    sys.exit(app.exec_())

