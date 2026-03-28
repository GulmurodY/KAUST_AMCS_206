% generate synthetic data for testing the fit
a = [0.5 1.2];
b = [0.3 0.8];

x = [0:.01:1]';
N = length(x); 
w = 2*pi;
f = a(1) * cos(w .* x) + b(1) * sin(w .* x) + ...
    a(2) * cos(2*w .* x) + b(2) * sin(2*w .* x);
y = f + 0.15 * randn([N 1]);   % add gaussian noise
plot(x, y, '.')


% your code goes here

