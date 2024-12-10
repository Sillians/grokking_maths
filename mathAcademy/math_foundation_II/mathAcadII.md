## Mathematical Foundations II

## **Imaginary Numbers**

Imaginary numbers extend the real number system to include solutions to equations that involve the square root of negative numbers. 
They play a critical role in mathematics, physics, and engineering.

---

### **Definition**
An **imaginary number** is a number of the form:

$`z = bi`$

where:
- $b$ is a real number,
- $i$ is the imaginary unit, defined as:
  
  $`i = \sqrt{-1}, \quad \text{so } i^2 = -1.`$


#### **Complex Numbers**
Imaginary numbers are a subset of **complex numbers**, which are of the form:

$`z = a + bi`$
,
where $a$ (the real part) and $b$ (the imaginary part) are real numbers.

---

### **Arithmetic with Imaginary Numbers**

1. **Addition and Subtraction**:
   Combine like terms.
   
   $`(bi_1) + (bi_2) = (b_1 + b_2)i, \quad (bi_1) - (bi_2) = (b_1 - b_2)i.`$


2. **Multiplication**:
   Use the property $`i^2 = -1`$:
   
   $`(b_1i)(b_2i) = b_1b_2i^2 = -b_1b_2.`$


3. **Division**:
   Simplify by rationalizing the denominator:
   
   $`\frac{b_1i}{b_2i} = \frac{b_1}{b_2}.`$

---

### **Powers of \(i\)**

The powers of $i$ cycle in a pattern:

$`i^1 = i, \quad i^2 = -1, \quad i^3 = -i, \quad i^4 = 1.`$

For higher powers:

$`i^n = i^{n \mod 4}.`$

---

### **Graphical Representation**

Imaginary numbers can be represented on the **complex plane**, where:
- The horizontal axis represents the real part $(a)$,
- The vertical axis represents the imaginary part $(b)$.

Pure imaginary numbers lie on the vertical axis $(a = 0)$.

---

### **Magnitude of Imaginary Numbers**

The **magnitude** (or absolute value) of an imaginary number $bi$ is given by:

$`|bi| = |b|.`$

For a complex number $`z = a + bi`$, the magnitude is:

$`|z| = \sqrt{a^2 + b^2}.`$

---

### **Applications of Imaginary Numbers**

1. **Quadratic Equations**:
   Imaginary numbers arise as solutions to equations with no real roots, such as:
   
   $`x^2 + 1 = 0 \implies x = \pm i.`$

2. **Signal Processing**:
   Imaginary numbers are used in Fourier transforms to represent waves and oscillations.

3. **Electrical Engineering**:
   Imaginary numbers represent the phase difference in alternating current (AC) circuits.

4. **Quantum Mechanics**:
   Imaginary numbers are integral to Schrödinger's equation and wave functions.

---

### **Properties**

1. **Conjugates**:
   The conjugate of $`z = a + bi`$ is:
   
   $`\overline{z} = a - bi.`$

   Conjugates are used to simplify expressions and compute magnitudes.

2. **Roots of Unity**:
   Imaginary numbers are essential in finding the $n$-th roots of unity, the solutions to:
   
   $`z^n = 1.`$

---

### **Euler's Formula**

A profound connection between imaginary numbers, trigonometry, and exponential functions is given by 
Euler's formula:

$`e^{i\theta} = \cos\theta + i\sin\theta,`$

where $`e^{i\pi} + 1 = 0`$, known as Euler's identity, is a celebrated equation in mathematics.

---

### **Misconceptions**

1. **Imaginary Numbers Aren't Real**:
   Though named "imaginary," they have real-world applications.
2. **Imaginary and Complex are Different**:
   Imaginary numbers are a subset of complex numbers.

Imaginary numbers expand the real number system and are essential in fields ranging from algebra to 
advanced physics and engineering.



## **Sets**

A **set** is a well-defined collection of distinct objects, called elements or members. Sets are fundamental in mathematics and serve as the basis for 
various mathematical structures and disciplines, such as algebra, topology, and logic.

---

### **Definition**

A set is denoted using curly braces:

$`S = \{a, b, c, \dots\}`$,

where $`a, b, c, \dots`$ are the elements of the set.

---

### **Basic Terminology**

1. **Element**:
   An object in a set. If $a$ is in $S$, we write $`a \in S`$; otherwise, $`a \notin S`$.

2. **Cardinality**:
   The number of elements in a set, denoted as $`|S|`$.

3. **Empty Set**:
   The set with no elements, denoted as $\emptyset$ or $\{\}$.

4. **Subset**:
   If every element of $A$ is also in $B$, then $A$ is a subset of $B$, written as $`A \subseteq B`$.

5. **Proper Subset**:
   $A$ is a proper subset of $B$ if $`A \subseteq B`$ and $`A \neq B`$, written as $`A \subset B`$.

6. **Universal Set**:
   The set containing all objects under consideration, usually denoted as $U$.

---

### **Set Notations**

1. **Roster/Tabular Form**:
   Elements are listed explicitly:
   
   $`A = \{1, 2, 3, 4\}.`$

2. **Set-Builder Form**:
   Describes the properties of the elements:
   
   $`A = \{x \mid x \text{ is an integer and } 1 \leq x \leq 4\}`$.

---

### **Types of Sets**

1. **Finite Set**:
   A set with a finite number of elements:
   
   $`B = \{2, 4, 6, 8\}`$.

2. **Infinite Set**:
   A set with an unbounded number of elements:
   
   $`C = \{x \mid x \text{ is a positive integer}\}`$.


3. **Equal Sets**:
   Two sets are equal if they have exactly the same elements:
   
   $`\{1, 2, 3\} = \{3, 2, 1\}`$.


4. **Disjoint Sets**:
   Two sets are disjoint if they have no elements in common:
   
   $`A \cap B = \emptyset`$.


5. **Singleton Set**:
   A set with exactly one element:
   
   $`D = \{a\}`$.

---

### **Set Operations**

1. **Union**:
   The set of elements in either $A$, $B$, or both:
   
   $`A \cup B = \{x \mid x \in A \text{ or } x \in B\}`$.


2. **Intersection**:
   The set of elements common to $A$ and $B$:
   
   $`A \cap B = \{x \mid x \in A \text{ and } x \in B\}`$.


3. **Difference**:
   The set of elements in $A$ but not in $B$:
   
   $`A \setminus B = \{x \mid x \in A \text{ and } x \notin B\}`$.


4. **Complement**:
   The set of elements not in $A$, relative to the universal set $U$:
   
   $`A^c = \{x \mid x \in U \text{ and } x \notin A\}`$.


5. **Symmetric Difference**:
   The set of elements in either $A$ or $B$, but not in both:
   
   $`A \oplus B = (A \setminus B) \cup (B \setminus A)`$.

---

### **Venn Diagrams**

A Venn diagram is a visual representation of sets and their relationships. Circles represent sets, 
and overlaps illustrate intersections or unions.

---

### **Applications**

1. **Mathematics**:
   - Basis for probability theory and number theory.
2. **Computer Science**:
   - Sets model collections of objects in programming and databases.
3. **Logic**:
   - Used in symbolic reasoning and propositional calculus.

---

Sets provide a foundation for understanding relationships between collections and form the building 
blocks of advanced mathematical structures.




## **Ellipsis Notation**

**Ellipsis notation** (`...`) is used to represent a sequence of elements or terms in a compact and understandable way when listing all terms explicitly 
is impractical or unnecessary. It implies continuity or repetition of a pattern.

---

### **Uses of Ellipsis Notation**

1. **Finite Sequences**:
   For sequences where the pattern is clear, ellipsis notation shortens the representation:
   
   $`\{1, 2, 3, ..., 10\} \quad \text{represents } \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}`$.


2. **Infinite Sequences**:
   Used to indicate sequences that continue indefinitely:
   
   $`\{1, 2, 3, ...\} \quad \text{represents all positive integers}`$.


3. **Series**:
   For mathematical series, it indicates ongoing addition of terms:
   
   $`1 + 2 + 3 + \cdots \quad \text{represents an infinite sum of natural numbers}`$.


4. **Matrices**:
   To represent repeated patterns in rows or columns:
   
   $`\begin{bmatrix} 1 & 2 & 3 & \cdots & n \\ 2 & 4 & 6 & \cdots & 2n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ m & 2m & 3m & \cdots & mn  \end{bmatrix}`$.

5. **Ranges**:
   Used to describe ranges or intervals:
   
   $`x \in [0, \dots, 10] \quad \text{represents } x \in \{0, 1, 2, \dots, 10\}`$.


6. **Set Representation**:
   When describing infinite or large sets:
   
   $`\{2, 4, 6, ..., 2n, ...\} \quad \text{represents all even integers}`$.

---

### **Formal Examples**

1. **Arithmetic Progression**:
   A finite sequence:
   
   $`\{3, 6, 9, ..., 30\} \quad \text{means } a_n = 3n, \, n \in \{1, 2, ..., 10\}`$.


2. **Geometric Progression**:
   An infinite sequence:
   
   $`\{1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, ...\} \quad \text{means } a_n = \frac{1}{2^{n-1}}, \, n \in \mathbb{N}`$.


3. **Ellipses in Text**:
   In descriptive text:
   
   $`\text{"The sequence continues as } 1, 2, 4, 8, 16, \dots \text{."}`$


---

### **Guidelines for Using Ellipses**

1. **Clarity**:
   Ensure the pattern is unambiguous. For example:
   
   $`\{1, 3, 5, \dots, 99\} \quad \text{is understood as all odd numbers up to 99}`$.


2. **Explicit Starting and Ending Terms**:
   If the sequence is finite, state the first and last terms to avoid confusion:
   
   $`\{2, 4, 6, ..., 20\}`$.


3. **Symbolic Explanation**:
   When necessary, define the sequence rule explicitly:
   
   $`a_n = n^2, \quad n = 1, 2, 3, \dots`$.


---

### **Common Notation Variants**

- $`\cdots`$: Indicates terms within one line (e.g., $`1 + 2 + 3 + \cdots + 100`$).
- $`\vdots`$: Vertical continuation in matrices or lists.
- $`\ddots`$: Diagonal continuation in matrices.

---

### **Applications**

1. **Mathematics**:
   - Compact representation in sequences, series, and sets.
   - Examples: Arithmetic/geometric sequences, factorial notation, polynomial expansions.

2. **Computer Science**:
   - Used in algorithms to represent repetitive steps.

3. **Physics**:
   - To describe periodic or infinite processes.

4. **Textual Representation**:
   - To indicate omitted details or parts of a list.

Ellipsis notation simplifies complex expressions, making mathematical and textual content more concise and readable.



## **The Arithmetic of Functions**

The arithmetic of functions refers to the operations that can be performed on functions, such as addition, 
subtraction, multiplication, division, and composition. These operations combine two or more functions to 
produce a new function.

---

### **Basic Operations**

Let $f(x)$ and $g(x)$ be two functions. The following operations can be defined:

1. **Addition**:
   
   $`(f + g)(x) = f(x) + g(x)`$

   The value of the new function at $x$ is the sum of the values of $`f(x)`$ and $`g(x)`$.

2. **Subtraction**:
   
   $`(f - g)(x) = f(x) - g(x)`$

   The value of the new function at $x$ is the difference between $`f(x)`$ and $`g(x)`$.

3. **Multiplication**:
   
   $`(f \cdot g)(x) = f(x) \cdot g(x)`$

   The value of the new function at $x$ is the product of $f(x)$ and $g(x)$.

4. **Division**:
   
   $`\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}, \quad \text{where } g(x) \neq 0`$.

   The value of the new function at $x$ is the quotient of $`f(x)`$ and $`g(x)`$.

---

### **Composition of Functions**

The **composition** of two functions $f(x)$ and $g(x)$ is a new function defined as:

$`(f \circ g)(x) = f(g(x))`$.

Here, the output of $`g(x)`$ becomes the input of $f(x)$.

- Example:
  If $`f(x) = x^2`$ and $`g(x) = x + 1`$, then:
  
  $`(f \circ g)(x) = f(g(x)) = f(x + 1) = (x + 1)^2`$.

---

### **Domain Considerations**

1. **Addition, Subtraction, Multiplication**:
   The domain of $f + g$, $f - g$, and $`f \cdot g`$ is the intersection of the domains of $f(x)$ and $g(x)$.

2. **Division**:
   The domain of $f / g$ is the intersection of the domains of $f(x)$ and $g(x)$, excluding points where$`g(x) = 0`$.

3. **Composition**:
   The domain of $`f \circ g`$ is all $x$ in the domain of $`g(x)`$ such that $`g(x)`$ is in the domain of $`f(x)`$.

---

### **Examples**

1. **Addition**:
   Let $`f(x) = x^2`$ and $`g(x) = 2x + 3`$:
   
   $`(f + g)(x) = x^2 + (2x + 3) = x^2 + 2x + 3`$.


2. **Subtraction**:
   
   $`(f - g)(x) = x^2 - (2x + 3) = x^2 - 2x - 3`$.


3. **Multiplication**:
   
   $`(f \cdot g)(x) = (x^2)(2x + 3) = 2x^3 + 3x^2`$.


4. **Division**:
   
   $`\left(\frac{f}{g}\right)(x) = \frac{x^2}{2x + 3}, \quad g(x) \neq -\frac{3}{2}`$.


5. **Composition**:
   Using the same $f(x)$ and $g(x)$:
   
   $`(f \circ g)(x) = f(g(x)) = f(2x + 3) = (2x + 3)^2`$.

---

### **Inverse Operations**

1. The **inverse** of a function $f(x)$, denoted $`f^{-1}(x)`$, "undoes" the operation of $f(x)$, such that:
   
   $`f(f^{-1}(x)) = x \quad \text{and} \quad f^{-1}(f(x)) = x`$.


2. A function must be **bijective** (one-to-one and onto) to have an inverse.

---

### **Applications**

1. **Modeling Relationships**:
   - Function arithmetic is used in combining and modifying mathematical models.
   
2. **Physics and Engineering**:
   - Combining wave functions or signal processing often requires addition or multiplication of functions.

3. **Data Analysis**:
   - Functions represent transformations in data pipelines.

---

Function arithmetic allows for the creation of new functions by combining existing ones, facilitating 
more complex mathematical modeling and problem-solving.



## **Probability from Experimental Data**

Experimental probability is the likelihood of an event occurring based on actual experimental outcomes, 
as opposed to theoretical probability, which is calculated based on assumptions or known conditions. 
Experimental probability uses observed data to estimate probabilities.

---

### **Formula for Experimental Probability**

The probability of an event $E$ is calculated as:

$`P(E) = \frac{\text{Number of times event } E \text{ occurs}}{\text{Total number of trials}}`$.


---

### **Steps to Calculate**

1. **Conduct an Experiment**:
   Perform a series of trials (e.g., rolling a die, flipping a coin, or observing outcomes in real-world data).

2. **Record Outcomes**:
   Track the frequency of each outcome or event.

3. **Calculate the Probability**:
   Divide the number of times the event occurred by the total number of trials.

---

### **Examples**

1. **Coin Flip**:
   - Experiment: Flip a coin 100 times.
   - Results: Heads appears 56 times.
   - Probability of getting heads:
     
     $`P(\text{Heads}) = \frac{56}{100} = 0.56`$.


2. **Rolling a Die**:
   - Experiment: Roll a six-sided die 60 times.
   - Results: The number $4$ appears 12 times.
   - Probability of rolling a $4$:
     
     $`P(\text{4}) = \frac{12}{60} = 0.2`$.


3. **Real-World Scenario**:
   - Experiment: Out of 500 cars passing a toll gate, 150 are red.
   - Probability of a red car passing:
     
     $`P(\text{Red Car}) = \frac{150}{500} = 0.3`$.

---

### **Comparison with Theoretical Probability**

- **Theoretical Probability**:
  Based on expected outcomes:
  
  $`P(E) = \frac{\text{Favorable outcomes}}{\text{Total possible outcomes}}`$.

  Example: Probability of rolling a $4$ on a six-sided die:
  
  $`P(\text{4}) = \frac{1}{6} \approx 0.1667`$.

- **Experimental Probability**:
  Based on actual results from trials.

---

### **Key Concepts**

1. **Law of Large Numbers**:
   As the number of trials increases, the experimental probability tends to approach the theoretical probability.

2. **Relative Frequency**:
   Experimental probability is also called relative frequency because it represents the proportion of times an event occurs.

3. **Cumulative Probability**:
   By accumulating data over multiple experiments, probabilities become more reliable.

---

### **Applications**

1. **Data-Driven Decision Making**:
   Used in fields like finance, healthcare, and marketing to estimate probabilities based on historical data.

2. **Quality Control**:
   Determines the probability of defects in manufacturing.

3. **Simulations**:
   Experimental probability is fundamental in Monte Carlo simulations for approximating complex probabilities.

---

### **Limitations**

- Experimental probability depends on the quality and quantity of data.
- Results can be biased if the experiment or sample size is not representative.
- Random variations might cause discrepancies in small samples.

Experimental probability bridges theoretical concepts with real-world data, making it a practical 
approach to understanding and predicting outcomes.




## **Exponential to Logarithmic Form**

Converting between exponential and logarithmic forms is a key skill in mathematics. 
These two forms express the same relationship between numbers in different ways.

---

### **Definition**

1. **Exponential Form**:
   
   $`a^b = c`$

   Here:
   - $a$ is the base,
   - $b$ is the exponent,
   - $c$ is the result.

2. **Logarithmic Form**:
   
   $`\log_a(c) = b`$

   This means $b$ is the power to which $a$ must be raised to get $c$.

---

### **Conversion**

To convert:
- From **exponential to logarithmic form**:
  
  $`a^b = c \quad \longrightarrow \quad \log_a(c) = b`$


- From **logarithmic to exponential form**:
  
  $`\log_a(c) = b \quad \longrightarrow \quad a^b = c`$

---

### **Examples**

1. **Exponential to Logarithmic**:
   - Given $2^3 = 8$,
     
     $`\log_2(8) = 3`$.

2. **Logarithmic to Exponential**:
   - Given $`\log_5(125) = 3`$,
     
     $`5^3 = 125`$.

---

### **Key Properties**

1. **Logarithms Undo Exponentials**:
   - $`a^{\log_a(c)} = c`$.
   - $`\log_a(a^b) = b`$.

2. **Natural Logarithms** (\(\ln\)):
   - Base $e$: $`\ln(x) = \log_e(x)`$.

3. **Common Logarithms** (\(\log\)):
   - Base $10$: $`\log(x) = \log_{10}(x)`$.

---

### **Applications**

1. **Solving Equations**:
   Exponentials are converted to logarithms to solve for the unknown:
   
   $`3^x = 81 \quad \longrightarrow \quad \log_3(81) = x \quad \implies x = 4`$.

2. **Data Modeling**:
   Logarithmic scales are used for exponential growth/decay, e.g., in population growth and radioactive decay.

3. **Engineering and Science**:
   Used in decibel scales, pH calculations, and more.

---

### **Summary Table**

| Exponential Form        | Logarithmic Form       |
|--------------------------|------------------------|
| \(a^b = c\)             | \(\log_a(c) = b\)     |
| \(2^3 = 8\)             | \(\log_2(8) = 3\)     |
| \(10^4 = 10000\)        | \(\log_{10}(10000) = 4\) |

The conversion between these forms simplifies calculations and aids in understanding exponential and logarithmic relationships.



## **Perfect Squares**

A **perfect square** is an integer that is the square of another integer. 
In mathematical terms, a number $n$ is a perfect square if there exists an integer $m$ such that:

$`n = m^2`$

For example:
- $1 = 1^2$
- $4 = 2^2$
- $9 = 3^2$
- $16 = 4^2$, and so on.

---

### **Properties of Perfect Squares**

1. **Non-Negativity**:
   - A perfect square is always non-negative because $`m^2 \geq 0`$ for any integer $m$.

2. **Odd and Even**:
   - The square of an even number is even.
   - The square of an odd number is odd.

3. **Ending Digits**:
   - In base 10, a perfect square can only end with $0, 1, 4, 5, 6,$ or $9$. It cannot end with $2, 3, 7,$ or $8$.

4. **Difference Between Consecutive Squares**:
   - The difference between the squares of two consecutive integers $m$ and $m+1$ is:
     
     $`(m+1)^2 - m^2 = 2m + 1`$.
     This is always odd.

5. **Prime Factorization**:
   - In the prime factorization of a perfect square, all exponents must be even.

---

### **Examples of Perfect Squares**

1. **Small Perfect Squares**:
   
   $`0^2 = 0, \quad 1^2 = 1, \quad 2^2 = 4, \quad 3^2 = 9, \quad 4^2 = 16, \quad \dots`$


2. **Larger Perfect Squares**:
   
   $`10^2 = 100, \quad 15^2 = 225, \quad 20^2 = 400, \quad 50^2 = 2500, \quad \dots`$


---

### **Identifying Perfect Squares**

To check if a number is a perfect square:
1. **Square Root Method**:
   - Take the square root and see if it is an integer.
   - Example: $`\sqrt{49} = 7`$, so $49$ is a perfect square.

2. **Prime Factorization**:
   - Check if all the exponents in the prime factorization are even.
   - Example: $`144 = 2^4 \cdot 3^2`$ (all exponents are even), so $144$ is a perfect square.

---

### **Applications of Perfect Squares**

1. **Geometry**:
   - Perfect squares represent the area of a square with integer side lengths.

2. **Pythagorean Triples**:
   - Perfect squares are involved in right triangles where $`a^2 + b^2 = c^2`$.

3. **Algebra**:
   - Perfect square trinomials: $`(a + b)^2 = a^2 + 2ab + b^2`$.

4. **Number Theory**:
   - Used in modular arithmetic, cryptography, and integer factorization problems.

---

### **Interesting Facts**

1. The sum of the first $n$ perfect squares is given by:
   
   $`S = \frac{n(n+1)(2n+1)}{6}`$.

   Example: The sum of the first 3 perfect squares is:
   
   $`1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14`$.


2. There are infinitely many perfect squares.

3. The square of any number is either $0$ or $`1 \mod 4`$.

---

Perfect squares are fundamental in mathematics, bridging algebra, geometry, and number theory.


## **The Cyclic Property of the Imaginary Unit**

The **imaginary unit** $i$ is defined as:

$`i = \sqrt{-1}`$.

A key property of $i$ is its **cyclic behavior** under repeated powers. 
Specifically, the powers of $i$ cycle through four distinct values:


$`i^1 = i, \quad i^2 = -1, \quad i^3 = -i, \quad i^4 = 1`$.

This cycle then repeats indefinitely:

$`i^5 = i, \quad i^6 = -1, \quad i^7 = -i, \quad i^8 = 1, \quad \dots`$

---

### **General Formula**

For any integer $n$, the value of $i^n$ depends on the remainder of $n$ when divided by 4 $`( n \mod 4 )`$:

$`i^n = \begin{cases} 1 & \text{if } n \mod 4 = 0, \\ i & \text{if } n \mod 4 = 1, \\ -1 & \text{if } n \mod 4 = 2, \\ -i & \text{if } n \mod 4 = 3.  \end{cases}`$

---

### **Explanation**

This cyclic behavior arises because $`i^4 = 1`$, so any higher power of $i$ can be written as:

$`i^n = (i^4)^k \cdot i^r`$,

where $k$ is the integer quotient of $`n \div 4`$, and $r$ is the remainder $`( r = n \mod 4 )`$.

- $`(i^4)^k = 1^k = 1`$,
- Thus, $`i^n = i^r`$, where $r$ determines the result as per the cycle.

---

### **Examples**

1. **Find $i^{10}$:**
   
   $`10 \mod 4 = 2, \quad \text{so } i^{10} = i^2 = -1`$.


2. **Find $i^{23}$:**
   
   $`23 \mod 4 = 3, \quad \text{so } i^{23} = i^3 = -i`$.


3. **Find $`i^{50}`$:**
   
   $`50 \mod 4 = 2, \quad \text{so } i^{50} = i^2 = -1`$.

---

### **Applications**

1. **Complex Numbers**:
   - Used in expressing roots of negative numbers, e.g., $\sqrt{-4} = 2i$.
   
2. **Euler's Formula**:
   - The cyclic behavior of $i$ is tied to $`e^{i\theta} = \cos\theta + i\sin\theta`$, which forms the foundation of complex exponential functions.

3. **Signal Processing**:
   - Imaginary numbers and their cyclic properties are critical in Fourier transforms and other periodic systems.

4. **Simplifying Powers**:
   - This property helps simplify powers of $i$ in algebraic and engineering problems.

The cyclic property of $i$ is fundamental in understanding and working with complex numbers.




## **The Distance Formula in Cartesian Coordinates**

The **distance formula** calculates the straight-line (Euclidean) distance between two points 
$(x_1, y_1)$ and $(x_2, y_2)$ in a 2D Cartesian plane. It is derived from the **Pythagorean theorem**.

---

### **Formula**


$`d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}`$

---

### **Derivation**

1. Consider two points $A(x_1, y_1)$ and $B(x_2, y_2)$.
2. Plot these points in a Cartesian plane and draw a right triangle where:
   - The horizontal side has a length $|x_2 - x_1|$,
   - The vertical side has a length $|y_2 - y_1|$.
3. By the **Pythagorean theorem**:
   
   $`\text{Hypotenuse}^2 = (\text{Horizontal side})^2 + (\text{Vertical side})^2`$

   Substituting the lengths:
   
   $`d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2`$

4. Taking the square root gives:
   
   $`d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}`$.

---

### **Example**

Find the distance between $A(3, 4)$ and $B(7, 1)$:

1. Use the formula:
   
   $`d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}`$

2. Substitute the values:
   
   $`d = \sqrt{(7 - 3)^2 + (1 - 4)^2}`$

   
   $`d = \sqrt{4^2 + (-3)^2}`$

   
   $`d = \sqrt{16 + 9} = \sqrt{25} = 5`$.


The distance is $5$ units.

---

### **In 3D Space**

For points $(x_1, y_1, z_1)$  and $(x_2, y_2, z_2)$ in three dimensions, the distance formula extends to:


$`d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}`$.

---

### **Applications**

1. **Geometry**: Measuring distances between points in a plane or space.
2. **Physics**: Calculating displacement in coordinate systems.
3. **Computer Graphics**: Determining pixel distances or collision detection.
4. **Machine Learning**: Used in clustering algorithms (e.g., K-means) and distance-based metrics.

The distance formula is a fundamental tool for solving problems involving distances in both 2D and 3D spaces.



## **Finite Limit of a Function**

The finite limit of a function describes the behavior of a function $f(x)$ as the input $x$ approaches a 
specific value $c$. It determines the value the function approaches, if any, as $x$ gets arbitrarily close to $c$, but not necessarily at $c$.

---

### **Definition**

For a function $f(x)$, the **finite limit** as $x$ approaches $c$ is $L$ if, for every small positive number $`\epsilon > 0`$, 
there exists a $`\delta > 0`$  such that:


$`0 < |x - c| < \delta \implies |f(x) - L| < \epsilon`$.

In simpler terms:
- As $x$ gets closer to $c$, $f(x)$ gets arbitrarily close to $L$.

We write this as:

$`\lim_{x \to c} f(x) = L`$.

---

### **Graphical Intuition**

- On a graph, the limit corresponds to the $y$-value $f(x)$ approaches as $x$ nears $c$, 
regardless of whether $f(x)$ is actually defined at $c$.

---

### **Example**

Find $`\lim_{x \to 2} (3x + 1)`$:

1. Substitute $x \to 2$:
   
   $`f(x) = 3(2) + 1 = 7`$.

2. Conclusion:
   
   $`\lim_{x \to 2} (3x + 1) = 7`$.

---

### **Key Properties of Limits**

1. **Uniqueness**:
   The limit, if it exists, is unique.

2. **Sum/Difference Rule**:
   
   $`\lim_{x \to c} [f(x) \pm g(x)] = \lim_{x \to c} f(x) \pm \lim_{x \to c} g(x)`$.


3. **Product Rule**:
   
   $`\lim_{x \to c} [f(x) \cdot g(x)] = \lim_{x \to c} f(x) \cdot \lim_{x \to c} g(x)`$.

4. **Quotient Rule**:
   
   $`\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\lim_{x \to c} f(x)}{\lim_{x \to c} g(x)}, \quad g(x) \neq 0`$.

---

### **Special Case: One-Sided Limits**

The limit as $x$ approaches $c$ from the left $`( x \to c^- )`$ or the right $`( x \to c^+ )`$ may differ:
- **Left-hand limit**:
  
  $`\lim_{x \to c^-} f(x)`$

- **Right-hand limit**:
  
  $`\lim_{x \to c^+} f(x)`$

The limit $`\lim_{x \to c} f(x)`$ exists only if:

$`\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x)`$.

---

### **Applications**

1. **Calculus**: Limits are foundational to defining derivatives and integrals.
2. **Continuity**: A function is continuous at $c$ if:
   
   $`\lim_{x \to c} f(x) = f(c)`$.

3. **Physics**: Modeling instantaneous rates of change (e.g., velocity).

The concept of finite limits allows for the precise analysis of function behavior near specific points.



## **Graphs of General Quadratic Functions**

A general quadratic function is expressed as:


$`f(x) = ax^2 + bx + c`$

where $a$, $b$, and $c$ are constants, and $a \neq 0$.

The graph of a quadratic function is a **parabola**, which can either open upwards or downwards depending on the sign of $a$.

---


### **Key Features of Quadratic Graphs**

1. **Direction of Opening**:
   - If $a > 0$, the parabola opens **upward**.
   - If $a < 0$, the parabola opens **downward**.

2. **Vertex**:
   - The vertex is the highest or lowest point of the parabola (depending on its direction).
   - The x-coordinate of the vertex is:
     
     $`x_v = -\frac{b}{2a}`$
   
   - The y-coordinate is found by substituting $x_v$ into $f(x)$:
     
     $`y_v = f\left(-\frac{b}{2a}\right)`$
   
   - The vertex is $`\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)`$.

3. **Axis of Symmetry**:
   - The parabola is symmetric about the vertical line passing through the vertex:
     
     $`x = -\frac{b}{2a}`$

4. **Y-Intercept**:
   - The y-intercept occurs where $x = 0$:
     
     $`f(0) = c`$
   
   - The point is $(0, c)$.

5. **X-Intercepts**:
   - Found by solving $`ax^2 + bx + c = 0`$ using the quadratic formula:
     
     $`x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}`$
   
   - The discriminant $`\Delta = b^2 - 4ac`$ determines the number of x-intercepts:
     - $\Delta > 0$: Two distinct real roots.
     - $\Delta = 0$: One real root (the vertex lies on the x-axis).
     - $\Delta < 0$: No real roots (the parabola does not cross the x-axis).

---

### **Graph Shape and Behavior**

1. **Width of the Parabola**:
   - The value of $|a|$ determines how "wide" or "narrow" the parabola is:
     - Larger $|a|$: Narrower parabola.
     - Smaller $|a|$: Wider parabola.

2. **End Behavior**:
   - As $`x \to \pm\infty`$:
     - If $`a > 0`$, $`f(x) \to +\infty`$.
     - If $`a < 0`$, $`f(x) \to -\infty`$.

---

### **Example: Graphing**

Graph $`f(x) = 2x^2 - 4x + 1`$.

1. **Direction of Opening**:
   - $a = 2 > 0$: Parabola opens upward.

2. **Vertex**:
   - $`x_v = -\frac{-4}{2(2)} = 1`$.
   - $`y_v = f(1) = 2(1)^2 - 4(1) + 1 = -1`$.
   - Vertex: $(1, -1)$.

3. **Axis of Symmetry**:
   - $x = 1$.

4. **Y-Intercept**:
   - $`f(0) = 2(0)^2 - 4(0) + 1 = 1`$.
   - Y-intercept: $(0, 1)$.

5. **X-Intercepts**:
   - Solve $`2x^2 - 4x + 1 = 0`$ using the quadratic formula:
     
     $`x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(2)(1)}}{2(2)} = \frac{4 \pm \sqrt{8}}{4} = \frac{4 \pm 2\sqrt{2}}{4} = 1 \pm \frac{\sqrt{2}}{2}`$.
   
   - X-intercepts: $`x = 1 \pm \frac{\sqrt{2}}{2}`$.

---

### **Applications**

1. **Optimization**: Finding maximum or minimum values (at the vertex).
2. **Physics**: Modeling projectile motion (parabolas describe trajectories).
3. **Economics**: Representing quadratic cost or revenue functions.

The graph of a quadratic function provides insights into its behavior and key properties like symmetry, intercepts, and extreme points.




## **Quadratic Equations with Purely Imaginary Solutions**

A quadratic equation has **purely imaginary solutions** when its roots involve only imaginary numbers (no real part). 
For this to occur, the **discriminant** of the quadratic equation must be negative, and the constant term or coefficient 
must allow for the imaginary square root to result in purely imaginary values.

---

### **Form of Quadratic Equations**
The standard form of a quadratic equation is:


$`ax^2 + bx + c = 0`$,

where $a, b, c$ are real constants, and  $`a \neq 0`$.

---

### **Condition for Purely Imaginary Solutions**

1. **Discriminant**:
   The discriminant of the quadratic equation is:
   
   $`\Delta = b^2 - 4ac`$.

   For the roots to be purely imaginary, $`\Delta < 0`$ because this results in the square root of a negative number.

2. **Root Formula**:
   Using the quadratic formula:
   
   $`x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}`$,

   when $\Delta < 0$, the square root produces an imaginary number, leading to complex roots:
   
   $`x = \frac{-b}{2a} \pm i \frac{\sqrt{|b^2 - 4ac|}}{2a}`$.

   For purely imaginary roots, the real part $`-\frac{b}{2a}`$ must equal zero, which occurs when $`b = 0`$.

---

### **Simplified Case: Purely Imaginary Roots**

If $b = 0$, the quadratic equation simplifies to:


$`ax^2 + c = 0`$,


or:


$`x^2 = -\frac{c}{a}`$.

If $`\frac{c}{a} > 0`$, the roots are:


$`x = \pm i \sqrt{\frac{c}{a}}`$.

These roots are purely imaginary because they are multiples of $i$, the imaginary unit.

---

### **Example**

Solve $2x^2 + 8 = 0$.

1. Rewrite the equation:
   
   $`x^2 = -\frac{8}{2} = -4`$.


2. Take the square root of both sides:
   
   $`x = \pm i \sqrt{4} = \pm 2i`$.

The roots are purely imaginary: $`x = 2i`$  and  $`x = -2i`$.

---

### **Graphical Interpretation**

- The parabola represented by $`ax^2 + bx + c = 0`$ does not intersect the x-axis if the roots are purely imaginary.
- It lies entirely above or below the x-axis, depending on the sign of $a$.

---

### **Applications**

1. **Electrical Engineering**: Imaginary numbers are critical in AC circuit analysis.
2. **Quantum Physics**: Complex solutions often describe wavefunctions.
3. **Control Systems**: Poles of systems can have imaginary components to describe oscillatory behavior.

Quadratic equations with purely imaginary solutions highlight cases where real-world systems require imaginary components to model behavior effectively.



## **Compound Events in Probability Using Experimental Data**

In probability, a **compound event** is an event that combines two or more simple events. When dealing with experimental data, 
probabilities are calculated based on the outcomes observed during experiments rather than theoretical assumptions.

---

### **Key Concepts**
1. **Simple Event**: A single outcome from a probability experiment (e.g., rolling a die and getting a "4").
2. **Compound Event**: Combines two or more simple events using the terms **"and"** or **"or"**:
   - **"And"**: Both events must occur.
   - **"Or"**: At least one of the events must occur.

The probability of a compound event is calculated from the frequency of occurrences in the experimental data.

---

### **Steps to Solve Compound Event Problems**

1. **Perform the Experiment**: Collect data on all possible outcomes of the events.

2. **Identify the Compound Event**: Define which combinations of simple events you are analyzing.

3. **Calculate Probabilities**:
   - **Experimental Probability Formula**:
     \[
     P(\text{Event}) = \frac{\text{Number of times the event occurred}}{\text{Total number of trials}}
     \]

4. **Combine Probabilities Based on the Event Type**:
   - **"And"** (Intersection):
     For events \( A \) and \( B \), calculate \( P(A \cap B) \) as the frequency where both \( A \) and \( B \) occur.
   - **"Or"** (Union):
     For events \( A \) and \( B \), calculate \( P(A \cup B) \) using:
     \[
     P(A \cup B) = P(A) + P(B) - P(A \cap B)
     \]

---

### **Example Problem**

An experiment involves flipping a coin and rolling a die 100 times. The results are recorded as follows:
- The coin lands heads 60 times.
- The die rolls an even number 40 times.
- Both heads and an even number occur 25 times.

#### Find:
1. The probability of flipping heads or rolling an even number.
2. The probability of flipping heads and rolling an even number.

---

### **Solution**

1. **Probability of Flipping Heads**:
   \[
   P(\text{Heads}) = \frac{\text{Number of heads outcomes}}{\text{Total trials}} = \frac{60}{100} = 0.6.
   \]

2. **Probability of Rolling an Even Number**:
   \[
   P(\text{Even Number}) = \frac{\text{Number of even outcomes}}{\text{Total trials}} = \frac{40}{100} = 0.4.
   \]

3. **Probability of Both Heads and Even Number**:
   \[
   P(\text{Heads} \cap \text{Even Number}) = \frac{\text{Number of times both occur}}{\text{Total trials}} = \frac{25}{100} = 0.25.
   \]

4. **Probability of Heads or Even Number**:
   Using the union formula:
   \[
   P(\text{Heads} \cup \text{Even Number}) = P(\text{Heads}) + P(\text{Even Number}) - P(\text{Heads} \cap \text{Even Number}).
   \]
   Substitute the values:
   \[
   P(\text{Heads} \cup \text{Even Number}) = 0.6 + 0.4 - 0.25 = 0.75.
   \]

---

### **Final Results**
1. The probability of flipping heads or rolling an even number is:
   \[
   P(\text{Heads} \cup \text{Even Number}) = 0.75.
   \]

2. The probability of flipping heads and rolling an even number is:
   \[
   P(\text{Heads} \cap \text{Even Number}) = 0.25.
   \]

---

### **Applications**
- Analyzing outcomes in games or experiments.
- Estimating probabilities in real-world scenarios (e.g., surveys, sports, and weather forecasting).



## **Axis of Symmetry of a Parabola**

The **axis of symmetry** of a parabola is a vertical line that divides the parabola into two symmetrical halves. This line always passes through the **vertex** of the parabola.

---

### **Equation of the Axis of Symmetry**
For a quadratic equation in standard form:
\[
y = ax^2 + bx + c,
\]
the axis of symmetry is given by:
\[
x = -\frac{b}{2a}.
\]

This formula gives the \(x\)-coordinate of the vertex, which is also the axis of symmetry for the parabola.

---

### **Steps to Find the Axis of Symmetry**
1. Identify the coefficients \(a\) and \(b\) from the quadratic equation.
2. Substitute these values into the formula:
   \[
   x = -\frac{b}{2a}.
   \]

---

### **Examples**

#### Example 1:
Find the axis of symmetry for the parabola:
\[
y = 2x^2 + 4x + 1.
\]

**Solution**:
1. Identify \(a = 2\) and \(b = 4\).
2. Substitute into the formula:
   \[
   x = -\frac{4}{2(2)} = -\frac{4}{4} = -1.
   \]

**Axis of Symmetry**:
\[
x = -1.
\]

---

#### Example 2:
Find the axis of symmetry for:
\[
y = -3x^2 + 6x - 5.
\]

**Solution**:
1. Identify \(a = -3\) and \(b = 6\).
2. Substitute into the formula:
   \[
   x = -\frac{6}{2(-3)} = -\frac{6}{-6} = 1.
   \]

**Axis of Symmetry**:
\[
x = 1.
\]

---

### **Vertex Form of a Parabola**
If the quadratic equation is in **vertex form**:
\[
y = a(x-h)^2 + k,
\]
the axis of symmetry is:
\[
x = h,
\]
where \((h, k)\) is the vertex of the parabola.

---

### **Applications**
1. Identifying the maximum or minimum value of a parabola.
2. Solving optimization problems in physics, engineering, and economics.
3. Graphing quadratic functions accurately. 



## **Understanding Radians of a Circle**

A **radian** is a unit of angular measure based on the radius of a circle. It is used to measure angles in mathematics and physics.

---

### **Definition of a Radian**
One radian is the angle subtended at the center of a circle by an arc that is equal in length to the radius of the circle.

---

### **Relationship Between Radians and Degrees**
The full circumference of a circle is \( 2\pi \) times the radius. In terms of angles:
- A full circle measures \( 360^\circ \) in degrees.
- A full circle measures \( 2\pi \) radians.

Thus, the conversion between radians and degrees is:
\[
1 \text{ radian} = \frac{180^\circ}{\pi} \quad \text{or} \quad 1^\circ = \frac{\pi}{180} \text{ radians}.
\]

---

### **Key Radian Measures**
For a circle, the following common angles in degrees and radians are important:

| Degrees (\(^\circ\)) | Radians (\(\text{rad}\)) |
|-----------------------|-------------------------|
| \( 0^\circ \)         | \( 0 \)                |
| \( 30^\circ \)        | \( \frac{\pi}{6} \)    |
| \( 45^\circ \)        | \( \frac{\pi}{4} \)    |
| \( 60^\circ \)        | \( \frac{\pi}{3} \)    |
| \( 90^\circ \)        | \( \frac{\pi}{2} \)    |
| \( 180^\circ \)       | \( \pi \)              |
| \( 270^\circ \)       | \( \frac{3\pi}{2} \)   |
| \( 360^\circ \)       | \( 2\pi \)             |

---

### **Converting Between Degrees and Radians**

#### Example 1: Convert \( 90^\circ \) to radians
Using the formula:
\[
\text{Radians} = \text{Degrees} \times \frac{\pi}{180},
\]
\[
90^\circ \times \frac{\pi}{180} = \frac{\pi}{2}.
\]

#### Example 2: Convert \( \frac{\pi}{3} \) radians to degrees
Using the formula:
\[
\text{Degrees} = \text{Radians} \times \frac{180}{\pi},
\]
\[
\frac{\pi}{3} \times \frac{180}{\pi} = 60^\circ.
\]

---

### **Applications of Radians**
1. **Trigonometry**: Angles in the unit circle and trigonometric functions are often expressed in radians.
2. **Physics**: Angular velocity and rotational motion are measured in radians per second.
3. **Calculus**: Many formulas in calculus, such as derivatives and integrals of trigonometric functions, assume angles are measured in radians.



## **Understanding Factorials**

The **factorial** of a non-negative integer \(n\), denoted as \(n!\), is the product of all positive integers from \(1\) to \(n\). It is defined as:
\[
n! = n \times (n-1) \times (n-2) \times \cdots \times 1, \quad \text{for } n \geq 1,
\]
with a special case:
\[
0! = 1.
\]

---

### **Examples**

1. **Calculate \(5!\):**
   \[
   5! = 5 \times 4 \times 3 \times 2 \times 1 = 120.
   \]

2. **Calculate \(0!\):**
   By definition:
   \[
   0! = 1.
   \]

3. **Calculate \(7!\):**
   \[
   7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5040.
   \]

---

### **Properties of Factorials**

1. **Recursive Property**:
   \[
   n! = n \times (n-1)!
   \]
   Example:
   \[
   5! = 5 \times 4!.
   \]

2. **Growth**:
   Factorials grow very rapidly with \(n\). For example:
   \[
   10! = 3,628,800 \quad \text{and} \quad 20! = 2,432,902,008,176,640,000.
   \]

3. **Division of Factorials**:
   When dividing factorials, many terms cancel out. For example:
   \[
   \frac{6!}{4!} = \frac{6 \times 5 \times 4!}{4!} = 6 \times 5 = 30.
   \]

---

### **Applications of Factorials**

1. **Combinatorics**: 
   - Counting permutations:
     \[
     P(n, r) = \frac{n!}{(n-r)!}.
     \]
   - Counting combinations:
     \[
     C(n, r) = \frac{n!}{r!(n-r)!}.
     \]

2. **Mathematics**:
   - Factorials appear in series expansions, such as the Taylor series:
     \[
     e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}.
     \]

3. **Probability**:
   - Used in probability distributions like the binomial and Poisson distributions.

4. **Computer Science**:
   - Algorithms for combinatorial problems often rely on factorials.



## 







































































































































































































































































































































