classdef board
    properties
        pieces;
    end
    properties(Constant = true)
        ME = 1;
        OPP = -1;
        BLANK = 0;
    end
    
    methods
        function obj = board()
        % constructor
            obj.pieces = zeros(6,7);
        end
        
        function obj = addPiece(obj, pieceType, r, c)
            obj.pieces(r, c) = pieceType;
        end
        
        function obj = printBoard(obj)
            display(obj.pieces);
        end
    end
end