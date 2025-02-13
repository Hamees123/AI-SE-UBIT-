# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number of
# cities from the keyboard and store the data in a file in the order in which they’re entered.





def save_city_info():
    file = open("cities.txt", "w")
    while True:
        city = input("Enter city name (or type 'exit' to stop): ")
        if city.lower() == "exit":
            break
        population = input("Enter population: ")
        mayor = input("Enter mayor's name: ")

        file.write(f"{city}, {population}, {mayor}\n")
        print("City information saved!\n")
    file.close()

save_city_info()





# Write a python program to create a data file student.txt and append the message “Now we are
# AI students”s



file = open("student.txt", "a")
file.write("Now we are BS students\n")
file.close()

