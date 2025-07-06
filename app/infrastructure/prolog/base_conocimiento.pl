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

diagnostico(1) :- sintoma(1), sintoma(2).
diagnostico(2) :- sintoma(3).
diagnostico(3) :- sintoma(4), sintoma(3).
diagnostico(4) :- sintoma(1), sintoma(2), sintoma(5).
diagnostico(5) :- sintoma(3), sintoma(8), sintoma(36).
diagnostico(6) :- sintoma(4), sintoma(6), sintoma(7).
diagnostico(7) :- sintoma(9), sintoma(10), sintoma(43).
diagnostico(8) :- sintoma(11), sintoma(12).
diagnostico(9) :- sintoma(13), sintoma(2), sintoma(1).
diagnostico(10) :- sintoma(2), sintoma(14), sintoma(15).
diagnostico(11) :- sintoma(14), sintoma(2), sintoma(32).
diagnostico(12) :- sintoma(3), sintoma(13), sintoma(8).
diagnostico(13) :- sintoma(38), sintoma(37), sintoma(19).
diagnostico(14) :- sintoma(20), sintoma(39), sintoma(42).
diagnostico(15) :- sintoma(1), sintoma(14), sintoma(17).
diagnostico(16) :- sintoma(1), sintoma(41), sintoma(21).
diagnostico(17) :- sintoma(16), sintoma(34), sintoma(27).
diagnostico(18) :- sintoma(15), sintoma(47), sintoma(16).
diagnostico(19) :- sintoma(24), sintoma(44), sintoma(23).
diagnostico(20) :- sintoma(1), sintoma(21), sintoma(41).
diagnostico(21) :- sintoma(1), sintoma(21), sintoma(20).
diagnostico(22) :- sintoma(22), sintoma(24), sintoma(25).
diagnostico(23) :- sintoma(22), sintoma(23), sintoma(1).
diagnostico(24) :- sintoma(26), sintoma(6), sintoma(1).
diagnostico(25) :- sintoma(25), sintoma(26), sintoma(7).
diagnostico(26) :- sintoma(7), sintoma(6), sintoma(1).
diagnostico(27) :- sintoma(45), sintoma(10), sintoma(49).
diagnostico(28) :- sintoma(28), sintoma(29), sintoma(35).
diagnostico(29) :- sintoma(30), sintoma(31), sintoma(50).
diagnostico(30) :- sintoma(33), sintoma(32), sintoma(31).