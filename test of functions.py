buy_in_amazon = input("You want to buy in amazon?(Yes/No)")
you_have_money = input("you have money to buy in amazon? (Yes/No)")
you_brother_has_money = input("your brother has money to buy in amazon? (Yes/No)")
amazon_account = input("Do you have an Amazon account to buy? (Yes/No)")

buy_in_amazon_2 = buy_in_amazon == "Yes"
has_money = you_brother_has_money == "yes" or you_have_money =="Yes"
amazon_account_2 = amazon_account = "Yes"

if buy_in_amazon_2 and has_money and amazon_account:
    print ("Well to buy")
else:
    print("That's wrong, then do not buy")

