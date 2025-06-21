:- dynamic sintoma/1.
:- dynamic diagnostico/1.

diagnostico(gripe) :- sintoma(fiebre), sintoma(tos).
diagnostico(cefalea) :- sintoma(dolor_cabeza).
diagnostico(intoxicacion) :- sintoma(nauseas), sintoma(dolor_cabeza).