from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mid_line import drawLine
import math
import numpy as np
import random
def line_translate_winter():
    global lines
    glPointSize(10)
    glColor3f(1,1,1)
    t = np.array([[0],[-1],[1]]) # Define t3
    for line in lines:
        v1 = np.array([[line[0]],[line[1]],[1]])
        v2 = np.array([[line[0]+1],[line[1]+1],[1]])
        
        
        # Adjust t to control animation speed
        t[1][0] -= 5# Increase the y-coordinate of t to move the lines downwards faster
        
        v11 = np.add(t,v1)
        v22 = np.add(t,v2)
        glColor3f(1,1,1)
        drawLine(v11[0][0],v11[1][0],v22[0][0],v22[1][0],5)
        
        # Update line position based on y-coordinate of v11
        line[0] = v11[0][0]
        line[1] = v11[1][0]
        if line[1] < 0 :
            line[1] = 780
def line_translate():
    global lines
    glPointSize(1)
    glColor3f(1,1,1)
    t = np.array([[0],[0],[1]]) # Define t
    for line in lines:
        v1 = np.array([[line[0]],[line[1]],[1]])
        v2 = np.array([[line[0]+5],[line[1]+30],[1]])
        
        
        # Adjust t to control animation speed
        t[1][0] -= 2# Increase the y-coordinate of t to move the lines downwards faster
        
        v11 = np.add(t,v1)
        v22 = np.add(t,v2)
        glColor3f(1,1,1)
        drawLine(v11[0][0],v11[1][0],v22[0][0],v22[1][0],1)
        
        # Update line position based on y-coordinate of v11
        line[0] = v11[0][0]
        line[1] = v11[1][0]
        if line[1] < 0 :
            line[1] = 780

        

def generate_lines(num_lines):
    lines = []
    for i in range(num_lines):  
        x = random.randint(0,2500)
        y = random.randint(0,2500)
        lines.append([x, y])
    return lines

def draw_building_1():
  glPointSize(2)
  glColor3f(0.8, 2.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(150, 250):
      midpoint_line(x, 350, x, 550,0)

  # draw the top and bottom horizontal lines
  for y in range(350, 550):
      midpoint_line(150, y, 250, y,0)

  glEnd()

### BUILDING 1 WINDOWS

def draw_window1_B1():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(162, 185):
      midpoint_line(x, 502, x, 540,0)

  # draw the top and bottom horizontal lines
  for y in range(502, 540):
      midpoint_line(162, y, 185, y,0)

  glEnd()

def draw_window2_B1():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(210, 233):
      midpoint_line(x, 502, x, 540,0)

  # draw the top and bottom horizontal lines
  for y in range(502, 540):
      midpoint_line(210, y, 233, y,0)

  glEnd()

def draw_window3_B1():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  for x in range(162, 185):
      midpoint_line(x, 440, x, 478,0)

  # draw the top and bottom horizontal lines
  for y in range(440, 478):
      midpoint_line(162, y, 185, y,0)

  glEnd()

def draw_window4_B1():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(210, 233):
      midpoint_line(x, 440, x, 478,0)

  # draw the top and bottom horizontal lines
  for y in range(440, 478):
      midpoint_line(210, y, 233, y,0)

  glEnd()

def draw_window5_B1():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  for x in range(162, 185):
      midpoint_line(x, 378, x, 416,0)

  # draw the top and bottom horizontal lines
  for y in range(378, 416):
      midpoint_line(162, y, 185, y,0)

  glEnd()

def draw_window6_B1():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  for x in range(210, 233):
      midpoint_line(x, 378, x, 416,0)

  # draw the top and bottom horizontal lines
  for y in range(378, 416):
      midpoint_line(210, y, 233, y,0)

  glEnd()


def draw_building_2():
  glPointSize(2)
  glColor3f(0.8, 2.0, 0.0)
  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(255, 530):
      midpoint_line(x, 350, x, 500,0)

  # draw the top and bottom horizontal lines
  for y in range(350, 500):
      midpoint_line(255, y, 530, y,0)

  glEnd()


#### BUILDING 2 WINDOWS######

def draw_window1_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(270, 330):
      midpoint_line(x, 455, x, 490,0)

  # draw the top and bottom horizontal lines
  for y in range(455, 490):
      midpoint_line(270, y, 330, y,0)

  glEnd()


def draw_window2_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(355, 415):
      midpoint_line(x, 455, x, 490,0)

  # draw the top and bottom horizontal lines
  for y in range(455, 490):
      midpoint_line(355, y, 415, y,0)

  glEnd()


def draw_window3_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(270, 330):
      midpoint_line(x, 405, x, 440,0)

  # draw the top and bottom horizontal lines
  for y in range(405, 440):
      midpoint_line(270, y, 330, y,0)

  glEnd()

def draw_window4_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(270, 330):
      midpoint_line(x, 355, x, 390,0)

  # draw the top and bottom horizontal lines
  for y in range(355, 390):
      midpoint_line(270, y, 330, y,0)

  glEnd()

def draw_window5_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(355, 415):
      midpoint_line(x, 405, x, 440,0)

  # draw the top and bottom horizontal lines
  for y in range(405, 440):
      midpoint_line(355, y, 415, y,0)

  glEnd()

def draw_window6_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(355, 415):
      midpoint_line(x, 355, x, 390,0)

  # draw the top and bottom horizontal lines
  for y in range(355, 390):
      midpoint_line(355, y, 415, y,0)

  glEnd()

def draw_window7_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(440, 500):
      midpoint_line(x, 455, x, 490,0)

  # draw the top and bottom horizontal lines
  for y in range(455, 490):
      midpoint_line(440, y, 500, y,0)

  glEnd()

def draw_window8_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines1
  for x in range(440, 500):
      midpoint_line(x, 405, x, 440,0)

  # draw the top and bottom horizontal lines
  for y in range(405, 440):
      midpoint_line(440, y, 500, y,0)

  glEnd()


def draw_window9_B2():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(440, 500):
      midpoint_line(x, 355, x, 390,0)

  # draw the top and bottom horizontal lines
  for y in range(355, 390):
      midpoint_line(440, y, 500, y,0)

  glEnd()



def draw_building_3():
  glPointSize(2)
  glColor3f(0.8, 2.0, 0.0)
  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(670, 880):
      midpoint_line(x, 350, x, 530,0)

  # draw the top and bottom horizontal lines
  for y in range(350, 530):
      midpoint_line(670, y, 880, y,0)

  glEnd()


#### BUILDING 3 WINDOWS###

def draw_window1_B3():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(680, 758):
      midpoint_line(x, 472, x, 515,0)

  # draw the top and bottom horizontal lines
  for y in range(472, 515):
      midpoint_line(680, y, 758, y,0)

  glEnd()

def draw_window2_B3():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(780, 858):
      midpoint_line(x, 472, x, 515,0)

  # draw the top and bottom horizontal lines
  for y in range(472, 515):
      midpoint_line(780, y, 858, y,0)

  glEnd()

def draw_window3_B3():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(680, 758):
      midpoint_line(x, 419, x, 462,0)

  # draw the top and bottom horizontal lines
  for y in range(419, 462):
      midpoint_line(680, y, 758, y,0)

  glEnd()

def draw_window4_B3():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(780, 858):
      midpoint_line(x, 419, x, 462,0)

  # draw the top and bottom horizontal lines
  for y in range(419, 462):
      midpoint_line(780, y, 858, y,0)

  glEnd()

def draw_window5_B3():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(680, 758):
      midpoint_line(x, 366, x, 409,0)

  # draw the top and bottom horizontal lines
  for y in range(366, 409):
      midpoint_line(680, y, 758, y,0)

  glEnd()

def draw_window6_B3():
  glPointSize(2)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(780, 858):
      midpoint_line(x, 366, x, 409,0)

  # draw the top and bottom horizontal lines
  for y in range(366, 409):
      midpoint_line(780, y, 858, y,0)

  glEnd()

################################################################
def draw_roadline_1():
  glPointSize(4)
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_POINTS)

  x1, y1, x2, y2 = 0, 350, 1000, 350
  midpoint_line(x1, y1, x2, y2,0)

  glEnd()

def draw_roadline_2():
  glPointSize(4)
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_POINTS)

  x1, y1, x2, y2 = 0, 300, 1000, 300
  midpoint_line(x1, y1, x2, y2,0)

  glEnd()


def draw_roadline_3():
  glPointSize(4)
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_POINTS)

  x1, y1, x2, y2 = 0, 80, 1000, 80
  midpoint_line(x1, y1, x2, y2,0)

  glEnd()

def draw_roadline_4():
  glPointSize(4)
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_POINTS)

  x1, y1, x2, y2 = 0, 30, 1000, 30
  midpoint_line(x1, y1, x2, y2,0)

  glEnd()

####################################################################

def draw_lines_1():
  glPointSize(1)
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_POINTS)

  # draw the horizontal lines with a distance of 10 between them
  distance = 10
  for y in range(300, 351, distance):
      midpoint_line(0, y, 1000, y,0)

  glEnd()

def draw_lines_2():
  glPointSize(1)
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_POINTS)

  # draw the horizontal lines with a distance of 10 between them
  distance = 10
  for y in range(30, 81, distance):
      midpoint_line(0, y, 1000, y,0)

  glEnd()


def draw_lines_5():
  glPointSize(1)
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_POINTS)

  x1, y1, x2, y2 = 0, 200, 1000, 200
  midpoint_line(x1, y1, x2, y2,0)

  glEnd()


############################################################################################

############ TREE####################

def draw_tree1_trunk1():
  glPointSize(2)
  glColor3f(0.5, 0.35, 0.05)
  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(60, 80):
      midpoint_line(x, 350, x,470 ,0)

  # draw the top and bottom horizontal lines
  for y in range(350, 470):
      midpoint_line(60, y, 80, y,0)

  glEnd()


def draw_tree2_trunk2():
  glPointSize(2)
  glColor3f(0.5, 0.35, 0.05)
  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(590, 610):
      midpoint_line(x, 350, x, 470,0)

  # draw the top and bottom horizontal lines
  for y in range(350, 470):
      midpoint_line(590, y, 610, y,0)

  glEnd()


def draw_tree3_trunk3():
  glPointSize(2)
  glColor3f(0.5, 0.35, 0.05)
  glBegin(GL_POINTS)

  # draw the left and right vertical lines
  for x in range(940, 960):
      midpoint_line(x, 350, x, 470,0)

  # draw the top and bottom horizontal lines
  for y in range(350, 470):
      midpoint_line(940, y, 960, y,0)

  glEnd()








#################################################################################

def draw_sun():
  glPointSize(7)
  glColor3f(1.7, 0.4, 0.0)
  glBegin(GL_POINTS)

  x_c, y_c = 700, 650  # center coordinates
  radius = 80

  num_circles = 24  # number of smaller circles to draw
  circle_radius = radius / num_circles

  for i in range(num_circles):
      r = radius - i * circle_radius  # radius of current circle
      x = 0
      y = r
      d = 1 - r

      while x <= y:
          glVertex2f(x_c + x, y_c + y)
          glVertex2f(x_c + y, y_c + x)
          glVertex2f(x_c - y, y_c + x)
          glVertex2f(x_c - x, y_c + y)
          glVertex2f(x_c - x, y_c - y)
          glVertex2f(x_c - y, y_c - x)
          glVertex2f(x_c + y, y_c - x)
          glVertex2f(x_c + x, y_c - y)

          x += 1
          if d < 0:
              d += 2 * x + 1
          else:
              y -= 1
              d += 2 * (x - y) + 1

  glEnd()


def midpoint_line(x1, y1, x2, y2, zone):
   # convert endpoints to zone 0

   dx = abs(x2 - x1)
   dy = abs(y2 - y1)

   if zone == 1:
       x1, y1 = y1, x1
       x2, y2 = y2, x2
   elif zone == 2:
       x1, y1 = -y1, x1
       x2, y2 = -y2, x2
   elif zone == 3:
       x1, y1 = -x1, y1
       x2, y2 = -x2, y2
   elif zone == 4:
       x1, y1 = -x1, -y1
       x2, y2 = -x2, -y2
   elif zone == 5:
       x1, y1 = -y1, -x1
       x2, y2 = -y2, -x2
   elif zone == 6:
       x1, y1 = y1, -x1
       x2, y2 = y2, -x2
   elif zone == 7:
       x1, y1 = x1, -y1
       x2, y2 = x2, -y2

   dx = abs(x2 - x1)
   dy = abs(y2 - y1)

   d = 2 * dy - dx
   y = y1

   # convert points back to the desired zone
   for x in range(x1, x2 + 1):
       if zone == 0:
           glVertex2f(x, y)
       elif zone == 1:
           glVertex2f(y, x)
       elif zone == 2:
           glVertex2f(x, -y)
       elif zone == 3:
           glVertex2f(-y, x)
       elif zone == 4:
           glVertex2f(-x, -y)
       elif zone == 5:
           glVertex2f(-y, -x)
       elif zone == 6:
           glVertex2f(-x, y)
       elif zone == 7:
           glVertex2f(y, -x)

       if d >= 0:
           y += 1
           d -= 2 * dx
       d += 2 * dy

angle = 0.0


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def render_frame():
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # Chrismas tree
    def city_winter():
        global angle
        glColor3f(1,1,1)
        drawLine(0,300,1000,300,5)
        draw_tree1_trunk1()

        draw_tree2_trunk2()

        draw_tree3_trunk3()

        
    def city():
        global angle
        glColor3f(1,1,1)
        drawLine(0,300,1000,300,5)
        draw_tree1_trunk1()

        draw_tree2_trunk2()

        draw_tree3_trunk3()

        # Rotate the tree
        glColor3f(0, 1, 0)
        a = math.cos(math.radians(angle))
        b = math.sin(math.radians(angle))
        r = np.array([[a, -b, 0], [b, a, 0], [0, 0, 1]])
        for i in range(0,40):
            v1 = np.array([[20 + i], [400 + i], [1]])
            v2 = np.array([[60], [550 - i], [1]])
            v3 = np.array([[100 - i], [400 + i], [1]])

            v11 = np.matmul(r, v1)
            v22 = np.matmul(r, v2)
            v33 = np.matmul(r, v3)

            glColor3f(0,1,0)

            drawLine(v11[0][0], v11[1][0], v22[0][0], v22[1][0],1)
            drawLine(v11[0][0], v11[1][0], v33[0][0], v33[1][0],1)
            drawLine(v33[0][0], v33[1][0], v22[0][0], v22[1][0],1)

        for i in range(0,50):
            v1 = np.array([[550 + i], [400 + i], [1]])
            v2 = np.array([[600], [500 - i], [1]])
            v3 = np.array([[650 - i], [400 + i], [1]])

            v11 = np.matmul(r, v1)
            v22 = np.matmul(r, v2)
            v33 = np.matmul(r, v3)

            glColor3f(0,1,0)

            drawLine(v11[0][0], v11[1][0], v22[0][0], v22[1][0],1)
            drawLine(v11[0][0], v11[1][0], v33[0][0], v33[1][0],1)
            drawLine(v33[0][0], v33[1][0], v22[0][0], v22[1][0],1)

        for i in range(0,50):
            v1 = np.array([[910 + i], [400 + i], [1]])
            v2 = np.array([[950], [570 - i], [1]])
            v3 = np.array([[990 - i], [400 + i], [1]])

            v11 = np.matmul(r, v1)
            v22 = np.matmul(r, v2)
            v33 = np.matmul(r, v3)

            glColor3f(0,1,0)

            drawLine(v11[0][0], v11[1][0], v22[0][0], v22[1][0],1)
            drawLine(v11[0][0], v11[1][0], v33[0][0], v33[1][0],1)
            drawLine(v33[0][0], v33[1][0], v22[0][0], v22[1][0],1)
        # Increment the angv3 = np.array([[100 - i], [400 + i], [1]])le for the next frame
        
    
    draw_building_1()

    draw_window1_B1()
    draw_window2_B1()
    draw_window3_B1()
    draw_window4_B1()
    draw_window5_B1()
    draw_window6_B1()

    #############################
    draw_building_2()

    draw_window1_B2()
    draw_window2_B2()
    draw_window3_B2()
    draw_window4_B2()
    draw_window5_B2()
    draw_window6_B2()
    draw_window7_B2()
    draw_window8_B2()
    draw_window9_B2()

    ###########################

    draw_building_3()

    draw_window1_B3()
    draw_window2_B3()
    draw_window3_B3()
    draw_window4_B3()
    draw_window5_B3()
    draw_window6_B3()
    ###################################################

    draw_roadline_1()
    draw_roadline_2()
    draw_roadline_3()
    draw_roadline_4()
    # draw_line_5()

    draw_lines_1()
    draw_lines_2()
    draw_lines_5()
    
    global angle
        
    if user =='1':
        draw_sun()
        city()
        
        angle += 0.0
        if angle >= 1:
            angle = 0
    elif user=="2":
        city()
        
        angle += 0.9
        if angle >= 1:
            angle = 0
            
        line_translate()
    elif user=="3":
        city_winter()
        
        angle += 0.0
        if angle >= 1:
            angle = 0
        line_translate_winter()
        
        


    glutSwapBuffers()

def idle_func():
    glutPostRedisplay()

def main():
    
    global lines,user
    lines = generate_lines(1000)
    user = input('1) Summemr 2) Rainy 3) winter')
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1024, 768)
    glutCreateWindow(b"Rain Animation")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glutDisplayFunc(render_frame)
    glutIdleFunc(idle_func)
    
    glutMainLoop()

if __name__ == '__main__':
    main()
    
