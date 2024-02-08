import graphics as gr
import tkinter as tr
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

def sqware(block):
    return abs(block.p2.x-block.p1.x)*abs(block.p2.y-block.p1.y)

def move(s_out, s_in):
    if not s_out:
        print('Нечего перекладывать!')
    elif not s_in:
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
        print(f'Перекложили {b} иЗ {s_out} в {s_in}')
    elif sqware(s_in[-1]) > sqware(s_out[-1]):
        print('Переклали')
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
        print(f'Перекложили {b} из {s_out} в {s_in}')
    else:
        print('Так не пойдет!')



st1 = [block1,block2, block3]
st2 = []
st3 = []







if block1 in st1:
    block1.move(0, 0)
elif block1 in st2:
    block1.move(150, 0)
elif block1 in st3:
    block1.move(300, 0)

if block2 in st1:
    block2.move(0,20)
elif block2 in st2:
    block2.move(150, 20)
elif block2 in st3:
    block2.move(300,20)

if block3 in st1:
    block3.move(0, 40)
elif block2 in st2
    block3.move(150, 40)
elif block3 in st3:
    block3.move(300, 40)



arr1 = tr.PhotoImage(file = r"F:\PYTHON\pyton\hanoy_tower\2.png")
arr2 =tr.PhotoImage(file = r"F:\PYTHON\pyton\hanoy_tower\98.jpg")

button1 = tr.Button(window, image=arr1, command = lambda: move(st1, st3)).place(x=100, y=200)
button2 = tr.Button(window, image=arr2, command = lambda: move(st1, st2)).place(x=160, y=200)
button3 = tr.Button(window, image=arr1, command = lambda: move(st2, st1)).place(x=250, y=200)
button4 = tr.Button(window, image=arr2, command = lambda: move(st2, st3)).place(x=310, y=200)
button5 = tr.Button(window, image=arr1, command = lambda: move(st3, st2)).place(x=400, y=200)
button6 = tr.Button(window, image=arr2, command = lambda: move(st3, st1)).place(x=460, y=200)






window.getMouse()
window.close()
