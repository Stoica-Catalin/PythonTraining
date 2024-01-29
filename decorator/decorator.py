
def ro_id_interpeter(func):
    def wrapper():
        cnp=func()
        length_of_cnp=len(cnp)
        if length_of_cnp != 13 or any(c.isalpha() for c in cnp):
            print ("CNP-ul furnizat nu este valid")
            return wrapper
        else:
            genre=cnp[0:1]
            if genre=='1' or genre=='5':
                print ("Sex: M")
            else:
                print ("Sex: F")
            year_of_birth=cnp[1:3]
            month_of_birth=cnp[3:5]
            day_of_birth=cnp[5:7]
            if genre==1 or genre==2:
                year_of_birth="19"+year_of_birth
            else:
                year_of_birth="20"+year_of_birth
            print("Data nasterii: "+day_of_birth+"."+month_of_birth+"."+year_of_birth)
            county=cnp[7:9]
            county_dict= {}
            file = open("counties.txt")
            for line in file:
                word = line.split("=")
                county_dict.update({word[0].strip(): word[1].strip()})
            print("Judet: "+ d[county])
            nnn_component=cnp[9:12]
            print("Componenta pentru diferentiere: "+nnn_component)
            control_number=cnp[12:13]
            print("Cifra de control: "+control_number)
                         
            
    return wrapper
 

@ro_id_interpeter
def f():
    cnp=input('Introduceti Cod Numeric Personal:')
    return cnp

f()

       

    