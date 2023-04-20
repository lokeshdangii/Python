# import xlsxwriter module     
import xlsxwriter    
      
book = xlsxwriter.Workbook('Example2.xlsx')     
sheet = book.add_worksheet()     
       
# Rows and columns are zero indexed.     
row = 5   
column = 0    
      
content = ["Ram", "Shyaam", "Mohan","Lal"]     
      
# iterating through the content list     
for item in content :     
      
    # write operation perform     
    sheet.write(row, column, item)     
      
    # incrementing the value of row by one with each iterations.     
    row += 1    
          
book.close()     