set terminal png size 400,300; set output 'fit1.png'
a= 120
b = 0.2
c = 150
d = 100
e = 10
f(x) = a +b*x + c*exp(-(x-d)**2/e**2)
fit f(x)"fitdata.dat" using 1:2:3 via a,b,c,d,e
set label 1 sprintf('a = %3.4f',a) at 80,40 font "arialbd,18"
plot f(x), "fitdata.dat" using  1:2:3 with yerrorbars
