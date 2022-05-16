import pygame

screenHeight = 400
screenWidth = 700

#loading images and game sizing
screen = pygame.display.set_mode((screenWidth, screenHeight))

bookshelfOne = pygame.image.load("bookshelf1.jpeg").convert()
bookshelfTwo = pygame.image.load("bookshelf2.jpg").convert()
bookshelfThree = pygame.image.load("bookshelf3.jpeg").convert()
bookshelfFour = pygame.image.load("bookshelf4.jpeg").convert()
bookshelfFive = pygame.image.load("bookshelf5.jpeg").convert()
bookshelfSix = pygame.image.load("bookshelf6.jpeg").convert()

leftArrow = pygame.image.load("leftArrow.jpg").convert()
rightArrow = pygame.image.load("rightArrow.jpg").convert()

leverOn = pygame.image.load("leverOn.png").convert()
leverOff = pygame.image.load("leverOff.png").convert()

oneOClock = pygame.image.load("1clock.png").convert()
twoOClock = pygame.image.load("2clock.png").convert()

#we have duplicates of three and four o'clock because of the wall needing two clocks

threeOClock = pygame.image.load("3clock.png").convert()
threeOClock2 = pygame.image.load("3clock2.png").convert()

fourOClock = pygame.image.load("4clock.png").convert()
fourOClock2 = pygame.image.load("4clock2.png").convert()

fiveOClock = pygame.image.load("5clock.png").convert()
sixOClock = pygame.image.load("6clock.png").convert()
sevenOClock = pygame.image.load("7clock.png").convert()
eightOClock = pygame.image.load("8clock.png").convert()
nineOClock = pygame.image.load("9clock.png").convert()
tenOClock = pygame.image.load("10clock.png").convert()
elevenOClock = pygame.image.load("11clock.png").convert()
twelveOClock = pygame.image.load("12clock.png").convert()

#classes
class imageScaling():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self):
     screen.blit(self.image, (self.rect.x, self.rect.y))


class Button():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self):
    action = False
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        action = True

      if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False

    screen.blit(self.image, (self.rect.x, self.rect.y))
    return action

bookshelfOne = imageScaling(0, 0, bookshelfOne, 3)
bookshelfTwo = imageScaling(0, 0, bookshelfTwo, 3)
bookshelfThree = imageScaling(0, 0, bookshelfThree, 3)
bookshelfFour = imageScaling(0, 0, bookshelfFour, 3)
bookshelfFive = imageScaling(0, 0, bookshelfFive, 3)
bookshelfSix = imageScaling(0, 0, bookshelfSix, 3)
leftArrow = Button(100, screenHeight/2, leftArrow, 0.3)
rightArrow = Button(600, screenHeight/2, rightArrow, 0.3)
leverOn = Button(550, 90, leverOn, 1)
leverOff = Button(550, 90, leverOff, 1)

#adding clock times individually to test
oneOClock = imageScaling(390, 40, oneOClock, 0.5)
twoOClock = imageScaling(390, 40, twoOClock, 0.5)
threeOClock = imageScaling(390, 40, threeOClock, 0.5)
fourOClock = imageScaling(390, 40, fourOClock, 0.5)
fiveOClock = imageScaling(390, 40, fiveOClock, 0.5)
sixOClock = imageScaling(390, 40, sixOClock, 0.5)
sevenOClock = imageScaling(390, 40, sevenOClock, 0.5)
eightOClock = imageScaling(390, 40, eightOClock, 0.5)
nineOClock = imageScaling(390, 40, nineOClock, 0.5)
tenOClock = imageScaling(390, 40, tenOClock, 0.5)
elevenOClock = imageScaling(390, 40, elevenOClock, 0.5)
twelveOClock = imageScaling(390, 40, twelveOClock, 0.5)

threeOClock2 = imageScaling(160, 40, threeOClock2, 0.5)
fourOClock2 = imageScaling(275, 40, fourOClock2, 0.5)

imageList = [bookshelfOne, bookshelfTwo, bookshelfThree, bookshelfFour, bookshelfFive, bookshelfSix]
clockTimes = [oneOClock, twoOClock, threeOClock, fourOClock, fiveOClock, sixOClock, sevenOClock, eightOClock, nineOClock, tenOClock, elevenOClock, twelveOClock]

clockIndex = 11
imageIndex = 0
#bookshelfOne.draw()
#leftArrow.draw()



run = True
imageOne = True
clocksIteration = True

while run:
  while imageOne == True:
    imageList[imageIndex].draw()
    leftArrow.draw()
    rightArrow.draw()
    imageOne = False
    
  if imageIndex == 1 and clocksIteration == True:
    threeOClock2.draw()
    fourOClock2.draw()
    clockTimes[clockIndex].draw() 
    clocksIteration = False

  #for all rooms
  if leftArrow.draw():
    print('left arrow clicked')
    if imageIndex == 0:
      imageIndex = len(imageList) - 1
    if imageIndex == 2:
      clocksIteration = True
      imageIndex -= 1
    else:
      imageIndex -= 1
    screen.fill((0, 0, 0, 0))
    imageList[imageIndex].draw()
    print(imageIndex)

  if rightArrow.draw():
    print('right arrow clicked')
    if imageIndex == len(imageList)-1:
      imageIndex = 0
    if imageIndex == 0:
      clocksIteration = True
      imageIndex += 1
    else:
      imageIndex += 1
    screen.fill((0, 0, 0, 0))
    imageList[imageIndex].draw()
    print(imageIndex)
    
  pygame.display.update()
  for event in pygame.event.get():
      #pygame.quit() will run and close window
    print(event)
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      x, y = event.pos
      if imageIndex == 1:
        rect = pygame.draw.rect(screen, (255, 255, 255, ), pygame.Rect(390, 39, 115, 114), 2)
        if rect.collidepoint(x, y):
          print("clock clicked")
          if clockIndex == 11:
            clockIndex = 0
            clockTimes[clockIndex].draw()
          else:
            clockIndex+=1
            clockTimes[clockIndex].draw()
  
    #im just testing events in for loop and using that to check if clock clicked

pygame.quit()
