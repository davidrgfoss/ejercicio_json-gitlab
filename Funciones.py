def ListarInformacion(farmacias):
    f=[]
    for x in farmacias:
        f.append({"propietario":x.get("schema_name")})
    return f

def ContarInformacion(farmacias,cad):
    f=0
    for x in farmacias:
        if x.get("schema_address_postalCode") == cad:
            f+=1
    return f

def FiltrarInformacion(farmacias,cad):
    f=[]
    for x in farmacias:
        if x.get("schema_address_postalCode") == cad:
            f.append({"propietario":x.get("schema_name"),"descripcion":x.get("schema_description")})
    return f

def InformacionRelacionada(farmacias,cad,cad1):
    f=[]
    for x in farmacias:
        if cad in x.get("schema_description") and cad1 in x.get("schema_description"):
            f.append(x.get("schema_address_streetAddress"))
    return f

def EjercicioLibre(farmacias,cad,cad1):
    result=[]
    if cad > cad1:
        cad2=cad
        cad=cad1
        cad1=cad2
    for x in farmacias:
        if cad > x.get("Horarios").get("Horario_de_manana_Opens") and cad1 < x.get("Horarios").get("Horario_de_tarde_Closes"):
            result.append({"telefono":x.get("schema_telephone"),"direccion":x.get("schema_address_streetAddress")})
    return result

def EjercicioLibre2(farmacias,cad):
    result=[]
    for x in farmacias:
        if cad > x.get("Horarios").get("Horario_de_manana_Opens") and cad < x.get("Horarios").get("Horario_de_tarde_Closes"):
            result.append({"telefono":x.get("schema_telephone"),"direccion":x.get("schema_address_streetAddress")})
    return result
