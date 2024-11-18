feature(introvertido).
feature(extrovertido).
feature(sensacion).
feature(intuicion).
feature(pensamiento).
feature(sentimiento).
feature(juicio).
feature(percepcion).


% Aqui ponen todas las personalidades con sus rasgos
personality('ISTJ', introvertido, sensacion, pensamiento, juicio).
personality('ENFP', extrovertido, intuicion, sentimiento, percepcion).

% la compatibilidad entre los rasgos
compatible('ISTJ', 'ENFP').

score('deacuerdo', 2).
score('un poco de acuerdo', 2).
score('ni en acuerdo ni desacuerdo', 2).
score('un poco en desacuerdo', 2).
score('desacuerdo', 2).

update_feature(Answer, Feature, CurrentScore)