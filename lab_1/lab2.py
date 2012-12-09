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
        self.alpha_enable = 0 
        self.blend_state = 0
    
    def drawScissor (self):
        glEnable(GL_SCISSOR_TEST)
        global scissor_params
        if scissor_params == []:
            glScissor(50, 50, 190, 190)
        else:
            glScissor(scissor_params[0], scissor_params[1], scissor_params[2], scissor_params[3])

    def drawAlpha(self):
        glEnable(GL_ALPHA_TEST)
        global alpha_params
        if alpha_params == []:
            alpha_params = [10, 10, 0, 0.5]
        try:
            ref = alpha_params[4]
        except:
            ref = 0.7
        print "Alpha params:" + str(alpha_params)
        print "Ref: " + str(ref)
        print "Alpha state: " + str(self.alpha_state)
        if self.alpha_state == 0: 
            glAlphaFunc(GL_NEVER, ref) 
        if self.alpha_state == 1: 
            glAlphaFunc(GL_LESS, ref) 
        if self.alpha_state == 2: 
            glAlphaFunc(GL_EQUAL, ref) 
        if self.alpha_state == 3: 
            glAlphaFunc(GL_LEQUAL, ref) 
        if self.alpha_state == 4: 
            glAlphaFunc(GL_GREATER, ref) 
        if self.alpha_state == 5: 
            glAlphaFunc(GL_NOTEQUAL, ref) 
        if self.alpha_state == 6: 
            glAlphaFunc(GL_GEQUAL, ref) 
        if self.alpha_state == 7: 
            glAlphaFunc(GL_ALWAYS, ref) 
        print "Call drawAlpha()"
        glColor4d(alpha_params[0], alpha_params[1], alpha_params[2], alpha_params[3])
        glBegin(GL_QUADS)
        glVertex3d(20,20,9)
        glVertex3d(-20,20,0 )
        glVertex3d(-20,-20,0)
        glVertex3d(20,-20,9)
        glEnd()
        

    def paintGL(self):
        WfWidget.paintGL(self)

        if self.scissor_state ==  2:
            self.drawScissor()
        else:
            glDisable(GL_SCISSOR_TEST)

        if self.alpha_enable ==  2:
            self.drawAlpha()
        else:
            glDisable(GL_ALPHA_TEST)

        if self.blend_state == 2:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        else:
            glDisable(GL_BLEND)

    def ScissorState (self, state):
        self.hide()
        print "Scissor " + str(state)
        self.scissor_state = state
        self.show()

    def AlphaState(self, state):
        self.hide()
        print "Alpha " + str(state)
        self.alpha_enable = state
        self.show()

    def setAlphaStyle(self, state):
        self.hide()
        self.alpha_state = state 
        print "Alpha " + str(state)
        self.show()
 
    def BlendState(self, state):
        self.hide()
        self.blend_state = state 
        print "Blend state " + str(state)
        self.show()

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
        self.grid.addWidget(self.checkAlpha, 5, 1)

        self.labelAlpha = QtGui.QLabel("Color params for addition figure: ")
        self.grid.addWidget(self.labelAlpha, 6, 1)

        self.alphaParams =  QtGui.QLineEdit()
        self.alphaParams.setValidator(self.validator)
        self.grid.addWidget(self.alphaParams, 7, 1)
        
        self.combo = QtGui.QComboBox()
        self.combo.addItem("GL_NEVER")
        self.combo.addItem("GL_LESS")
        self.combo.addItem("GL_EQUAL")
        self.combo.addItem("GL_LEQUAL")
        self.combo.addItem("GL_GREATER")
        self.combo.addItem("GL_NOTEQUAL")
        self.combo.addItem("GL_GEQUAL")
        self.combo.addItem("GL_ALWAYS")
        self.grid.addWidget(self.combo, 8, 1)
        
        self.checkBlend = QtGui.QCheckBox("Enable blend function")
        self.grid.addWidget(self.checkBlend, 10, 1)

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
                self.inputdata[i] = float(self.inputdata[i])
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
    controlWidget.connect (controlWidget.checkBlend, QtCore.SIGNAL("stateChanged (int)"),
            GLWidget.BlendState)
    controlWidget.show()
    app.exec_()
