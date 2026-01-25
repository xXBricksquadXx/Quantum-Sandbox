# The Born Identity: Probability and the Unit Vector

## 🧬 The Core Logic

The **Born Rule** is the mathematical "handshake" between the quantum world and our observed reality. It states that the probability ($P$) of finding a particle in a specific state is the square of its amplitude.

$$P(x) = |\Psi(x)|^2$$

## 📡 S6/Radio Analogy: Signal Power

In radio terms, the **Wavefunction ($\Psi$)** is like the voltage of a signal. Voltage can be positive or negative (or complex). However, **Power** (what actually hits the speaker) is proportional to the **Square** of that voltage.

- **The Wave**: The underlying "unseen" potential.
- **The Square**: The "heard" or observed result.

## 🏹 Unit Vectors ($i$ and $j$)

We represent these states using **Unit Vectors**. Think of these as "Directional Markers" in a complex map. To move the "Mirror," we rotate these vectors. If the vector isn't "Normalized" (Length = 1), our math "leaks," and the probability doesn't add up to 100%.

## 📝 Lab Implementation

Our `core_physics/wave_mechanics.py` enforces this via the `get_probabilities()` method, ensuring our "Sandbox" stays within the bounds of physical reality.
