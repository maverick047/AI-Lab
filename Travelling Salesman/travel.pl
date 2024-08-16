% Define the roads between towns
road("tampa", "houston", 200).
road("gordon", "tampa", 300).
road("houston", "gordon", 100).
road("houston", "kansas_city", 120).
road("gordon", "kansas_city", 130).

% Base case for direct route
route(Town1, Town2, Distance) :-
    road(Town1, Town2, Distance).

% Recursive case for indirect route
route(Town1, Town2, Distance) :-
    road(Town1, X, Dist1),
    route(X, Town2, Dist2),
    Distance is Dist1 + Dist2, !.

% Example Queries
% To find the distance between Tampa and Kansas City:
% ?- route("tampa", "kansas_city", Distance).

% To find the distance between Houston and Kansas City:
% ?- route("houston", "kansas_city", Distance).
