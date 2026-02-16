#!/usr/bin/env python3
"""
Create a tracked-changes version of the full paper with proposed insertions.
"""

# Read the original paper
with open('/home/jeltz/aIware/paper/full/four-model-theory-full.md', 'r') as f:
    lines = f.readlines()

# Define the header text
header = '''# Tracked Changes — Four-Model Theory (Full Paper)

**Purpose**: This is the working version of the full paper with proposed changes tracked inline. The canonical clean version remains at `four-model-theory-full.md`. Changes here are proposed additions/modifications for the journal submission (target: Physics of Life Reviews or BBS).

**Convention**:
- Proposed insertions are wrapped in: `<!-- [PROPOSED INSERTION — Source: X, Date: Y] -->` and `<!-- [END INSERTION] -->`
- Proposed deletions are wrapped in: `<!-- [PROPOSED DELETION — Source: X, Date: Y] -->` and `<!-- [END DELETION] -->`
- Proposed modifications show both old and new text
- All changes include source attribution and rationale

**Change Log**:
| Date | Source | Section | Type | Description |
|------|--------|---------|------|-------------|
| 2026-02-16 | Session 53, Perplexity review analysis | 6.7 (new) | Addition | Developmental Psychology Bridge |
| 2026-02-16 | Session 53, Perplexity review analysis | 4.2 | Addition | "Simulation must feel" functional necessity argument |
| 2026-02-16 | Session 53, Perplexity review analysis | 3.4 | Addition | Identity claim framing with H2O analogy |

---

'''

# Define the three proposed insertions

# Change 1: Section 6.7 (new section after 6.6)
section_6_7 = '''
<!-- [PROPOSED INSERTION — Source: Session 53, Perplexity review analysis, Date: 2026-02-16] -->
<!-- Rationale: Bridges theory to developmental psychology literature; generates testable predictions about mirror self-recognition, theory of mind, social deprivation, and CBT as adult developmental recalibration. Addresses gap in empirical grounding for the four-model architecture's developmental trajectory. -->

### 6.7 Developmental Psychology Bridge

The four-model architecture predicts a specific developmental trajectory for consciousness. The implicit models (IWM, ISM) are learned; the explicit models (EWM, ESM) are generated from them. Since the implicit models of a newborn are nearly empty, the newborn's simulation should be thin — basic consciousness at most — with richness increasing as the implicit models accumulate content through experience and, critically, through social interaction.

This generates several testable developmental predictions:

1. **Mirror self-recognition (~18 months)** marks the point where the ESM becomes rich enough to model the physical self as an object. This corresponds to the transition from basic to simply extended consciousness.

2. **Theory of mind (~3-4 years)** marks the emergence of the ESM modeling other ESMs — the capacity to understand that another person's beliefs may differ from one's own. This corresponds to the emergence of doubly extended consciousness.

3. **Phenomenal character is developmental**: The qualitative character of experience (what pain, pleasure, or fear *feel like*) is shaped by the training history of the implicit models, particularly through caregiver feedback and social interaction. A baby's experience of pain is structurally different from an adult's because the ISM that generates the ESM is different. The four-model architecture provides the *capacity* for experience; the social environment provides the *content*.

4. **Social deprivation predicts phenomenal impoverishment**: Children raised without social contact (feral child cases) have the neural architecture for consciousness but profoundly impoverished implicit models. The theory predicts that their ESM should be stunted — not because the hardware is broken, but because the training data for the implicit models was never provided.

5. **CBT as adult developmental recalibration**: Cognitive behavioral therapy works by the same mechanism as infant social learning — conscious experience (guided by the therapist) reshaping implicit structure through repetition. The adult ISM is more consolidated than the infant's, requiring more repetition, but the mechanism is identical.

This developmental perspective connects the four-model architecture to a rich empirical literature in developmental psychology (Piaget's stages, Tomasello's shared intentionality, Meltzoff's imitation studies) while generating predictions that distinguish the theory from competitors that lack a developmental account of phenomenal consciousness.

<!-- [END INSERTION] -->

'''

# Change 2: In Section 4.2, after the paragraph about the "dual evaluation architecture"
section_4_2_insertion = '''
<!-- [PROPOSED INSERTION — Source: Session 53, Perplexity review analysis, Date: 2026-02-16] -->
<!-- Rationale: Addresses "Why must the simulation feel?" critique. Argues that phenomenality is functionally necessary for evaluation, not epiphenomenal. Distinguishes theory from both classical epiphenomenalism and standard functionalism. -->

This functional essentiality extends specifically to phenomenality. The substrate deploys the simulation as its evaluation mechanism — presenting situations so the simulation can assess consequences and register outcomes. For this evaluation to work, simulated states must have valence: they must *matter* to the simulation. A pain signal that is merely a numerical value without aversive character cannot drive avoidance at the simulation level. Only a simulation whose states carry hedonic valence — whose representations of threat, opportunity, and consequence are genuinely aversive or attractive — can perform the evaluative function that justifies the metabolic cost of maintaining the simulation. Phenomenality is not an optional feature of the simulation; it is the mechanism by which the simulation evaluates. Remove phenomenality and the simulation becomes a passive model rather than an evaluation engine — a spreadsheet rather than a simulation.

This distinguishes the theory's position from both traditional epiphenomenalism and functionalism: qualia lack independent causal power over the substrate, but the phenomenal character of the simulation is constitutive of its evaluative function. The simulation cannot "run dark" — cannot perform its function without phenomenality — because valence *is* the evaluation.

<!-- [END INSERTION] -->

'''

# Change 3: In Section 3.4, after the argument about self-referential closure
section_3_4_insertion = '''
<!-- [PROPOSED INSERTION — Source: Session 53, Perplexity review analysis, Date: 2026-02-16] -->
<!-- Rationale: Addresses "Why should we accept this as an answer?" critique. Frames the theory as making an identity claim (analogous to "water is H2O") rather than providing a further explanation. Makes clear that identity claims are stopping points, not gaps. Emphasizes falsifiability via empirical predictions. -->

This constitutes an identity claim: experience is what four-model self-simulation at criticality *is*. Identity claims in science are stopping points, not gaps. "Water is H₂O" cannot be further explained — the identity is the explanation. Similarly, the claim that experience is identical to self-referential simulation of this specific type at this specific dynamical regime is falsifiable (if the predictions fail, the identity is wrong) but cannot be "further explained" without requesting a different kind of universe. The identity claim's strength lies precisely in its falsifiability: it stands or falls with the empirical predictions in Section 8.

<!-- [END INSERTION] -->

'''

# Now find the insertion points and insert the text
output_lines = []

# First, add the header
for line in header.split('\n'):
    output_lines.append(line + '\n')

i = 0
while i < len(lines):
    line = lines[i]

    # Check if we're at Section 6.6 Clinical Psychology Bridge
    # We need to find the end of section 6.6 and insert 6.7 before section 7
    if line.strip().startswith('## 7. Comparative Analysis'):
        # Insert section 6.7 before this
        output_lines.append(section_6_7)
        output_lines.append(line)

    # Check if we're in Section 4.2, looking for the dual evaluation architecture paragraph
    elif line.strip().startswith('### 4.2 Consciousness as Process, Not Agent'):
        output_lines.append(line)
        # Now we need to find the end of the "dual evaluation architecture" paragraph
        # This is complex, so let me read ahead
        i += 1
        while i < len(lines):
            output_lines.append(lines[i])
            # Look for the paragraph that ends with "...the very thing natural selection shaped the architecture to do."
            if 'the very thing natural selection shaped the architecture to do.' in lines[i]:
                # Insert after this paragraph
                output_lines.append('\n')
                output_lines.append(section_4_2_insertion)
                output_lines.append('\n')
                break
            i += 1

    # Check if we're in Section 3.4, looking for the self-referential closure paragraph
    elif line.strip().startswith('### 3.4 Virtual Qualia: Dissolving the Hard Problem'):
        output_lines.append(line)
        # Now we need to find the end of the self-referential closure argument
        i += 1
        while i < len(lines):
            output_lines.append(lines[i])
            # Look for the paragraph that ends with "the gap between process and feeling does not exist."
            if 'the gap between process and feeling does not exist.' in lines[i]:
                # Insert after this paragraph
                output_lines.append('\n')
                output_lines.append(section_3_4_insertion)
                output_lines.append('\n')
                break
            i += 1

    else:
        output_lines.append(line)

    i += 1

# Write the output
with open('/home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md', 'w') as f:
    f.writelines(output_lines)

print(f"Created tracked version with {len(output_lines)} lines")
print("Original had {0} lines".format(len(lines)))
print("\nFile written to: /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md")
