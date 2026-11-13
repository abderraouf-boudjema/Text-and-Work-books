# Text and Work Books

> Comprehensive university-level textbooks and accompanying complete exercise workbooks in Classical Mechanics, Structure of Matter (Chemistry), and University Mathematics I.

**Author:** Abderraouf Boudjema  
**Curriculum Level:** Undergraduate (L1 / First-Year STEM & Exact Sciences)

---

## 📚 Overview of Collections

This repository contains the complete LaTeX source code, vector TikZ figures, authentic historical portraits, and compiled publication-ready PDF documents for three foundational science disciplines:

```
Text-and-Work-books/
├── textbooks/
│   ├── classical-mechanics/          # 121 pages · 15 chapters + 2 appendices
│   ├── structure-of-matter/          # 44 pages  · 3 chapters + reference tables
│   └── university-mathematics-i/     # 49 pages  · 6 chapters + analysis tables
└── workbooks/
    ├── classical-mechanics/          # 195 pages · 16 problem sets + appendices
    ├── structure-of-matter/          # 70 pages  · 3 deep problem sets + solutions
    └── university-mathematics-i/     # 92 pages  · 6 extensive problem sets + proofs
```

---

## 📖 Catalog of Volumes

### 1. Principles of Classical Mechanics
*Volume I: Mechanics of a Material Point*

* **Textbook**: [`Principles_of_Classical_Mechanics_Textbook.pdf`](textbooks/classical-mechanics/Principles_of_Classical_Mechanics_Textbook.pdf) (121 pages)
  * Rigorous coverage of foundational Newtonian mechanics, vector kinematics in 1D/2D/3D, curvilinear & intrinsic coordinates, relative motion & fictitious forces, energy theorems, conservative fields & potential wells, harmonic/damped oscillations, central force gravitation, Kepler orbits, and multi-particle collision kinematics.
* **Workbook**: [`Mechanics_of_a_Material_Point_Complete_Exercise_Book.pdf`](workbooks/classical-mechanics/Mechanics_of_a_Material_Point_Complete_Exercise_Book.pdf) (195 pages)
  * Comprehensive solved problem bank with complete step-by-step derivations, free-body diagrams, and exam-level challenges covering all 16 chapters.

---

### 2. Structure of Matter (*Structure de la Matière*)
*University General Chemistry & Subatomic Physics*

* **Textbook**: [`Structure_of_Matter_Comprehensive_Textbook.pdf`](textbooks/structure-of-matter/Structure_of_Matter_Comprehensive_Textbook.pdf) (44 pages)
  * Macroscopic states of matter, phase equilibria, Lavoisier conservation, stoichiometry, solution concentration metrics (molarity, molality, normality, titers), subatomic constituents, mass spectrometry, Aston stability curve, nuclear mass defects, and radioactive decay kinetics ($\alpha, \beta, \gamma$, half-life, dating).
* **Workbook**: [`Structure_of_Matter_Complete_Exercise_Book.pdf`](workbooks/structure-of-matter/Structure_of_Matter_Complete_Exercise_Book.pdf) (70 pages)
  * Exhaustive solved exercise sets covering solution concentrations, dilution formulas, mass spectrometry calculations, nuclear binding energy, and radiometric kinetics.

---

### 3. University Mathematics I
*Calculus, Real Analysis, Mathematical Logic, and Algebraic Structures*

* **Textbook**: [`University_Mathematics_I_Comprehensive_Textbook.pdf`](textbooks/university-mathematics-i/University_Mathematics_I_Comprehensive_Textbook.pdf) (49 pages)
  * Mathematical logic, quantifiers, set theory, binary relations, algebraic structures (groups, rings, fields), axiomatic construction of $\mathbb{R}$, supremum/infimum, sequence convergence ($\varepsilon$-$N$), continuity ($\varepsilon$-$\delta$), differentiability, Mean Value Theorem, Taylor polynomials with Lagrange remainder, and Riemann integration.
* **Workbook**: [`University_Mathematics_I_Complete_Exercise_Book.pdf`](workbooks/university-mathematics-i/University_Mathematics_I_Complete_Exercise_Book.pdf) (92 pages)
  * Step-by-step proofs, quantifier verification, epsilon-delta calculations, sequence convergence techniques, and integral evaluation exercises.

---

## 🛠️ Building from Source

To compile the LaTeX source documents into PDF format, make sure you have `texlive-full` or standard LaTeX distribution installed with `pdflatex`.

```bash
# Compile all textbooks and workbooks
make all

# Compile only textbooks
make textbooks

# Compile only workbooks
make workbooks

# Compile a specific book
make mechanics-textbook
make chemistry-workbook

# Clean auxiliary compilation files (.aux, .log, .out, etc.)
make clean
```

---

## 📄 License & Intellectual Property

All rights reserved © Abderraouf Boudjema. Academic and personal educational use permitted.
