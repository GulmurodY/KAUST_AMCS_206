m = 100;   % number of points 

% generate random m data points 
t = -1 + 2*rand(m, 1);
y = t.^3 - t + 0.4 ./ (1 + 25*t.^2) + 0.10*randn(m,1);

plot(t, y, 'o');  % plot the points as circles

