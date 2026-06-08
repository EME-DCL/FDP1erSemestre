# Validador de correo electrónico

correo = input("Ingresa tu correo electrónico: ").strip().lower()
partes = correo.split("@")

if len(partes) == 2:
    usuario = partes[0]
    dominio = partes[1]
    
    partes_dominio = dominio.split(".")
    ext = partes_dominio[-1]
    
    condicion_es_valido = ("." in dominio) and (usuario[0] != ".") and (2 <= len(ext) <= 4)
    
    es_valido = "Valido" if condicion_es_valido else "Invalido"
    
    if es_valido == "Valido":
        print(f"Email {es_valido}: usuario='{usuario}' dominio='{dominio}' ext='{ext}'")
    else:
        print("Error: El formato es incorrecto (revisa el punto en el dominio, el inicio o la extensión).")

else:
    print("Error: El correo debe tener exactamente un '@'.")
