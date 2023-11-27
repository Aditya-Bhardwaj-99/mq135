import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from matplotlib.widgets import CheckButtons, Button
from matplotlib.animation import FuncAnimation

def clear_all(what):
    ds = pd.DataFrame({"Ammonia":[],"Benzene":[],"CO2":[],"Nitrox":[],"Alcohol":[]})
    ds.to_csv('./BufferData.csv',index=False)
    ds2 = pd.DataFrame({"Bill":[]})
    ds2.to_csv('./BillData.csv',index=False)
    ds3 = pd.DataFrame({"Trees":[]})
    ds3.to_csv('./Trees.csv',index=False)

ds = pd.read_csv('./BufferData.csv')
ds2 = pd.read_csv('./BillData.csv')
trees = pd.read_csv('./Trees.csv')
if len(ds["CO2"])>0:
    bill_co2 = ds["CO2"].mean()
    ds3 = pd.DataFrame({"Bill":[bill_co2]})
    plant = bill_co2/200
    newTree = pd.concat([trees,pd.DataFrame({"Trees":[plant]})])
    ds2 = pd.concat([ds2,ds3])
    ds2.to_csv('./BillData.csv',index=False)
trees = pd.read_csv('./Trees.csv')

# figure, axis
fig = plt.figure(num='abc', figsize=(10, 10))
ax = fig.add_subplot(1,1,1)
rax = fig.add_axes([0.03, 0.4, 0.1, 0.1])
# fig.set_size_inches(12,8)
if trees["Trees"].sum() >= 2:
    print_text="Over Polluting!! Please Plant trees"
else:
    print_text=""

text3=fig.text(0.01,0.09,print_text,fontsize=14)
text1=fig.text(0.01,0.01,"Avg Bill:- "+str(ds2["Bill"].mean()),fontsize=14)
text2=fig.text(0.01,0.05,"Total Trees:- "+str(trees["Trees"].sum()),fontsize=14)
fing1, = ax.plot(ds["Ammonia"], 'r', label="Ammonia", marker='s', ms='3')
fing2, = ax.plot(ds["Benzene"], 'g', label="Benzene", marker='s', ms='3')
fing3, = ax.plot(ds["CO2"], 'b', label="CO2", marker='s', ms='3')
fing4, = ax.plot(ds["Nitrox"], 'y', label="Nitrox", marker='s', ms='3')
thumb, = ax.plot(ds["Alcohol"], 'k', label="Alcohol", marker='s', ms='3')
cost, = ax.plot(ds2["Bill"], 'c', label = "Bill", marker='s', ms='3')

lines = [fing1, fing2, fing3, fing4, thumb, cost]


plt.subplots_adjust(left=0.25, bottom=0.1, right=0.95, top=0.95)

Fingers = ["Ammonia", "Benzene", "CO2", "Nitrox", "Alcohol", "Bill"]
btn = Button(rax,"Clear All")
btn.on_clicked(clear_all)

# activated = [True, True, True, True, True]
# Checkbox = plt.axes([0.03, 0.4, 0.15, 0.20])
# chkbox = CheckButtons(Checkbox, Fingers, activated)
#
# def set_visible(finger):
#     index = Fingers.index(finger)
#     lines[index].set_visible(not lines[index].get_visible())
#     plt.draw()


def animate(i):
    ds = pd.read_csv('./BufferData.csv')
    ds2 = pd.read_csv('./BillData.csv')
    trees = pd.read_csv('./Trees.csv')
    if len(ds["CO2"])>0:
        bill_co2 = ds["CO2"].mean()
        ds3 = pd.DataFrame({"Bill":[bill_co2]})
        plant = bill_co2/200
        newTree = pd.concat([trees,pd.DataFrame({"Trees":[plant]})])
        ds2 = pd.concat([ds2,ds3])
        ds2.to_csv('./BillData.csv',index=False)
        newTree.to_csv("./Trees.csv",index=False)
    trees = pd.read_csv('./Trees.csv')
    ax.clear()
    if trees["Trees"].sum() >= 2:
        print_text="Over Polluting!! Please Plant trees"
    else:
        print_text=""
    
    text3.set_text(print_text)
    text1.set_text("Bill:- "+str(ds2["Bill"].mean()))
    text2.set_text("Total Trees:- "+str(trees["Trees"].sum()))
    fing1, = ax.plot(ds["Ammonia"], 'r', label="Ammonia", marker='s', ms='3')
    fing2, = ax.plot(ds["Benzene"], 'g', label="Benzene", marker='s', ms='3')
    fing3, = ax.plot(ds["CO2"], 'b', label="CO2", marker='s', ms='3')
    fing4, = ax.plot(ds["Nitrox"], 'y', label="Nitrox", marker='s', ms='3')
    thumb, = ax.plot(ds["Alcohol"], 'k', label="Alcohol", marker='s', ms='3')
    cost, = ax.plot(ds2["Bill"], 'c', label = "Bill", marker='s', ms='3')
    plt.legend(loc="upper left")
    plt.subplots_adjust(left=0.25, bottom=0.1, right=0.95, top=0.95)

    lines = [fing1, fing2, fing3, fing4, thumb, cost]

    # chkbox.on_clicked(set_visible)




ani = FuncAnimation(fig, animate, 50)
# checkboxes
plt.show()