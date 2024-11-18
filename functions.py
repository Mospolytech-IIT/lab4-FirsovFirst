"""
    File with functions
"""
import math

def calculate_square_root(value):
    """ Step 1 """
    if value < 0:
        raise ValueError("Значение не может быть отрицательным.")
    return math.sqrt(value)

def divide_numbers(numerator, denominator):
    """ Step 1 """
    if denominator == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return numerator / denominator

def factorial(n):
    """ Step 2 """
    try:
        if n < 0:
            raise ValueError("Факториал не определен для отрицательных чисел.")
        if not isinstance(n, int):
            raise TypeError("Факториал может быть вычислен только для целых чисел.")
        
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def concatenate_strings(*args):
    """ Step 3 """
    result = ""

    try:
        # Проверяем, чтобы все переданные аргументы были строками
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError(f"Неверный тип: {arg} не является строкой.")
            result += arg
        
        # Проверяем, чтобы не было пустых строк
        if any(arg == "" for arg in args):
            raise ValueError("Аргументы не должны быть пустыми строками.")

        # Возвращаем объединённую строку
        return result
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
    finally:
        print("Завершение работы функции concatenate_strings.")

# Список продуктов с их количеством на складе
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0
}

def check_product_availability(product):
    """ Step 4 """
    try:
        if product not in inventory:
            raise KeyError(f"Продукт '{product}' не найден в наличии.")
        
        stock = inventory[product]
        if stock <= 0:
            raise ValueError(f"Продукт '{product}' отсутствует на складе.")
        
        return stock

    except KeyError as ke:
        print(f"Ошибка: {ke}")
        return None
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None
    finally:
        print(f"Проверка наличия продукта '{product}' завершена.")

def place_order(product, quantity):
    """ Step 4 """
    try:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Количество должно быть положительным целым числом.")

        stock = check_product_availability(product)
        if stock is None:
            return None  # Продукт не найден или отсутствует на складе

        if stock < quantity:
            raise ValueError(f"Недостаточно товара '{product}' на складе. Запрашиваемое количество: {quantity}, доступно: {stock}.")

        # Обновление запасов
        inventory[product] -= quantity
        print(f"Заказ на {quantity} '{product}' успешно размещен.")

    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None
    finally:
        print(f"Обработка заказа на '{product}' завершена.")

def restock_product(product, quantity):
    """ Step 4 """
    try:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Количество должно быть положительным целым числом.")

        if product not in inventory:
            raise KeyError(f"Продукт '{product}' не найден в наличии.")

        # Обновление запасов
        inventory[product] += quantity
        print(f"Продукт '{product}' успешно пополнен на {quantity} единиц.")

    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None
    except KeyError as ke:
        print(f"Ошибка: {ke}")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None
    finally:
        print(f"Пополнение продукта '{product}' завершено.")

def process_order(product, quantity, price_per_unit):
    """ Step 5 """
    try:
        # Проверка типа продукта
        if not isinstance(product, str) or not product:
            raise ValueError("Название продукта должно быть непустой строкой.")

        # Проверка количества
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Количество должно быть положительным целым числом.")

        # Проверка цены
        if not isinstance(price_per_unit, (int, float)) or price_per_unit < 0:
            raise ValueError("Цена за единицу должна быть неотрицательным числом.")

        # Вычисление общей стоимости
        total_price = quantity * price_per_unit
        print(f"Заказ на '{product}' успешно обработан. Общая стоимость: {total_price:.2f}")

    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None
    finally:
        print(f"Обработка заказа на '{product}' завершена.")

class InvalidProductError(Exception):
    """Исключение для недопустимого продукта."""
    pass

class InsufficientStockError(Exception):
    """Исключение для недостаточного количества товара на складе."""
    pass

class InvalidPriceError(Exception):
    """Исключение для недопустимой цены."""
    pass

def purchase_product(product, quantity, price_per_unit):
    """ Step 6 """
    try:
        if product not in inventory:
            raise InvalidProductError(f"Продукт '{product}' не найден в наличии.")
        
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным целым числом.")
        
        if price_per_unit < 0:
            raise InvalidPriceError("Цена за единицу должна быть неотрицательным числом.")

        if inventory[product] < quantity:
            raise InsufficientStockError(f"Недостаточно товара '{product}' на складе. Доступно: {inventory[product]}.")

        # Обновление запасов
        inventory[product] -= quantity
        total_price = quantity * price_per_unit
        print(f"Заказ на {quantity} '{product}' успешно размещен. Общая стоимость: {total_price:.2f}")

    except InvalidProductError as e:
        print(f"Ошибка: {e}")
    except InsufficientStockError as e:
        print(f"Ошибка: {e}")
    except InvalidPriceError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        print("Обработка заказа завершена.")

def check_product_availability_with_custom_exception(product, quantity):
    """ Step 7 """
    try:
        # Проверка наличия продукта
        if product not in inventory:
            raise InvalidProductError(f"Продукт '{product}' не найден в наличии.")

        # Проверка количества
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным целым числом.")

        # Проверка наличия достаточного количества товара
        if inventory[product] < quantity:
            raise ValueError(f"Недостаточно товара '{product}' на складе. Доступно: {inventory[product]}.")

        print(f"Продукт '{product}' доступен в количестве {quantity}.")
    
    except InvalidProductError as e:
        print(f"Ошибка: {e}")
        # Логика обработки ошибки: например, можно предложить альтернативные продукты
        print("Пожалуйста, проверьте наличие других продуктов в инвентаре.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        print("Проверка наличия продукта завершена.")

class DivisionError(Exception):
    """Исключение для ошибок деления."""
    pass

def divide_numbers_with_custom_exception(num1, num2):
    """ Step 8 """
    try:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Оба параметра должны быть числами.")
        
        if num2 == 0:
            raise DivisionError("Деление на ноль невозможно.")
        
        result = num1 / num2
        print(f"Результат деления {num1} на {num2} = {result:.2f}")
    
    except DivisionError as de:
        print(f"Ошибка: {de}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        print("Операция деления завершена.")

class FileReadError(Exception):
    """Исключение для ошибок чтения файла."""
    pass

def read_file(file_path):
    """ Step 8 """
    try:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Содержимое файла:\n{content}")
        
        except FileNotFoundError:
            raise FileReadError(f"Файл '{file_path}' не найден.")
        except IOError as e:
            raise FileReadError(f"Ошибка чтения файла: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
    except FileReadError as e:
        print(e)
    finally:
        print("Операция чтения файла завершена.")

class InvalidAgeError(Exception):
    """Исключение для недопустимого возраста."""
    pass

def check_age(age):
    """ Step 8 """
    try:
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError("Возраст должен быть положительным целым числом.")
        
        print(f"Возраст {age} принят.")
    
    except InvalidAgeError as iae:
        print(f"Ошибка: {iae}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        print("Проверка возраста завершена.")