def add_product(src):
    def tru_product():
        product = input("Введіть продукт який необхідно купити: ")
        list_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for letters in product:
            for number in list_numbers:
                if number == letters:
                    print("Назва продукту не повинна містити символів!")
                    return tru_product()
                else:
                    return product

    def tru_number():
        def types():
            type_p = input("оберіть розмірність g/kg/litrs/number: ")
            elements = ["g", "kg", "litrs", "number"]
            trigers = False   
            for element in elements:    
                if type_p == element:
                    trigers = True
                    return type_p
                    break
    
            if trigers == False:
                print("Розмірність введена не коректно")
                return types()
        
        def number_p(type_p):
            try:        
                number_product = float(input("Введіть кількість продукту яку необхідно купити: "))
                if type_p == "number":
                    number_product = int(number_product)
            except:
                print("Кількість введена некоректно")
                return number_p
            return str(number_product)     
        
        rozmir = types()
        type_p = number_p(rozmir) + " " + rozmir
        return type_p

    file = open(src, "a")
    file.write(tru_product()+ " - " + tru_number() + "\n")
    file.close()
    

def read_file(src):
    file = open(src, "r")
    text = file.read()
    return text

def put_file(src):
    file = open(src)
    text = file.read()
    for i in text:
        print(i, end="")

    list_users = text.split("\n")
    
    true_list = []
    
    for element in list_users:
        true_list.append(element)   
    file.close()
     
    return true_list

def remove_product():
    user_in_list = False
    users = input("Введіть назву продукту який ви вже купили: ")
    list = put_file(src)
    for element in list:
        name_adres = element.split(" - ")
        for date in name_adres:
            if date == users:
                print(f"{element} is delited")
                user_in_list = True
                list.remove(element)
                break

    if user_in_list == False:        
        print("not found user")  
    else:
        file = open(src, "w")
        for element in list:
            file.write(f"{element}\n")    

src = "E:\Python\lab\product.txt"

while True:
    operation = input("додати продукт '+', видалити продукт '-', перегляну список покупок 'a': ") 
    if operation == "-":
        remove_product()
    elif operation == "+":
        add_product(src)
    elif operation == "a":
        print(read_file(src))
    else:
        break   