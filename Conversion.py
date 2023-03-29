import pandas as pd
name = input("Enter name of the file : ")
sourcePath = "/Users/hemu/Downloads/1/Others/"
data = pd.read_csv(f"{sourcePath}{name}.csv")
destinationPath = "/Users/hemu/Downloads/1/Others/Excel/"
try:
    data.to_excel("{destinationPath}{name}.xlsx",
                  index=None, header=True)
    print("Done")
except:
    print("Error")
