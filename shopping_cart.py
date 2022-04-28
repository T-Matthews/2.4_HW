from random import random


def random_shopping():
    """
    This function allows the user to input any string as a purchase item, to add
    to their cart, with adaptive responses based on plurality. The item is stored in
    a dictionary, with a random cost from 0-100 dollars asigned, and added to the 
    total. Items can be removed.

    Im pretty happy with this project, although the 2 main issues i am still struggling with:
    1) UNDERLINING LOOKS WEIRD ON 'y' and 'q' especially. Wish it looked the same
            as the underscore character. Run option 3, and look at the column headings.
    2) LEAVING TRAILING '0's ON ROUNDED #S!! I could NOT figure out a way to keep the
            2nd decimal place if it was a 0. 78.80 would become 78.8, and this throws off
            the grid in option 3. Add 10 of any item to the cart to see what I mean.
    """
    #create an empty dictionary, an active user flag, and total cost variable.
    s_cart = {}
    active = True
    
    print("\n\n______________________________________\n\nWelcome to Rand_Co, where all prices are random from $1-$100!\n"
         +"Maybe you\'ll get lucky today! please select from the following options:")
    while active == True:
        #total cost is used in a couple places, and needs to be recalculated each iteration.
        total_cost=0
        for k in s_cart:
            s_cart[k][1]=int(s_cart[k][1])
            total_cost+=s_cart[k][0]*s_cart[k][1]
        choice1 = input('\n\n            -----Options-----\n\t[1] Add Item to Cart\n\t[2] Remove Item from Cart\n\t[3]'
             +' View Cart\n\t[4] Quit/Check Out\n\n')
        #Choice 1: Add item to cart. If else used to allow user to quit back to the menu.
        if choice1 == "1":
            new_item=input('\nLet\'s do it! What would you like to purchase today?\n')
            if new_item.lower() == 'quit':
                break
            else:
                #Creating random value from 1-100 to assign to the item.
                cost=round(random()*100,2)
                #Create key value dictionary pair with item name(lowercase) as the key.
                s_cart[new_item.lower()]=cost
                plural_flag=False
                if new_item.lower()[len(new_item)-1] =="s":
                    plural_flag=True
                #Create if conditions to change text output based on quantity purchased and plurality of input. 
                if cost < 35 and plural_flag == False:
                    print(f'\nGreat purchase, those {new_item.lower()}s will only set you back ${cost} each.\nQuite a deal!')
                elif cost < 35 and plural_flag == True:
                    print(f'\nGreat purchase, those {new_item.lower()} will only set you back ${cost} each.\nQuite a deal!')
                elif cost <65 and plural_flag == False:
                    print(f'\nPretty average price, those {new_item.lower()}s will cost you ${cost}.\nYou may have better prices if you keep shopping!')    
                elif cost <65 and plural_flag == True:
                    print(f'\nPretty average price, those {new_item.lower()} will cost you ${cost}.\nYou may have better prices if you keep shopping!')
                elif cost >= 65 and plural_flag == False:
                    print(f'\nYikes that\'s expensive! Those {new_item.lower()}s will cost you ${cost}.\nCan\'t do much worse than that!')
                else:
                    print(f'\nYikes those are expensive! Those {new_item.lower()} will cost you ${cost}.\nCan\'t do much worse than that!')
                quantity=input('\nHow many would you like to purchase?\n\n')
                #Quantity needs to be an integer, so a try except block was added to attempt to prevent other input.
                try:
                    quantity=int(quantity)
                except:
                    print(f'Sorry, try again! Your input, {quantity}, needs to be an integer.')       
                #add item quantity to the dictionary, creating a {<key == item_name> : [<cost>,<quantity>,<length of item title>]} dictionary structure.
                #The length of item name will be used to format the option 3, when they go to look at their cart.
                s_cart[new_item.lower()] = [cost,quantity,len(new_item)]
                print()
                total_cost+=round(cost*quantity,2)
                if quantity == 1 and plural_flag == False:
                    print(f'Great! You purchased one {new_item} for ${cost}.'
                    +f'You now have ${round(total_cost,2)} worth of goods in your cart.')
                elif quantity>1 and plural_flag ==False:
                    print(f'Great! You purchased those {str(quantity)} {new_item}s for  ${cost} each, totaling ${round(quantity*cost,2)}.\n'
                    +f'You now have ${round(total_cost,2)} worth of goods in your cart.')
                else:
                    print(f'Great! You purchased those {str(quantity)} {new_item} for  ${cost} each, totaling ${round(quantity*cost,2)}.\n'
                    +f'You now have ${round(total_cost,2)} worth of goods in your cart.')
            
        if choice1 == "2":
                print('Your current cart items are:\n')
                for k in s_cart:
                    print(k.title())
                remove_item=input('\nW\u0332H\u0332I\u0332C\u0332H\u0332 I\u0332T\u0332E\u0332M\u0332 would you like to remove?\n')
                if s_cart[remove_item.lower()]:
                    rem_item_qty=int(input('H\u0332O\u0332W\u0332 M\u0332A\u0332N\u0332Y\u0332 would you like to remove?'))
                    if rem_item_qty>s_cart[remove_item][1]:
                        del s_cart[remove_item]
                        print('That\'s more than you had in your basket, but all have been removed.')
                    elif rem_item_qty==s_cart[remove_item][1]:
                        del s_cart[remove_item]
                        print(f'Sounds good, all of your {remove_item} have been removed')
                    else:
                        s_cart[remove_item][1] = s_cart[remove_item][1] - rem_item_qty
                        print(f'Sounds good, {rem_item_qty} {remove_item} have been removed from your cart.\n'
                        +f'You have {s_cart[remove_item][1]} {remove_item} remaining.')
                else:
                    print('Sorry! That item is not in your cart.')

        if choice1 == "3":   
            print('Your cart consists of the following:\n')
            #The following horrible line of code creates the table that I am trying to use to display cart items. Underlined text looks funky, but better than nothing...
            print('\ni\u0332t\u0332e\u0332m\u0332__________________|\u0332c\u0332o\u0332s\u0332t\u0332___|\u0332q\u0332t\u0332y\u0332__|\u0332t\u0332o\u0332t\u0332a\u0332l\u0332____')
            for k in s_cart:
                #calculating the correct number of spaces between the item name and the cost in the table. The other spacings hopefully can be automated.
                spaces=22-int(s_cart[k][2])
                #need to make sure that the quantity prints with a '0' in front, if less than 10, for spacing on the table.
                if int(s_cart[k][1])<9 and int(s_cart[k][1])>0:
                    s_cart[k][1]='0'+str(s_cart[k][1])
                    #print item, cost, quantity and total in the correct tabular formatting
                print(f"{k.title()}{spaces*' '}|{s_cart[k][0]}  |{s_cart[k][1]}   |${round(s_cart[k][0]*int(s_cart[k][1]),2)}")
            #once the loop has run, print a breaker line followed by the grand total, referencing the total_cost variable.
            print(f'______________________________________________\nGRAND TOTAL                         |${round(total_cost,2)}')
            s_cart[k][1]=int(s_cart[k][1])

        if choice1 == "4":
            return f'Thank you for shopping with us! Your total comes to ${round(total_cost,2)}.'

  
      
print(random_shopping())
