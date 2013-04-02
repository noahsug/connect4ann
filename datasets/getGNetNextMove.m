function col = getGNetNextMove(input)

  board = vec2mat(input,6)';
  cl = @(x)(find(x==0,1,'first'));

load('netR','netR');

score = ones(1,7) .* -1;

temp = board;
for row = 1:7
    c = cl(board(:,row));
    if (size(c,1) ~= 0)
        temp(c(1),row) = 1;
        score(row) = sim(netR, temp(:));
        temp = board;
    end
end

[C, I] = max(score);
score
col = I;



