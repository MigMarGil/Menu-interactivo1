#!/bin/python3
import time
import os
import subprocess

opcio = None
while opcio != "5":
    os.system('clear')
    print("Que quieres ver de la teoria?")
    print("1. Python")
    print("2. Git")
    print("3. Sistemas Operativos")
    print("4. Información y ayuda")
    print("5. Salir del programa")
    opcio = input()
    
    match opcio:
        case "1":
            print("Python, interesante...")
            time.sleep(0.5)
            opcio_PY = None
            while opcio_PY != "8":
                os.system('clear')
                print("Que estructura estas interesado en aprender o repasar?")
                print("1. Variables y operadores")
                print("2. Control de flujo (if/else, match)")
                print("3. Bucles (while, for)")
                print("4. Listas y cadenas")
                print("5. Gestión de archivos")
                print("6. Ejercicios prácticos")
                print("7. Zen de Python")
                print("8. Atrás")
                opcio_PY = input()
                
                match opcio_PY:
                    case "1":  # Variables y operadores
                        os.system('clear')
                        print(80*"-")
                        print("VARIABLES Y OPERADORES EN PYTHON")
                        print("\nVariables:")
                        print("- NO se declaran")
                        print("- Asignación con '='")
                        print("- El tipo depende de los datos almacenados")
                        
                        print("\nTipos básicos:")
                        print("- int: enteros (ej: -1, 4, 2300)")
                        print("- float: números reales (ej: -1.1, 4.3, 2.3E3)")
                        print("- bool: valores booleanos (True/False)")
                        print("- str: cadenas de caracteres (\"Hola\", \"A23\")")
                        
                        print("\nOperadores aritméticos:")
                        print("+  Suma          // División entera")
                        print("-  Resta         %  Módulo")
                        print("*  Multiplicación ** Exponenciación")
                        print("/  División")
                        
                        print("\n>>> Ejemplo:")
                        print("x = 7 * 4          # Resultado: 28")
                        print("y = 10 - 7         # Resultado: 3")
                        print("z = x * y          # Resultado: 84")
                        print("w = z / 2          # Resultado: 42.0")
                        print("div_entera = 77 // 6  # Resultado: 12")
                        print("modulo = 77 % 6     # Resultado: 5")
                        print("potencia = 2 ** 5   # Resultado: 32")
                        
                        print("\n>>> Ejemplo con input():")
                        print('nombre = input("¿Cómo te llamas?: ")')
                        print('edad = int(input("¿Cuántos años tienes?: "))')
                        print('print("Hola", nombre, "tienes", edad, "años")')
                        print(80*"-")
                        
                        ejemplo = input("¿Quieres probar el ejemplo? (s/n): ")
                        if ejemplo == "s":
                            nombre = input("¿Cómo te llamas?: ")
                            edad = int(input("¿Cuántos años tienes?: "))
                            print("Hola", nombre, "tienes", edad, "años")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "2":  # Control de flujo
                        os.system('clear')
                        print(80*"-")
                        print("CONTROL DE FLUJO EN PYTHON")
                        print("\n>>> Estructura if/else:")
                        print("if condicion:")
                        print("    # acciones si es verdadero")
                        print("else:")
                        print("    # acciones si es falso")
                        
                        print("\n>>> Estructura match (Python 3.10+):")
                        print("match variable:")
                        print('    case "1":')
                        print('        print("Opción 1")')
                        print('    case "2":')
                        print('        print("Opción 2")')
                        print('    case _:')
                        print('        print("Opción no válida")')
                        
                        print("\nOperadores relacionales:")
                        print("== igual       != diferente")
                        print("<  menor       >  mayor")
                        print("<= menor o igual >= mayor o igual")
                        
                        print("\nOperadores lógicos:")
                        print("and  Y lógico")
                        print("or   O lógico")
                        print("not  NO lógico")
                        
                        print("\n>>> Ejemplo if/else:")
                        print('numero = int(input("Introduce un número: "))')
                        print('if numero >= 1 and numero <= 10:')
                        print('    print("Número entre 1 y 10")')
                        print('else:')
                        print('    print("Número fuera del rango")')
                        
                        print("\n>>> Ejemplo match:")
                        print('opcion = input("Elige 1, 2 o 3: ")')
                        print('match opcion:')
                        print('    case "1":')
                        print('        print("Tarea 1")')
                        print('    case "2":')
                        print('        print("Tarea 2")')
                        print('    case "3":')
                        print('        print("Tarea 3")')
                        print('    case _:')
                        print('        print("Error: elige 1, 2 o 3")')
                        print(80*"-")
                        
                        ejemplo = input("¿Quieres probar los ejemplos? (s/n): ")
                        if ejemplo == "s":
                            # Ejemplo if/else
                            print("\n--- Ejemplo if/else ---")
                            num = int(input("Introduce un número: "))
                            if num >= 1 and num <= 10:
                                print("Número entre 1 y 10")
                            else:
                                print("Número fuera del rango")
                            
                            # Ejemplo match
                            print("\n--- Ejemplo match ---")
                            op = input("Elige 1, 2 o 3: ")
                            match op:
                                case "1":
                                    print("Ejecutando tarea 1")
                                case "2":
                                    print("Ejecutando tarea 2")
                                case "3":
                                    print("Ejecutando tarea 3")
                                case _:
                                    print("Error: opción no válida")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "3":  # Bucles
                        os.system('clear')
                        print(80*"-")
                        print("BUCLES EN PYTHON")
                        
                        print("\n>>> Bucle while:")
                        print("while condicion:")
                        print("    # acciones")
                        print("    # actualizar condición")
                        
                        print("\n>>> Ejemplo while:")
                        print("i = 1")
                        print("while i <= 10:")
                        print("    print(i)")
                        print("    i = i + 1")
                        
                        print("\n>>> Bucle for:")
                        print("for variable in secuencia:")
                        print("    # acciones")
                        
                        print("\n>>> Función range():")
                        print("range(inicio, fin, paso)")
                        print("- inicio: valor inicial (opcional, default=0)")
                        print("- fin: valor final (excluido)")
                        print("- paso: incremento (opcional, default=1)")
                        
                        print("\n>>> Ejemplo for con range():")
                        print("for i in range(5):        # 0, 1, 2, 3, 4")
                        print("    print(i)")
                        print("\nfor i in range(2, 10, 2): # 2, 4, 6, 8")
                        print("    print(i)")
                        
                        print("\n>>> Ejemplo for con lista:")
                        print('colores = ["rojo", "verde", "azul"]')
                        print("for color in colores:")
                        print('    print("Color:", color)')
                        print(80*"-")
                        
                        ejemplo = input("¿Quieres probar los ejemplos? (s/n): ")
                        if ejemplo == "s":
                            print("\n--- Ejemplo while ---")
                            i = 1
                            while i <= 5:
                                print(f"i = {i}")
                                i += 1
                            
                            print("\n--- Ejemplo for con range ---")
                            for j in range(3):
                                print(f"j = {j}")
                            
                            print("\n--- Ejemplo for con lista ---")
                            colores = ["rojo", "verde", "azul"]
                            for color in colores:
                                print(f"Color: {color}")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "4":  # Listas y cadenas
                        os.system('clear')
                        print(80*"-")
                        print("LISTAS Y CADENAS EN PYTHON")
                        
                        print("\n>>> Creación de listas:")
                        print('lista1 = ["rojo", "verde", "azul"]')
                        print('lista2 = ["gato", "perro", "pájaro"]')
                        print('lista3 = [1, 2, 3, 4, 5]')
                        print('lista_mixta = ["texto", 123, True, 3.14]')
                        
                        print("\n>>> Operaciones con listas:")
                        print("len(lista)           # Longitud")
                        print("lista[índice]        # Acceso por índice")
                        print("lista.append(valor)  # Añadir al final")
                        print("lista.insert(pos, valor) # Insertar en posición")
                        print("lista.remove(valor)  # Eliminar valor")
                        print("lista.sort()         # Ordenar")
                        print("lista1 + lista2      # Concatenar")
                        print("del lista[índice]    # Eliminar por índice")
                        
                        print("\n>>> Métodos de cadenas:")
                        print('texto = "  Hola Mundo  "')
                        print("texto.strip()        # Eliminar espacios")
                        print("texto.upper()        # Mayúsculas")
                        print("texto.lower()        # Minúsculas")
                        print("texto.split(',')     # Dividir por separador")
                        print("texto.replace('a', 'o') # Reemplazar")
                        print("len(texto)           # Longitud")
                        
                        print("\n>>> Ejemplo completo:")
                        print('fila = "Ana Maria,Fernandez,Marin,22,Natacio,Sabadell"')
                        print('campos = fila.split(",")')
                        print("# Resultado: ['Ana Maria', 'Fernandez', 'Marin', '22', 'Natacio', 'Sabadell']")
                        print("print(campos[0])    # Ana Maria")
                        print("print(campos[3])    # 22")
                        
                        print(80*"-")
                        
                        ejemplo = input("¿Quieres probar los ejemplos? (s/n): ")
                        if ejemplo == "s":
                            print("\n--- Trabajando con listas ---")
                            colores = ["rojo", "verde", "azul", "amarillo"]
                            print(f"Lista original: {colores}")
                            print(f"Longitud: {len(colores)}")
                            print(f"Primer elemento: {colores[0]}")
                            print(f"Último elemento: {colores[-1]}")
                            
                            colores.append("naranja")
                            print(f"Después de append: {colores}")
                            
                            colores.sort()
                            print(f"Ordenada: {colores}")
                            
                            print("\n--- Trabajando con cadenas ---")
                            texto = "  Python es genial!  "
                            print(f"Original: '{texto}'")
                            print(f"Sin espacios: '{texto.strip()}'")
                            print(f"Mayúsculas: {texto.strip().upper()}")
                            
                            datos = "nombre:edad:ciudad"
                            partes = datos.split(":")
                            print(f"Split por ':': {partes}")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "5":  # Gestión de archivos
                        os.system('clear')
                        print(80*"-")
                        print("GESTIÓN DE ARCHIVOS EN PYTHON")
                        
                        print("\n>>> Modos de apertura:")
                        print("'r'  - Lectura (default)")
                        print("'w'  - Escritura (sobrescribe)")
                        print("'a'  - Añadir al final")
                        print("'x'  - Crear (falla si existe)")
                        print("'+'  - Actualizar (lectura + escritura)")
                        
                        print("\n>>> Métodos principales:")
                        print("open(nombre, modo)  # Abrir archivo")
                        print("archivo.read()       # Leer todo")
                        print("archivo.readline()   # Leer una línea")
                        print("archivo.readlines()  # Leer todas las líneas")
                        print("archivo.write(texto) # Escribir")
                        print("archivo.close()      # Cerrar")
                        
                        print("\n>>> Ejemplo lectura:")
                        print('# Forma 1: readline()')
                        print('with open("datos.txt", "r") as f:')
                        print('    linea = f.readline()')
                        print('    while linea:')
                        print('        print(linea.strip())')
                        print('        linea = f.readline()')
                        
                        print('\n# Forma 2: readlines()')
                        print('with open("datos.txt", "r") as f:')
                        print('    lineas = f.readlines()')
                        print('    for linea in lineas:')
                        print('        print(linea.strip())')
                        
                        print('\n# Forma 3: iteración directa')
                        print('with open("datos.txt", "r") as f:')
                        print('    for linea in f:')
                        print('        print(linea.strip())')
                        
                        print("\n>>> Ejemplo escritura:")
                        print('with open("salida.txt", "w") as f:')
                        print('    f.write("Línea 1\\n")')
                        print('    f.write("Línea 2\\n")')
                        print('    f.write("Línea 3\\n")')
                        
                        print("\n>>> Ejemplo añadir:")
                        print('with open("registro.txt", "a") as f:')
                        print('    f.write("Nueva entrada\\n")')
                        print(80*"-")
                        
                        ejemplo = input("¿Quieres crear archivos de ejemplo? (s/n): ")
                        if ejemplo == "s":
                            # Crear archivo de ejemplo
                            with open('ejemplo_lectura.txt', 'w') as f:
                                f.write("Ana Maria:Fernandez:Marin:22:Natacio:Sabadell\n")
                                f.write("Pere:San:Cugat:25:Hoquei herba:Terrassa\n")
                                f.write("Laura:Mili:Arias:23:futbol:Barcelona\n")
                            
                            print("\n--- Leyendo archivo ---")
                            with open('ejemplo_lectura.txt', 'r') as f:
                                for i, linea in enumerate(f, 1):
                                    campos = linea.strip().split(":")
                                    print(f"Línea {i}: {campos}")
                            
                            # Limpiar
                            os.remove('ejemplo_lectura.txt')
                            print("\nArchivo temporal eliminado.")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "6":  # Ejercicios prácticos
                        os.system('clear')
                        print(80*"-")
                        print("EJERCICIOS PRÁCTICOS DE PYTHON")
                        
                        print("\nEjercicio 1: Mitjana.py")
                        print("Crear una lista llamada 'esportistes' con elementos de formato:")
                        print("nom:cognom1:cognom2:edat:esport:club")
                        print("Mostrar la media de edad de todos los elementos.")
                        
                        print("\nEjercicio 2: Mitjana-file.py")
                        print("Leer un archivo 'esportistes' con líneas del mismo formato")
                        print("y calcular la media de edad.")
                        
                        print("\nEjercicio 3: Preguntar-club.py")
                        print("Leer el archivo 'esportistes' y preguntar al usuario un club.")
                        print("Mostrar las líneas donde se encuentre ese club.")
                        
                        print("\nEjercicio 4: Guardar-esports.py")
                        print("Leer 'esportistes' y crear un archivo 'esports'")
                        print("que contenga solo los nombres de los deportes.")
                        
                        print("\n>>> Solución Ejercicio 1 (esquema):")
                        print('esportistes = [')
                        print('    "Ana Maria:Fernandez:Marin:22:Natacio:Sabadell",')
                        print('    "Pere:San:Cugat:25:Hoquei herba:Terrassa",')
                        print('    "Laura:Mili:Arias:23:futbol:Barcelona",')
                        print(']')
                        print('')
                        print('total_edat = 0')
                        print('for element in esportistes:')
                        print('    camps = element.split(":")')
                        print('    edat = int(camps[3])')
                        print('    total_edat += edat')
                        print('')
                        print('mitjana = total_edat / len(esportistes)')
                        print('print(f"Mitjana d\'edat: {mitjana:.2f}")')
                        print(80*"-")
                            
                        probar = input("¿Quieres ejecutar el ejercicio 1? (s/n): ")
                        if probar == "s":
                            print("\n--- Ejecutando Ejercicio 1 ---")
                            esportistes = [
                                "Ana Maria:Fernandez:Marin:22:Natacio:Sabadell",
                                "Pere:San:Cugat:25:Hoquei herba:Terrassa",
                                "Laura:Mili:Arias:23:futbol:Barcelona",
                                "Sarai:Farell:Casasus:10:basquet:Joventut"
                            ]
                                
                            total_edat = 0
                            print("Procesando deportistas:")
                            for i, element in enumerate(esportistes, 1):
                                camps = element.split(":")
                                edat = int(camps[3])
                                total_edat += edat
                                print(f"  {i}. {camps[0]} {camps[1]} - {edat} años")
                                
                            mitjana = total_edat / len(esportistes)
                            print(f"\nTotal deportistas: {len(esportistes)}")
                            print(f"Suma de edades: {total_edat}")
                            print(f"Mitjana d'edat: {mitjana:.2f}")
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "7":  # Zen de Python
                        os.system('clear')
                        print(80*"-")
                        print("ZEN DE PYTHON")
                        print(80*"-")
                        
                        print("\nPara ver el Zen de Python en consola:")
                        print("$ python3 -c \"import this\"")
                        
                        ver_zen = input("\n¿Quieres ver el Zen de Python? (s/n): ")
                        if ver_zen == "s":
                            try:
                                import this
                            except:
                                print("No se pudo importar 'this'")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "8":
                        os.system('clear')
                        print("Volviendo al menu...")
                        time.sleep(0.5)
        
        case "2":  # Git
            print("Git... vamos avanzando")
            time.sleep(0.5)
            opcio_GIT = None
            while opcio_GIT != "6":
                os.system('clear')
                print("Que estructura estas interesado en aprender o repasar?")
                print("1. Fundamentos y conceptos básicos")
                print("2. Comandos básicos de Git")
                print("3. Trabajo con ramas (branches)")
                print("4. Repositorios remotos (GitHub)")
                print("5. Estrategias de uso y flujos de trabajo")
                print("6. Atrás")
                opcio_GIT = input()
                
                match opcio_GIT:
                    case "1":  # Fundamentos
                        os.system('clear')
                        print(80*"-")
                        print("FUNDAMENTOS DE GIT")
                        print("\n¿Qué es un Sistema de Control de Versiones (VCS)?")
                        print("- Sistema que registra cambios en archivos")
                        print("- Permite revertir y combinar versiones")
                        print("- Controla la evolución de proyectos")
                        
                        print("\nTipos de VCS:")
                        print("1. Local:")
                        print("   - Base de datos en sistema local")
                        print("   - No permite colaboración")
                        print("   - Ej: RCS")
                        
                        print("\n2. Centralizado:")
                        print("   - Un único servidor con todos los archivos")
                        print("   - Clientes obtienen copias")
                        print("   - Punto único de fallo")
                        print("   - Ej: CVS, Subversion, Perforce")
                        
                        print("\n3. Distribuido:")
                        print("   - Cada cliente tiene repositorio completo")
                        print("   - Se puede restaurar desde cualquier cliente")
                        print("   - Permite múltiples repositorios")
                        print("   - Ej: Git, Mercurial")
                        
                        print("\nFundamentos de Git:")
                        print("- Git guarda datos como SNAPSHOTS (instantáneas)")
                        print("- Cada commit es una foto completa del proyecto")
                        print("- Si un archivo no cambia, guarda enlace al anterior")
                        print("- Stream of snapshots vs Delta-based")
                        
                        print("\nHistoria de Git:")
                        print("1991-2002: Linux con archivos")
                        print("2002-2005: BitKeeper (propietario)")
                        print("2005: Creación de Git por Linus Torvalds")
                        print("- Velocidad")
                        print("- Diseño simple")
                        print("- Soporte para desarrollo no-lineal")
                        print("- Totalmente distribuido")
                        print("- Eficiente con grandes proyectos")
                        print(80*"-")
                        input("Presiona cualquier tecla para continuar...")
                    
                    case "2":  # Comandos básicos
                        os.system('clear')
                        print(80*"-")
                        print("COMANDOS BÁSICOS DE GIT")
                        
                        print("\n>>> Configuración inicial:")
                        print("git config --global user.name \"Tu Nombre\"")
                        print("git config --global user.email \"tu@email.com\"")
                        print("git config --global init.defaultBranch main")
                        
                        print("\n>>> Iniciar repositorio:")
                        print("git init               # Crear nuevo repositorio")
                        print("git clone <url>        # Clonar repositorio existente")
                        print("git status             # Estado de archivos")
                        
                        print("\n>>> Estados de archivos:")
                        print("Working directory  # Directorio de trabajo")
                        print("Staging area       # Área de preparación")
                        print("Repository         # Repositorio Git")
                        
                        print("\n>>> Estados principales:")
                        print("Modified   # Modificado pero no confirmado")
                        print("Staged     # Marcado para próximo commit")
                        print("Committed  # Guardado en repositorio")
                        
                        print("\n>>> Ciclo de trabajo:")
                        print("git add <archivo>      # Añadir al staging")
                        print("git add .              # Añadir todos los cambios")
                        print("git commit -m \"mensaje\" # Confirmar cambios")
                        print("git rm --cached <arch> # Quitar del staging")
                        
                        print("\n>>> Historial y recuperación:")
                        print("git log                 # Ver historial")
                        print("git log --pretty=oneline # Historial compacto")
                        print("git reset --hard <hash> # Restaurar estado anterior")
                        print("git commit --amend      # Corregir último commit")
                        
                        print("\n>>> Ejemplo de flujo básico:")
                        print("1. git init")
                        print("2. git add .")
                        print('3. git commit -m "Primer commit"')
                        print("4. (modificar archivos)")
                        print("5. git add .")
                        print('6. git commit -m "Segundo commit"')
                        print("7. git log")
                        print(80*"-")
                        
                        ejemplo = input("¿Quieres ver un ejemplo práctico? (s/n): ")
                        if ejemplo == "s":
                            print("\n--- Simulación de comandos Git ---")
                            print("$ mkdir mi-proyecto && cd mi-proyecto")
                            print("$ git init")
                            print("Initialized empty Git repository")
                            print("")
                            print("$ echo '# Mi Proyecto' > README.md")
                            print("$ git add README.md")
                            print("$ git commit -m \"Añadir README\"")
                            print("[main (root-commit) abc123] Añadir README")
                            print(" 1 file changed, 1 insertion(+)")
                            print("")
                            print("$ echo 'print(\"Hola Mundo\")' > hola.py")
                            print("$ git add .")
                            print("$ git commit -m \"Añadir script Python\"")
                            print("[main def456] Añadir script Python")
                            print(" 1 file changed, 1 insertion(+)")
                            print("")
                            print("$ git log --pretty=oneline")
                            print("def456... Añadir script Python")
                            print("abc123... Añadir README")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "3":  # Ramas
                        os.system('clear')
                        print(80*"-")
                        print("TRABAJO CON RAMAS (BRANCHES) EN GIT")
                        
                        print("\nConceptos básicos:")
                        print("- main: rama principal por defecto")
                        print("- HEAD: apuntador a la rama actual")
                        print("- Branch: línea de desarrollo independiente")
                        
                        print("\n>>> Comandos de ramas:")
                        print("git branch                   # Listar ramas")
                        print("git branch <nombre>          # Crear nueva rama")
                        print("git checkout <nombre>        # Cambiar a rama")
                        print("git checkout -b <nombre>     # Crear y cambiar")
                        print("git merge <rama>             # Fusionar rama")
                        print("git branch -d <nombre>       # Eliminar rama")
                        
                        print("\nTipos de merge:")
                        print("1. Fast-forward:")
                        print("   - Rama objetivo está adelantada")
                        print("   - Simplemente mueve el puntero")
                        print("   - No crea commit de merge")
                        
                        print("\n2. Merge commit:")
                        print("   - Ramas han divergido")
                        print("   - Crea nuevo commit con dos padres")
                        print("   - Puede tener conflictos")
                        
                        print("\n>>> Ejemplo de flujo con ramas:")
                        print("# Trabajar en nueva funcionalidad")
                        print("git checkout -b nueva-funcionalidad")
                        print("# ... hacer cambios ...")
                        print("git add .")
                        print('git commit -m "Añadir funcionalidad"')
                        print("# Volver a main y fusionar")
                        print("git checkout main")
                        print("git merge nueva-funcionalidad")
                        print("git branch -d nueva-funcionalidad")
                        
                        print("\n>>> Diagrama de ejemplo:")
                        print("       C1---C2---C3    main")
                        print("              \\")
                        print("               C4---C5  feature")
                        print("                     \\")
                        print("               C6---C7  main (después de merge)")
                        
                        print("\nConflictos de merge:")
                        print("1. Git no puede fusionar automáticamente")
                        print("2. Marca archivos conflictivos")
                        print("3. Debes resolver manualmente")
                        print("4. git add archivos resueltos")
                        print("5. git commit para finalizar merge")
                        print(80*"-")
                        
                        print("\nEjercicios prácticos:")
                        print("Dado un diagrama de ramas, deducir secuencia")
                        print("de comandos git que lo generó")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "4":  # Repositorios remotos
                        os.system('clear')
                        print(80*"-")
                        print("REPOSITORIOS REMOTOS - GITHUB")
                        
                        print("\nConceptos:")
                        print("- Repositorio remoto: versión en servidor")
                        print("- origin: nombre por defecto del remoto")
                        print("- PAT: Personal Access Token (autenticación)")
                        
                        print("\n>>> Comandos de repositorios remotos:")
                        print("git remote -v                 # Ver remotos")
                        print("git remote add <nom> <url>    # Añadir remoto")
                        print("git push <remoto> <rama>      # Subir cambios")
                        print("git pull <remoto> <rama>      # Bajar cambios")
                        print("git fetch <remoto>            # Traer sin fusionar")
                        print("git clone <url>               # Clonar remoto")
                        
                        print("\n>>> Flujo de trabajo con GitHub:")
                        print("1. Crear cuenta en GitHub")
                        print("2. Generar PAT (Settings > Developer settings)")
                        print("3. Crear repositorio nuevo en GitHub")
                        print("4. En local: git remote add origin <url>")
                        print("5. git push -u origin main")
                        print("6. Colaborador: git clone <url>")
                        print("7. Colaborador trabaja y hace git push")
                        print("8. Tú: git pull para actualizar")
                        
                        print("\n>>> Comandos detallados:")
                        print("git push origin main")
                        print("# Pide usuario y PAT como contraseña")
                        print("# Sube commits al servidor")
                        
                        print("\ngit pull origin main")
                        print("# Combina fetch + merge")
                        print("# Trae cambios y los fusiona")
                        
                        print("\ngit fetch origin")
                        print("# Solo trae cambios")
                        print("# No fusiona automáticamente")
                        print("# Útil para inspeccionar antes de merge")
                        
                        print("\n>>> Ejemplo completo:")
                        print("# Desde cero en local")
                        print("mkdir proyecto")
                        print("cd proyecto")
                        print("git init")
                        print("echo 'Hola' > archivo.txt")
                        print("git add .")
                        print('git commit -m "Primer commit"')
                        print("# En GitHub crear repositorio 'proyecto'")
                        print('git remote add origin https://github.com/usuario/proyecto.git')
                        print("git push -u origin main")
                        print(80*"-")
                        
                        print("\nPAT (Personal Access Token):")
                        print("1. GitHub > Settings")
                        print("2. Developer settings")
                        print("3. Personal access tokens")
                        print("4. Generate new token")
                        print("5. Seleccionar scopes necesarios")
                        print("6. Copiar token (solo se muestra una vez)")
                        print("7. Usar como contraseña en git push/pull")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "5":  # Estrategias
                        os.system('clear')
                        print(80*"-")
                        print("ESTRATEGIAS DE USO Y FLUJOS DE TRABAJO")
                        
                        print("\nNecesidades típicas en desarrollo:")
                        print("1. Seguimiento claro de versiones en producción")
                        print("2. Hotfixes para errores críticos")
                        print("3. Desarrollo de características sin afectar producción")
                        print("4. Cambiar entre tareas sin perder trabajo")
                        
                        print("\nReglas comunes:")
                        print("- No commits directos a main")
                        print("- Características nacen de development")
                        print("- Tests antes de taggear versión")
                        print("- Hotfixes solo de main")
                        
                        print("\n>>> Flujo Git Flow (simplificado):")
                        print("main        -- solo versiones de producción (taggeadas)")
                        print("development -- rama de integración")
                        print("feature/*   -- ramas para nuevas funcionalidades")
                        print("hotfix/*    -- ramas para correcciones urgentes")
                        
                        print("\n>>> Modus operandi:")
                        print("1. Developers trabajan en feature branches")
                        print("2. Feature completa → merge a development")
                        print("3. Tests en development")
                        print("4. Listo para producción → merge a main + tag")
                        print("5. Error en producción → hotfix desde tag")
                        print("6. Hotfix corregido → merge a main y development")
                        
                        print("\n>>> Ejemplo visual:")
                        print("main:      v1.0 --- v1.1 --- v2.0")
                        print("            |        |        |")
                        print("            | hotfix |        |")
                        print("            | /      |        |")
                        print("dev:     ----|-------|--------|----")
                        print("            /|      /|       /|")
                        print("feature1: --/      / |      / |")
                        print("feature2: --------/  |     /  |")
                        print("feature3: -----------/    /   |")
                        print("                          feature4")
                        
                        print("\n>>> Buenas prácticas:")
                        print("- Commits atómicos (una cosa por commit)")
                        print("- Mensajes descriptivos")
                        print("- Pull antes de push")
                        print("- Resolver conflictos localmente")
                        print("- Usar .gitignore para archivos no necesarios")
                        print("- Tags para versiones importantes")
                        print(80*"-")
                        
                        print("\nComandos útiles adicionales:")
                        print("git stash              # Guardar cambios temporales")
                        print("git stash pop          # Recuperar cambios")
                        print("git tag v1.0           # Crear tag")
                        print("git diff               # Ver diferencias")
                        print("git show <commit>      # Ver cambios de commit")
                        print(".gitignore             # Archivo para ignorar")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "6":
                        os.system('clear')
                        print("Volviendo al menu...")
                        time.sleep(0.5)
        
        case "3":  # Sistemas Operativos
            print("Sistemas operativos... lo último")
            time.sleep(0.5)
            opcio_SO = None
            while opcio_SO != "7":
                os.system('clear')
                print("Que estructura estas interesado en aprender o repasar?")
                print("1. Conceptos básicos de SO")
                print("2. Procesos y estados")
                print("3. Planificación de CPU")
                print("4. FCFS (First Come First Served)")
                print("5. SPN (Shortest Process Next)")
                print("6. RR (Round Robin)")
                print("7. Atrás")
                opcio_SO = input()
                
                match opcio_SO:
                    case "1":  # Conceptos básicos
                        os.system('clear')
                        print(80*"-")
                        print("CONCEPTOS BÁSICOS DE SISTEMAS OPERATIVOS")
                        
                        print("\nDefiniciones:")
                        print("Linus Torvalds:")
                        print("\"Un SO no ha de ser visto, la gente usa programas.")
                        print("La única misión de un SO es ayudar a los programas")
                        print("a ejecutarse.\"")
                        
                        print("\nOtras definiciones:")
                        print("- J. Carretero: Programa que simplifica gestión")
                        print("  y uso del computador")
                        print("- H. Deitel: Programa entre HW y usuario")
                        print("- Katzan: Controla ejecución de programas")
                        print("- Madnick y Donovan: Gestiona recursos del sistema")
                        
                        print("\nEstructura general:")
                        print("Usuarios → Aplicaciones → Shell")
                        print("↓")
                        print("Interfaz con SO (system calls)")
                        print("↓")
                        print("Gestión de: Procesos | Memoria | Archivos | E/S")
                        print("↓")
                        print("Interfaz con HW (drivers)")
                        print("↓")
                        print("Hardware (CPU, memoria, dispositivos)")
                        
                        print("\nComponentes principales:")
                        print("- Kernel: núcleo del SO")
                        print("- Shell: interfaz usuario-SO")
                        print("- System calls: interfaz programas-SO")
                        print("- Drivers: controladores de hardware")
                        
                        print("\nFunciones principales:")
                        print("1. Gestión de procesos")
                        print("2. Gestión de memoria")
                        print("3. Gestión de archivos")
                        print("4. Gestión de E/S")
                        print("5. Seguridad y protección")
                        print("6. Interfaz de usuario")
                        print(80*"-")
                        input("Presiona cualquier tecla para continuar...")
                    
                    case "2":  # Procesos y estados
                        os.system('clear')
                        print(80*"-")
                        print("PROCESOS Y ESTADOS EN SISTEMAS OPERATIVOS")
                        
                        print("\nConceptos:")
                        print("Programa → Ejecutable → Proceso")
                        print("\nProceso: programa en ejecución consumiendo recursos")
                        
                        print("\n>>> Fases de un programa:")
                        print("1. Compilación:")
                        print("   .c/.asm → Compilador → .o (objeto)")
                        print("2. Enlazado (linking):")
                        print("   .o + librerías → Linker → .exe (ejecutable)")
                        print("3. Carga (loading):")
                        print("   .exe → SO carga en memoria → Proceso")
                        
                        print("\nBloque de Control de Proceso (BCP/PCB):")
                        print("- Estado del procesador (registros)")
                        print("- Imagen de memoria")
                        print("- Información de control")
                        print("- Identificación (PID)")
                        print("- Recursos asignados")
                        
                        print("\nDiagrama de estados de un proceso:")
                        print("     Nuevo")
                        print("       ↓")
                        print("     Listo (Ready) ←┐")
                        print("       ↓           │")
                        print("  En ejecución   ←─┘ (expira tiempo)")
                        print("    ↓      ↓")
                        print("  Finalizado  Bloqueado")
                        print("              (espera evento)")
                        
                        print("\nEstados explicados:")
                        print("1. Nuevo: proceso recién creado")
                        print("2. Listo: esperando CPU")
                        print("3. En ejecución: usando CPU")
                        print("4. Bloqueado: esperando evento (E/S)")
                        print("5. Finalizado: terminó ejecución")
                        
                        print("\nMultiprogramación:")
                        print("- Múltiples procesos en memoria")
                        print("- Intercalados en ejecución")
                        print("- Aumenta utilización de CPU")
                        
                        print("\nDiagrama de Gantt:")
                        print("Tiempo: 0 1 2 3 4 5 6 7 8 9 10")
                        print("P1:     === === ===")
                        print("P2:         === ===")
                        print("P3:             === ===")
                        print("SO:   *   *   *   *   *")
                        
                        print("\nModos de ejecución:")
                        print("- Modo usuario: procesos normales")
                        print("- Modo supervisor/kernel: SO")
                        print("- Interrupciones cambian modo")
                        print(80*"-")
                        input("Presiona cualquier tecla para continuar...")
                    
                    case "3":  # Planificación
                        os.system('clear')
                        print(80*"-")
                        print("PLANIFICACIÓN DE CPU")
                        
                        print("\nPlanificador a corto plazo:")
                        print("- Decide qué proceso ejecutar")
                        print("- Gestiona transición Listo → Ejecución")
                        print("- Se ejecuta frecuentemente (ms)")
                        
                        print("\nDefiniciones de tiempos:")
                        print("Ta - Tiempo de llegada (Arrival Time)")
                        print("    Cuando el proceso llega al sistema")
                        print("\nTs - Tiempo de servicio (Burst Time)")
                        print("    Tiempo total de CPU necesario")
                        print("\nTc - Tiempo de finalización (Completion Time)")
                        print("    Cuando termina su ejecución")
                        print("\nTq - Tiempo de retorno (Turnaround Time)")
                        print("    Tq = Tc - Ta  (vida total)")
                        print("\nTw - Tiempo de espera (Waiting Time)")
                        print("    Tw = Tq - Ts  (en estado listo)")
                        print("\nTr - Tiempo de respuesta (Response Time)")
                        print("    Desde llegada hasta primera atención")
                        
                        print("\nFunciones de selección (FS):")
                        print("Cómo seleccionar el siguiente proceso:")
                        print("- Prioridades")
                        print("- Necesidades de recursos")
                        print("- Características del proceso")
                        
                        print("\nModos de selección (MS):")
                        print("1. No apropiativo:")
                        print("   - Proceso mantiene CPU hasta que:")
                        print("     * Finaliza")
                        print("     * Bloquea (E/S)")
                        print("   - Simple pero puede causar inanición")
                        
                        print("\n2. Apropiativo:")
                        print("   - SO puede quitar CPU")
                        print("   - En cualquier momento")
                        print("   - Más flexible")
                        print("   - Overhead por cambios de contexto")
                        
                        print("\nMétricas de evaluación:")
                        print("1. Throughput: procesos/tiempo")
                        print("2. Utilización de CPU: % tiempo ocupada")
                        print("3. Tiempo de retorno promedio")
                        print("4. Tiempo de espera promedio")
                        print("5. Tiempo de respuesta promedio")
                        
                        print("\nAlgoritmos comunes:")
                        print("1. FCFS - First Come First Served")
                        print("2. SPN  - Shortest Process Next")
                        print("3. RR   - Round Robin")
                        print("4. SRT  - Shortest Remaining Time")
                        print("5. Prioridades")
                        print(80*"-")
                        input("Presiona cualquier tecla para continuar...")
                    
                    case "4":  # FCFS
                        os.system('clear')
                        print(80*"-")
                        print("FCFS - FIRST COME FIRST SERVED")
                        
                        print("\nCaracterísticas:")
                        print("- Función selección: mayor tiempo de espera")
                        print("- Modo: No apropiativo")
                        print("- Simple de implementar")
                        print("- Justo en orden de llegada")
                        
                        print("\nProceso: P1, P2, P3, P4, P5")
                        print("Datos:")
                        print("Proceso | Ta | Ts")
                        print("--------|----|----")
                        print("   P1   |  0 |  3")
                        print("   P2   |  2 |  6")
                        print("   P3   |  4 |  4")
                        print("   P4   |  6 |  5")
                        print("   P5   |  8 |  2")
                        
                        print("\nDiagrama de Gantt:")
                        print("Tiempo: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")
                        print("P1:     = = =                                         ")
                        print("P2:         = = = = = =                               ")
                        print("P3:                 = = = =                           ")
                        print("P4:                     = = = = =                     ")
                        print("P5:                         = =                       ")
                        
                        print("\nCálculos:")
                        print("Tw(P1) = 0 - 0 = 0")
                        print("Tw(P2) = 3 - 2 = 1")
                        print("Tw(P3) = 9 - 4 = 5")
                        print("Tw(P4) = 13 - 6 = 7")
                        print("Tw(P5) = 18 - 8 = 10")
                        print("Tw promedio = (0+1+5+7+10)/5 = 23/5 = 4.6")
                        
                        print("\nTq(P1) = 3 - 0 = 3")
                        print("Tq(P2) = 9 - 2 = 7")
                        print("Tq(P3) = 13 - 4 = 9")
                        print("Tq(P4) = 18 - 6 = 12")
                        print("Tq(P5) = 20 - 8 = 12")
                        print("Tq promedio = (3+7+9+12+12)/5 = 43/5 = 8.6")
                        
                        print("\nVentajas:")
                        print("- Muy simple de implementar")
                        print("- Sin inanición (starvation)")
                        print("- Justo en tiempo de llegada")
                        
                        print("\nDesventajas:")
                        print("- Tiempo promedio de espera alto")
                        print("- Penaliza procesos cortos (convoy effect)")
                        print("- Poco responsivo")
                        print("- No óptimo para tiempos de respuesta")
                        
                        print("\nConvoy Effect:")
                        print("Si llega un proceso largo primero,")
                        print("todos los procesos cortos detrás")
                        print("deben esperar mucho tiempo.")
                        print(80*"-")
                        
                        simular = input("¿Quieres simular FCFS? (s/n): ")
                        if simular == "s":
                            print("\n--- Simulación FCFS ---")
                            procesos = [
                                {"nombre": "P1", "ta": 0, "ts": 3},
                                {"nombre": "P2", "ta": 2, "ts": 6},
                                {"nombre": "P3", "ta": 4, "ts": 4},
                                {"nombre": "P4", "ta": 6, "ts": 5},
                                {"nombre": "P5", "ta": 8, "ts": 2}
                            ]
                            
                            # Ordenar por tiempo de llegada
                            procesos.sort(key=lambda x: x["ta"])
                            
                            tiempo_actual = 0
                            print("\nEjecución:")
                            for p in procesos:
                                if tiempo_actual < p["ta"]:
                                    tiempo_actual = p["ta"]
                                
                                print(f"T={tiempo_actual}: Comienza {p['nombre']}")
                                tiempo_actual += p["ts"]
                                p["tc"] = tiempo_actual
                                print(f"T={tiempo_actual}: Termina {p['nombre']}")
                            
                            # Cálculos
                            print("\nResultados:")
                            total_tw = 0
                            total_tq = 0
                            for p in procesos:
                                tq = p["tc"] - p["ta"]
                                tw = tq - p["ts"]
                                total_tw += tw
                                total_tq += tq
                                print(f"{p['nombre']}: Tq={tq}, Tw={tw}")
                            
                            print(f"\nPromedio Tw: {total_tw/len(procesos):.1f}")
                            print(f"Promedio Tq: {total_tq/len(procesos):.1f}")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "5":  # SPN
                        os.system('clear')
                        print(80*"-")
                        print("SPN - SHORTEST PROCESS NEXT (SJF No Apropiativo)")
                        
                        print("\nCaracterísticas:")
                        print("- Función selección: menor tiempo de servicio")
                        print("- Modo: No apropiativo")
                        print("- Requiere conocimiento de Ts")
                        print("- También llamado SJF (Shortest Job First)")
                        
                        print("\nMismo ejemplo:")
                        print("Proceso | Ta | Ts")
                        print("--------|----|----")
                        print("   P1   |  0 |  3")
                        print("   P2   |  2 |  6")
                        print("   P3   |  4 |  4")
                        print("   P4   |  6 |  5")
                        print("   P5   |  8 |  2")
                        
                        print("\nDiagrama de Gantt:")
                        print("Tiempo: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")
                        print("P1:     = = =                                         ")
                        print("P2:         = = = = = =                               ")
                        print("P3:                     = = = =                       ")
                        print("P4:                         = = = = =                 ")
                        print("P5:                 = =                               ")
                        
                        print("\nSecuencia:")
                        print("T=0: Solo P1 (Ts=3) → P1")
                        print("T=3: P2 (Ts=6), P3 no ha llegado → P2")
                        print("T=9: P3 (Ts=4), P4 (Ts=5), P5 (Ts=2) → P5 (menor)")
                        print("T=11: P3 (Ts=4), P4 (Ts=5) → P3 (menor)")
                        print("T=15: P4 (Ts=5) → P4")
                        
                        print("\nCálculos:")
                        print("Tw(P1) = 0 - 0 = 0")
                        print("Tw(P2) = 3 - 2 = 1")
                        print("Tw(P3) = 11 - 4 = 7")
                        print("Tw(P4) = 15 - 6 = 9")
                        print("Tw(P5) = 9 - 8 = 1")
                        print("Tw promedio = (0+1+7+9+1)/5 = 18/5 = 3.6")
                        
                        print("\nTq(P1) = 3 - 0 = 3")
                        print("Tq(P2) = 9 - 2 = 7")
                        print("Tq(P3) = 15 - 4 = 11")
                        print("Tq(P4) = 20 - 6 = 14")
                        print("Tq(P5) = 11 - 8 = 3")
                        print("Tq promedio = (3+7+11+14+3)/5 = 38/5 = 7.6")
                        
                        print("\nVentajas:")
                        print("- Minimiza tiempo de espera promedio")
                        print("- Óptimo para Tw promedio")
                        print("- Alto throughput")
                        print("- Buen tiempo de respuesta")
                        
                        print("\nDesventajas:")
                        print("- Posible inanición para procesos largos")
                        print("- Dificultad para estimar Ts")
                        print("- No apropiativo (poco responsivo)")
                        print("- Necesita conocimiento futuro")
                        
                        print("\nInanición (Starvation):")
                        print("Si llegan continuamente procesos cortos,")
                        print("los procesos largos pueden nunca ejecutarse.")
                        print(80*"-")
                        
                        simular = input("¿Quieres simular SPN? (s/n): ")
                        if simular == "s":
                            print("\n--- Simulación SPN ---")
                            procesos = [
                                {"nombre": "P1", "ta": 0, "ts": 3},
                                {"nombre": "P2", "ta": 2, "ts": 6},
                                {"nombre": "P3", "ta": 4, "ts": 4},
                                {"nombre": "P4", "ta": 6, "ts": 5},
                                {"nombre": "P5", "ta": 8, "ts": 2}
                            ]
                            
                            tiempo_actual = 0
                            completados = []
                            en_sistema = []
                            
                            print("\nEjecución paso a paso:")
                            while len(completados) < len(procesos):
                                # Añadir procesos que han llegado
                                for p in procesos:
                                    if p["ta"] <= tiempo_actual and p not in completados and p not in en_sistema:
                                        en_sistema.append(p)
                                
                                if en_sistema:
                                    # Seleccionar proceso con menor Ts
                                    en_sistema.sort(key=lambda x: x["ts"])
                                    actual = en_sistema[0]
                                    en_sistema.remove(actual)
                                    
                                    print(f"T={tiempo_actual}: Comienza {actual['nombre']} (Ts={actual['ts']})")
                                    tiempo_actual += actual["ts"]
                                    actual["tc"] = tiempo_actual
                                    completados.append(actual)
                                    print(f"T={tiempo_actual}: Termina {actual['nombre']}")
                                else:
                                    tiempo_actual += 1
                            
                            # Cálculos
                            print("\nResultados:")
                            total_tw = 0
                            total_tq = 0
                            for p in procesos:
                                tq = p["tc"] - p["ta"]
                                tw = tq - p["ts"]
                                total_tw += tw
                                total_tq += tq
                                print(f"{p['nombre']}: Tc={p['tc']}, Tq={tq}, Tw={tw}")
                            
                            print(f"\nPromedio Tw: {total_tw/len(procesos):.1f}")
                            print(f"Promedio Tq: {total_tq/len(procesos):.1f}")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "6":  # Round Robin
                        os.system('clear')
                        print(80*"-")
                        print("ROUND ROBIN (Torn Rotatori)")
                        
                        print("\nCaracterísticas:")
                        print("- Función selección: orden en cola de listos")
                        print("- Modo: Apropiativo (por quantum)")
                        print("- Quantum: porción de tiempo asignada")
                        print("- Justo para todos los procesos")
                        
                        print("\nMismo ejemplo con quantum=4:")
                        print("Proceso | Ta | Ts")
                        print("--------|----|----")
                        print("   P1   |  0 |  3")
                        print("   P2   |  2 |  6")
                        print("   P3   |  4 |  4")
                        print("   P4   |  6 |  5")
                        print("   P5   |  8 |  2")
                        
                        print("\nDiagrama de Gantt:")
                        print("Tiempo: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")
                        print("P1:     = = =                                         ")
                        print("P2:           = = = =     = =                         ")
                        print("P3:                 = = = =                           ")
                        print("P4:                     = = = =   =                   ")
                        print("P5:                               = =                 ")
                        
                        print("\nExplicación:")
                        print("T=0: P1 (queda 3) → ejecuta 3 (termina)")
                        print("T=3: P2 (Ts=6) → ejecuta 4 (queda 2)")
                        print("T=7: P3 (Ts=4) → ejecuta 4 (termina)")
                        print("T=11: P4 (Ts=5) → ejecuta 4 (queda 1)")
                        print("T=15: P2 (queda 2) → ejecuta 2 (termina)")
                        print("T=17: P5 (Ts=2) → ejecuta 2 (termina)")
                        print("T=19: P4 (queda 1) → ejecuta 1 (termina)")
                        
                        print("\nCálculos:")
                        print("Tw(P1) = 0 (no espera)")
                        print("Tw(P2) = (3-2) + (15-7) = 1 + 8 = 9")
                        print("Tw(P3) = 7-4 = 3")
                        print("Tw(P4) = (11-6) + (19-15) = 5 + 4 = 9")
                        print("Tw(P5) = 17-8 = 9")
                        print("Tw promedio = (0+9+3+9+9)/5 = 30/5 = 6")
                        
                        print("\nTq(P1) = 3 - 0 = 3")
                        print("Tq(P2) = 17 - 2 = 15")
                        print("Tq(P3) = 11 - 4 = 7")
                        print("Tq(P4) = 20 - 6 = 14")
                        print("Tq(P5) = 19 - 8 = 11")
                        print("Tq promedio = (3+15+7+14+11)/5 = 50/5 = 10")
                        
                        print("\nEfecto del quantum:")
                        print("q muy pequeño → muchos cambios de contexto")
                        print("q muy grande → se comporta como FCFS")
                        print("q ideal: 80% ráfagas < q")
                        print("q >> tiempo cambio contexto")
                        
                        print("\nVentajas:")
                        print("- Sin inanición")
                        print("- Buen tiempo de respuesta")
                        print("- Justo para todos")
                        print("- Responsivo")
                        
                        print("\nDesventajas:")
                        print("- Overhead por cambios de contexto")
                        print("- Performance depende del quantum")
                        print("- Penaliza procesos con mucha E/S")
                        print("- Tiempo retorno puede ser alto")
                        
                        print("\nQuantum típico:")
                        print("- Sistemas time-sharing: 10-100 ms")
                        print("- Debe ser >> tiempo cambio contexto")
                        print("- Sintonizable según carga")
                        print(80*"-")
                        
                        simular = input("¿Quieres simular Round Robin? (s/n): ")
                        if simular == "s":
                            print("\n--- Simulación Round Robin (quantum=4) ---")
                            procesos = [
                                {"nombre": "P1", "ta": 0, "ts": 3, "restante": 3},
                                {"nombre": "P2", "ta": 2, "ts": 6, "restante": 6},
                                {"nombre": "P3", "ta": 4, "ts": 4, "restante": 4},
                                {"nombre": "P4", "ta": 6, "ts": 5, "restante": 5},
                                {"nombre": "P5", "ta": 8, "ts": 2, "restante": 2}
                            ]
                            
                            quantum = 4
                            tiempo_actual = 0
                            cola = []
                            completados = []
                            tiempos_inicio = {}
                            tiempos_espera = {p["nombre"]: 0 for p in procesos}
                            ultimo_tiempo = {p["nombre"]: p["ta"] for p in procesos}
                            
                            print("\nEjecución:")
                            while len(completados) < len(procesos):
                                # Añadir procesos que han llegado
                                for p in procesos:
                                    if p["ta"] <= tiempo_actual and p not in completados and p not in cola:
                                        cola.append(p)
                                
                                if cola:
                                    actual = cola.pop(0)
                                    
                                    # Calcular tiempo de espera
                                    tiempos_espera[actual["nombre"]] += tiempo_actual - ultimo_tiempo[actual["nombre"]]
                                    
                                    # Ejecutar
                                    tiempo_ejecucion = min(quantum, actual["restante"])
                                    print(f"T={tiempo_actual}: Ejecuta {actual['nombre']} ({tiempo_ejecucion}u)")
                                    
                                    tiempo_actual += tiempo_ejecucion
                                    actual["restante"] -= tiempo_ejecucion
                                    ultimo_tiempo[actual["nombre"]] = tiempo_actual
                                    
                                    if actual["restante"] > 0:
                                        # Revisar nuevos llegados
                                        for p in procesos:
                                            if p["ta"] <= tiempo_actual and p not in completados and p not in cola and p != actual:
                                                cola.append(p)
                                        cola.append(actual)
                                    else:
                                        actual["tc"] = tiempo_actual
                                        completados.append(actual)
                                        print(f"  {actual['nombre']} termina en T={tiempo_actual}")
                                else:
                                    tiempo_actual += 1
                            
                            # Cálculos
                            print("\nResultados:")
                            total_tw = 0
                            total_tq = 0
                            for p in procesos:
                                tq = p["tc"] - p["ta"]
                                tw = tiempos_espera[p["nombre"]]
                                total_tw += tw
                                total_tq += tq
                                print(f"{p['nombre']}: Tc={p['tc']}, Tq={tq}, Tw={tw}")
                            
                            print(f"\nPromedio Tw: {total_tw/len(procesos):.1f}")
                            print(f"Promedio Tq: {total_tq/len(procesos):.1f}")
                        
                        input("\nPresiona cualquier tecla para continuar...")
                    
                    case "7":
                        os.system('clear')
                        print("Volviendo al menu...")
                        time.sleep(0.5)
        
        case "4":  # Información y ayuda
            os.system('clear')
            print(80*"=")
            print("INFORMACIÓN Y AYUDA")
            print(80*"=")
            print("\nEste programa contiene todo el temario de:")
            print("1. PROGRAMACIÓN PYTHON")
            print("2. SISTEMAS DE CONTROL DE VERSIONES (GIT)")
            print("3. FUNDAMENTOS DE SISTEMAS OPERATIVOS")
            
            print("\nContenido detallado:")
            
            print("\n=== PYTHON ===")
            print("✓ Variables y operadores")
            print("✓ Control de flujo (if/else, match)")
            print("✓ Bucles (while, for)")
            print("✓ Listas y cadenas de caracteres")
            print("✓ Gestión de archivos")
            print("✓ Ejercicios prácticos")
            print("✓ Zen de Python")
            
            print("\n=== GIT ===")
            print("✓ Fundamentos y conceptos básicos")
            print("✓ Comandos básicos de Git")
            print("✓ Trabajo con ramas (branches)")
            print("✓ Repositorios remotos (GitHub)")
            print("✓ Estrategias de uso y flujos de trabajo")
            print("✓ PAT (Personal Access Token)")
            print("✓ Merge y conflictos")
            
            print("\n=== SISTEMAS OPERATIVOS ===")
            print("✓ Conceptos básicos de SO")
            print("✓ Procesos y estados")
            print("✓ Planificación de CPU")
            print("✓ FCFS (First Come First Served)")
            print("✓ SPN (Shortest Process Next)")
            print("✓ RR (Round Robin)")
            print("✓ Diagramas de Gantt")
            print("✓ Cálculo de tiempos (Tq, Tw, Tr)")
            
            print("\nCaracterísticas del programa:")
            print("- Explicaciones teóricas completas")
            print("- Ejemplos prácticos interactivos")
            print("- Simulaciones de algoritmos")
            print("- Ejercicios con soluciones")
            print("- Navegación intuitiva por menús")
            
            print("\nInstrucciones de uso:")
            print("1. Selecciona un tema principal (1-4)")
            print("2. Elige subtema específico")
            print("3. Sigue las explicaciones")
            print("4. Prueba los ejemplos cuando se ofrezcan")
            print("5. Usa 's' para Sí y 'n' para No")
            print("6. Presiona cualquier tecla para continuar")
            
            print("© 2026 - Programa de aprendizaje integral - Miguel Martín Gil")
            print(80*"=")
            input("\nPresiona cualquier tecla para volver al menú principal...")
        
        case "5":
            os.system('clear')
            print("Saliendo del programa...")
            time.sleep(0.5)
        
        case _:
            print("ERROR: Opción no válida. Por favor, selecciona 1-5.")
            time.sleep(1)

print("\n¡Gracias por usar el programa!")
print("¡Feliz Navidad!")