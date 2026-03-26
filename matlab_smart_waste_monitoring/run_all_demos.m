%% ========================================================================
% IoT Smart Waste Monitoring System - Master Demo Script
% ========================================================================
% This script runs all demonstration modules sequentially
% Run this file to see the complete system demonstration
% ========================================================================

%% Initialization
clear all;
close all;
clc;

fprintf('\n========================================================================\n');
fprintf('       IoT SMART WASTE MONITORING SYSTEM - COMPLETE DEMO\n');
fprintf('========================================================================\n\n');

%% Module 1: Bin Fill Level Simulation
fprintf('\n========================================================================\n');
fprintf('                    MODULE 1: BIN FILL SIMULATION\n');
fprintf('========================================================================\n');
fprintf('Simulating 20 smart waste bins over 24 hours...\n\n');
pause(1);

run('1_bin_simulation.m');

fprintf('\n[Module 1 Complete] - Press any key to continue to Module 2...\n');
pause;

%% Module 2: Sensor Model Simulation
fprintf('\n========================================================================\n');
fprintf('                   MODULE 2: SENSOR MODEL SIMULATION\n');
fprintf('========================================================================\n');
fprintf('Simulating Time-of-Flight distance sensors with noise...\n\n');
pause(1);

run('2_sensor_model.m');

fprintf('\n[Module 2 Complete] - Press any key to continue to Module 3...\n');
pause;

%% Module 3: MQTT Communication Demo
fprintf('\n========================================================================\n');
fprintf('                  MODULE 3: MQTT COMMUNICATION DEMO\n');
fprintf('========================================================================\n');
fprintf('Demonstrating IoT message payload generation and MQTT publishing...\n\n');
pause(1);

run('3_mqtt_demo.m');

fprintf('\n[Module 3 Complete] - Press any key to continue to Module 4...\n');
pause;

%% Module 4: Route Optimization
fprintf('\n========================================================================\n');
fprintf('                    MODULE 4: ROUTE OPTIMIZATION\n');
fprintf('========================================================================\n');
fprintf('Computing optimal collection route for full bins...\n\n');
pause(1);

run('4_route_optimization.m');

fprintf('\n[Module 4 Complete]\n');

%% Final Summary
fprintf('\n========================================================================\n');
fprintf('                   ALL MODULES COMPLETED SUCCESSFULLY\n');
fprintf('========================================================================\n');
fprintf('Summary:\n');
fprintf('  ✓ Module 1: Bin fill level simulation (20 bins, 24 hours)\n');
fprintf('  ✓ Module 2: ToF sensor accuracy analysis (10 bins)\n');
fprintf('  ✓ Module 3: IoT message payload and MQTT demo\n');
fprintf('  ✓ Module 4: Collection route optimization (15 bins)\n');
fprintf('\nDemo presentation ready!\n');
fprintf('========================================================================\n\n');
