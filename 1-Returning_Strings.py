def greet(name):
    return f'Hello, {name} how are you doing today?'


ask_name = str(input('What is your name?: '))
greeting = greet(ask_name)
print(greeting)
