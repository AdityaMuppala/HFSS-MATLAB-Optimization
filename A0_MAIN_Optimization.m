%% *MAKE SURE TO INCLUDE IRONPYTHON TO SYSTEM PATH*

% Make sure there is only 1 HFSS running and it has the design open.
% If more than 1 HFSS applications are open, matlab may try to open the 
% design in the wrong HFSS application.

clc
clear

%% Set up Nelder-Mead Optimizer
%All units are in mm
param_X = [2.5,3.5,1.2,1,10,6.75,-0.75]; % Initial values
LB_X = [1.5,2.0,0.5,0.5,8.00,5.0,-3]; % Lower bounds
UB_X = [4.1,4.1,3.0,2,15.0,9.0,3.0]; % Upper bounds

%% Seed simulation for reference
runPyCmd = ['ipy64 HFSS_Main.py ',num2str(param_X)];
[~,msg] = system(runPyCmd);

SData_original = readtable('S11.csv');

figure(1)
plot(SData_original{:,1},SData_original{:,2},'r--');
xlabel('Freq (GHz)'); ylabel('S11 (dB)'); grid on; hold on;

%% Run optimization routine

tic
options = optimset('PlotFcns',@optimplotfval);options.MaxFunctionEvaluations = 500;
optim_X = fminsearchbnd(@(param_X)func_Optimize(param_X),param_X,LB_X,UB_X,options);
time = toc;

%% Optimized results

runPyCmd = ['ipy64 HFSS_Main.py ',num2str(optim_X)];
[~,msg] = system(runPyCmd);

SData_final = readtable('S11.csv');

figure(1)
plot(SData_final{:,1},SData_final{:,2},'k');
xlabel('Freq (GHz)'); ylabel('S11 (dB)'); grid on; hold on;

legend('Original', 'Optimized')
title(['Simulation time: ',num2str(time/60),' minutes'])
