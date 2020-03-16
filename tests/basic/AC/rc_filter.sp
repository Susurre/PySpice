simple one order rc-circuit for ac simulation
* Qixu Xie 2020-3-9

vdc 1 0 1 1
r1 1 2 1k
c1 2 0 100u
.AC 1 0 100
.plot ac vm(2)
.end

