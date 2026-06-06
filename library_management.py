library = []
print("___________________________________________________________________")
print("book_ISBN\t\t\tbook_name\t\tbook_author")
print("___________________________________________________________________")
for i in library:
    print(i["book_ISBN"],"\t",i["book_name"],"\t\t",i["book_author"])
def add_book():
    n=int(input("no.of books:"))
    for i in range(n):
        book_ISBN=int(input("enter the ISBN:"))
        book_name=input("enter the book name:")
        book_author=input("enter the book author:")
        book = {
            "book_ISBN":book_ISBN,
            "book_name":book_name,
            "book_author":book_author
        }
        library.append(book)

add_book()
print("__________________________________________________________________")
print("book_ISBN\t\tbook_name\t\tbook_author")
print("__________________________________________________________________")
for i in library:
    print(i["book_ISBN"],"\t\t\t",i["book_name"],"\t\t\t",i["book_author"])

print("_________________________________________________________________")

def issue_book():
    issue_ISBN=int(input("enter issue book ISBN:"))
    for i in library:
        if i["book_ISBN"]==issue_ISBN:
            library.remove(i)

issue_book()
print("_________________________________________________________________")
print("book_ISBN\t\tbook_name\t\tbook_author")
print("_________________________________________________________________")
for i in library:
    print(i["book_ISBN"],"\t\t\t",i["book_name"],"\t\t\t",i["book_author"])

print("_________________________________________________________________")


def return_book():
    return_isbn=int(input("Enter return book ISBN: "))
    for i in library:
        if i["book_ISBN"]==return_isbn:
            library.remove(i)
            print("book returned successfully")
            break
    else:
        print("book not found")

return_book()
print("books after returning:")
print("__________________________________________________________________")
print("book_ISBN\tbook_name\tbook_author")
print("___________________________________________________________________")
for i in library:
    print(i["book_ISBN"],"\t\t",i["book_name"],"\t\t",i["book_author"])



def calculate_fine_days():
    fine_per_day=5
late_days=int(input("enter late days:"))
fine=late_days * 5
print(fine)

print("\n\n")
while True:
    print("\n___________________________Library Management_________________________")
    option=int(input("1.add_book\n2.issue_book\n3.return_book\n4.calculate_fine_days\n5.exist\n"))

    if option==1:
        print(add_book())
    elif option==2:
        print(issue_book())
    elif option==3:
        print(return_book())
    elif option==4:
        print(calculate_fine_days())
    elif option==5:
            print("exiting library")
            break
    else:
            print("invalid option")
	
	
	





