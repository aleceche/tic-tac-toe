# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:42:55 2020

@author: Alec
"""

gameBoard = {'TL': ' ', 'TC': ' ', 'TR': ' ',
             'L': ' ', 'C': ' ', 'R': ' ',
             'BL': ' ', 'BC': ' ', 'BR': ' '}
           
board_keys = []

for key in gameBoard:
    board_keys.append(key)
    
def printBoard(board):
    print(board['TL'] + '|' + board['TC'] + '|' + board['TR'])
    print('-+-+-')
    print(board['L'] + '|' + board['C'] + '|' + board['R'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BC'] + '|' + board['BR'])

def choosePlayerLetter(player):
    options = ['X', 'O']
    print ('\n' + str(options))
    choice = input('Player ' + player + ' choose your letter: \n')
    choice = choice.upper()
    while choice not in options:
        choice = input('That is not a valid input. Player ' + player + ', please try again.\n')
        choice = choice.upper()
    print('\nPlayer ' + player + ' has chosen ' + choice)
    if choice == 'X':
        return options
    else:
        return options[::-1]

def makePlayerMove(board, pL, choice):
    board[choice] = pL

def isWinner(board,pL):
    return ((board['TL'] == pL and board['TC'] == pL and board['TR'] == pL) or
            (board['L'] == pL and board['C'] == pL and board['R'] == pL) or
            (board['BL'] == pL and board['BC'] == pL and board['BR'] == pL) or
            (board['TL'] == pL and board['L'] == pL and board['BL'] == pL) or
            (board['TC'] == pL and board['C'] == pL and board['BC'] == pL) or
            (board['TR'] == pL and board['R'] == pL and board['BR'] == pL) or
            (board['TL'] == pL and board['C'] == pL and board['BR'] == pL) or
            (board['TR'] == pL and board['C'] == pL and board['BL'] == pL))

def playAgain(score1, score2, lastWin, compGame = False):
    options2 = ['Y', 'N']    
    playAgain = input('Would you like to play again? Y/N\n')
    playAgain = playAgain.upper()
    
    while playAgain not in options2:
        playAgain = input("That is not a valid input. Would you like to play again?\n")
        playAgain = playAgain.upper()

    if playAgain == 'Y':
        print('\nCurrent Score - \nPlayer 1: ' + str(score1) + '\nPlayer 2: ' + str(score2))
        for key in board_keys:
            gameBoard[key] = " "
        return tictactoe(score1, score2, lastWin)
    else:
        print('\nThanks for playing! Final Score - \nPlayer 1: ' + str(score1) + '\nPlayer 2: ' + str(score2) + '\n')
        if score1 > score2:
            print ("Player 1 wins!")
        elif score2 > score1:
            print ("Player 2 wins!")
        else:
            print ("It's a tie!")
        return None

    
def tictactoe(score1, score2, lastWin = '2'):
    if lastWin == '2':
        player = '1'
    else:
        player = '2'
    
    playerLetters = choosePlayerLetter(player)  
    options = ['TL','TC','TR','L','C','R','BL','BC','BR']
    printOptions = {'TL': 'Top Left', 'TC': 'Top Center', 'TR': 'Top Right',
                 'L': 'Left', 'C': 'Center', 'R': 'Right',
                 'BL': 'Bottom Left', 'BC': 'Bottom Center', 'BR': 'Bottom Right'}
    
    for i in range(1,10):
        if lastWin == '2':
            if player == '1':
                playerLetter = playerLetters[0]
            else:
                playerLetter = playerLetters[1]
        else:
            if player == '1':
                playerLetter = playerLetters[1]
            else:
                playerLetter = playerLetters[0]
        printBoard(gameBoard) 
        print('\n' + 'Available Options: ' + str(options))       
        choice = input("Player " + player + "'s move. Please choose an open square.\n")
        choice = choice.upper()
        
        while choice not in options:
            choice = input("That is not a valid input. Player " + player + ", please try again.\n")
            choice = choice.upper()     
        
        options.remove(choice)
        makePlayerMove(gameBoard, playerLetter, choice)
        print('\nPlayer ' + player + ' has chosen ' + printOptions[choice])
            
        if i >= 5:
            gameWon = isWinner(gameBoard, playerLetter)
            if gameWon:
                printBoard(gameBoard)
                print ("Player " + player + " wins!")
                if player == '1':
                    score1 += 1
                else:
                    score2 += 1
                lastWin = player
                break
            elif i == 9:
                printBoard(gameBoard)
                print ("It's a tie")
                lastWin = player
                break
        
        if player == '1':
            player = '2'
        else:
            player = '1'
    
    playAgain(score1, score2, lastWin)
    

if __name__ == "__main__":
    tictactoe(0,0)