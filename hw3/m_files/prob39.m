% generate random data
a = [0.8; 1.2];
b =  0.5;

N = 100;
x = 2*rand(N, 2)-1;                  % x is Nx2
z = x * a + b + 0.15*randn([N, 1]);  % add gaussian noise

plot3(x(:,1), x(:,2), z, 'o')
grid on

% your code goes here
