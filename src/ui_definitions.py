# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UI_GeneratorMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UI_GeneratorMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneratorMainWindow(object):
    def setupUi(self, GeneratorMainWindow):
        GeneratorMainWindow.setObjectName("GeneratorMainWindow")
        GeneratorMainWindow.resize(791, 574)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeneratorMainWindow.sizePolicy().hasHeightForWidth())
        GeneratorMainWindow.setSizePolicy(sizePolicy)
        GeneratorMainWindow.setIconSize(QtCore.QSize(22, 22))
        GeneratorMainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        GeneratorMainWindow.setDocumentMode(False)
        GeneratorMainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(GeneratorMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(100, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 610, 148))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.num_parts_spin_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_parts_spin_box.sizePolicy().hasHeightForWidth())
        self.num_parts_spin_box.setSizePolicy(sizePolicy)
        self.num_parts_spin_box.setProperty("value", 1)
        self.num_parts_spin_box.setObjectName("num_parts_spin_box")
        self.horizontalLayout_17.addWidget(self.num_parts_spin_box)
        self.gridLayout.addLayout(self.horizontalLayout_17, 0, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.exam_date_edit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exam_date_edit.sizePolicy().hasHeightForWidth())
        self.exam_date_edit.setSizePolicy(sizePolicy)
        self.exam_date_edit.setObjectName("exam_date_edit")
        self.horizontalLayout_6.addWidget(self.exam_date_edit)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.course_code_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.course_code_line_edit.setObjectName("course_code_line_edit")
        self.horizontalLayout_4.addWidget(self.course_code_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.exam_name_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exam_name_line_edit.sizePolicy().hasHeightForWidth())
        self.exam_name_line_edit.setSizePolicy(sizePolicy)
        self.exam_name_line_edit.setObjectName("exam_name_line_edit")
        self.horizontalLayout_2.addWidget(self.exam_name_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.marks_spin_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marks_spin_box.sizePolicy().hasHeightForWidth())
        self.marks_spin_box.setSizePolicy(sizePolicy)
        self.marks_spin_box.setMaximum(300)
        self.marks_spin_box.setObjectName("marks_spin_box")
        self.horizontalLayout_5.addWidget(self.marks_spin_box)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.duration_spin_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.duration_spin_box.sizePolicy().hasHeightForWidth())
        self.duration_spin_box.setSizePolicy(sizePolicy)
        self.duration_spin_box.setMaximum(400)
        self.duration_spin_box.setObjectName("duration_spin_box")
        self.horizontalLayout_8.addWidget(self.duration_spin_box)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_18.addWidget(self.label_16)
        self.qp_data_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qp_data_line_edit.sizePolicy().hasHeightForWidth())
        self.qp_data_line_edit.setSizePolicy(sizePolicy)
        self.qp_data_line_edit.setObjectName("qp_data_line_edit")
        self.horizontalLayout_18.addWidget(self.qp_data_line_edit)
        self.qp_data_tool_button = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qp_data_tool_button.sizePolicy().hasHeightForWidth())
        self.qp_data_tool_button.setSizePolicy(sizePolicy)
        self.qp_data_tool_button.setObjectName("qp_data_tool_button")
        self.horizontalLayout_18.addWidget(self.qp_data_tool_button)
        self.gridLayout.addLayout(self.horizontalLayout_18, 1, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.sem_spin_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sem_spin_box.sizePolicy().hasHeightForWidth())
        self.sem_spin_box.setSizePolicy(sizePolicy)
        self.sem_spin_box.setObjectName("sem_spin_box")
        self.horizontalLayout_7.addWidget(self.sem_spin_box)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.programLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.programLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.programLabel.setObjectName("programLabel")
        self.horizontalLayout_3.addWidget(self.programLabel)
        self.program_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.program_line_edit.sizePolicy().hasHeightForWidth())
        self.program_line_edit.setSizePolicy(sizePolicy)
        self.program_line_edit.setObjectName("program_line_edit")
        self.horizontalLayout_3.addWidget(self.program_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.qp_code_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qp_code_line_edit.sizePolicy().hasHeightForWidth())
        self.qp_code_line_edit.setSizePolicy(sizePolicy)
        self.qp_code_line_edit.setObjectName("qp_code_line_edit")
        self.horizontalLayout_9.addWidget(self.qp_code_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.qpd_open_push_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qpd_open_push_button.sizePolicy().hasHeightForWidth())
        self.qpd_open_push_button.setSizePolicy(sizePolicy)
        self.qpd_open_push_button.setObjectName("qpd_open_push_button")
        self.verticalLayout_3.addWidget(self.qpd_open_push_button)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.qp_tree_view = QtWidgets.QTreeView(self.centralwidget)
        self.qp_tree_view.setObjectName("qp_tree_view")
        self.verticalLayout.addWidget(self.qp_tree_view)
        GeneratorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GeneratorMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        GeneratorMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GeneratorMainWindow)
        self.statusbar.setObjectName("statusbar")
        GeneratorMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(GeneratorMainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        GeneratorMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_QP = QtWidgets.QAction(GeneratorMainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/new_qp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_QP.setIcon(icon)
        self.actionNew_QP.setObjectName("actionNew_QP")
        self.actionLoad_QP = QtWidgets.QAction(GeneratorMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/open_qp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_QP.setIcon(icon1)
        self.actionLoad_QP.setObjectName("actionLoad_QP")
        self.actionSave_QP = QtWidgets.QAction(GeneratorMainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/save_qp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_QP.setIcon(icon2)
        self.actionSave_QP.setObjectName("actionSave_QP")
        self.actionSave_As = QtWidgets.QAction(GeneratorMainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionQuit = QtWidgets.QAction(GeneratorMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(GeneratorMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGenerate = QtWidgets.QAction(GeneratorMainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionPreview = QtWidgets.QAction(GeneratorMainWindow)
        self.actionPreview.setObjectName("actionPreview")
        self.actionPreferences = QtWidgets.QAction(GeneratorMainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionPrint = QtWidgets.QAction(GeneratorMainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/print_qp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionOpen_QPD_Edior = QtWidgets.QAction(GeneratorMainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/qpd_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_QPD_Edior.setIcon(icon4)
        self.actionOpen_QPD_Edior.setObjectName("actionOpen_QPD_Edior")
        self.menuFile.addAction(self.actionNew_QP)
        self.menuFile.addAction(self.actionLoad_QP)
        self.menuFile.addAction(self.actionSave_QP)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuActions.addAction(self.actionGenerate)
        self.menuActions.addAction(self.actionPreview)
        self.menuActions.addAction(self.actionOpen_QPD_Edior)
        self.menuSettings.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew_QP)
        self.toolBar.addAction(self.actionLoad_QP)
        self.toolBar.addAction(self.actionSave_QP)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionOpen_QPD_Edior)

        self.retranslateUi(GeneratorMainWindow)
        QtCore.QMetaObject.connectSlotsByName(GeneratorMainWindow)

    def retranslateUi(self, GeneratorMainWindow):
        _translate = QtCore.QCoreApplication.translate
        GeneratorMainWindow.setWindowTitle(_translate("GeneratorMainWindow", "Question Paper Generator"))
        self.label_15.setText(_translate("GeneratorMainWindow", "Number of Parts:"))
        self.label_4.setText(_translate("GeneratorMainWindow", "Exam date:"))
        self.label_2.setText(_translate("GeneratorMainWindow", "Course code:"))
        self.label.setText(_translate("GeneratorMainWindow", "Exam name:"))
        self.label_5.setText(_translate("GeneratorMainWindow", "Max marks:"))
        self.label_7.setText(_translate("GeneratorMainWindow", "Duration(mins):"))
        self.label_16.setText(_translate("GeneratorMainWindow", "Question paper data:"))
        self.qp_data_tool_button.setText(_translate("GeneratorMainWindow", "..."))
        self.label_6.setText(_translate("GeneratorMainWindow", "Semester:"))
        self.programLabel.setText(_translate("GeneratorMainWindow", "Program"))
        self.label_3.setText(_translate("GeneratorMainWindow", "Question.p code"))
        self.pushButton.setText(_translate("GeneratorMainWindow", "Generate Question Paper"))
        self.qpd_open_push_button.setText(_translate("GeneratorMainWindow", "        Open QPD Editor       "))
        self.menuFile.setTitle(_translate("GeneratorMainWindow", "File"))
        self.menuHelp.setTitle(_translate("GeneratorMainWindow", "Help"))
        self.menuActions.setTitle(_translate("GeneratorMainWindow", "Actions"))
        self.menuSettings.setTitle(_translate("GeneratorMainWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("GeneratorMainWindow", "toolBar"))
        self.actionNew_QP.setText(_translate("GeneratorMainWindow", "New"))
        self.actionLoad_QP.setText(_translate("GeneratorMainWindow", "Load"))
        self.actionSave_QP.setText(_translate("GeneratorMainWindow", "Save"))
        self.actionSave_As.setText(_translate("GeneratorMainWindow", "Save As"))
        self.actionQuit.setText(_translate("GeneratorMainWindow", "Quit"))
        self.actionAbout.setText(_translate("GeneratorMainWindow", "About"))
        self.actionGenerate.setText(_translate("GeneratorMainWindow", "Generate into..."))
        self.actionPreview.setText(_translate("GeneratorMainWindow", "Preview"))
        self.actionPreferences.setText(_translate("GeneratorMainWindow", "Preferences"))
        self.actionPrint.setText(_translate("GeneratorMainWindow", "Print"))
        self.actionOpen_QPD_Edior.setText(_translate("GeneratorMainWindow", "Open QPD Editor"))

import icons_rc



class Ui_GeneratorWelcomeDialog(object):
    def setupUi(self, GeneratorWelcomeDialog):
        GeneratorWelcomeDialog.setObjectName("GeneratorWelcomeDialog")
        GeneratorWelcomeDialog.resize(350, 190)
        GeneratorWelcomeDialog.setMinimumSize(QtCore.QSize(400, 200))
        GeneratorWelcomeDialog.setMaximumSize(QtCore.QSize(400, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneratorWelcomeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_label = QtWidgets.QLabel(GeneratorWelcomeDialog)
        self.welcome_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.welcome_label.setFont(font)
        self.welcome_label.setTextFormat(QtCore.Qt.AutoText)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setWordWrap(False)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout.addWidget(self.welcome_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(GeneratorWelcomeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignBottom)
        self.openPushButton = QtWidgets.QPushButton(GeneratorWelcomeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openPushButton.sizePolicy().hasHeightForWidth())
        self.openPushButton.setSizePolicy(sizePolicy)
        self.openPushButton.setObjectName("openPushButton")
        self.horizontalLayout.addWidget(self.openPushButton, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(GeneratorWelcomeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        self.label = QtWidgets.QLabel(GeneratorWelcomeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.label_2 = QtWidgets.QLabel(GeneratorWelcomeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(GeneratorWelcomeDialog)
        QtCore.QMetaObject.connectSlotsByName(GeneratorWelcomeDialog)
        self.setFixedSize(self.size())

    def retranslateUi(self, GeneratorWelcomeDialog):
        _translate = QtCore.QCoreApplication.translate
        GeneratorWelcomeDialog.setWindowTitle(_translate("GeneratorWelcomeDialog", "Welcome"))
        self.welcome_label.setText(_translate("GeneratorWelcomeDialog", "Welcome to Question Paper Generator"))
        self.pushButton_3.setText(_translate("GeneratorWelcomeDialog", "Create a new Question Paper"))
        self.openPushButton.setText(_translate("GeneratorWelcomeDialog", "Open an existing Question Paper"))
        self.pushButton.setText(_translate("GeneratorWelcomeDialog", "Settings"))
        self.label.setText(_translate("GeneratorWelcomeDialog", "Ver: 1.0.0"))
        self.label_2.setText(_translate("GeneratorWelcomeDialog", "Created by: Amit Kumar Gupta"))


class Ui_NewQPDialog(object):
    def setupUi(self, NewQPDialog):
        NewQPDialog.setObjectName("NewQPDialog")
        NewQPDialog.resize(457, 163)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewQPDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(NewQPDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.qp_path_line_edit = QtWidgets.QLineEdit(NewQPDialog)
        self.qp_path_line_edit.setObjectName("qp_path_line_edit")
        self.horizontalLayout.addWidget(self.qp_path_line_edit)
        self.qp_path_tool_button = QtWidgets.QToolButton(NewQPDialog)
        self.qp_path_tool_button.setObjectName("qp_path_tool_button")
        self.horizontalLayout.addWidget(self.qp_path_tool_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(NewQPDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.qp_filename_line_edit = QtWidgets.QLineEdit(NewQPDialog)
        self.qp_filename_line_edit.setObjectName("qp_filename_line_edit")
        self.horizontalLayout_2.addWidget(self.qp_filename_line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancel_push_button = QtWidgets.QPushButton(NewQPDialog)
        self.cancel_push_button.setObjectName("cancel_push_button")
        self.horizontalLayout_3.addWidget(self.cancel_push_button)
        self.create_qp_push_button = QtWidgets.QPushButton(NewQPDialog)
        self.create_qp_push_button.setObjectName("create_qp_push_button")
        self.horizontalLayout_3.addWidget(self.create_qp_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(NewQPDialog)
        QtCore.QMetaObject.connectSlotsByName(NewQPDialog)

    def retranslateUi(self, NewQPDialog):
        _translate = QtCore.QCoreApplication.translate
        NewQPDialog.setWindowTitle(_translate("NewQPDialog", "Create new QP"))
        self.label.setText(_translate("NewQPDialog", "Path of Question Paper: "))
        self.qp_path_tool_button.setText(_translate("NewQPDialog", "..."))
        self.label_2.setText(_translate("NewQPDialog", "Question Paper File name (.qp):"))
        self.cancel_push_button.setText(_translate("NewQPDialog", "Cancel"))
        self.create_qp_push_button.setText(_translate("NewQPDialog", "Create Question Paper"))
