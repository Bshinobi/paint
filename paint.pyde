iswhite = True
def setup ():
    size (600, 400)
    background(255, 255, 255)
    fill(0)
    rect(5, 1, 100, 400, 8)
    stroke(255,255,255)
    line(150, 20, 10, 20)
    
    
    
def draw():
    if mousePressed and (mouseButton == CENTER):
        stroke((255), (255), (0))
        line(pmouseX, pmouseY, mouseX, mouseY)
        
        
def mouseClicked():
    global iswhite
    if iswhite :
        print("iswhite true")
        stroke((255), (0), (0))
        iswhite = False
    else:
        print("iswhite false")
        stroke((255), (255), (255))
    
    
    
