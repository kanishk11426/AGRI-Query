%% ========================================================================
% Module 3: MQTT IoT Communication Demo
% ========================================================================
% Demonstrates IoT message payload creation
% Converts sensor data to JSON format
% Attempts MQTT publishing (with graceful fallback)
% ========================================================================

fprintf('IoT Communication Demonstration\n');
fprintf('-------------------------------\n\n');

%% Simulate Sensor Data
% Simulate data from a single smart bin
bin_id = 3;
bin_height_cm = 100;

% Simulate current sensor reading
rng('shuffle');  % Use current time as seed
fill_percent = 20 + rand() * 60;  % Random fill: 20-80%
waste_height = (fill_percent / 100) * bin_height_cm;
distance_cm = bin_height_cm - waste_height;

% Add small sensor noise
distance_cm = distance_cm + randn() * 1.5;
distance_cm = max(0, min(bin_height_cm, distance_cm));

% Recalculate fill percentage from noisy distance
measured_fill = ((bin_height_cm - distance_cm) / bin_height_cm) * 100;

% Determine status
if measured_fill >= 95
    status = 'CRITICAL';
elseif measured_fill >= 80
    status = 'ALERT';
elseif measured_fill >= 50
    status = 'MEDIUM';
else
    status = 'NORMAL';
end

% Get current timestamp
timestamp = datetime('now', 'Format', 'yyyy-MM-dd HH:mm:ss');

fprintf('Simulated Sensor Data:\n');
fprintf('  Bin ID:        %d\n', bin_id);
fprintf('  Distance:      %.2f cm\n', distance_cm);
fprintf('  Fill Level:    %.2f%%\n', measured_fill);
fprintf('  Status:        %s\n', status);
fprintf('  Timestamp:     %s\n\n', timestamp);

%% Create JSON Payload
fprintf('Creating IoT message payload...\n');

% Create structured data payload
payload = struct();
payload.bin_id = bin_id;
payload.timestamp = char(timestamp);
payload.distance_cm = round(distance_cm, 2);
payload.fill_percent = round(measured_fill, 2);
payload.status = status;
payload.battery_percent = 85;  % Simulated battery level
payload.temperature_c = 18 + rand() * 12;  % Ambient temperature 18-30°C
payload.location = struct('latitude', 28.6139, 'longitude', 77.2090);  % Delhi, India

% Convert to JSON string
try
    json_payload = jsonencode(payload, 'PrettyPrint', true);
    fprintf('JSON payload created successfully!\n\n');
catch
    % Fallback for older MATLAB versions without PrettyPrint
    json_payload = jsonencode(payload);
    fprintf('JSON payload created (compact format)!\n\n');
end

% Display the JSON payload
fprintf('--- IoT Message Payload (JSON) ---\n');
fprintf('%s\n', json_payload);
fprintf('----------------------------------\n\n');

%% MQTT Publishing Demo
fprintf('Attempting MQTT connection...\n');

% MQTT broker settings (using public test broker)
broker_address = 'broker.hivemq.com';  % Public MQTT broker
broker_port = 1883;
topic = sprintf('smartwaste/demo/bin%d', bin_id);

% Try to publish via MQTT
mqtt_success = false;

try
    % Check if MQTT client is available in this MATLAB version
    if exist('mqttclient', 'file') == 2
        fprintf('MQTT client support detected. Connecting to broker...\n');

        % Create MQTT client
        mqtt_client = mqttclient(broker_address, 'Port', broker_port);

        fprintf('Connected to %s:%d\n', broker_address, broker_port);
        fprintf('Publishing to topic: %s\n', topic);

        % Publish the JSON payload
        write(mqtt_client, topic, json_payload);

        fprintf('✓ Message published successfully!\n');
        mqtt_success = true;

        % Clean up
        clear mqtt_client;
    else
        % MQTT not available
        fprintf('MQTT client not available in this MATLAB installation.\n');
    end
catch ME
    % Handle any errors gracefully
    fprintf('MQTT publishing failed: %s\n', ME.message);
end

%% Summary
fprintf('\n========================================\n');
fprintf('       IoT Communication Summary\n');
fprintf('========================================\n');
fprintf('Payload Generation:  ✓ SUCCESS\n');
if mqtt_success
    fprintf('MQTT Publishing:     ✓ SUCCESS\n');
    fprintf('Broker:              %s:%d\n', broker_address, broker_port);
    fprintf('Topic:               %s\n', topic);
else
    fprintf('MQTT Publishing:     ⚠ SKIPPED\n');
    fprintf('Note: MQTT support not available or connection failed.\n');
    fprintf('      This is normal for basic MATLAB installations.\n');
    fprintf('      Payload was generated successfully for demo purposes.\n');
end
fprintf('========================================\n');

%% Additional Demo: Multiple Bins
fprintf('\n--- Simulating Multiple Bin Messages ---\n');

num_demo_bins = 5;
fprintf('Generating payloads for %d bins...\n\n', num_demo_bins);

for i = 1:num_demo_bins
    % Create payload for each bin
    temp_fill = 20 + rand() * 70;
    temp_status = 'NORMAL';
    if temp_fill >= 95
        temp_status = 'CRITICAL';
    elseif temp_fill >= 80
        temp_status = 'ALERT';
    elseif temp_fill >= 50
        temp_status = 'MEDIUM';
    end

    temp_payload = struct();
    temp_payload.bin_id = i;
    temp_payload.fill_percent = round(temp_fill, 2);
    temp_payload.status = temp_status;

    % Display compact info
    fprintf('Bin %d: %.1f%% [%s]\n', i, temp_fill, temp_status);
end

fprintf('\n✓ IoT communication demo complete!\n');
