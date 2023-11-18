from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Ingreso a la pagina del juego')
def abrirPagina(context):
    context.driver = webdriver.Chrome()
    #context.driver.get("http://localhost:5000/")


@when(u'Comienza el juego')
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
def cantidad_vidas(context):
    h2 = context.driver.find_element(By.ID,'vidas').text
    print(h2)
    digitos = ''.join(caracter for caracter in h2 if caracter.isdigit())

    print(digitos)

    assert digitos == 6


@then('las letras incorrectas deben estar vacias')
def incorrectas_vacias(context):
    texto = context.driver.find_element(By.ID,'incorrectas').text
  
    inicio_lista = texto.find("[")

    incorrectas = eval(texto[inicio_lista:])
    assert len(incorrectas) == 0

@given(u'La palabra a adivinar del juego es "agiles"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given La palabra a adivinar del juego es "agiles"')


@when(u'El jugador adivina la letra "g"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When El jugador adivina la letra "g"')


@then(u'Se muestra "_ G _ _ _ _"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Se muestra "_ G _ _ _ _"')


@given(u'La palabra a adivinar del juego es "python"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given La palabra a adivinar del juego es "python"')


@when(u'El jugador adivina la letra "u"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When El jugador adivina la letra "u"')


@then(u'Pierde una vida')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Pierde una vida')


@then(u'Se muestra como letra incorrecta "u"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Se muestra como letra incorrecta "u"')


@given(u'La palabra a adivinar del juego es "puerta"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given La palabra a adivinar del juego es "puerta"')


@when(u'El jugador adivina las letras "P", "U", "E", "R", "T", "A"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When El jugador adivina las letras "P", "U", "E", "R", "T", "A"')


@then(u'Gana el juego')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Gana el juego')


@then(u'Muestra mensaje ganador con la palabra a adivinar')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Muestra mensaje ganador con la palabra a adivinar')


@when(u'El jugador adivina 6 letras incorrectas')
def step_impl(context):
    raise NotImplementedError(u'STEP: When El jugador adivina 6 letras incorrectas')


@then(u'Pierde el juego')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Pierde el juego')


@then(u'Muestra el mensaje de que perdio con la palabra a adivinar')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Muestra el mensaje de que perdio con la palabra a adivinar')