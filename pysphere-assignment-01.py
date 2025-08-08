print("*** Velocity Calculator ***")
I=input("Enter Current 'I' in amperes : ")
I_int=int(I)
R=input("Enter Resistance in ohms 'R': ")
R_int=int(R)
V=I_int*R_int
print("Velocity of I of "+ I + " resistance of " +R + " is: "+str(V))