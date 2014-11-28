import datetime

class SubtaskDetailsDialogCustomizer:
    ###########################
    def __init__( self, gui, logic, subtaskState ):
        self.gui            = gui
        self.logic          = logic
        self.subtaskState        = subtaskState
        self.__setupConnections()
        self.updateView( self.subtaskState )

    ###########################
    def updateView( self, subtaskState ):
        self.subtaskState = subtaskState
        self.__updateData()

    ###########################
    def __updateData(self):
        self.gui.ui.subtaskIdLabel.setText( self.subtaskState.subtaskId )
        self.gui.ui.nodeIdLabel.setText( self.subtaskState.computer.nodeId )
        self.gui.ui.nodeIpAddressLabel.setText( self.subtaskState.computer.ipAddress )
        self.gui.ui.statusLabel.setText( self.subtaskState.subtaskStatus )
        self.gui.ui.performanceLabel.setText( "{}".format( self.subtaskState.computer.performance ) )
        self.gui.ui.subtaskDefinitionTextEdit.setPlainText( self.subtaskState.subtaskDefinition )

    ###########################
    def __setupConnections( self ):
        self.gui.ui.closeButton.clicked.connect( self.gui.window.close )
