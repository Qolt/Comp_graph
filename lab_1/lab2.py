import sys
import string
from OpenGL.GL import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtOpenGL import *
from lab1 import WfWidget, ControlWindow 

params = []
scissor_params = []
alpha_params = []

class GLWidget2 (WfWidget):
    def __init__(self, parent=None):
        super(GLWidget2, self).__init__(parent)
        self.scissor_state = 0
        self.alpha_state = 0
    
    def drawScissor (self):
        glEnable(GL_SCISSOR_TEST)
        if scissor_params == []:
            glScissor(50, 50, 190, 190)
        else:
            glScissor(scissor_params[0], scissor_params[1], scissor_params[2], scissor_params[3])

    def drawAlpha(self):
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(GL_GEQUAL, 0.4) 
        print "Call drawAlpha()"
        glColor4d(0,0,10,0.5)
        glBegin(GL_QUADS)
        glVertex3d(30,30,9)
        glVertex3d(-30,30,0 )
        glVertex3d(-30,-30,0)
        glVertex3d(30,-30,9)
        glEnd()
        

    def paintGL(self):
        WfWidget.paintGL(self)
        if self.scissor_state ==  2:
            self.drawScissor()
        else:
            glDisable(GL_SCISSOR_TEST)

        if self.alpha_state ==  2:
            self.drawAlpha()
        else:
            glDisable(GL_ALPHA_TEST)


    def ScissorState (self, state):
        self.hide()
        print "Scissor " + str(state)
        self.scissor_state = state
        self.show()

    def AlphaState(self, state):
        self.hide()
        print "Alpha " + str(state)
        self.alpha_state = state
        self.show()

    def setAlphaStyle(self, state):
        print string
 
class ControlWidget2 (ControlWindow):
    def __init__ (self, parent=None):
        super(ControlWidget2, self).__init__(parent)
        
        self.checkScissor = QtGui.QCheckBox("Enable scissor")
        self.grid.addWidget(self.checkScissor, 1, 1)

        self.labelScissor = QtGui.QLabel(" Scissor params: ")
        self.grid.addWidget(self.labelScissor, 2, 1)

        self.scissorParams =  QtGui.QLineEdit()
        self.scissorParams.setValidator(self.validator)
        self.grid.addWidget(self.scissorParams, 3, 1)
        
        self.checkAlpha = QtGui.QCheckBox("Enable alpha function")
        self.grid.addWidget(self.checkAlpha, 4, 1)

        self.labelAlpha = QtGui.QLabel("Color params for addition figure: ")
        self.grid.addWidget(self.labelAlpha, 5, 1)

        self.alphaParams =  QtGui.QLineEdit()
        self.alphaParams.setValidator(self.validator)
        self.grid.addWidget(self.alphaParams, 6, 1)
        
        self.combo = QtGui.QComboBox()
        self.combo.addItem("GL_NEVER")
        self.combo.addItem("GL_LESS")
        self.combo.addItem("GL_EQUAL")
        self.combo.addItem("GL_LEQUAL")
        self.combo.addItem("GL_GREATER")
        self.combo.addItem("GL_NOTEQUAL")
        self.combo.addItem("GL_GEQUAL")
        self.combo.addItem("GL_ALWAYS")
        self.grid.addWidget(self.combo, 7, 1)
        
    def SetScissorParams(self):
       global scissor_params
       self.inputdata = string.split(str(self.scissorParams.text()), " ")
       for i, item  in enumerate(self.inputdata):
            try:
                self.inputdata[i] = int(self.inputdata[i])
                self.inputdata.remove('')
            except:
                pass
       if self.inputdata == ['']:
            self.inputdata = []
       print "Set scissor params: " + str(self.inputdata)
       scissor_params = self.inputdata

    def SetAlphaParams(self):
       global alpha_params
       self.inputdata = string.split(str(self.alphaParams.text()), " ")
       for i, item  in enumerate(self.inputdata):
            try:
                self.inputdata[i] = int(self.inputdata[i])
                self.inputdata.remove('')
            except:
                pass
       if self.inputdata == ['']:
            self.inputdata = []
       print "Set alpha params: " + str(self.inputdata)
       alpha_params = self.inputdata


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GLWidget = GLWidget2()
    controlWidget = ControlWidget2()

    controlWidget.connect (controlWidget.btnPoints, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowPoints)
    controlWidget.connect (controlWidget.btnLines, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowLines)
    controlWidget.connect (controlWidget.btnStripLines, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowStripLines)
    controlWidget.connect (controlWidget.btnLoopLines, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowLoopLines)
    controlWidget.connect (controlWidget.btnTriangles, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowTriangles)
    controlWidget.connect (controlWidget.btnStripTriangles, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowStripTriangles)
    controlWidget.connect (controlWidget.btnStripTrianglesFan, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowTrianglesFan)
    controlWidget.connect (controlWidget.btnQuads, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowQuads)
    controlWidget.connect (controlWidget.btnQuadsStrip, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowQuadsStrip)
    controlWidget.connect (controlWidget.btnPolygon, QtCore.SIGNAL("clicked ()"),
            GLWidget.ShowPolygon)
    controlWidget.connect (controlWidget.txtLabel, QtCore.SIGNAL("editingFinished()"),
            controlWidget.SetParams)
    controlWidget.connect (controlWidget.scissorParams, QtCore.SIGNAL("editingFinished()"),
            controlWidget.SetScissorParams)
    controlWidget.connect (controlWidget.checkScissor, QtCore.SIGNAL("stateChanged (int)"),
            GLWidget.ScissorState)
    controlWidget.connect (controlWidget.checkAlpha, QtCore.SIGNAL("stateChanged (int)"),
            GLWidget.AlphaState)
    controlWidget.connect (controlWidget.alphaParams, QtCore.SIGNAL("editingFinished()"),
            controlWidget.SetAlphaParams)
    controlWidget.connect (controlWidget.combo, QtCore.SIGNAL("activated(int)"),
            GLWidget.setAlphaStyle)
    controlWidget.show()
    app.exec_()
