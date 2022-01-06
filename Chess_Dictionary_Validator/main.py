#Chess Dictionary Validator
def chessValidator(dict):
    positions = list(dict.keys())
    pieces = list(dict.values())
    validBlackPieces = {"king": 1, "queen": 1, "rook": 2, "bishop": 2, "knight": 2, "pawn": 8}
    validWhitePieces = {"king": 1, "queen": 1, "rook": 2, "bishop": 2, "knight": 2, "pawn": 8}
    validAlphaPositions = ["a", "b", "c", "d", "e", "f", "g", "h"]
    validNumPositions = [1, 2, 3, 4, 5, 6, 7, 8]
    

    for k,v in dict.items():
        if int(k[0]) in validNumPositions and k[1] in validAlphaPositions:
            currentPiece = v[1:]
            if v[0] == "b" and currentPiece in validBlackPieces:
                    if validBlackPieces[currentPiece] > 0:
                        validBlackPieces[currentPiece] -= 1
                    else:
                        return False
    
            elif v[0] == "w" and currentPiece in validWhitePieces:
                    if validWhitePieces[currentPiece] > 0:
                        validWhitePieces[currentPiece] -= 1
                    else:
                        return False
            else:
                return False
        else:
            return False
    return True

print(chessValidator({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))