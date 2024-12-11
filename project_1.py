print ("Welcome to skill circle library management system ")

print("Available Books:")
print("1. Atomic Habits (Book Number: 101)")
print("2. The Lean Startup (Book Number: 102)")
print("3. Sapiens: A Brief History of Humankind (Book Number: 103)")
print("4. Rich Dad Poor Dad (Book Number: 104)")
print("5. The Subtle Art of Not Giving a F*ck (Book Number: 105)")


def library(book_num):
    if book_num == 101:
        print("Book Name = Atomic Habits")
        print("Author: James Clear")
        print("Launch Date: October 16, 2018")
        print("Description: A practical guide to building good habits.")
    elif book_num == 102:
        print("Book Name = The Lean Startup")
        print("Author: Eric Ries")
        print("Launch Date: September 13, 2011")
        print("Description: Offers a scientific approach to creating and managing successful startups in anage of innovation.")    
    elif book_num==103:
        print("Book Name = Sapiens: A Brief History of Humankind")
        print("Author: Yuval Noah Harari")
        print("Launch Date: 2011")
        print("Description: Explores the history of humanity, from the Stone Age to the 21st century")
    elif book_num==104:
        print("Book Name = Rich Dad Poor Dad")
        print("Author: Robert T. Kiyosaki")
        print("Launch Date: 1997")
        print("Description: Shares lessons on financial literacy, investing, and building wealth")
    elif book_num==105:
        print("Book Name = The Subtle Art of Not Giving a F*ck")
        print("Author: Mark Manson")
        print("Launch Date: September 13, 2016")
        print("Description: A counterintuitive approach to living a good life")

    else :
        print("Enter a Valid Book Number :")

user_1= int(input("Enter the book number: "))
library(user_1)



print("If you want to exit: press 2.")
print("If you want to continue: press 1.")
x = int(input("Enter here: "))
if x == 1:
    user_1 = int(input("Enter the book number: "))
    library(user_1)
elif x==2:
    print("Thanks for visiting")
else:
    print("enter a vaild num ")

        