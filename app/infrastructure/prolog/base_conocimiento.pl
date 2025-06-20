%Hechos
sintoma(fiebre).
sintoma(tos).
sintoma(dolor_cabeza).
sintoma(nauseas).


%Reglas
diagnostico(gripe) :- sintoma(fiebre), sintoma(tos).
diagnostico(cefalea) :- sintoma(dolor_cabeza).
diagnostico(intoxicacion) :- sintoma(nauseas), sintoma(dolor_cabeza).