"""
 * Alpha Mask. 
 * 
 * Loads a "mask" for an image to specify the transparency 
 * in different parts of the image. The two images are blended
 * together using the mask() method of PImage. 
 """

img = None
grow = 0
step = 0.01
factor = 100
factor_2 = 1

lines = []

rects=[]
texts = ['BLITSKRIEG\nBOY', 'RANTICHRIST']
text_index = 0
a = 0
def setup():
    frameRate(100)
    fullScreen(2)
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
        stroke(0,0,0)
        strokeWeight(10)
        line(self.x, height/2 - self.y, self.x_2, height/2 - self.y)
        stroke(0)
        line(self.x, height/2 - self.y-10, self.x_2, height/2 - self.y-10)
        stroke(0, 255,0)
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
        stroke(255,0,0)

        rect(width/2-self.x-10, 50, self.x*2+20, height-100)

             

def keyPressed():
    global factor, factor_2, lines, step, text_index
    if key == 'a':
        factor  = max(factor -1, 0)
    elif key == 's':
        factor = min(factor +1, 150)
    elif key=='q':
        factor_2 = max(factor_2 -1, 0)
    elif key=='w':
        factor_2 = min(factor_2+1, 150)
    elif key=='x':
        step = max(step-0.0001, 0.0001)
    elif key=='c':
        step = min(step+0.0001, 1.0)
    elif key=='v':
        text_index = int(not text_index)
    print(factor, factor_2, step)
    if key >='1' and key <= '9':
        lines.append(Line(int(key)))
    elif key=='z':
        rects.append(Rect())


def draw():
    global img, grow, factor, factor_2, lines, rects, step, text_index, texts
    t = texts[text_index]
    radius = int((sin(grow) * factor)+ factor)+1
    radius_2 = int((cos(grow) * factor_2)+ factor_2)+1
    two_radius = radius * 2
    two_radius_2 = radius_2 * 2

    blend(img, 0, 0, width, height, 0,0,width, height, SCREEN)

    img2 = get(radius_2+1, radius_2+1, width-two_radius_2+1, height-two_radius_2+1)

    blend(img, 0, 0, width, height,radius,radius,width-two_radius, height-two_radius, DIFFERENCE)

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
    blend(img2, 1, 1, 2, 2,radius_2,radius_2,width-two_radius_2, height-two_radius_2, DIFFERENCE)
    img = get(radius_2+1, radius_2+1, width-two_radius_2+2, height-two_radius_2+2)

    grow += step

    noFill()#(255)
    strokeWeight(300)
    stroke(0)
    ellipse(width/2, height/2, height+250, height+250) 
    color(0)

    #text('BLITZKRIEG\nBOY', width/2, height/2+10)