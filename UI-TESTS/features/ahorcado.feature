Feature: Hangman Game

    Scenario: Empezar nuevo juego
        Given Ingreso a la pagina del juego
        When Comienza el juego
        Then la palabra a adivinar debe mostrarse con guiones
        And el numero de vidas debe ser 6
        And las letras incorrectas deben estar vacias

   

  Scenario: Make a correct guess
    Given the Hangman game has a secret word "PYTHON"
    When the player guesses the letter "P"
    Then the display shows "P _ _ _ _ _"
    And the number of incorrect guesses is 0

  Scenario: Make an incorrect guess
    Given the Hangman game has a secret word "PYTHON"
    When the player guesses the letter "X"
    Then the display remains unchanged
    And the number of incorrect guesses is 1

  Scenario: Win the game
    Given the Hangman game has a secret word "PYTHON"
    When the player guesses the letters "P", "Y", "T", "H", "O", "N"
    Then the display shows "PYTHON"
    And the game is won

  Scenario: Lose the game
    Given the Hangman game has a secret word "PYTHON"
    When the player makes 6 incorrect guesses
    Then the game is lost

