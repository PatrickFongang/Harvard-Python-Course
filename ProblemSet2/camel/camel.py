def main():
    camel=input("camelCase: ")
    print(to_snake(f"snake_case: {camel}"))

def to_snake(camel):
    snake=""
    for char in camel:
        if char.isupper():
            snake+='_'
        snake+=char
    return snake.lower()

main()

