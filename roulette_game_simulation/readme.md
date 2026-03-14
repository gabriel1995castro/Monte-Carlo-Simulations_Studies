# Casino Simulation with Monte Carlo

This project uses the Monte Carlo method to simulate the outcomes of multiple players in a casino game with a slight house edge (2%). It demonstrates how randomness and probability lead to predictable losses over time.

---

## Concept

The simulation is based on a "Random Walk" logic where a player bets $1 per round.

  Win: 49% chance (number between 1 and 49).

  Loss: 51% chance (number between 50 and 100).

  House Edge: 2% (51%−49%).

\[
  Expected Value=(1×0.49)+(−1×0.51)=−0.02
\]


The negative expected value ensures that, on average, a player loses $0.02 for every $1 betted.

---

The script will:

  Simulate multiple players concurrently.
  Store the balance history for each session.
  Display two types of plots:
  Time Series Plot: Shows individual paths and the "cloud" of results.
  Histogram: Shows the distribution of final balances and the mean.
  
## Simulations Results

| Multiple Trajectories (Cloud) |
|-----------------------------|
| ![](./100_simulations.png)  |

| Final Distribution (100 Players) |
|------------------------------|
| ![](./10000_simulations.png) |

| 1000000 Simulações |
|--------------------|
| ![](./1000000_simulations.png) |

## Execution

Run the script:

```bash
python pi_estimation.py

