% generate random data
N = 100;
x = -2 + 4*rand(N, 1);
y = 1 + 2*(x-1) - 3*max(x+1, 0) + 4*max(x-1, 0) + 0.2*randn(N, 1);
plot(x, y, 'o')

% your code goes here
