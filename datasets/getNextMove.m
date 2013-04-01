function col = getNextMove(input)

  board = vec2mat(input,6)';
  cl = @(x)(find(x==0,1,'first'));

load('net','net');

y = zeros(3,1);
score = ones(1,7) .* -1;

temp = board;
for row = 1:7
    c = cl(board(:,row));
    if (size(c,1) ~= 0)
        temp(c(1),row) = 1;
        y = sim(net, temp(:)');
        score(row) = y(1,row) - y(2,row);
        temp = board;
    end
end

[C, I] = max(score);
col = I;



