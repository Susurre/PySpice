R+NMOS inverter-- transient sim
Vin 1 0 1 0 tran pulse (0,1.8,0,0.1,0.1,0.5,1)
Vdd 3 0 1.8 0 tran const (1.8)
M1 2 1 0 0 NMOS l=2u
R1 2 3 5000
.tran 0.01 2 0
.end

