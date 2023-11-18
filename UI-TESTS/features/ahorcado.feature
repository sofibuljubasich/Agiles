Feature: Hangman Game

  Scenario: Empezar nuevo juego
      Given Ingreso a la pagina del juego
      When Comienza el juego
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6
      And las letras incorrectas deben estar vacias
  
  Scenario: Adivinar una letra correcta
      Given La palabra a adivinar del juego es "agiles"
      When El jugador adivina la letra "g"
      Then Se muestra "["_","G","_","_","_","_"]"

  Scenario: Adivinar una letra incorrecta
      Given La palabra a adivinar del juego es "python"
      When El jugador adivina la letra "u"
      Then Pierde una vida
      And Se muestra como letra incorrecta "u"

  Scenario: Gana el juego
    Given La palabra a adivinar del juego es "puerta"
    When El jugador adivina las letras "P", "U", "E", "R", "T", "A"
    Then Gana el juego
    And Muestra mensaje ganador con la palabra a adivinar
  
  Scenario: Pierde el juego
    Given La palabra a adivinar del juego es "puerta"
    When El jugador adivina 6 letras incorrectas
    Then Pierde el juego
    And Muestra el mensaje de que perdio con la palabra a adivinar


