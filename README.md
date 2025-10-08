
# TECH2: Introduction to Programming, Data, and Information Technology

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Course material for part 2, fall 2025 (H25)

Author: Richard Foltyn


## Course outline for part 2

`L` = Lecture, `W` = Workshop


| Week | Day         | L/W | Topic | Notes & Exercises | Solutions |
|------|-------------|-----|-------|----------------------|------------------------------------------|
|  39  | Wed, Sep 24 | `L` | Git & VS Code (& NumPy) | [Slides](lectures/lecture1/lecture1-slides.pdf) | —  |
|      | Fri, Sep 26 | `W` | Git & VS Code (& NumPy) | [Notebook](workshops/workshop1/workshop1.ipynb), [PDF](workshops/workshop1/workshop1.pdf) | [Notebook](workshops/workshop1/workshop1-solution.ipynb), [PDF](workshops/workshop1/workshop1-solution.pdf) |
|  40  | Wed, Oct 1  | `L` | Intro to pandas | [Notebook](lectures/lecture2/lecture2.ipynb), [PDF](lectures/lecture2/lecture2.pdf) | —  |
|      | Wed, Oct 3  | `W` | Intro to pandas | [Notebook](workshops/workshop2/workshop2.ipynb), [PDF](workshops/workshop2/workshop2.pdf) | [Notebook](workshops/workshop2/workshop2-solution.ipynb), [PDF](workshops/workshop2/workshop2-solution.pdf) |
|  41  | Wed, Oct 8  | `L` | Plotting | [Notebook](lectures/lecture3/lecture3.ipynb), [PDF](lectures/lecture3/lecture3.pdf) | —  |
|      | Fri, Oct 10 | `W` | Plotting | [Notebook](workshops/workshop3/workshop3.ipynb), [PDF](workshops/workshop3/workshop3.pdf) |  |
|  42  | Wed, Oct 15 | `L` | Grouping and aggregation | [Notebook](lectures/lecture4/lecture4.ipynb), [PDF](lectures/lecture4/lecture4.pdf) | —  |
|      | Fri, Oct 17 | `W` | Grouping and aggregation | [Notebook](workshops/workshop4/workshop4.ipynb), [PDF](workshops/workshop4/workshop4.pdf) |  |
|  43  | Wed, Oct 22 | `L` | Concatenating and merging | [Notebook](lectures/lecture5/lecture5.ipynb), [PDF](lectures/lecture5/lecture5.pdf) | —  |
|      | Fri, Oct 24 | `W` | Concatenating and merging | [Notebook](workshops/workshop5/workshop5.ipynb), [PDF](workshops/workshop5/workshop5.pdf) | |


## Guides

See the [guides/](guides/README.md) folder for instructions on how to 
install Anaconda (Python), Visual Studio Code, and git version control.


## Forking & Cloning

### Forking

- Click on the `Fork` icon to fork this repository (create your own personal copy)
- In the future, you need to click on `Sync Fork` to get new commits made to this repository into your forked version.

### Cloning

1. Click on the green `Code` icon to clone the repository to your computer
2. Select HTTPS or SSH depending on your authentication method (SSH keys will only work if you have configured them) and copy the URL.
3. You can clone the repository directly in Visual Studio Code, or use the command line:

    _Using HTTPS (no SSH key configured):_
    ```bash
    git clone https://github.com/richardfoltyn/TECH2-H25.git
    ```
    _Using SSH keys:_
    ```bash
    git clone git@github.com:richardfoltyn/TECH2-H25.git
    ```


## Creating a Conda environment

Using the Anaconda Prompt (Windows) or Terminal (Mac), you can use 
the environment definition file ([environment.yml](environment.yml)) provided in this repository to create 
a conda environment called `TECH2`:
```bash
conda env create -f environment.yml
```
Note that you first need to change to the directly where `environment.yml` is located for this to work.


## Additional resources

1. [Think Python](https://allendowney.github.io/ThinkPython/index.html) by Allen B. Downey:
   general intro to Python, chapters are available as Jupyter notebooks.
2. [Python for Everybody](https://www.py4e.com/book) by Charles R. Severance:
   general intro to Python with a focus on data analysis, available as PDF.
3. [QuantEcon](https://quantecon.org/lectures/): Python programming for economics & finance
    (beginners & advanced)
3. [Introduction to Programming and Numerical Analysis](https://sites.google.com/view/numeconcph-introprog/home): 
    Python for macroeconomics, taught at the University of Copenhagen

## License

This material is licensed under a 
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/),
except for the data files contained in the `data/` folder, which
fall under the terms imposed by the original content creators.
