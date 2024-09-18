print("\t\t\t LEE Pizzas\t")
print()
print()
print() 
A  = int(input('''  Welcome sir!
\t How are you sir?
\t Which type of Pizza do you want?

\t   1 . Small (Price rs.80)

\t   2 . Medium (Price rs.100)

\t   3 . Large (Price rs.150)


\t Enter The number  to select :'''))
print()

match A:
    case 1 :
        print("\tYou have selected Small pizza ")
        print()
        B = int(input("\t How many  do you want?"))
        print()
        C = int(input('''\t Do you want any Add-on's like

\t   1. Extra cheese (Rs. 20)

\t   2 . Extra Toppings (Rs. 40)

\t   3 . Extra Sauces (Rs. 10)

\t   4 . I don't need any Add-on's

\t Enter an number to select :'''))
        print()

        match C:
            case 1 :
                print("\tOk sir you have an Extra cheese")
                print()
                print("\t    Your total bill is:")
                print("\t small  :   80* ",B," : ",80*B)
                print("\t Extra cheese :20*",B," :",20*B)
                print("\t-----------------------")
                print("\t Total           : ",80*B+20)
                print("Please wait your order is being cooked")
            case 2 :
                print("\tOk sir you have an Extra Toppings")
                print()
                print("\t    Your total bill is:")
                print("\t small  :  80* ",B," : ",80*B)
                print("\t Extra Topping:40*",B,":",40*B)
                print("\t-----------------------")
                print("\t Total           : ",80*B+40)
                print("Please wait your order is being cooked")
            case 3 :
                print("\tOk sir you have an Extra sauces")
                print()
                print("\t    Your total bill is:")
                print("\t small  :  80* ",B," : ",80*B)
                print("\t Extra Sauces:10*",B,":",10*B)
                print("\t-----------------------")
                print("\t Total           : ",80*B+10)
                print("Please wait your order is being cooked")
            case 4 :
                print("\tOk sir you don't have any Add-on's")
                print()
                print("\t    Your total bill is:")
                print("\t small  : 80*",B," : ",80*B)
                print("\t-----------------------")
                print("\t Total           : ",80*B)
                print("Please wait your order is being cooked")

    case 2 :
        print("\tYou have selected Medium pizza ")
        print()
        B = int(input("\t How many do you want?"))
        print()
        C = int(input('''\t Do you want any Add-on's like

\t   1. Extra cheese (Rs. 20)

\t   2 . Extra Toppings (Rs. 40)

\t   3 . Extra Sauces (Rs. 10)

\t   4 . I don't need any Add-on's

\t Enter an number to select :'''))
        print()

        match C:
            case 1 :
                print("\tOk sir you have an Extra cheese")
                print()
                print("\t    Your total bill is:")
                print("\t Medium  :   100* ",B," : ",100*B)
                print("\t Extra cheese :20*",B," :",20*B)
                print("\t-----------------------")
                print("\t Total           : ",100*B+20)
                print("Please wait your order is being cooked")
            case 2 :
                print("\tOk sir you have an Extra Toppings")
                print()
                print("\t    Your total bill is:")
                print("\t Medium  :  100* ",B," : ",100*B)
                print("\t Extra Topping:40*",B,":",40*B)
                print("\t-----------------------")
                print("\t Total           : ",100*B+40)
                print("Please wait your order is being cooked")
            case 3 :
                print("\tOk sir you have an Extra sauces")
                print()
                print("\t    Your total bill is:")
                print("\t Medium  :  100* ",B," : ",100*B)
                print("\t Extra Sauces:10*",B,":",10*B)
                print("\t-----------------------")
                print("\t Total           : ",100*B+10)
                print("Please wait your order is being cooked")
            case 4 :
                print("\tOk sir you don't have any Add-on's")
                print()
                print("\t    Your total bill is:")
                print("\t Medium  : 100*",B," : ",100*B)
                print("\t-----------------------")
                print("\t Total           : ",100*B)
                print("Please wait your order is being cooked")


    case 3 :
        print("\tYou have selected Large pizza ")
        print()
        B = int(input("\t How many do you want?"))
        print()
        C = int(input('''\t Do you want any Add-on's like

\t   1. Extra cheese (Rs. 20)

\t   2 . Extra Toppings (Rs. 40)

\t   3 . Extra Sauces (Rs. 10)

\t   4 . I don't need any Add-on's

\t Enter an number to select :'''))
        print()

        match C:
            case 1 :
                print("\tOk sir you have an Extra cheese")
                print()
                print("\t    Your total bill is:")
                print("\t Large  :   150* ",B," : ",150*B)
                print("\t Extra cheese :20*",B," :",20*B)
                print("\t-----------------------")
                print("\t Total           : ",150*B+20)
                print("Please wait your order is being cooked")
            case 2 :
                print("\tOk sir you have an Extra Toppings")
                print()
                print("\t    Your total bill is:")
                print("\t Large  :  150* ",B," : ",150*B)
                print("\t Extra Topping:40*",B,":",40*B)
                print("\t-----------------------")
                print("\t Total           : ",150*B+40)
                print("Please wait your order is being cooked")
            case 3 :
                print("\tOk sir you have an Extra sauces")
                print()
                print("\t    Your total bill is:")
                print("\t Large  :  150* ",B," : ",150*B)
                print("\t Extra Sauces:10*",B,":",10*B)
                print("\t-----------------------")
                print("\t Total           : ",150*B+10)
                print("Please wait your order is being cooked")
            case 4 :
                print("\tOk sir you don't have any Add-on's")
                print()
                print("\t    Your total bill is:")
                print("\t Large  : 150*",B," : ",150*B)
                print("\t-----------------------")
                print("\t Total           : ",150*B)
                print("Please wait your order is being cooked")

    case _ :
        print("Sorry!You have entered Wrong number please Enter an number between  1,2 and 3")


        

                
                


                
            

            
                
