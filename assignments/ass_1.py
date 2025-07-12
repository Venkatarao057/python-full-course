#integer
movie_id=int(input("Enter the movie id: "))
ticket_price=int(input("Enter movie price: "))
#float
movie_rating=float(input("Enter movie rating: "))
movie_ticket_discount=float(input("Enter movie ticket discount: "))
#string
movie_name=input("Enter movie name : ")
#list
location=input("Enter movie releasing locations: ").split(',')
#tuple
movie_timings=(input("Enter movie starting time: "),input("Enter movie ending time: "))
#set
movie_languages=set(input("Enter movie languages: ").split())
#dictionary
movie_detailes={"movie name":movie_name,"ticket price":ticket_price,"discount":movie_ticket_discount}
                    
print("///////////////////// Here we use the separated by comma////////////")               
print("Movie name is:",movie_name, "Movie ticket Price is:",ticket_price, "Movie releasing locations:",location)

print("****************Here we use the f-strings method*******************")
print(f"These are the  movie detailes {movie_detailes}")
print(f"Movie id is {movie_id}")

print("------------------Here we use the perecentage formatting-----------------")
print("Movie ticket discount: %.2f" % movie_ticket_discount)
print("Movie rating out 5 is: %.2f" % movie_rating)

print("~~~~~~~~~~~~~~~~~~~Here we have to use the .format method~~~~~~~~~~~~")
print("Movie Ticket price is: ${}".format(movie_detailes["ticket price"]))

