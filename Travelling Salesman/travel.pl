% Production Rules
route(Town1, Town2, Distance) :-
    road(Town1, Town2, Distance).

route(Town1, Town2, Distance) :-
    road(Town1, X, Dist1),
    route(X, Town2, Dist2),
    Distance is Dist1 + Dist2,
    !.

% Domains
% town = symbol
% distance = integer

% Predicates
% nondeterm road(town, town, distance)
% nondeterm route(town, town, distance)

% Clauses
road("tampa", "houston", 200).
road("gordon", "tampa", 300).
road("houston", "gordon", 100).
road("houston", "kansas_city", 120).
road("gordon", "kansas_city", 130).

% Initialization Directive
:- initialization(main).

% Main Predicate for Testing
main :-
    % Example query
    route("tampa", "kansas_city", Distance),
    format('Distance from tampa to kansas_city is ~w~n', [Distance]),
    
    % You can add more test queries here
    fail. % To ensure it doesn’t stop at the first result, you can use fail or remove it if you only want the first result
