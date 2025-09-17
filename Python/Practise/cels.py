def celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    
    return fahrenheit

print(celsius_to_fahrenheit(10))

def fahrenheit_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * (5/9)
    
    return celsius

print(fahrenheit_to_celsius(10))


#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    # total_ticket_cost=0
    #Write your logic here
    rate_per_adult = 37550.0
    rate_per_child = 1/3 * (rate_per_adult)
    
    # cost_of_adults = no_of_adults * rate_per_adult
    
    # cost_of_child = no_of_children * rate_per_child
    # total_ticket_cost = cost_of_adults + cost_of_child
    
    return rate_per_child
    # return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost = calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)