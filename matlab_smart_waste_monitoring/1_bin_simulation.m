%% ========================================================================
% Module 1: Smart Waste Bin Fill Level Simulation
% ========================================================================
% Simulates 20 smart waste bins over a 24-hour period
% Models fill level growth with different rates for each bin
% Classifies bins by fill status and generates visualizations
% ========================================================================

%% Parameters
num_bins = 20;              % Number of waste bins to simulate
num_hours = 24;             % Simulation duration (hours)
bin_height_cm = 100;        % Standard bin height in cm

% Status classification thresholds
threshold_normal = 50;      % Below 50%: NORMAL
threshold_medium = 80;      % 50-80%: MEDIUM
threshold_alert = 95;       % 80-95%: ALERT
                           % 95%+: CRITICAL

%% Initialize Simulation
fprintf('Initializing simulation for %d bins over %d hours...\n', num_bins, num_hours);

% Generate random initial conditions for each bin
rng(42);  % Set seed for reproducibility
initial_fill = rand(num_bins, 1) * 30;  % Initial fill: 0-30%
growth_rate = 1 + rand(num_bins, 1) * 4; % Growth rate: 1-5% per hour

% Time vector
time_hours = 0:num_hours;

% Preallocate fill level matrix
fill_levels = zeros(num_bins, length(time_hours));

%% Simulate Fill Level Growth
fprintf('Simulating fill level growth...\n');

for bin = 1:num_bins
    for t = 1:length(time_hours)
        if t == 1
            fill_levels(bin, t) = initial_fill(bin);
        else
            % Linear growth with small random variation
            fill_levels(bin, t) = fill_levels(bin, t-1) + ...
                                  growth_rate(bin) * (0.9 + 0.2*rand());
            % Cap at 100%
            fill_levels(bin, t) = min(fill_levels(bin, t), 100);
        end
    end
end

%% Calculate Final Status
final_fill = fill_levels(:, end);
status = cell(num_bins, 1);

for bin = 1:num_bins
    if final_fill(bin) >= threshold_alert
        status{bin} = 'CRITICAL';
    elseif final_fill(bin) >= threshold_medium
        status{bin} = 'ALERT';
    elseif final_fill(bin) >= threshold_normal
        status{bin} = 'MEDIUM';
    else
        status{bin} = 'NORMAL';
    end
end

%% Display Results Table
fprintf('\n--- Bin Status Summary ---\n\n');

% Create results table
bin_id = (1:num_bins)';
results_table = table(bin_id, initial_fill, growth_rate, final_fill, status, ...
    'VariableNames', {'BinID', 'InitialFillPercent', 'GrowthRatePerHour', ...
                      'FinalFillPercent', 'Status'});

disp(results_table);

% Count status categories
num_normal = sum(strcmp(status, 'NORMAL'));
num_medium = sum(strcmp(status, 'MEDIUM'));
num_alert = sum(strcmp(status, 'ALERT'));
num_critical = sum(strcmp(status, 'CRITICAL'));

fprintf('\nStatus Distribution:\n');
fprintf('  NORMAL:   %2d bins (%.1f%%)\n', num_normal, num_normal/num_bins*100);
fprintf('  MEDIUM:   %2d bins (%.1f%%)\n', num_medium, num_medium/num_bins*100);
fprintf('  ALERT:    %2d bins (%.1f%%)\n', num_alert, num_alert/num_bins*100);
fprintf('  CRITICAL: %2d bins (%.1f%%)\n', num_critical, num_critical/num_bins*100);

%% Visualization 1: Fill Levels Over Time
figure('Position', [100, 100, 1000, 500], 'Name', 'Bin Fill Simulation');

subplot(1, 2, 1);
hold on;

% Plot all bin trajectories
for bin = 1:num_bins
    plot(time_hours, fill_levels(bin, :), 'LineWidth', 1.5);
end

% Add threshold lines
plot([0, num_hours], [threshold_medium, threshold_medium], 'r--', ...
     'LineWidth', 2, 'DisplayName', 'Alert Threshold (80%)');
plot([0, num_hours], [threshold_alert, threshold_alert], 'k--', ...
     'LineWidth', 2, 'DisplayName', 'Critical Threshold (95%)');

xlabel('Time (hours)', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('Fill Level (%)', 'FontSize', 12, 'FontWeight', 'bold');
title('Bin Fill Levels Over 24 Hours', 'FontSize', 14, 'FontWeight', 'bold');
grid on;
legend('Location', 'northwest');
ylim([0, 105]);
xlim([0, num_hours]);
hold off;

%% Visualization 2: Final Fill Levels Bar Chart
subplot(1, 2, 2);
hold on;

% Color code bars by status
bar_colors = zeros(num_bins, 3);
for bin = 1:num_bins
    switch status{bin}
        case 'NORMAL'
            bar_colors(bin, :) = [0.2, 0.8, 0.2];  % Green
        case 'MEDIUM'
            bar_colors(bin, :) = [1.0, 0.8, 0.0];  % Yellow
        case 'ALERT'
            bar_colors(bin, :) = [1.0, 0.5, 0.0];  % Orange
        case 'CRITICAL'
            bar_colors(bin, :) = [0.9, 0.1, 0.1];  % Red
    end
end

% Create bar chart
b = bar(bin_id, final_fill);
b.FaceColor = 'flat';
b.CData = bar_colors;

% Add threshold lines
plot([0, num_bins+1], [threshold_medium, threshold_medium], 'r--', ...
     'LineWidth', 2, 'DisplayName', 'Alert (80%)');
plot([0, num_bins+1], [threshold_alert, threshold_alert], 'k--', ...
     'LineWidth', 2, 'DisplayName', 'Critical (95%)');

xlabel('Bin ID', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('Final Fill Level (%)', 'FontSize', 12, 'FontWeight', 'bold');
title('Final Status by Bin', 'FontSize', 14, 'FontWeight', 'bold');
grid on;
legend('Location', 'northwest');
ylim([0, 105]);
xlim([0, num_bins+1]);
hold off;

fprintf('\n✓ Visualization generated successfully!\n');
