function col = getNextMove(input)
format long
  board = vec2mat(input,6)';
  cl = @(x)(find(x==0,1,'first'));

load('net','net');

y = zeros(3,7);
score = ones(1,7) .* -1;

temp = board;
for row = 1:7
    c = cl(board(:,row));
    if (size(c,1) ~= 0)
        temp(c(1),row) = 1;
        y(:,row) = sim(net, temp(:));
        score(row) = y(1,row) - y(3,row);
        temp = board;
    end
end

[C, I] = max(y(1,:));
if sum(y(1,:) >= C) > 1
  y = repmat(y(1,:) == C, size(y,1),1) .* y;
  y(:,find(sum(abs(A)) == 0)) = [];
  y
  [C, I] = min(y(3,:));
  if sum(y(3,:) <= C) > 1
    y = repmat(y(3,:) == C, size(y,1),1) .* y;
    y(:,find(sum(abs(A)) == 0)) = [];
    y
    [C, I] = min(y(2,:));
  end
end
%[c,i] = max(score);
col = I;



