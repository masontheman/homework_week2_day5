def main():
    total_money = 0.00
    firstInput = ''
    print('Welcome to the Dollar Tree!\n###########################')
    dictionary_of_store_items = dict()
    while firstInput != 'quit':
        total_items = ''
        firstInput = input('(add/del/tik) (item/s that you want)\nOr you can quit with (quit)\n\n')
        if firstInput[0:3] == 'add':
            how_many_items = [x for x in firstInput if x.isdigit() is True]
            try: 
                for y in how_many_items: total_items+=y
                total_money+= (int(total_items)*1.25)
            except: total_money += 1.25
            try: dictionary_of_store_items[firstInput[4:]] = int(total_items)*1.25
            except:dictionary_of_store_items[firstInput[4:]] = 1.25
        elif firstInput[0:3] == 'del':
            del dictionary_of_store_items[firstInput[4:]]
            how_many_items = [x for x in firstInput if x.isdigit() is True]
            try: 
                for y in how_many_items: total_items+=y
                total_money-= (int(total_items)*1.25)
            except: total_money -= 1.25
        elif firstInput[0:3] == 'tik':  
             what_you_have_purchased = [f"{key} ------ {value}$" for key,value in dictionary_of_store_items.items()]
             print('Nothing to show on ticket\n\n') if len(what_you_have_purchased) == 0 else [print(f"{key} ------ {value}$".format(**dictionary_of_store_items,end='\n')) for key,value in dictionary_of_store_items.items()]
        else:print(f'did not recognize {firstInput}')
    what_you_have_purchased = [print(f"{key} ------ {value}$".format(**dictionary_of_store_items,end='\n')) for key,value in dictionary_of_store_items.items()]
    print('total: ',total_money,'$')
main()