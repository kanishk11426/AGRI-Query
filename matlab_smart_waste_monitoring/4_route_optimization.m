%% ========================================================================
% Module 4: Waste Collection Route Optimization
% ========================================================================
% Simulates 15 bins at random locations
% Selects bins requiring collection (fill >= 80%)
% Computes nearest-neighbor route from depot
% Visualizes the optimized collection route
% ========================================================================

%% Parameters
num_bins = 15;              % Total number of bins
collection_threshold = 80;  % Collect bins with fill >= 80%
map_size = 10;              % Map area: 10km x 10km

fprintf('Route Optimization for Waste Collection\n');
fprintf('---------------------------------------\n\n');

%% Initialize Bin Locations and Fill Levels
rng(456);  % Set seed for reproducibility

% Generate random 2D coordinates (in km)
bin_x = map_size * rand(num_bins, 1);
bin_y = map_size * rand(num_bins, 1);

% Generate random fill percentages
bin_fill = 30 + rand(num_bins, 1) * 70;  % 30% to 100%

% Define depot location (waste processing center)
depot_x = map_size / 2;
depot_y = map_size / 2;

fprintf('Generated %d bins across %.0f x %.0f km area\n', num_bins, map_size, map_size);
fprintf('Depot location: (%.2f, %.2f) km\n\n', depot_x, depot_y);

%% Select Bins for Collection
% Only collect bins above threshold
bins_to_collect = find(bin_fill >= collection_threshold);
num_to_collect = length(bins_to_collect);

fprintf('Bins requiring collection (fill >= %.0f%%): %d bins\n\n', ...
        collection_threshold, num_to_collect);

if num_to_collect == 0
    fprintf('No bins require collection at this time.\n');
    fprintf('All bins are below %.0f%% threshold.\n', collection_threshold);
    return;
end

% Extract coordinates of bins to collect
collect_x = bin_x(bins_to_collect);
collect_y = bin_y(bins_to_collect);
collect_fill = bin_fill(bins_to_collect);

%% Nearest Neighbor Route Optimization
fprintf('Computing nearest-neighbor route...\n');

% Initialize route
route_order = zeros(num_to_collect, 1);
visited = false(num_to_collect, 1);

% Start from depot
current_x = depot_x;
current_y = depot_y;
total_distance = 0;

% Visit each bin using nearest-neighbor heuristic
for step = 1:num_to_collect
    % Find nearest unvisited bin
    min_dist = inf;
    nearest_bin = -1;

    for i = 1:num_to_collect
        if ~visited(i)
            % Calculate Euclidean distance
            dist = sqrt((collect_x(i) - current_x)^2 + ...
                       (collect_y(i) - current_y)^2);

            if dist < min_dist
                min_dist = dist;
                nearest_bin = i;
            end
        end
    end

    % Visit the nearest bin
    route_order(step) = nearest_bin;
    visited(nearest_bin) = true;
    total_distance = total_distance + min_dist;

    % Update current position
    current_x = collect_x(nearest_bin);
    current_y = collect_y(nearest_bin);
end

% Return to depot
return_distance = sqrt((depot_x - current_x)^2 + (depot_y - current_y)^2);
total_distance = total_distance + return_distance;

fprintf('Route optimization complete!\n');
fprintf('Total route distance: %.2f km\n\n', total_distance);

%% Create Route Table
fprintf('--- Optimized Collection Route ---\n\n');

% Build route coordinates in order
route_x = [depot_x; collect_x(route_order); depot_x];
route_y = [depot_y; collect_y(route_order); depot_y];
route_bin_ids = [0; bins_to_collect(route_order); 0];  % 0 = depot
route_fill = [NaN; collect_fill(route_order); NaN];

% Create table for route steps
step_num = (0:num_to_collect+1)';
location_names = cell(num_to_collect+2, 1);
location_names{1} = 'DEPOT (Start)';
for i = 1:num_to_collect
    location_names{i+1} = sprintf('Bin %d', bins_to_collect(route_order(i)));
end
location_names{end} = 'DEPOT (End)';

route_table = table(step_num, location_names, route_bin_ids, route_fill, ...
                    route_x, route_y, ...
    'VariableNames', {'Step', 'Location', 'BinID', 'FillPercent', 'X_km', 'Y_km'});

disp(route_table);

fprintf('\nRoute Summary:\n');
fprintf('  Total stops:    %d (excluding depot)\n', num_to_collect);
fprintf('  Total distance: %.2f km\n', total_distance);
fprintf('  Avg distance per stop: %.2f km\n', total_distance / (num_to_collect + 1));

%% Visualization: Route Map
figure('Position', [100, 100, 900, 700], 'Name', 'Collection Route Optimization');
hold on;

% Plot all bins (gray for not collected, colored for collected)
for i = 1:num_bins
    if bin_fill(i) >= collection_threshold
        % Bins to be collected (colored by fill level)
        if bin_fill(i) >= 95
            color = [0.9, 0.1, 0.1];  % Red - CRITICAL
        else
            color = [1.0, 0.5, 0.0];  % Orange - ALERT
        end
        scatter(bin_x(i), bin_y(i), 150, color, 'filled', ...
                'MarkerEdgeColor', 'black', 'LineWidth', 1.5);
    else
        % Bins below threshold (gray)
        scatter(bin_x(i), bin_y(i), 100, [0.7, 0.7, 0.7], 'filled', ...
                'MarkerEdgeColor', 'black', 'LineWidth', 1);
    end

    % Add bin ID labels
    text(bin_x(i), bin_y(i), sprintf(' %d', i), ...
         'FontSize', 9, 'FontWeight', 'bold', 'VerticalAlignment', 'middle');
end

% Plot depot
scatter(depot_x, depot_y, 300, [0.2, 0.6, 0.9], 'p', 'filled', ...
        'MarkerEdgeColor', 'black', 'LineWidth', 2, 'DisplayName', 'Depot');
text(depot_x, depot_y - 0.4, 'DEPOT', ...
     'FontSize', 11, 'FontWeight', 'bold', 'HorizontalAlignment', 'center');

% Plot optimized route
plot(route_x, route_y, 'r-', 'LineWidth', 2.5, 'DisplayName', 'Collection Route');

% Add arrows to show direction
for i = 1:(length(route_x)-1)
    % Add small arrows along the route
    dx = route_x(i+1) - route_x(i);
    dy = route_y(i+1) - route_y(i);
    mid_x = route_x(i) + 0.5 * dx;
    mid_y = route_y(i) + 0.5 * dy;
    quiver(mid_x, mid_y, dx*0.1, dy*0.1, 0, 'r', ...
           'LineWidth', 1.5, 'MaxHeadSize', 2);
end

% Labels and formatting
xlabel('X Coordinate (km)', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('Y Coordinate (km)', 'FontSize', 12, 'FontWeight', 'bold');
title('Optimized Waste Collection Route', 'FontSize', 14, 'FontWeight', 'bold');
grid on;
axis equal;
xlim([-0.5, map_size + 0.5]);
ylim([-0.5, map_size + 0.5]);

% Add legend
legend_entries = {
    sprintf('Depot'), ...
    sprintf('Collection Route (%.2f km)', total_distance), ...
    sprintf('Bins to Collect (n=%d)', num_to_collect), ...
    sprintf('Bins OK (n=%d)', num_bins - num_to_collect)
};

% Create custom legend
h1 = scatter(NaN, NaN, 300, [0.2, 0.6, 0.9], 'p', 'filled', ...
             'MarkerEdgeColor', 'black', 'LineWidth', 2);
h2 = plot(NaN, NaN, 'r-', 'LineWidth', 2.5);
h3 = scatter(NaN, NaN, 150, [1.0, 0.5, 0.0], 'filled', ...
             'MarkerEdgeColor', 'black', 'LineWidth', 1.5);
h4 = scatter(NaN, NaN, 100, [0.7, 0.7, 0.7], 'filled', ...
             'MarkerEdgeColor', 'black', 'LineWidth', 1);

legend([h1, h2, h3, h4], legend_entries, 'Location', 'bestoutside');

hold off;

fprintf('\n✓ Route visualization complete!\n');

%% Additional Statistics
fprintf('\n--- Collection Statistics ---\n');
fprintf('Total bins in system:     %d\n', num_bins);
fprintf('Bins requiring service:   %d (%.1f%%)\n', ...
        num_to_collect, num_to_collect/num_bins*100);
fprintf('Bins below threshold:     %d (%.1f%%)\n', ...
        num_bins - num_to_collect, (num_bins - num_to_collect)/num_bins*100);
fprintf('Average fill (to collect): %.1f%%\n', mean(collect_fill));
fprintf('Maximum fill (to collect): %.1f%%\n', max(collect_fill));
