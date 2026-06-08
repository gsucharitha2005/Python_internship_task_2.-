library=[]
def add_book():
	n=int(input("no.of books:"))
	for i in range(n):
        	book_ISBN=int(input("enter the ISBN:"))
        	book_name=input("enter the book name:")
        	book_author=input("enter the book author:")
        	book={
            		"book_ISBN":book_ISBN,
            		"book_name":book_name,
            		"book_author":book_author
        		}
        	library.append(book)
	print("___________________________________________________________")
	print("book_ISBN\tbook_name\tbook_author")
	print("____________________________________________________________")
	for i in library:
		print(i["book_ISBN"],"\t\t",i["book_name"],"\t\t",i["book_author"])
	print("books added successfully")
	
def issue_book():
    issue_ISBN=int(input("Enter ISBN to issue: "))
    for i in library:
        if i["book_ISBN"]==issue_ISBN:
            library.remove(i)
            print("book issued successfully")
            break
    else:
        print("book not found")

def return_book():
    return_ISBN=int(input("Enter ISBN to return: "))
    for i in library:
        if i["book_ISBN"]==return_ISBN:
            library.pop()
            print("book return successfully")
            break
    else:
        print("book not found")
         
def calculate_fine_days():
	fine_per_day=5
	late_days=int(input("enter late days:"))
	fine=late_days * 5
	print(fine)
def menu():
	while True:
		print("\n___________________________Library Management_________________________")
		option=int(input("1.add_book\n2.issue_book\n3.return_book\n4.calculate_fine_days\n5.exist\n"))

		if option==1:
        		add_book()
		elif option==2:
        		issue_book()
		elif option==3:
        		return_book()
		elif option==4:
        		calculate_fine_days()
		elif option==5:
			print("exiting library")
			break
		else:
            		print("invalid option")
	
                        
menu()

	
	
	





