# BifDraw Application Documentation

## Introduction

BifDraw is a Python application designed to generate bifurcation plots for the classical logistic equation and its q-generalizations.

## Development Environment

- **Software**: Microsoft Visual Studio Code (ver. 1.41.1).
- **Programming Language**: Python (ver. 3.7).

## Libraries and Dependencies

1. **NumPy**: 
   - For working with arrays, linear algebra, Fourier transformations, and matrices.
   - Useful for managing large arrays.
   
2. **Matplotlib**:
   - Responsible for generating plots compatible with NumPy.
   - Used to render the bifurcation diagram in BifDraw.

3. **TkInter**:
   - Framework for creating simple GUIs in Python.
   - GUIs built using TkInter have a native OS look.

## Application Flow

1. Initialization of GUI.
2. Default initialization of equation parameters.
3. The user takes control of the menu:
   - Alter specific equation parameters.
   - Choose the type of equation (classical or q-generalized).
   - Generate and display the diagram based on the input.
   - Terminate the application.

## Code Structure

1. Import libraries and assign aliases.
2. Initialize the GUI.
3. Define methods for progress bar updates and interrupting computations.
4. Handle errors using a dedicated method.
5. Compute the logistic equation based on user parameters.
6. Plot the equation results and display the chart.

## Using the Application for Classical Logistic Equation

1. **User Interface**:
   - Minimalistic and easy to navigate.
   - Choose the equation type (classic logistic or q-generalized).
   
2. **Parameters for Classic Logistic Equation**:
   - **Number of Steps**: Iterations to be executed for each α.
   - **Discarded Steps**: How many of the last iterations will be plotted.
   - **Initial Value**: Starting value of the logistic equation.
   - **Resolution**: Defines the increment step for α.

3. **Self-similarity in Bifurcation Plot**:
   - Bifurcation plots have a self-similar nature. 
   - The pattern repeats infinitely, showcasing the fractal nature of the bifurcation diagram.

## Using the Application for q-Generalized Logistic Equation

1. **User Interface**:
   - Offers options to modify seven parameters.

2. **New Parameters**:
   - **q (or w) Parameter Value**: Determines the value of q.
   - **Range of w (or q) Values**: Defines the range for the q-generalized equation.
   - **Dependency Type**: Dictates the kind of relationship plotted on the bifurcation diagram.

---

**Note**: The BifDraw application is best suited for those familiar with bifurcation diagrams and the logistic equation. Before using, it's advisable to understand the nuances of the logistic equation and how the parameters affect the resulting plots.

## 🛡 License

[![License](https://img.shields.io/github/license/zszprz/bifdraw)](https://github.com/zszprz/bifdraw/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/zszprz/bifdraw/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{bifdraw,
  author = {Department of Complex Systems, Rzeszów University of Technology},
  title = {bifdraw.py is a python gui application that helps creating bifuraction graphs},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/zszprz/bifdraw}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
