name = "Jen"
print (name)


def say_hello():
    print ("Hello")
    print("I'm inside")
print("I'm outside")

#Indentation = inside the code "block"#
#Same space indentation = same block#

#calls
say_hello()
say_hello()

# data structures ->114

# an array in js-> python is list
prices = [2,15,32,78,99]

# add
prices.append(2)

print(prices)

 # sum all the prices
total = 0 
for price in prices:
    total += price

print(total)


# dictionary 
me = {
    "name": "jen",
    "age": 36,
    "hobbies": [],
    "address": {
        "street": "muncy",
        "city": "dodger nation"
    }
}

print(me)

# read
print(me["name"])

# warning: reading a key that does not exist 
print(me["last"])


# modify
me["age"] = 99


# add keys
me["last"] = "navarro"


print("the end!!!")