"""
 * Alpha Mask. 
 * 
 * Loads a "mask" for an image to specify the transparency 
 * in different parts of the image. The two images are blended
 * together using the mask() method of PImage. 
 """

img = None
grow = 0
factor = 100
factor_2 = 100

lines = []

rects=[]
a = 0
def setup():
    frameRate(100)
   # fullScreen(2)
    size(800, 600)
    background(0, 0, 0)
    global img
    img = get(0, 0, width, height)
    f = createFont("Helvetica", 78)
    textFont(f)
    textAlign(CENTER, CENTER)

class Line:
    def __init__(self, step=1):
        self.x = 0
        self.y = 0
        self.x_2 = width
        self.step=step
    def update(self):
        self.y += self.step
        return self.y > height/2
    def draw(self):
        stroke(255,255,255)
        strokeWeight(10)
        line(self.x, height/2 - self.y, self.x_2, height/2 - self.y)
        stroke(0)
        line(self.x, height/2 - self.y-10, self.x_2, height/2 - self.y-10)
        stroke(255, 0,0)
        line(self.x, height/2 + self.y, self.x_2, height/2 + self.y)
        stroke(0)
        line(self.x, height/2 + self.y+10, self.x_2, height/2 + self.y+10)

        
class Rect:
    def __init__(self, step=10):
        self.x = 0
        self.y = 0
        self.x_2 = width
        self.step=step
    def update(self):
        self.x += self.step
        return self.x > width/2
    def draw(self):
        strokeWeight(10)
        stroke(0)
        noFill()

        rect(width/2-self.x, 50, self.x*2, height-100)
        stroke(255,255,255)

        rect(width/2-self.x-10, 50, self.x*2+20, height-100)

             

def keyPressed():
    global factor, factor_2, lines
    if key == 'a':
        factor  = max(factor -1, 0)
    elif key == 's':
        factor = min(factor +1, 100)
    elif key=='q':
        factor_2 = max(factor_2 -1, 0)
    elif key=='w':
        factor_2 = min(factor_2+1, 100)
    print(factor, factor_2)
    if key >='1' and key <= '9':
        lines.append(Line(int(key)))
    elif key=='z':
        rects.append(Rect())


def draw():
    global img, grow, factor, factor_2, lines, rects

    radius = int((sin(grow) * factor)+ factor)+1
    radius_2 = int((cos(grow) * factor_2)+ factor_2)+1
    two_radius = radius * 2
    two_radius_2 = radius_2 * 2

    fill(0)
    strokeWeight(30)
    text('BLITZKRIEG\nBOY', width/2, height/2)
    fill(255,0,0)
    text('BLITZKRIEG\nBOY', width/2, height/2+5)
    
    blend(img, 0, 0, width, height, 0,0,width, height, DIFFERENCE)

    img2 = get(radius_2+1, radius_2+1, width-two_radius_2+1, height-two_radius_2+1)

    blend(img, 0, 0, width, height,radius,radius,width-two_radius, height-two_radius, ADD)
    new_lines = []
    for index, l in enumerate(lines):
        if not l.update():
            new_lines.append(l)
        l.draw()
    del lines
    lines = new_lines    
    new_lines = []
    for index, l in enumerate(rects):
        if not l.update():
            new_lines.append(l)
        l.draw()
    del rects
    rects = new_lines
    img = get(radius_2+1, radius_2+1, width-two_radius_2+2, height-two_radius_2+2)
    blend(img2, 1, 1, 2, 2,radius_2,radius_2,width-two_radius_2, height-two_radius_2, DIFFERENCE)

    grow += 0.01

    noFill()#(255)
    strokeWeight(200)
    stroke(0)
    ellipse(width/2, height/2, height+200, height+200) 
    color(0)

    fill(255,0,0)
    #text('BLITZKRIEG\nBOY', width/2, height/2+10)

