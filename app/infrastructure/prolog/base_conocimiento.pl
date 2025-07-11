%diagnosticos
%gripe-1
%cefalea-2
%intoxicacion-3
%covid-4
%migraña-5
%gastritis-6
%alergia-7
%infeccion_urinaria-8
%resfriado_comun-9
%bronquitis-10
%asma-11
%sinusitis-12
%otitis-13
%faringitis-14
%neumonia-15
%dengue-16
%anemia-17
%hipertension-18
%diabetes-19
%varicela-20
%sarampion-21
%hepatitis_a-22
%hepatitis_b-23
%apendicitis-24
%colitis-25
%ulceras_gastricas-26
%infeccion_piel-27
%artritis-28
%depresion-29
%ansiedad-30
%sintomas
%fiebre-1
%tos-2
%dolor_cabeza-3
%nauseas-4
%perdida_olfato-5
%vomitos-6
%dolor_estomago-7
%dolor_ojos-8
%estornudos-9
%picazon_piel-10
%ardor_orina-11
%orinar_frecuente-12
%congestion_nasal-13
%dificultad_respirar-14
%dolor_pecho-15
%cansancio-16
%sudoracion_nocturna-17
%escalofrios-18
%zumbido_oidos-19
%dolor_garganta-20
%manchas_piel-21
%piel_amarilla-22
%vision_borrosa-23
%perdida_apetito-24
%diarrea-25
%dolor_abdomen-26
%sangrado_encias-27
%inflamacion_articulaciones-28
%rigidez-29
%tristeza-30
%insomnio-31
%palpitaciones-32
%ansiedad-33
%mareos-34
%dolor_espalda-35
%sensibilidad_luz-36
%secrecion_oido-37
%dolor_oido-38
%dificultad_tragar-39
%ronquera-40
%dolor_muscular-41
%inflamacion_garganta-42
%urticaria-43
%perdida_peso-44
%infeccion_herida-45
%baja_presion-46
%alta_presion-47
%sudoracion_excesiva-48
%piel_seca-49
%vision_doble-50
:- dynamic sintoma/1.
:- dynamic diagnostico/1.

sintomas_diagnostico(1, [1,2]).
sintomas_diagnostico(2, [3]).
sintomas_diagnostico(3, [4,3]).
sintomas_diagnostico(4, [1,2,5]).
sintomas_diagnostico(5, [3,8,36]).
sintomas_diagnostico(6, [4,6,7]).
sintomas_diagnostico(7, [9,10,43]).
sintomas_diagnostico(8, [11,12]).
sintomas_diagnostico(9, [13,2,1]).
sintomas_diagnostico(10, [2,14,15]).
sintomas_diagnostico(11, [14,2,32]).
sintomas_diagnostico(12, [3,13,8]).
sintomas_diagnostico(13, [38,37,19]).
sintomas_diagnostico(14, [20,39,42]).
sintomas_diagnostico(15, [1,14,17]).
sintomas_diagnostico(16, [1,41,21]).
sintomas_diagnostico(17, [16,34,27]).
sintomas_diagnostico(18, [15,47,16]).
sintomas_diagnostico(19, [24,44,23]).
sintomas_diagnostico(20, [1,21,41]).
sintomas_diagnostico(21, [1,21,20]).
sintomas_diagnostico(22, [22,24,25]).
sintomas_diagnostico(23, [22,23,1]).
sintomas_diagnostico(24, [26,6,1]).
sintomas_diagnostico(25, [25,26,7]).
sintomas_diagnostico(26, [7,6,1]).
sintomas_diagnostico(27, [45,10,49]).
sintomas_diagnostico(28, [28,29,35]).
sintomas_diagnostico(29, [30,31,50]).
sintomas_diagnostico(30, [33,32,31]).

% Cuenta cuántos síntomas coinciden con los ingresados
contar_coincidencias([], 0).
contar_coincidencias([S|R], N) :-
    sintoma(S),
    contar_coincidencias(R, N1),
    N is N1 + 1.
contar_coincidencias([S|R], N) :-
    \+ sintoma(S),
    contar_coincidencias(R, N).

% Calcular porcentaje por diagnóstico
porcentaje_diagnostico(DiagnosticoID, Porcentaje) :-
    sintomas_diagnostico(DiagnosticoID, Sintomas),
    contar_coincidencias(Sintomas, Coinciden),
    length(Sintomas, Total),
    Total > 0,
    Porcentaje is (Coinciden * 100) // Total.

% Obtener diagnóstico más probable
diagnostico_mas_probable(ID) :-
    findall((P, D), (sintomas_diagnostico(D, _), porcentaje_diagnostico(D, P), P > 0), Resultados),
    sort(0, @>=, Resultados, [(MejorP, ID)|_]),
    MejorP > 0.
