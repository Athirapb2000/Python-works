"""
OOP CONCEPTS
1. Encapsulation - wrapping up of data and functions into a single unit (eg: class)
2. Inheritance   - to acquire the properties of one to another class (use-Code Reusability)
    Types of Inheritance
        1. Single Inheritance      - One Base class and one derived class
        2. Multilevel Inheritance  - One base class, intermediatory class and base class
        3. Multiple Inheritance    - Multiple(or two) base class and one derived class
        4. Hierarchical Inheritance- One base class and multiple derived classes
        5. Hybrid Inheritance      - Combination of Hierarchical and multiple
3. Polymorphism  - One in many forms
    Types of Polymorphism
        1. Compile time Polymorphism (eg: function overloading or early binding or static binding)
            Python does not have compile time so python does not support compile time polymorphism or overloading
        2. Run time Polymorphism(eg: function overriding or late binding or dynamic binding)
            Function overloading - is one class have more than one function with same function name and different
                                   signatures (number,order and type of parameters)
            Function overriding - different class have different functions with same function name and same signatures
4. Abstraction - is to represent the essential features without representing explanation or background details.
                 Main advantage is data hiding
"""
"""
CONSTRUCTOR
    constructors are the member functions of a class which will automatically executed when a object of a class is 
    created. Constructors do not have return value. We can define a constructor by using __init__(self)
    Mainly 2 types of constructors
    1. Non Parameterized Constructor (Default Constructor)
    2. Parameterized Constructor
"""