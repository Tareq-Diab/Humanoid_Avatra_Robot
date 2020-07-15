import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import math 
from threading import Thread

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
counter =0
def data():
    global counter 
    while True:
        counter +=1
data_thread=Thread(target=data)
xs = [0]
ys = [0]

def animate(i):
    global xs
    global ys
    

    
    x=(math.sin(counter))
    y=counter


    xs.append(float(x))
    ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

data_thread.start()


ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()



