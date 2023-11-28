from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


LOST_URL = "http://localhost:5000/adivinar"
LOST_MESSAGE = "Oh no, Perdiste!"
PALABRA_LOST_MESSAGE = "No pudiste adivinar la palabra: "

@given('Ingreso a la pagina del juego')
def abrirPagina(context):
    context.driver = webdriver.Chrome()
    #context.driver.get("http://localhost:5000/")


@when('Comienza el juego')
def comienza_juego(context):
    context.driver.get("http://localhost:5000/")


@then('la palabra a adivinar debe mostrarse con guiones')
def palabra_con_guiones(context):
    texto = context.driver.find_element(By.ID,'palabraAhorcado').text  
    inicio_lista = texto.find("[")

    palabra_con_guiones = eval(texto[inicio_lista:])

    print(palabra_con_guiones)
    print(palabra_con_guiones.count('_'))
    print(len(palabra_con_guiones))
    assert palabra_con_guiones.count('_') == len(palabra_con_guiones)


@then('el numero de vidas debe ser 6')
def mantiene_vidas(context):
    h2 = context.driver.find_element(By.ID,'vidas').text
    print(h2)
    digitos = int(''.join(caracter for caracter in h2 if caracter.isdigit()))

    print(digitos)

    assert digitos == 6


@then('las letras incorrectas deben estar vacias')
def incorrectas_vacias(context):
    texto = context.driver.find_element(By.ID,'incorrectas').text
  
    inicio_lista = texto.find("[")

    incorrectas = eval(texto[inicio_lista:])
    assert len(incorrectas) == 0



@given('El jugador empieza el juego')
def empieza_juego(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/")

@when('El jugador ingresa la letra "{letra}"')
def ingresa_letra(context,letra):
    elemento =  context.driver.find_element(By.NAME,"input")
    elemento.send_keys(letra)
    context.driver.implicitly_wait(40) # seconds

    context.driver.find_element(By.NAME,"adivinar").click()
    
    
@then('Pierde una vida')
def pierde_vida(context):
    h2 = context.driver.find_element(By.ID,'vidas').text
    print(h2)
    vidas = int(''.join(caracter for caracter in h2 if caracter.isdigit()))

    assert vidas < 6



@then('Se muestra como letra incorrecta "{letra}"')
def letras_incorrectas(context,letra):
    
    texto = context.driver.find_element(By.ID,'incorrectas').text  
    inicio_lista = texto.find("[")

    incorrectas = eval(texto[inicio_lista:])

    assert letra in incorrectas

@then('La palabra se actualiza y contiene la "{letra}"')
def estado_palabra_adivinar(context,letra):
    texto = context.driver.find_element(By.ID,'palabraAhorcado').text  
    inicio_lista = texto.find("[")

    palabra_adivinar = eval(texto[inicio_lista:])

    assert letra in palabra_adivinar
    
@when('El jugador ingresa 6 caracteres incorrectos')
def adivina_6_incorrectas(context):
    caracteres = ["!","*","+",".","&",":"]
    context.driver.implicitly_wait(40) # seconds

    for c in caracteres:
        elemento =  context.driver.find_element(By.NAME,"input")
        elemento.send_keys(c)
        context.driver.implicitly_wait(40) # seconds

        context.driver.find_element(By.NAME,"adivinar").click()
    

@then('Pierde el juego')
def pierde(context):
    assert LOST_URL in context.driver.current_url

@then('Muestra el mensaje de que perdio con la palabra a adivinar')
def mensaje_pierde(context):
    mensaje = context.driver.find_element(By.ID,'lost').text
    palabra = context.driver.find_element(By.ID,'palabra').text

    assert mensaje == LOST_MESSAGE
    assert  PALABRA_LOST_MESSAGE in palabra

@given('El jugador ingresa la letra "{letra}"')
def ingresa_letra(context,letra):
    elemento =  context.driver.find_element(By.NAME,"input")
    elemento.send_keys(letra)
    context.driver.implicitly_wait(40) # seconds

    context.driver.find_element(By.NAME,"adivinar").click()
    
    
@when('El jugador reinicia el juego')
def reinicia(context):
    context.driver.find_element(By.NAME,"reinicia").click()

