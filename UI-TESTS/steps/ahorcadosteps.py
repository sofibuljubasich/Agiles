from behave import *
from selenium import webdriver

@given('Ingreso a la pagina del juego')
def abrirPagina(context):
    context.driver = webdriver.Chrome("D:\Docs\Agiles\UI-TESTS\chromedriver.exe")
    context.driver.get("http://localhost:5000/")

@when(u'Inicializa el juego')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Inicializa el juego')


@then(u'la palabra a adivinar debe mostrarse con guiones')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then la palabra a adivinar debe mostrarse con guiones')


@then(u'el numero de vidas debe ser 6')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el numero de vidas debe ser 6')


@then(u'las letras incorrectas deben estar vacias')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then las letras incorrectas deben estar vacias')
