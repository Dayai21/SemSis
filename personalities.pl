% Preguntas con sus ejes y opciones
question(1, "Prefieres trabajar solo o en equipo?", 'EI', 1, -1).
question(2, "Tomas decisiones basadas en lógica o emociones?", 'TF', 1, -1).
question(3, "Te enfocas en los detalles o en el panorama general?", 'SN', 1, -1).
question(4, "Prefieres planificar todo o ser espontáneo?", 'JP', 1, -1).

% Determinar personalidad basado en puntajes
determine_mbti(EI_Score, SN_Score, TF_Score, JP_Score, Personality) :-
    (EI_Score > 0 -> E = 'E'; E = 'I'),
    (SN_Score > 0 -> S = 'S'; S = 'N'),
    (TF_Score > 0 -> T = 'T'; T = 'F'),
    (JP_Score > 0 -> J = 'J'; J = 'P'),
    atom_concat(E, S, ES),
    atom_concat(ES, T, EST),
    atom_concat(EST, J, Personality).

% Afinidades y conflictos
high_affinity('ENFP', ['INFJ', 'INTJ']).
low_affinity('ENFP', ['ISTJ', 'ESTJ']).

high_affinity('INTP', ['ENTP', 'ENTJ']).
low_affinity('INTP', ['ESFP', 'ESTJ']).

% Consultar personalidades compatibles
compatible(Personality, CompatibleList) :- high_affinity(Personality, CompatibleList).

% Consultar personalidades incompatibles
incompatible(Personality, IncompatibleList) :- low_affinity(Personality, IncompatibleList).
