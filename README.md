## Coupled Epidemics

### Installing and running the software

This software uses a quick and dirty combination of [Python] and [GNU Make]. The
python scripts serve two purposes:

  1. `scripts/stratify` allows python fragments and iteration to be embedded in [Kappa] models
  2. post-processing of the data (`scripts/combine`, and `scripts/coupled-epidemics-caseplot`)

To get the dependencies, doing

    python setup.py install

should be sufficient.

To generate the data and plots, you must have [KaSim] and [GNU Parallel] installed in addition, and
then it is simply typing,

    make

in this top-level directory.

### Example - second wave

This is a very simple example of a stratified SEIR model with interventions changing the
contact rate in such a way as to produce a [two-wave epidemic]. There are two age strata.
The first makes up 40% of the population, and the second, 60%. The contact matrix is
asymmetric,

$$
c = \left[
  \begin{array}{cc}
    13.0 & 8.0 \\
    4.0 & 10.0
  \end{array}
\right]
$$

Individuals in the first strata have more contact with each other than individuals in the 
second strata. They are also more likely to have contact first with second than second with
first. The infection rule looks like,

$$
\mathtt{%
  P(x\{s\}, age\{=\mathrm{i}\}),
  P(x\{i\}, age\{=\mathrm{j}\}) ->
  P(x\{e\}), P(x\{i\}) @
} \frac{\beta c_{ij}}{N}
$$

After some time, \\(c\\) is reduced by 70%, representing a lock-down, and after a longer time
it is then increased to 80% of its initial magnitude.

The result:
<image src="https://wwaites.github.io/coupled-epidemics/plots/second-wave.png" />

And using \\(c^T\\) in place of \\(c\\),
<image src="https://wwaites.github.io/coupled-epidemics/plots/second-wave-T.png" />

[Python]: https://python.org/
[GNU Make]: https://www.gnu.org/software/make
[GNU Parallel]: https://www.gnu.org/software/parallel
[Kappa]: https://kappalanguage.org/
[KaSim]: https://kappalanguage.org/download
[two-wave epidemic]: models/second-wave.pka

<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script>
