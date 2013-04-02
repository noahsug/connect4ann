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
            a = obj.pieces;
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
        
        function playHumanVsComp(obj, ply8, heuristic)
            obj.clearBoard();
            
            turn = 1;
            winner = 0;
            while (winner == 0 && turn < 43)
                disp(sprintf('=============turn %d', turn));
                if mod(turn,2) == 1
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
                    result = 2;
                    disp(sprintf('ANN played %d', result));
                    added = obj.add(-1, result);
                    while added == 0
                        result = 3;
                        disp(sprintf('again: RAND played %d', result));
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
                disp('****** And the winner is: RANDOM');
            end
        end
        
        function playCompVsComp(obj)
        % 8-ply is COMP1 is 1
        % heuristic is COMP2 is -1
            obj.clearBoard();
            
            turn = 1;
            winner = 0;
            while (winner == 0 && turn < 43)
                disp(sprintf('=============turn %d', turn));
                if mod(turn,2) == 1
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
                    result = 2;
                    disp(sprintf('ANN played %d', result));
                    added = obj.add(-1, result);
                    while added == 0
                        result = 3;
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
        
        function playCompVSRand(obj)
        % RANDOM is 1
        % Neural network is -1
            obj.clearBoard();
            
            turn = 1;
            winner = 0;
            while (winner == 0 && turn < 43)
                disp(sprintf('=============turn %d', turn));
                if mod(turn,2) == 1
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
                    result = 2;
                    disp(sprintf('ANN played %d', result));
                    added = obj.add(-1, result);
                    while added == 0
                        result = 3;
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