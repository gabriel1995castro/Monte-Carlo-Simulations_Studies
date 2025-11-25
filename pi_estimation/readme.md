# Pi Estimation with Monte Carlo

This project uses the Monte Carlo method to estimate the value of π by generating random points within a square and counting how many fall within the inscribed circle.

---

## Concept

\[
\pi \approx 4 \times \frac{\text{points inside the circle}}{\text{total points}}
\]

- Square: side 2, centered at the origin  
- Circle: radius 1  
- `x² + y² <= 1` defines whether the point is inside the circle  

---

The script will:

Generate random points

Calculate the π estimation

Display a plot with:

Points inside the circle (blue)

Points outside the circle (red)

Reference circle and square

## Simulations Results
<div align="center">
  <div style="display: inline-block; margin: 10px; text-align: center;">
    <img src="./100_simulations.png" width="30" alt="Results of 100 Simulations">
    <p>Results of 100 Simulations</p>
  </div>
  <div style="display: inline-block; margin: 10px; text-align: center;">
    <img src="./10000_simulations.png" width="300" alt="Results of 10000 Simulations">
    <p>Results of 10000 Simulations</p>
  </div>
  <div style="display: inline-block; margin: 10px; text-align: center;">
    <img src="./1000000_simulations.png" width="300" alt="Results of 1000000 Simulations">
    <p>Results of 1000000 Simulations</p>
  </div>
</div>

## Execution

Run the script:

```bash
python pi_estimation.py

