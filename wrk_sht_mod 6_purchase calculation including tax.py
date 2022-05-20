










    
    
    







rs = 'yes'
    
    
    

while rs == 'yes':

    print('--State Tax and Sales Tax calculator---\n')




#    print("""*IF YOU DO NOT KNOW YOUR STATE TAX TYPE "1",TO SEE A LIST OF STATE TAX*\n""")
    sst_tx = float(input('1) What is the state tax\n: ' ))
    if sst_tx == 1:
        print(st_tx)
        sst_tx = float(input('1) What is the state tax\n: ' ))
    ct_tx = float(input('2) what is the city sales tax\n:  '))
    
    


#creating the variables for the total cost and teh tax totals while
#creating an input for the dollar amount.


    tl_cst = float(input("Please enter the cost of your item:$"))

    txt =float(ct_tx + sst_tx)

    total_std = float( txt * tl_cst)

    sub = float(total_std - tl_cst )

    print(sep = ' ')
    
    print ('Your total amount for this item is :$',format(tl_cst + total_std,'.2f'))

    print(sep=' ')
    
    print('The diffrence is $',format(total_std,'.2f'))

    print(sep= '')
    
    rs = input("""Enter "yes" or "no" if you want to continue: """)

    print(sep=' ')

if rs == 'no':
    print('Thank you have a good day')
  


