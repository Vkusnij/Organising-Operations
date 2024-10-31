# Simple function

this_text = "Hello World"

def log_into_terminal():
   print(this_text)

log_into_terminal()

# Local variables

def log_into_terminal_1():
   local_text = "Hello function!"
   print(local_text)

log_into_terminal_1()

# Multiple functions

def another_function():
   log_into_terminal()
   log_into_terminal_1()

another_function()

# Assign a function

third_function = log_into_terminal

third_function()

# Funception

def log_into_terminal():
    local_text = "Hello Function!"
    print(this_text)
    print(local_text)
    def fourth_function():
        print("This console.log belongs to the fourth function!")
    fourth_function()

log_into_terminal()

# Arguments and Parameters

def log_into_terminal(to_log):
    return to_log
my_msg = log_into_terminal("It's from anotherFunction()!")

def another_function(msg):
    print(msg)

another_function(my_msg)

# Multiple arguments

def log_into_terminal(message, second_to_log):
    print(message)
    print(second_to_log)

log_into_terminal("First message", "Second message")

# The big return 

def greetings(name):
    return f"Hello, {name}!"

print(greetings("Alice"))
print(greetings("Bob"))
print(greetings("Charlie"))
print(greetings("Dave"))
print(greetings("Eve"))