Feature: Hangman Game

  Scenario: Empezar nuevo juego
      Given Ingreso a la pagina del juego
      When Comienza el juego
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6
      And las letras incorrectas deben estar vacias

  Scenario Outline: Adivinar una letra correcta
      Given El jugador empieza el juego
      When El jugador ingresa la letra "<letra>"
      Then La palabra se actualiza y contiene la "<letra>"
      And el numero de vidas debe ser 6
      And las letras incorrectas deben estar vacias


    
    Examples: 
      | letra |                       
      | a |
      | e |

  Scenario Outline: Ingresar una letra incorrecta
      Given El jugador empieza el juego
      When El jugador ingresa la letra "<letra>"
      Then Pierde una vida
      And Se muestra como letra incorrecta "<letra>"

    Examples: 
      | letra |                       
      | ñ |
      | x |

 
  Scenario: Pierde el juego
    Given El jugador empieza el juego
    When El jugador ingresa 6 caracteres incorrectos
    Then Pierde el juego
    Then Muestra el mensaje de que perdio con la palabra a adivinar
  
  Scenario Outline: Reinicia el juego
    Given El jugador empieza el juego
    And El jugador ingresa la letra "<letra>"
    When El jugador reinicia el juego
    Then la palabra a adivinar debe mostrarse con guiones
    And el numero de vidas debe ser 6
    And las letras incorrectas deben estar vacias
  Examples: 
      | letra |                       
      | a |
      | x |


