% Read-only environment diagnostic. No toolbox is installed by this script.
disp(version);
ver;
names = {'ss','lqr','lqi','hinfsyn','h2syn','robstab','robgain',...
         'sdpvar','optimize','ode45'};
for i = 1:numel(names)
    fprintf('%s: %s\n', names{i}, which(names{i}));
end
% "which" confirms a visible function, not an available license or solver.
% If using YALMIP, independently verify one small known-feasible SDP.
