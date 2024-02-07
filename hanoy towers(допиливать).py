import graphics as gr
window = gr.GraphWin('HanoyTowers', 600, 600)
osnovanie = gr.Rectangle(gr.Point(100, 500), gr.Point(500, 600)).draw(window)
osnovanie.setFill('black')
stolb1 = gr.Line(gr.Point(150, 500), gr.Point(150, 200)).draw(window)
stolb2 = gr.Line(gr.Point(300, 500), gr.Point(300, 200)).draw(window)
stolb3 = gr.Line(gr.Point(450, 500), gr.Point(450, 200)).draw(window)

block1 = gr.Rectangle(gr.Point(100, 500), gr.Point(200, 480)).draw(window)
block1.setFill('red')
block2 = gr.Rectangle(gr.Point(125, 480), gr.Point(175, 460)).draw(window)
block2.setFill('green')
block3 = gr.Rectangle(gr.Point(140, 460), gr.Point(160, 440)).draw(window)
block3.setFill('yellow')

 
while True:
    
    clickPoint = window.getMouse()
    print(clickPoint)
    if block2.getP1().getX() < clickPoint.getX() < block2.getP2().getX() and block2.getP1().getY() < clickPoint.getY() < block2.getP2().getY():
        block2.move()
    # # elif block2.getP1().getX() < clickPoint.getX() < block2.getP2().getX() and block2.getP1().getY() < clickPoint.getY() < block2.getP2().getY():
    # #     block2.move(150, 0)
    # # elif block1.getP1().getX() < clickPoint.getX() < block1.getP2().getX() and block1.getP1().getY() < clickPoint.getY() < block1.getP2().getY():
    # #     block2.move(150, 0)
    

window.getMouse()
window.close()