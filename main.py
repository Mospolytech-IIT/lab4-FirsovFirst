"""
    File calling functions
"""
import functions

if __name__ == "__main__":
    try:
        print(functions.calculate_square_root(9))
        print(functions.calculate_square_root(-1))
    except ValueError as e:
        print(e)

    try:
        print(functions.divide_numbers(10, 2))
        print(functions.divide_numbers(10, 0))
    except ZeroDivisionError as e:
        print(e)
    
    print(f"Факториал 5: {functions.factorial(5)}")
    print(f"Факториал -3: {functions.factorial(-3)}")

    print(functions.concatenate_strings("Hello, ", "world!"))
    print(functions.concatenate_strings("Hello", 123))

    functions.check_product_availability("apple")
    functions.check_product_availability("banana")
    functions.check_product_availability("orange")
    functions.check_product_availability("grape")

    functions.place_order("apple", 3)
    functions.place_order("banana", 6)
    functions.place_order("orange", 1)
    functions.place_order("apple", -1)

    functions.restock_product("apple", 5)
    functions.restock_product("banana", 0)
    functions.restock_product("grape", 10)

    functions.process_order("apple", 5, 2.5)
    functions.process_order("", 5, 2.5)
    functions.process_order("banana", -1, 2.0) 
    functions.process_order("orange", 3, -1)

    functions.purchase_product("apple", 3, 2.5)
    functions.purchase_product("orange", 1, 3.0)
    functions.purchase_product("grape", 1, 2.0)
    functions.purchase_product("apple", 2, -1)
    functions.purchase_product("banana", 0, 2.0)

    functions.check_product_availability_with_custom_exception("apple", 3)
    functions.check_product_availability_with_custom_exception("grape", 1)
    functions.check_product_availability_with_custom_exception("orange", 1)
    functions.check_product_availability_with_custom_exception("banana", 0)

    functions.divide_numbers_with_custom_exception(10, 2)
    functions.divide_numbers_with_custom_exception(10, 0)
    functions.divide_numbers_with_custom_exception(10, "a")

    functions.read_file("test.txt")
    functions.read_file("non_existing_test.txt")

    functions.check_age(25)
    functions.check_age(-5)
    functions.check_age("тридцать")