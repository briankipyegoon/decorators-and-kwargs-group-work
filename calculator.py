def dynamic_calculator(*args, **kwargs):

    if not args:
        raise ValueError("At least one number must be provided.")
    
    # Extract operation and reverse from kwargs
    operation = kwargs.get('operation')
    reverse = kwargs.get('reverse', False) #reverse the order of numbers in the list for the operation to be done
    
    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        raise ValueError(f"Invalid operation: {operation}. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.")
    
    numbers = list(args)
    if reverse:
        numbers.reverse()
    
    if operation == 'add':
        result = sum(numbers)
    elif operation == 'subtract':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    elif operation == 'multiply':
        result = 1
        for num in numbers:
            result *= num
    elif operation == 'divide':
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num
    
    return result

# Test cases
if __name__ == "__main__":
    print(dynamic_calculator(1, 2, 3, operation="add"))  
    print(dynamic_calculator(10, 2, 1, operation="subtract", reverse=True)) 
    print(dynamic_calculator(2, 3, 4, operation="multiply"))  
    print(dynamic_calculator(20, 5, 2, operation="divide")) 
