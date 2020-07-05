## Coupled Epidemics

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

in this top-level directtory.

[Python]: https://python.org/
[GNU Make]: https://www.gnu.org/software/make
[GNU Parallel]: https://www.gnu.org/software/parallel
[Kappa]: https://kappalanguage.org/
[KaSim]: https://kappalanguage.org/download
