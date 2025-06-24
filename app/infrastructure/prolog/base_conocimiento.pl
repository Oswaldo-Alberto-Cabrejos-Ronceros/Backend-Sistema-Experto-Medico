%diagnosticos
%gripe-1
%cefalea-2
%intoxicacion-3
%sintomas
%fiebre-1
%tos-2
%dolor_cabeza-3
%nauseas-4
:- dynamic sintoma/1.
:- dynamic diagnostico/1.

diagnostico(1) :- sintoma(1), sintoma(2).
diagnostico(2) :- sintoma(3).
diagnostico(3) :- sintoma(4), sintoma(3).