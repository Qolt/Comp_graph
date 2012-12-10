import sys
import string
from OpenGL.GL import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtOpenGL import *

params = []

class WfWidget(QGLWidget):
    def __init__(self, parent = None):
        super(WfWidget, self).__init__(parent)
        self.obj = "points"

    def drawPoints(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glPointSize(6)
        glBegin(GL_POINTS)
        glColor4d(10, 0, 0, 0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def drawLines(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_LINES)
        glColor4d(0,10,0,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def drawStripLines (self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_LINE_STRIP)
        glColor4d(0,0,10,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def drawLoopLines(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_LINE_LOOP)
        glColor4d(10,0,0,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def drawTriangles(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, -20, -20, 0, 0, -20, 0, 30, 30, 0, 1, 1, 0, 0, 30, 0]
        glBegin(GL_TRIANGLES)
        glColor4d(0,10,10,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()
        
    def drawStripTriangles(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_TRIANGLE_STRIP)
        glColor4d(0,0,10,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()  

    def drawTrianglesFan(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_TRIANGLE_FAN);
        glColor4d(0,0,10,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def drawQuads(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [20, 20, 0, -20, 20, 0, -20, -20, 0, 20, -20, 0, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_QUADS);
        glColor4d(10,0,10,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def drawQuadStrip(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_QUAD_STRIP);
        glColor4d(0,10,0,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def drawPolygon(self):
        coord = []
        global params
        coord = params
        if coord == []:
            coord = [0, 0, 0, 20, 20, 20, -20, -20, 30, -30, 30, 5, 5, 30, -30, 0, 10, 10, 0]
        glBegin(GL_POLYGON);
        glColor4d(0,0,10,0.3)
        for i in range (0, len(coord)-2, 3):
            glVertex3d(coord[i],coord[i+1],coord[i+2])
        glEnd()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if self.obj == "points":
            self.drawPoints()
        if self.obj == "lines":
            self.drawLines()
        if self.obj == "strip_lines":
            self.drawStripLines()
        if self.obj == "loop_lines":
            self.drawLoopLines()
        if self.obj == "triangles":
            self.drawTriangles()
        if self.obj == "strip_triangles":
            self.drawStripTriangles()
        if self.obj == "triangles_fan":
            self.drawTrianglesFan()
        if self.obj == "quads":
            self.drawQuads()
        if self.obj == "quads_strip":
            self.drawQuadStrip()
        if self.obj == "polygon":
            self.drawPolygon()
        
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        glViewport(0, 0, w, h)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def ShowPoints(self):
        self.hide()
        self.obj = "points"
        print (self.obj)
        self.show() 

    def ShowLines(self):
        self.hide()
        self.obj = "lines"
        print (self.obj)
        self.show() 

    def ShowStripLines(self):
        self.hide()
        self.obj = "strip_lines"
        print (self.obj)
        self.show() 

    def ShowLoopLines(self):
        self.hide()
        self.obj = "loop_lines"
        print (self.obj)
        self.show() 

    def ShowTriangles(self):
        self.hide()
        self.obj = "triangles"
        print (self.obj)
        self.show() 

    def ShowStripTriangles(self):
        self.hide()
        self.obj = "strip_triangles"
        print (self.obj)
        self.show() 
        
    def ShowTrianglesFan(self):
        self.hide()
        self.obj = "triangles_fan"
        print (self.obj)
        self.show() 
    
    def ShowQuads(self):
        self.hide()
        self.obj = "quads"
        print (self.obj)
        self.show() 
    
    def ShowQuadsStrip(self):
        self.hide()
        self.obj = "quads_strip"
        print (self.obj)
        self.show() 
    
    def ShowPolygon(self):
        self.hide()
        self.obj = "polygon"
        print (self.obj)
        self.show() 
    
class ControlWindow(QtGui.QWidget):
    def __init__ (self, parent=None):
        self.inputdata = []
        QtGui.QWidget.__init__(self, parent)

        self.grid = QtGui.QGridLayout()

        self.label = QtGui.QLabel("Enter coordinats here:")
        self.btnPoints= QtGui.QPushButton("Draw points")
        self.btnLines= QtGui.QPushButton("Draw lines")
        self.btnStripLines= QtGui.QPushButton("Draw strip lines")
        self.btnLoopLines= QtGui.QPushButton("Draw loop lines")
        self.btnTriangles= QtGui.QPushButton("Draw triangles")
        self.btnStripTriangles= QtGui.QPushButton("Draw strip triangles")
        self.btnStripTrianglesFan= QtGui.QPushButton("Draw triangles fans")
        self.btnQuads= QtGui.QPushButton("Draw quads")
        self.btnQuadsStrip= QtGui.QPushButton("Draw strip quads")
        self.btnPolygon= QtGui.QPushButton("Draw polygon")
        self.txtLabel = QtGui.QLineEdit()
        self.validator = QtGui.QRegExpValidator(QtCore.QRegExp("((\-?\d+(\.\d{0,})?)[ ]?){0,99}"))
        self.txtLabel.setValidator(self.validator)
        self.grid.addWidget(self.label)
        self.grid.addWidget(self.txtLabel)
        self.grid.addWidget(self.btnPoints)
        self.grid.addWidget(self.btnLines)
        self.grid.addWidget(self.btnStripLines)
        self.grid.addWidget(self.btnLoopLines)
        self.grid.addWidget(self.btnTriangles)
        self.grid.addWidget(self.btnStripTriangles)
        self.grid.addWidget(self.btnStripTrianglesFan)
        self.grid.addWidget(self.btnQuads)
        self.grid.addWidget(self.btnQuadsStrip)
        self.grid.addWidget(self.btnPolygon)
        self.setLayout(self.grid)


    def SetParams(self):
       global params
       self.inputdata = string.split(str(self.txtLabel.text()), " ")
       for i, item  in enumerate(self.inputdata):
            try:
                self.inputdata[i] = float(self.inputdata[i])
                self.inputdata.remove('')
            except:
                pass
       if self.inputdata == ['']:
            self.inputdata = []
       print ("Set Params: " , str(self.inputdata))
       params = self.inputdata

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GLWidget = WfWidget()
    controlWidget = ControlWindow()
    controlWidget.resize(300, 70)
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
    controlWidget.show()
    app.exec_()
