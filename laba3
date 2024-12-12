from abc import ABC, abstractmethod

# Singleton (Одиночка)
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value):
        self.value = value

# Factory Method (Фабричный метод)
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "ConcreteProductB"

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code works with {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Abstract Factory (Абстрактная фабрика)
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_x(self):
        pass

    @abstractmethod
    def create_product_y(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_x(self):
        return ProductX1()

    def create_product_y(self):
        return ProductY1()

class ConcreteFactory2(AbstractFactory):
    def create_product_x(self):
        return ProductX2()

    def create_product_y(self):
        return ProductY2()

class ProductX(ABC):
    @abstractmethod
    def useful_function_x(self):
        pass

class ProductX1(ProductX):
    def useful_function_x(self):
        return "The result of ProductX1"

class ProductX2(ProductX):
    def useful_function_x(self):
        return "The result of ProductX2"

class ProductY(ABC):
    @abstractmethod
    def useful_function_y(self):
        pass

class ProductY1(ProductY):
    def useful_function_y(self):
        return "The result of ProductY1"

class ProductY2(ProductY):
    def useful_function_y(self):
        return "The result of ProductY2"

# Builder (Строитель)
class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    def build_part_a(self):
        self._product.add("PartA")

    def build_part_b(self):
        self._product.add("PartB")

    def get_result(self):
        product = self._product
        self.reset()
        return product

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)

# Пример использования
if __name__ == "__main__":
    # Singleton
    singleton1 = Singleton("First")
    singleton2 = Singleton("Second")
    print(singleton1.value)  # Output: First
    print(singleton2.value)  # Output: First

    # Factory Method
    creator_a = ConcreteCreatorA()
    print(creator_a.some_operation())

    creator_b = ConcreteCreatorB()
    print(creator_b.some_operation())

    # Abstract Factory
    factory1 = ConcreteFactory1()
    product_x1 = factory1.create_product_x()
    product_y1 = factory1.create_product_y()
    print(product_x1.useful_function_x())
    print(product_y1.useful_function_y())

    factory2 = ConcreteFactory2()
    product_x2 = factory2.create_product_x()
    product_y2 = factory2.create_product_y()
    print(product_x2.useful_function_x())
    print(product_y2.useful_function_y())

    # Builder
    builder = ConcreteBuilder()
    builder.build_part_a()
    builder.build_part_b()
    product = builder.get_result()
    print(product.list_parts())  # Output: PartA, PartB
