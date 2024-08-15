% solve(Node, Solution): 
%    Solution is an acyclic path (in reverse order) between Node and a goal 
solve(Node, Solution) :- 
    depthfirst([], Node, Solution).

% depthfirst(Path, Node, Solution): 
%   Extending the path [Node | Path] to a goal gives Solution 
depthfirst(Path, Node, [Node | Path]) :- 
    goal(Node).

depthfirst(Path, Node, Solution) :- 
    s(Node, Node1), 
    \+ member(Node1, Path),   % Prevent a cycle
    depthfirst([Node | Path], Node1, Solution).

% depthfirst2(Node, Solution, Maxdepth): 
%   Depth-limited search from Node to a goal with a maximum depth of Maxdepth
depthfirst2(Node, [Node], _) :- 
    goal(Node).

depthfirst2(Node, [Node | Solution], Maxdepth) :- 
    Maxdepth > 0, 
    s(Node, Node1), 
    Max1 is Maxdepth - 1, 
    depthfirst2(Node1, Solution, Max1).

% Define goal nodes
goal(f).
goal(j).

% Define edges
s(a, b).
s(a, c).
s(b, d).
s(b, e).
s(c, f).
s(c, g).
s(d, h).
s(e, i).
s(e, j).
