import pandas as pd

trees = pd.read_csv('./Trees.csv')
bill = pd.read_csv('./BillData.csv')

avg = bill["Bill"].mean()
plant = avg/1000

newTree = pd.concat([trees,pd.DataFrame({"Trees":[plant]})])
newBill = pd.DataFrame({"Bill":[avg]})

newBill.to_csv('./BillData.csv',index=False)
newTree.to_csv("./Trees.csv",index=False)