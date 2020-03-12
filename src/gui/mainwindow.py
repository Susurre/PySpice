# -*- coding: utf-8 -*-

# Filename : mainwindow.py
# Author   : Hao Limin
# Date     : 2020-03-12
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
GUI for PySpice.
"""

from PyQt5.QtGui          import *
from PyQt5.QtWidgets      import *
from PyQt5.QtCore         import *
from PyQt5.QtPrintSupport import * 

import os
import sys

import gui.mainwindow_rc

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.create_center_widget()
        self.create_action()
        self.create_menu()
        self.create_toolbar()

        self.cur_file = ''
        self.editor.document().contentsChanged.connect(self.document_was_modified)
        self.set_current_file('')
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.show()

    def create_center_widget(self):
        layout = QVBoxLayout()

        # Edit netlist in this TextEdit.
        self.editor = QTextEdit()

        # Setup the QTextEdit editor configuration
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPointSize(18)
        self.editor.setFont(font)

        # Message display
        self.message = QTextEdit()
        self.message.setReadOnly(True)

        layout.addWidget(self.editor, 5)
        layout.addWidget(self.message, 2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

    def create_action(self):
        self.open_action = QAction(QIcon(":/images/open.png"), "Open file...", self)
        self.open_action.setStatusTip("Open file")
        self.open_action.setShortcut(QKeySequence.Open)
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction(QIcon(":/images/save.png"), "Save", self)
        self.save_action.setStatusTip("Save current page")
        self.save_action.setShortcut(QKeySequence.Save)
        self.save_action.triggered.connect(self.save)

        self.saveas_action = QAction(QIcon(":/images/saveas.png"), "Save As...", self)
        self.saveas_action.setStatusTip("Save current page to specified file")
        self.saveas_action.setShortcut(QKeySequence.SaveAs)
        self.saveas_action.triggered.connect(self.save_as)

        self.undo_action = QAction(QIcon(":/images/undo.png"), "Undo", self)
        self.undo_action.setStatusTip("Undo last change")
        self.undo_action.setShortcut(QKeySequence.Undo)
        self.undo_action.triggered.connect(self.editor.undo)

        self.redo_action = QAction(QIcon(":/images/redo.png"), "Redo", self) 
        self.redo_action.setStatusTip("Redo last change")
        self.redo_action.setShortcut(QKeySequence.Redo)
        self.redo_action.triggered.connect(self.editor.redo)

        self.select_action = QAction(QIcon(":/images/select_all.png"), "Select all", self)
        self.select_action.setStatusTip("Select all text")
        self.select_action.setShortcut(QKeySequence.SelectAll)
        self.select_action.triggered.connect(self.editor.selectAll)

        self.cut_action = QAction(QIcon(":/images/cut.png"), "Cut", self)
        self.cut_action.setStatusTip("Cut selected text")
        self.cut_action.setShortcut(QKeySequence.Cut)
        self.cut_action.triggered.connect(self.editor.cut)

        self.copy_action = QAction(QIcon(":/images/copy.png"), "Copy", self)
        self.copy_action.setStatusTip("Copy selected text")
        self.copy_action.setShortcut(QKeySequence.Copy)
        self.copy_action.triggered.connect(self.editor.copy)

        self.paste_action = QAction(QIcon(":/images/paste.png"), "Paste", self)
        self.paste_action.setStatusTip("Paste from clipboard")
        self.paste_action.setShortcut(QKeySequence.Paste)
        self.paste_action.triggered.connect(self.editor.paste)

        self.simulate_action = QAction(QIcon(":/images/simulate.png"), "Run Simulation", self)
        self.simulate_action.setStatusTip("Run Simulation")
        self.simulate_action.setShortcut("Ctrl+R")
        self.simulate_action.triggered.connect(self.simulate)
    
    def create_menu(self):
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.saveas_action)

        edit_menu = self.menuBar().addMenu("&Edit")
        edit_menu.addAction(self.undo_action)
        edit_menu.addAction(self.redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)
        edit_menu.addAction(self.select_action)

        simulate_menu = self.menuBar().addMenu("&Simulate")
        simulate_menu.addAction(self.simulate_action)

    def create_toolbar(self):
        file_toolbar = QToolBar("File")
        file_toolbar.setIconSize(QSize(25, 25))
        self.addToolBar(file_toolbar)
        file_toolbar.addAction(self.open_action)
        file_toolbar.addAction(self.save_action)
        file_toolbar.addAction(self.saveas_action)

        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(25, 25))
        self.addToolBar(edit_toolbar)
        edit_toolbar.addAction(self.redo_action)
        edit_toolbar.addAction(self.undo_action)
        edit_toolbar.addAction(self.cut_action)
        edit_toolbar.addAction(self.copy_action)
        edit_toolbar.addAction(self.paste_action)
        edit_toolbar.addAction(self.select_action)

        simulate_toolbar = QToolBar("Simulate")
        simulate_toolbar.setIconSize(QSize(25, 25))
        self.addToolBar(simulate_toolbar)
        simulate_toolbar.addAction(self.simulate_action)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file",
                      "./", "Netlist(*.sp);;Netlist(*.cir);;ALL(*.*)")
        if filename:
            file = QFile(filename)
            if not file.open(QFile.ReadOnly | QFile.Text):
                self.show_critical_dialog("Can't open {}".format(filename))

            inf = QTextStream(file)
            QApplication.setOverrideCursor(Qt.WaitCursor)
            self.editor.setPlainText(inf.readAll())
            QApplication.restoreOverrideCursor()

            self.set_current_file(filename)
            self.statusBar().showMessage("File loaded", 2000)

    def save(self):
        if self.cur_file:
            self.save_file(self.cur_file)
        else:
            self.save_as()

    def save_as(self):
        filename, _ = QFileDialog.getSaveFileName(self)
        if filename:
            self.save_file(filename)
    
    def save_file(self, filename):
        file = QFile(filename)
        if not file.open(QFile.WriteOnly | QFile.Text):
            self.show_critical_dialog("Can't open {}".format(filename))
        
        outf = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        outf << self.editor.toPlainText()
        QApplication.restoreOverrideCursor()

        self.set_current_file(filename)
        self.statusBar().showMessage("File saved", 2000)  

    def set_current_file(self, filename):
        self.cur_file = filename
        self.editor.document().setModified(False)
        self.setWindowModified(False)
        self.update_window_title();
    
    def document_was_modified(self):
        self.setWindowModified(self.editor.document().isModified())
        self.update_window_title(True)
    
    def update_window_title(self, modified = False):
        if self.cur_file:
            shown_name = QFileInfo(self.cur_file).fileName()
        else:
            shown_name = 'untitled.sp'
        
        if modified:
            title = "%s* - PySpice" % shown_name
        else:
            title = "%s - PySpice" % shown_name 
        self.setWindowTitle(title)

    def show_critical_dialog(self, msg):
        dlg = QMessageBox(self)
        dlg.setText(msg)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    """
    Do simulation
    """
    def simulate(self):
        if self.editor.document().isModified():
            self.save() 
        
        print('simulate')
