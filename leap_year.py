def leap_year():
    age = int(input("Ingrese un año: "))
    age_m = age % 4
    age_c = age % 100
    age_q = age % 400

    if age_m == 0 or age_c ==0:
            if age_m == 0 and age_c !=0:
                print(f"El año {age} es bisiesto")
            elif age_c == 0 and age_q == 0:
                print(f"El año {age} es bisiesto")
            elif age_c == 0 and age_q != 0:
                print(f"El año {age} no es bisiesto")
    else:
        print(f"El año {age} no es bisiesto")
