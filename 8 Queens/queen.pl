:- use_module(library(clpfd)).

% Main predicate to find solutions for N-Queens problem
n_queens(N, Qs) :-
    length(Qs, N),          % Create a list of length N
    Qs ins 1..N,           % Each queen must be in one of the columns 1 to N
    safe_queens(Qs).       % Ensure no two queens threaten each other

% Base case: An empty list is trivially safe
safe_queens([]).

% Recursive case: Ensure the queen at the head is safe from all others in the tail
safe_queens([Q|Qs]) :-
    safe_queens(Qs, Q, 1),  % Check the current queen against all other queens
    safe_queens(Qs).        % Ensure all remaining queens are safe

% Base case for recursive checking
safe_queens([], _, _).

% Check that a queen at position Q0 is safe from another queen at position Q
safe_queens([Q|Qs], Q0, D0) :-
    Q0 #\= Q,                % Not in the same column
    abs(Q0 - Q) #\= D0,      % Not on the same diagonal
    D1 #= D0 + 1,           % Increment distance for the next check
    safe_queens(Qs, Q0, D1). % Recursively check the remaining queens

% Example query to solve the 8-Queens problem
