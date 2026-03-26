%% ========================================================================
% Module 2: Time-of-Flight Sensor Model Simulation
% ========================================================================
% Simulates ToF distance sensors mounted on top of waste bins
% Models sensor noise and measurement error
% Compares true fill levels with measured values
% ========================================================================

%% Parameters
num_bins = 10;              % Number of bins to simulate
bin_height_cm = 100;        % Standard bin height in cm
sensor_noise_std = 2.0;     % Sensor noise standard deviation (cm)

fprintf('Simulating ToF sensors for %d bins...\n', num_bins);

%% Generate True Fill Levels
rng(123);  % Set seed for reproducibility

% Generate random true fill percentages (0-100%)
true_fill_percent = 10 + rand(num_bins, 1) * 85;  % 10% to 95%

% Convert fill percentage to waste height (cm)
waste_height_cm = (true_fill_percent / 100) * bin_height_cm;

% Calculate true sensor distance (from sensor to waste surface)
% Sensor is at the top, so distance = bin_height - waste_height
true_distance_cm = bin_height_cm - waste_height_cm;

%% Add Sensor Noise
fprintf('Adding Gaussian noise to sensor readings...\n');

% Generate noisy sensor measurements
% Gaussian noise simulates real-world sensor imperfections
noise = sensor_noise_std * randn(num_bins, 1);
measured_distance_cm = true_distance_cm + noise;

% Ensure measured distance is within physical limits [0, bin_height]
measured_distance_cm = max(0, min(bin_height_cm, measured_distance_cm));

%% Convert Measured Distance to Fill Percentage
% Reverse calculation: fill_height = bin_height - measured_distance
measured_waste_height = bin_height_cm - measured_distance_cm;
measured_fill_percent = (measured_waste_height / bin_height_cm) * 100;

% Calculate measurement error
error_percent = measured_fill_percent - true_fill_percent;
absolute_error = abs(error_percent);

%% Display Results Table
fprintf('\n--- Sensor Measurement Results ---\n\n');

% Create results table
bin_id = (1:num_bins)';
sensor_table = table(bin_id, true_fill_percent, true_distance_cm, ...
                     measured_distance_cm, measured_fill_percent, error_percent, ...
    'VariableNames', {'BinID', 'TrueFillPercent', 'TrueDistanceCm', ...
                      'MeasuredDistanceCm', 'MeasuredFillPercent', 'ErrorPercent'});

disp(sensor_table);

% Statistics
fprintf('\nSensor Performance Statistics:\n');
fprintf('  Mean Absolute Error:  %.2f%%\n', mean(absolute_error));
fprintf('  Max Absolute Error:   %.2f%%\n', max(absolute_error));
fprintf('  RMS Error:            %.2f%%\n', sqrt(mean(error_percent.^2)));
fprintf('  Sensor Noise Std Dev: %.2f cm\n', sensor_noise_std);

%% Visualization 1: True vs Measured Fill Levels
figure('Position', [100, 100, 1000, 500], 'Name', 'Sensor Model Analysis');

subplot(1, 2, 1);
hold on;

% Plot true vs measured
x_positions = bin_id;
bar_width = 0.35;

% True fill levels (blue bars)
bar(x_positions - bar_width/2, true_fill_percent, bar_width, ...
    'FaceColor', [0.2, 0.4, 0.8], 'DisplayName', 'True Fill');

% Measured fill levels (orange bars)
bar(x_positions + bar_width/2, measured_fill_percent, bar_width, ...
    'FaceColor', [0.9, 0.5, 0.2], 'DisplayName', 'Measured Fill');

% Add error bars on measured values
errorbar(x_positions + bar_width/2, measured_fill_percent, absolute_error, ...
         'k.', 'LineWidth', 1.5, 'DisplayName', 'Absolute Error');

xlabel('Bin ID', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('Fill Level (%)', 'FontSize', 12, 'FontWeight', 'bold');
title('True vs Measured Fill Levels', 'FontSize', 14, 'FontWeight', 'bold');
legend('Location', 'northwest');
grid on;
ylim([0, 110]);
xlim([0, num_bins+1]);
hold off;

%% Visualization 2: Error Distribution Histogram
subplot(1, 2, 2);

% Create histogram of sensor errors
histogram(error_percent, 10, 'FaceColor', [0.3, 0.7, 0.3], ...
          'EdgeColor', 'black', 'LineWidth', 1.5);

% Add vertical line at zero error
hold on;
y_limits = ylim;
plot([0, 0], y_limits, 'r--', 'LineWidth', 2, 'DisplayName', 'Zero Error');
hold off;

xlabel('Measurement Error (%)', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('Frequency', 'FontSize', 12, 'FontWeight', 'bold');
title('Sensor Error Distribution', 'FontSize', 14, 'FontWeight', 'bold');
legend('Location', 'northwest');
grid on;

% Add text box with statistics
dim = [0.65, 0.15, 0.2, 0.15];
str = sprintf('Mean Error: %.2f%%\nStd Dev: %.2f%%\nRMS: %.2f%%', ...
              mean(error_percent), std(error_percent), sqrt(mean(error_percent.^2)));
annotation('textbox', dim, 'String', str, 'FitBoxToText', 'on', ...
           'BackgroundColor', 'white', 'EdgeColor', 'black', 'FontSize', 10);

fprintf('\n✓ Sensor model analysis complete!\n');

%% Additional Analysis: Distance Measurement
fprintf('\n--- Distance Measurement Analysis ---\n');
fprintf('Bin Height: %d cm\n', bin_height_cm);
fprintf('Average True Distance: %.2f cm\n', mean(true_distance_cm));
fprintf('Average Measured Distance: %.2f cm\n', mean(measured_distance_cm));
fprintf('Distance Measurement Std Dev: %.2f cm\n', std(measured_distance_cm - true_distance_cm));
