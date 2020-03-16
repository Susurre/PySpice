nonlinear tran simulation of two diodes
*from lecture8 page24
C1 2 0 1
Is 0 1 1 0 tran const (1)
D1 1 0 somemodel
D2 2 0 somemodel
R1 1 0 1000 
R2 1 2 1m
.TRAN 0.01 1 0
.END



