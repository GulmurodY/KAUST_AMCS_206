"""
From the lecture notes we conclude that the number of flops requried for the Least Squares Algorithm 
is approximately m*n^2 + 1/3 * n^3. Here m is the number of data points while n is the number of the 
parameters of the model.

Lets consider how many flops does the computer do for the first case presented in the problem.
For 20 parameters and 10^6 data points we have 10^6 * 400 + 8000/3 which is approximately 4*10^8 flops.
This means that the computer makes around 4*10^8 flops per second. Now let us find out how the result changes
when the data input changes.

1) We have 20 parameters and 10^7 data points thus we will make approximately 10^7 * 400 + 8000/3 which is
approximately 4 * 10^9 flops i.e. we require around 10 times more time than the initial case.

2) We have 200 parameters and 10^6 data points therefore we will make approximately 
10^6 * 40000 + 8000000/3 flops which is approximately 4 * 10^10 flops i.e.
we will spend around 100x time than the initla case. But if we were to increase the number of parameters
a bit more then the second term would start to dominate the sum and therefore we would have to include it in the
approximation of the time as well. But we are safe for now since it is much smaller than the first term.

Note: This solution assumes that the computation scales linearly which is not always the case in reality. 
"""