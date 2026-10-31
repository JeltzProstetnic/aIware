---
title: "Call sheet — Michiel, Fri 30 Oct, 10:00"
---

## Questions, in this order

**1. Which brain map is it?**

*Say:* "Your brain network has 96 pieces. Which brain map is that? And could we plug a few of our small spiking brains into some of those pieces?"

*Why:* His network is a map of the whole brain, one piece per brain region. We would like to use his map as the frame and put our detailed pieces into it. His code actually works with 68 pieces, not 96, so ask which it is.

**2. Did you test your chaos meter on something calm?**

*Say:* "Your λ is above zero everywhere. Did you check what it shows for a calm system that is only being shaken by noise? We have test cases like that. Shall we swap: you run our test cases, and we run yours?"

*Why:* λ is a meter for chaos: above zero is supposed to mean chaos. But shake a calm system with random noise and the meter also goes above zero. Without that test, "above zero" proves nothing. This question opens the swap of tools we want.

**3. Only after he says yes to the swap: why does the memory meter go below zero?**

*Say:* "In Fig. 2 your DFA scale runs from −0.2 to 1.2. Which window sizes did you use, and how do you read the part below zero?"

*Why:* DFA is a meter for how long a signal remembers its own past. Done correctly, it can never go below zero. Then offer him the two PDFs: his paper with the errors marked, and the note on his code with the fixes.

## If the call turns to our own models

- **Our simple network** works best when it is calm and orderly, not at the edge of chaos. We saw this in 30 out of 30 tries.
- **Our simulated animal** has a brain of 8,000 cells and looks for food in a small world. We looked for activity patterns in its brain that last over time. Our pattern finder was too blunt to see weak patterns, so we don't know yet whether they are there.
- **Learning:** we let it learn from rewards. It did not eat more than copies that could not learn. A copy whose brain was unplugged from its arm ate just as much, because its reflexes do the eating.
- **First search, this morning (unchecked):** in the brain parts with no direct input from the senses, our animal shows a steady pattern of cells firing together. It does not follow the arm or the food. The overall activity of the frontal part goes up and down with hunger: a weaker copy of the hunger signal from the sensory part, in all three animals. By our definition that copy probably already counts as the simplest kind of inner model, one locked to its input; we are still checking. What the rest of the pattern stands for, we don't know yet.
- **Next:** a bigger animal (40,000 cells), with learning switched on.
- **Say only "the simplest kind"** (a copy locked to its input). Do not say we found models that predict, plan or run ahead of the input.

## The experiment for his compute

*Say:* "This is what we'd like to run with you. In our creature, the brain parts without sensory input show a steady pattern. So far the frontal part carries a copy of the hunger signal, probably the simplest kind of model, locked to its input. What we want to find out is whether richer models of the creature's own state form there, the self-model regulating itself that you wrote about, once the brain is bigger and learns. We want to test that four ways: cut its direct input and see whether it rebuilds from other cues; see whether it moves before the change comes; push the network along it and see whether behaviour changes; damage parts of the brain or change the body and see whether it survives. The deciding test: put a new obstacle between the arm and the food that the built-in reflexes cannot get around, and see whether the creature finds a way. First we make sure the experiment is sound on our own GPU, at 40,000 cells, with every control and the analysis fixed in advance. Once it is, we would like to run it with you on millions of neurons, with learning switched on and many repeats. Our cell is NEST's standard neuron, so the model can move to NEST on your machines."

*If he asks for numbers:* up to about a million cells we estimate 1,000 to 10,000 GPU-hours with learning; for millions we would work out the cost together, because we have no multi-GPU code yet.
