
# 📶 VLSI Switching Network Simulator

This Python project implements a **discrete event simulation** of a network of 2-input/1-output VLSI switching elements. It evaluates the **throughput performance** of each switching element under varying input probabilities.

## 🧠 Project Overview

The simulated network includes three switching elements: A, B, and C. Packets arrive at A and B according to a **Bernoulli process**, and the simulation computes how often each element produces a successful output.

### Simulation Logic

* Each **time slot**, packets may arrive at A and B with a fixed probability `p`.
* If both A and B receive packets, only one reaches C; the other is dropped.
* Throughput for A and C is computed over **1000 slots** for each `p` value.

## 📊 Output

Two graphs are generated:

* **Throughput of A vs. Probability `p`**
* **Throughput of C vs. Probability `p`**

These graphs help analyze the network’s behavior as input probability increases from `0.025` to `1.0`.

## 🛠️ Technologies Used

* Python 3
* `matplotlib` for plotting
* `random` module for simulating Bernoulli arrivals


## 📈 Sample Output

![Throughput Graphs](screenshots/example_output.png) 



## ✅ Author

**Naafiul Hossain**

---
