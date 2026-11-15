% Self-study diagnostic replacing the zero-feasible constraints in the helper.
% The original Exercises/Exercise_5_3.m is unchanged.
% Requires YALMIP and a configured SDP solver. Not executed in course creation.
assert(exist('sdpvar','file') ~= 0, 'YALMIP is not on the MATLAB path.');
P = sdpvar(2,2,'symmetric');
vertices = {[0 1;-1 -0.5], [0 1;-1 0],...
            [0 1;-2 -0.5], [0 1;-2 0]};
margin = 1e-6;
constraints = [P >= eye(2)];
for i = 1:numel(vertices)
    A = vertices{i};
    constraints = [constraints, A'*P+P*A <= -margin*eye(2)];
end
diagnostics = optimize(constraints,[],sdpsettings('verbose',1));
disp(diagnostics.info);
if diagnostics.problem == 0
    Pnumeric = value(P);
    fprintf('min eig(P): %.8g\n', min(eig((Pnumeric+Pnumeric')/2)));
    for i = 1:numel(vertices)
        A = vertices{i};
        L = A'*Pnumeric+Pnumeric*A;
        fprintf('vertex %d max Lyapunov eigenvalue: %.8g\n',i,max(eig((L+L')/2)));
    end
    disp('A numerical success is suspicious here: inspect tolerances and residuals.');
    disp('The undamped vertices preclude a strict asymptotic-stability certificate.');
elseif diagnostics.problem == 1
    disp('Infeasibility is consistent with the undamped vertices in the original set.');
else
    error('Solver/configuration issue is not a stability conclusion: %s',diagnostics.info);
end
