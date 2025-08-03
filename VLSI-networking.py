import random
import matplotlib.pyplot as plt

# Function to Simulate a Slot
def simulate_slot(p):
    packet_a = 1 if random.random() < p else 0
    packet_b = 1 if random.random() < p else 0
    return packet_a, packet_b

# Process Each Slot
def process_slot(p):
    packet_a, packet_b = simulate_slot(p)
    output_a = packet_a or packet_b  # Output at A
    output_c = 0  # Initialize output at C

    if packet_a + packet_b > 1:  # If both inputs have packets
        output_c = 1  # Only one packet can reach C
    elif packet_a or packet_b:
        output_c = 1

    return output_a, output_c

# Run Simulation for Different p Values
def run_simulation():
    p_values = [i * 0.025 for i in range(1, 41)]  # 0.025 to 1.0 in 0.025 steps
    num_slots = 1000
    throughput_a = []
    throughput_c = []

    for p in p_values:
        total_output_a = 0
        total_output_c = 0

        for _ in range(num_slots):
            output_a, output_c = process_slot(p)
            total_output_a += output_a
            total_output_c += output_c

        # Calculate normalized throughput
        throughput_a.append(total_output_a / num_slots)
        throughput_c.append(total_output_c / num_slots)

    return p_values, throughput_a, throughput_c

# Plot Separate Graphs for A and C
def plot_separate_graphs(p_values, throughput_a, throughput_c):
    # Plot for Throughput A
    plt.figure()
    plt.plot(p_values, throughput_a, label="Throughput A", marker='o', color='blue')
    plt.xlabel("Probability p")
    plt.ylabel("Normalized Throughput")
    plt.title("Throughput for Element A vs Probability p")
    plt.legend()
    plt.show()

    # Plot for Throughput C
    plt.figure()
    plt.plot(p_values, throughput_c, label="Throughput C", marker='x', color='orange')
    plt.xlabel("Probability p")
    plt.ylabel("Normalized Throughput")
    plt.title("Throughput for Element C vs Probability p")
    plt.legend()
    plt.show()

# Main Function to Run Simulation and Plot
def main():
    p_values, throughput_a, throughput_c = run_simulation()
    plot_separate_graphs(p_values, throughput_a, throughput_c)

if __name__ == "__main__":
    main()