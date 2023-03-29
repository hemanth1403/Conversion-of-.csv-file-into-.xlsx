# Conversion-of-.csv-file-into-.xlsx

Using pandas library we can convert .csv files into excel files i.e .xlsx format

1. Read the file which is in csv format
```python
 data = pd.read_csv(f"{sourcePath}{name}.csv")
 ```
 2. convert it into .xlsx format by using to_excel() function which takes the parameters as excel_writer[destination path along with the filename as shown below], sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True
 ```python
 data.to_excel("{destinationPath}{name}.xlsx",index=None, header=True)
 ```
 excel_writer is the mandatory parameter and the rest of all are optional.
