%---- Board class
% After adding board.m to your path you can:
%
%       To create a board:
%           b = board();
%
%       To play human vs computer:
%           b.playHumanVsComp(ply8) -- 1 if use ply8 NN, 0 for heuristic NN
%
%       To play ply8 NN vs heuristic NN:
%           b.playCompVsComp()
%
%       To play NN vs entirely random:
%           b.playCompVSRand(ply8) -- 1 if use ply8 NN, 0 for heuristic NN
%
%----- Other helpful methods:
%       b.print() to print the board
%       


classdef board<handle
    properties
        pieces;
    end
    properties(Constant = true)
        ME = 1;
        OPP = -1;
        BLANK = 0;
        ROWS = 6;
        COLS = 7;
    end
    
    methods
        function obj = board()
        % constructor
            obj.pieces = zeros(6,7);
        end
        
        % for testing/debugging
        function obj = setPieces(obj, val)
            obj.pieces = val;
        end
        
        function obj = clearBoard(obj)
            for r=1:obj.ROWS
                for c=1:obj.COLS
                    obj.pieces(r,c) = 0;
                end
            end
        end
        
        function added = add(obj, pieceType, c)
            a = obj.pieces;
            for r = 1:obj.ROWS
                if a(r,c) == 0
                    obj.pieces(r,c) = pieceType;
                    added = 1;
                    return
                end
            end
            added = 0;
            disp('Piece could not be added');
        end

        function print(obj)
            output = '1 2 3 4 5 6 7';
            disp(output);
            for r= obj.ROWS:-1:1
                row = '';
                for c = 1:obj.COLS
                    a = obj.pieces(r,c);
                    if a == obj.ME
                        row = strcat(row, 'X|');
                    elseif a == obj.OPP
                        row = strcat(row, 'O|');
                    else
                        row = strcat(row, '.|');
                    end
                end
                disp(row);
            end
        end
        
        % Outputs state of the game as a vector
        % starting from bottom of board upwards
        function value = vectorizeBoard(obj)
            value = [];
            a = obj.pieces * -1;
            for r = obj.ROWS:-1:1
                for c = 1:obj.COLS
                    value = [value a(r, c)];
                end
            end
        end
        
        %{
=================================================================
        Playing functions
        
        %}
        
        function playHumanVsComp(obj, ply8)
        % RANDOM is 1
        % Neural network is -1
        % ply8: bool, are we using ply 8 NN; else use heuristic NN
            obj.clearBoard();
            
            turn = 1;
            winner = 0;
            whogoesfirst = randi([0 1]);
            while (winner == 0 && turn < 43)
                disp(sprintf('=============turn %d', turn));
                if mod(turn,2) == whogoesfirst
                    obj.print();
                    % Get input from human player
                    result = input('P1: enter column: ');
                    added = obj.add(1, result);
                    while added == 0
                        result = input('P1 try again. enter column: ');
                        added = obj.add(1, result);
                    end
                else
                    % Get input from neural network
                    if ply8 == 1
                        result = getNextMove(obj.vectorizeBoard());
                    else
                        result = getGNetNextMove(obj.vectorizeBoard());
                    end
                    
                    disp(sprintf('ANN played %d', result));
                    added = obj.add(-1, result);
                    while added == 0
                        if ply8 == 1
                            result = getNextMove(obj.vectorizeBoard());
                        else
                            result = getGNetNextMove(obj.vectorizeBoard());
                        end
                        disp(sprintf('again: ANN played %d', result));
                        added = obj.add(-1, result);
                    end
                end
                
                turn = turn + 1;
                winner = obj.getWinner(turn);
            end
            
            if turn == 43
                disp('xxxxxx TIE xxxxxx');
            elseif winner == -1
                disp('****** And the winner is: COMPUTER');
            elseif winner == 1
                disp('****** And the winner is: HUMAN');
            end
        end
        
%---------------------------------------------------------------------
        function playCompVsComp(obj)
        % 8-ply is COMP8 is 1
        % heuristic is HEUR is -1
            obj.clearBoard();
            
            turn = 1;
            winner = 0;
            whogoesfirst = randi([0 1]);
            while (winner == 0 && turn < 43)
                disp(sprintf('=============turn %d', turn));
                if mod(turn,2) == whogoesfirst
                    % Get input from 8-ply neural network
                    result = getNextMove(obj.vectorizeBoard());
                    disp(sprintf('COMP8 played %d', result));
                    added = obj.add(1, result);
                    while added == 0
                        result = getNextMove(obj.vectorizeBoard());
                        disp(sprintf('again: COMP8 played %d', result));
                        added = obj.add(1, result);
                    end
                else
                    % Get input from heuristic neural network
                    result = getGNetNextMove(obj.vectorizeBoard());
                    disp(sprintf('HEUR played %d', result));
                    added = obj.add(-1, result);
                    while added == 0
                        result = getGNetNextMove(obj.vectorizeBoard());
                        disp(sprintf('again: HEUR played %d', result));
                        added = obj.add(-1, result);
                    end
                end
                
                turn = turn + 1;
                winner = obj.getWinner(turn);
            end
            
            if turn == 43
                disp('xxxxxx TIE xxxxxx');
            elseif winner == -1
                disp('****** And the winner is: HEUR');
            elseif winner == 1
                disp('****** And the winner is: COMP8');
            end
        end
%----------------------------------------------------------------------        
        function playCompVSRand(obj, ply8)
        % RANDOM is 1
        % Neural network is -1
        % ply8: bool, are we using ply 8 NN; else, use heuristic NN
            obj.clearBoard();
            
            turn = 1;
            winner = 0;
            whogoesfirst = randi([0 1]);
            while (winner == 0 && turn < 43)
                disp(sprintf('=============turn %d', turn));
                if mod(turn,2) == whogoesfirst
                    % Get RANDOM
                    result = randi([1,7]);
                    disp(sprintf('RAND played %d', result));
                    added = obj.add(1, result);
                    while added == 0
                        result = randi([1,7]);
                        disp(sprintf('again: RAND played %d', result));
                        added = obj.add(1, result);
                    end
                else
                    % Get input from neural network
                    if ply8 == 1
                            result = getNextMove(obj.vectorizeBoard());
                        else
                            result = getGNetNextMove(obj.vectorizeBoard());
                    end
                    disp(sprintf('ANN played %d', result));
                    added = obj.add(-1, result);
                    while added == 0
                        if ply8 == 1
                            result = getNextMove(obj.vectorizeBoard());
                        else
                            result = getGNetNextMove(obj.vectorizeBoard());
                        end
                        disp(sprintf('again: ANN played %d', result));
                        added = obj.add(-1, result);
                    end
                end
                
                turn = turn + 1;
                winner = obj.getWinner(turn);
            end
            
            if turn == 43
                disp('xxxxxx TIE xxxxxx');
            elseif winner == -1
                disp('****** And the winner is: COMPUTER');
            elseif winner == 1
                disp('****** And the winner is: HUMAN');
            end
        end
        

        
        %{
===================================================================
        Winner validation
        
        %}
        
        
        function winner = checkVert(obj)
            consec = [];
            a = obj.pieces;
            for c = 1:obj.COLS
                for r = 1:obj.ROWS
                    if isempty(consec) && a(r,c) ~= 0
                        consec = [a(r,c)];
                    elseif isempty(consec)
                        continue
                    elseif consec(1) == a(r, c)
                        consec = [consec a(r,c)];
                    else
                        consec = [];
                    end
                    
                    if length(consec) >= 4
                        winner = consec(1);
                        return
                    end
                end
                
                % clear vector at end of col
                consec = [];
            end
            
            winner = 0;
        end
        
        function winner = checkHoriz(obj)
            consec = [];
            a = obj.pieces;
            for r = 1:obj.ROWS
                for c = 1:obj.COLS
                    if isempty(consec) && a(r,c) ~= 0
                        consec = [a(r,c)];
                    elseif isempty(consec)
                        continue
                    elseif consec(1) == a(r, c)
                        consec = [consec a(r,c)];
                    else
                        consec = [];
                    end
                    
                    if length(consec) >= 4
                        winner = consec(1);
                        return
                    end
                end
                
                % clear vector at end of row
                consec = [];
            end
            
            winner = 0;
        end

        %{
        function winner = checkWinner(obj)
            for r = 1: obj.ROWS
                for c = 1:obj.COLS
                    % right to left diagonal
                    checkSequence(r, c, -1, 1);
                    % left to right diagonal
                    checkSequence(r, c, 1, 1);
                    % columns
                    checkSequence(r, c, 1, 0);
                    % horizontal 
                end
            end
        end
        
        function winner = checkDiagLeftToRight(obj)
            consec = [];
            a = obj.pieces;
            for ry = 1:3
                
                r = ry;
                c = 1;
                while r < obj.COLS
                    if isempty(consec) && a(r,c) ~= 0
                    consec = [a(r,c)];
                    elseif isempty(consec)
                        c = c + 1;
                        r = r + 1;
                        continue;
                    elseif consec(1) == a(r, c)
                        consec = [consec a(r,c)];
                    else
                        consec = [];
                    end

                    if length(consec) >= 4
                        winner = consec(1);
                        return
                    end
                    c = c + 1;
                    r = r + 1;
                end
                
            end
            winner = 0;
        end
        %}
        
        % To check: left to right: dx = 1, dy = 1
        % right to left: dx = 1, dy = -1
        function winner = checkDiag(obj, dx, dy)
            consec = [];
            a = obj.pieces();
            for x = 1:4
                for y = 1:obj.ROWS
                    r = y;
                    c = x;
                    while r <= obj.ROWS && c <= obj.COLS && r > 0 && c > 0
                        if isempty(consec) && a(r,c) ~= 0
                        consec = [a(r,c)];
                        elseif isempty(consec)
                            c = c + dx;
                            r = r + dy;
                            continue;
                        elseif consec(1) == a(r, c)
                            consec = [consec a(r,c)];
                        else
                            consec = [];
                        end

                        if length(consec) >= 4
                            winner = consec(1);
                            return
                        end
                        c = c + dx;
                        r = r + dy;
                    end
                end
            end
            winner = 0;
        end
        
        function winner = getWinner(obj, turns)
            if turns < 8
                winner = 0;
                return;
            end
            
            v = obj.checkVert();
            if v ~= 0
                winner = v;
                return;
            end
                
            h = obj.checkHoriz();
            if h ~= 0
                winner = h;
                return;
            end
                
            d1 = obj.checkDiag(1, 1);
            if d1 ~= 0
                winner = d1;
                return;
            end
                
            d2 = obj.checkDiag(1, -1);
            winner = d2;
        end
        
        
    end
end