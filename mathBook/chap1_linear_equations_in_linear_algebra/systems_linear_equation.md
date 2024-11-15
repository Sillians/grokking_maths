# Systems of Linear Equation

A **linear equation** in the variables $`x_1, x_2, \dots, x_n`$ has the general form:

$`a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b`$

where:
- $`a_1, a_2, \dots, a_n`$ are constants (real or complex) called **coefficients** of the equation, and are usually known in advance.
- $b$ is also a constant (real or complex), often representing the **constant term** on the right side of the equation.
- $x_1, x_2, \dots, x_n$ are **variables** in the equation.

The subscript $n$ indicates that this form of the equation can have any positive number of variables, 
so a linear equation can involve one, two, or many variables, depending on the context.

A **system of linear equations** (or simply a **linear system**) consists of multiple linear equations that share the same set of variables, 
such as $`x_1, x_2, \dots, x_n`$. The goal is typically to find values for these variables that satisfy all the equations simultaneously.

For example, in the system:

$`\begin{cases} 2x_1 - x_2 + 1.5x_3 = 8 \\ x_1 - 4x_3 = -7  \end{cases}`$


we have two linear equations with the variables $x_1$, $x_2$, and $x_3$. 
To solve this system, we would find values for $x_1$, $x_2$, and $x_3$ that satisfy both equations at the same time.

### Key Points:
- Each equation in the system is linear (e.g., in the form $`a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b`$).
- The system may have one solution, no solution, or infinitely many solutions depending on the relationships between the equations.
- Various methods, such as substitution, elimination, and matrix techniques (like Gaussian elimination), can be used to solve these systems.


A **solution** to a system of linear equations is a list of values, say $`(s_1, s_2, \dots, s_n)`$, 
that satisfy each equation in the system. When these values are substituted for the variables $`x_1, x_2, \dots, x_n`$, 
they make each equation in the system hold true.

For example, for the system:

$`\begin{cases}  2x_1 - x_2 + 1.5x_3 = 8 \\ x_1 - 4x_3 = -7 \end{cases}`$

the list $`(5, 6.5, 3)`$ is a solution. When we substitute $`x_1 = 5`$, $`x_2 = 6.5`$, and $`x_3 = 3`$ into each equation:

1. In the first equation:

   $`2(5) - (6.5) + 1.5(3) = 10 - 6.5 + 4.5 = 8`$

   which simplifies to $8 = 8$, a true statement.

2. In the second equation:
   
   $`5 - 4(3) = 5 - 12 = -7`$

   which simplifies to $-7 = -7$, also a true statement.

Since both equations are true, $(5, 6.5, 3)$ is indeed a solution to the system.


The **solution set** of a linear system is the complete collection of all possible solutions that satisfy each equation in the system. 
If two linear systems have the same solution set, they are called **equivalent systems**. This means that every solution of the first 
system is also a solution of the second system, and vice versa.

In the case of two linear equations with two variables, finding the solution set corresponds to finding the **intersection point** of the two lines represented by these equations. 
This intersection point, if it exists, represents the unique solution to the system.

Here are some scenarios:

1. **One unique solution**: If the lines intersect at a single point, there is one unique solution.
2. **Infinitely many solutions**: If the lines are identical (i.e., they lie on top of each other), every point on the line is a solution, giving infinitely many solutions.
3. **No solution**: If the lines are parallel and distinct, they do not intersect, meaning there is no solution.

Finding the solution set for larger systems of equations (e.g., in three or more variables) is more complex, often requiring techniques like substitution, elimination, or matrix methods, 
but the concept remains the same: finding points that satisfy all equations simultaneously.

A system of linear equations has
1. no solution,or
2. exactly one solution,or 
3. infinitely many solutions.

A system of linear equations is said to be consistent if it has either one solution or infinitely many solutions; a system is inconsistent if it has no solution.


## Matrix Notation

The essential information of a linear system can be recorded compactly in a rectangular array called a matrix.

1. **Coefficient Matrix**: This matrix includes only the coefficients of the variables from the system of equations. 
   For the example system:
   
   $`x_1 - 2x_2 + x_3 = 0`$

   $`2x_2 - 8x_3 = 8`$

   $`5x_1 - 5x_3 = 10`$


   the coefficient matrix (3x3 in this case) is:

   $`\begin{bmatrix} 1 & -2 & 1 \\ 0 & 2 & -8 \\ 5 & 0 & -5  \end{bmatrix}`$


2. **Augmented Matrix**: This matrix includes an additional column with the constants from the right side of each equation. 
This is useful for applying methods like Gaussian elimination. The augmented matrix for the example system (a $3x4$ matrix) would be:

   $`\begin{bmatrix} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{bmatrix}`$

3. **Matrix Size**: The size, denoted as $m \times n$, represents the number of rows $(m)$ by the number of columns $(n)$.

By using matrices, we can apply systematic techniques to find solutions, check for consistency, and even determine the nature of the solution set. 
Matrix methods allow for efficient computation, particularly for larger systems, where manual substitution would be time-consuming.


## Solving a Linear System

Solving systems of linear equations involves a systematic procedure known as **Gaussian Elimination**. This method involves transforming a system of equations into
smaller equivalent system that can be solved more easily. The basic strategy is to replace one system with an equivalent system (i.e., one with the same solution set) that is easier to solve.

The general strategy is to use the first variable (e.g., $x1$) to eliminate its occurrences in the other equations, 
followed by eliminating subsequent variables in order (e.g., $x2$, $x3$), until a simple equivalent system is obtained.

Three basic operations simplify a linear system:

- Replace an equation by adding a multiple of another equation to it.
- Interchange two equations.
- Multiply all terms in an equation by a nonzero constant.

These operations preserve the solution set of the system and help transform the system into a more solvable form.


**Elementary Row Operations** are fundamental manipulations performed on the rows of a matrix to simplify solving linear systems. 
These operations do not alter the solution set of the system. The three operations are:

1. **Replacement**: Replace a row with the sum of itself and a multiple of another row.
   - Example: $`R_2 \to R_2 + 3R_1`$.

2. **Interchange**: Swap two rows.
   - Example: $`R_1 \leftrightarrow R_3`$.

3. **Scaling**: Multiply all entries in a row by a nonzero constant.
   - Example: $`R_3 \to 2R_3`$.

These operations are essential for techniques like **Gaussian elimination** and **row-reduction** to solving systems of linear equations or finding the rank of a matrix.













































