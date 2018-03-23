input("press an enter key to conituate")

buy_in_amazon = input("You want to buy in amazon?(Yes/No)").upper()


if buy_in_amazon == "YES":
    buy_in_amazon_2 = True
elif buy_in_amazon == "NO":
    buy_in_amazon_2 = False
    has_money = False
    amazon_account_2 = False
else:
    print("Your answer is not valid, please try again with the options indicated")
    buy_in_amazon_2 = False

you_have_money = input("you have money to buy in amazon? (Yes/No)").upper()
you_brother_has_money = input("your brother has money to buy in amazon? (Yes/No)").upper()
amazon_account = input("Do you have an Amazon account to buy? (Yes/No)").upper()

buy_in_amazon_2 = buy_in_amazon == "YES"
has_money = you_brother_has_money == "YES" or you_have_money =="YES"
amazon_account_2 = amazon_account = "YES"

if buy_in_amazon_2 and has_money and amazon_account:
    print ("Well to buy")
else:
    print("That's wrong, then do not buy")

