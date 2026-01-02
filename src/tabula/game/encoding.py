"""
Board Encoding for tabula.

AlphaZero uses a 119-plane representation.
- 8 time steps x (6 piece types x 2 colors) - 96 planes for piece positions
- 8 time steps x 2 = 16 planes for repetitions (T1 and  T2 indicators)
- 4 planes for castling rights
- 1 plane for side to move 
- 1 plane for total move count
- 1 plane for no-progress count (50-move rule)

Start with a reduced representation and then scale up.
"""

import numpy as np 
from typing import List, Optional
import chess

# Piece type to plane index mapping 
PIECE_TO_PLANE = {
    chess.PAWN :0,
    chess.KNIGHT: 1,
    chess.BISHOP: 2, 
    chess.ROOK: 3,
    chess.QUEEN: 4,
    chess.KING: 5,
}

class BoardEncoder:
    """Encodes chess positions into input tensors"""

    def __init__(self, history_length: int = 8) -> None:
        """
        Args:
            history_length: Number of past positions to include (default: 8)
        """