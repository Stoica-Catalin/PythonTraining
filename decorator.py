
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
            if county=="01":
                print("Judet: Alba")
            elif county=="02":
                print("Judet: Arad")
            elif county=="03":
                print("Judet: Arges")
            elif county=="04":
                print("Judet: Bacău")
            elif county=="05":
                print("Judet: Bihor")
            elif county=="06":
                print("Judet: Bistrița-Năsăud")
            elif county=="07":
                print("Judet: Botoșani")
            elif county=="08":
                print("Judet: Brașov")
            elif county=="09":
                print("Judet: Brăila")
            elif county=="10":
                print("Judet: Buzău")
            elif county=="11":
                print("Judet: Caraș-Severin")
            elif county=="12":
                print("Judet: Cluj")
            elif county=="13":
                print("Judet: Constanța")
            elif county=="14":
                print("Judet: Covasna")
            elif county=="15":
                print("Judet: Dâmbovița")
            elif county=="16":
                print("Judet: Dolj")
            elif county=="17":
                print("Judet: Galați")
            elif county=="18":
                print("Judet: Gorj")
            elif county=="19":
                print("Judet: Harghita")
            elif county=="20":
                print("Judet: Hunedoara")
            elif county=="21":
                print("Judet: Ialomița")
            elif county=="22":
                print("Judet: Iași")
            elif county=="23":
                print("Judet: Ilfov")
            elif county=="24":
                print("Judet: Maramureș")
            elif county=="25":
                print("Judet: Mehedinți")
            elif county=="26":
                print("Judet: Mureș")
            elif county=="27":
                print("Judet: Neamț")
            elif county=="28":
                print("Judet: Olt")
            elif county=="29":
                print("Judet: Prahova")
            elif county=="30":
                print("Judet: Satu Mare")
            elif county=="31":
                print("Judet: Sălaj")
            elif county=="32":
                print("Judet: Sibiu")
            elif county=="33":
                print("Judet: Suceava")
            elif county=="34":
                print("Judet: Teleorman")
            elif county=="35":
                print("Judet: Timiș")
            elif county=="36":
                print("Judet: Tulcea")
            elif county=="37":
                print("Judet: Vaslui")
            elif county=="38":
                print("Judet: Vâlcea")
            elif county=="39":
                print("Judet: Vrancea")
            elif county=="40":
                print("București")
            elif county=="41":
                print("București - Sector 1")
            elif county=="42":
                print("București - Sector 2")
            elif county=="43":
                print("București - Sector 3")
            elif county=="44":
                print("	București - Sector 4")
            elif county=="45":
                print("București - Sector 5")
            elif county=="46":
                print("București - Sector 6")
            elif county=="51":
                print("Judet: Calarasi")
            elif county=="52":
                print("Judet: Giurgiu")
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

       

    