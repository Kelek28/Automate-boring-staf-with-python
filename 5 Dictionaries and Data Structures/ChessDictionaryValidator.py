# Chapter 5
# Project: Chess Dictionary Validator


def isValidChessBoard(boardDictionary):
    ValidListOfPieces, ValidBoardList = generateChessListAndBoard()
    # Check if space where piece stand is valid
    for space in boardDictionary.keys():
        if space not in ValidBoardList:
            return False
        ValidBoardList.remove(space)
    # Check if piece is valid
    for piece in boardDictionary.values():
        if piece not in ValidListOfPieces:
            return False
        ValidListOfPieces.remove(piece)
    return True

# Generate valid list of board and pieces


def generateChessListAndBoard():
    allPieces = []
    allSpaces = []
    validBoardDic = {"a": 8, "b": 8, "c": 8,
                     "d": 8, "e": 8, "f": 8, "g": 8, "h": 8}
    validChessDic = {"queen": 1, "king": 1, 'pawn': 8,
                     'knight': 2, 'bishop': 2, 'rook': 2}

    # generate list of all piece bking, wking ...
    for piece in validChessDic:
        for amount in range(validChessDic[piece]):
            allPieces.append("w"+piece)
            allPieces.append("b"+piece)
    # generate list of all spaces 1a, 1b ...
    for letter in validBoardDic:
        for i in range(validBoardDic[letter]):
            allSpaces.append("{}{}".format(i+1, letter))
    return allPieces, allSpaces


# return True
chessBoardTest = {'1h': 'bking', '6c': 'wqueen',
                  '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
isValidChessBoard(chessBoardTest)

# return False
chessBoardTest = {'1h': 'bking', '6c': 'wqueen',
                  '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '1a': "wking"}
isValidChessBoard(chessBoardTest)
