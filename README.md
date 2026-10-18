## 100 numpy exercises

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/rougier/numpy-100/notebooks/100%20Numpy%20exercises.ipynb)

This is a collection of numpy exercises from numpy mailing list, stack overflow, and numpy documentation. I've also created some problems myself to reach the 100 limit. The goal of this collection is to offer a quick reference for both old and new users but also to provide a set of exercises for those who teach. For extended exercises, make sure to read [From Python to NumPy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/).

→ [Test them on Binder](http://mybinder.org:/repo/rougier/numpy-100/notebooks/100_Numpy_exercises.ipynb)  
→ [Read them on GitHub](100_Numpy_exercises.md)  

Note: markdown and ipython notebook are created programmatically from the source data in `source/exercises.ktx`.
To modify the content of these files, please change the text in the source and run `uv run generators.py`.

### Practice locally

With [uv](https://docs.astral.sh/uv/) installed:

```sh
uv run jupyter lab 100_Numpy_exercises.ipynb
```

This creates the environment on first run (Python 3.14, NumPy 2.x, JupyterLab) and opens the exercises notebook.
Inside the notebook, `hint(n)` and `answer(n)` print the hint and solution for exercise `n`.

The keyed text format (`ktx`) is a minimal human readable key-values to store text (markdown or others) indexed by keys. 

This work is licensed under the MIT license.  
[![DOI](https://zenodo.org/badge/10173/rougier/numpy-100.svg)](https://zenodo.org/badge/latestdoi/10173/rougier/numpy-100)


### Variants in Other Languages

 - **Julia**: [100 Julia Exercises](https://github.com/RoyiAvital/Julia100Exercises).
