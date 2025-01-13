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

2. **Natural Logarithms** $(\ln)$:
   - Base $e$: $`\ln(x) = \log_e(x)`$.

3. **Common Logarithms** $(\log)$:
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

| Exponential Form | Logarithmic Form         |
|------------------|--------------------------|
| $a^b = c$        | $`\log_a(c) = b`$        |
| $2^3 = 8$        | $`\log_2(8) = 3`$        |
| $10^4 = 10000$   | $`\log_{10}(10000) = 4`$ |

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
     
     $`P(\text{Event}) = \frac{\text{Number of times the event occurred}}{\text{Total number of trials}}`$
   

4. **Combine Probabilities Based on the Event Type**:
   - **"And"** (Intersection):
     For events $A$ and $B$, calculate $`P(A \cap B)`$ as the frequency where both $A$ and $B$ occur.
   - **"Or"** (Union):
     For events $A$ and $B$, calculate $`P(A \cup B)`$ using:
     
     $`P(A \cup B) = P(A) + P(B) - P(A \cap B)`$

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
   
   $`P(\text{Heads}) = \frac{\text{Number of heads outcomes}}{\text{Total trials}} = \frac{60}{100} = 0.6`$.


2. **Probability of Rolling an Even Number**:
   
   $`P(\text{Even Number}) = \frac{\text{Number of even outcomes}}{\text{Total trials}} = \frac{40}{100} = 0.4`$.


3. **Probability of Both Heads and Even Number**:
   
   $`P(\text{Heads} \cap \text{Even Number}) = \frac{\text{Number of times both occur}}{\text{Total trials}} = \frac{25}{100} = 0.25`$.


4. **Probability of Heads or Even Number**:
   Using the union formula:
   
   $`P(\text{Heads} \cup \text{Even Number}) = P(\text{Heads}) + P(\text{Even Number}) - P(\text{Heads} \cap \text{Even Number})`$.
   
   Substitute the values:
   
   $`P(\text{Heads} \cup \text{Even Number}) = 0.6 + 0.4 - 0.25 = 0.75$.

---

### **Final Results**
1. The probability of flipping heads or rolling an even number is:
   
   $`P(\text{Heads} \cup \text{Even Number}) = 0.75`$.


2. The probability of flipping heads and rolling an even number is:
   
   $`P(\text{Heads} \cap \text{Even Number}) = 0.25`$.

---

### **Applications**
- Analyzing outcomes in games or experiments.
- Estimating probabilities in real-world scenarios (e.g., surveys, sports, and weather forecasting).



## **Axis of Symmetry of a Parabola**

The **axis of symmetry** of a parabola is a vertical line that divides the parabola into two symmetrical halves. 
This line always passes through the **vertex** of the parabola.

---

### **Equation of the Axis of Symmetry**
For a quadratic equation in standard form:

$`y = ax^2 + bx + c`$,

the axis of symmetry is given by:

$`x = -\frac{b}{2a}`$.

This formula gives the $x$-coordinate of the vertex, which is also the axis of symmetry for the parabola.

---

### **Steps to Find the Axis of Symmetry**
1. Identify the coefficients $a$ and $b$ from the quadratic equation.
2. Substitute these values into the formula:
   
   $`x = -\frac{b}{2a}`$.


---

### **Examples**

#### Example 1:
Find the axis of symmetry for the parabola:

$`y = 2x^2 + 4x + 1`$.


**Solution**:
1. Identify $a = 2$ and $b = 4$.
2. Substitute into the formula:
   
   $`x = -\frac{4}{2(2)} = -\frac{4}{4} = -1`$.


**Axis of Symmetry**:

$`x = -1`$.


---

#### Example 2:
Find the axis of symmetry for:

$`y = -3x^2 + 6x - 5`$.


**Solution**:
1. Identify $a = -3$ and $b = 6$.
2. Substitute into the formula:
   
   $`x = -\frac{6}{2(-3)} = -\frac{6}{-6} = 1`$.


**Axis of Symmetry**:

$x = 1$.

---

### **Vertex Form of a Parabola**
If the quadratic equation is in **vertex form**:

$`y = a(x-h)^2 + k`$,

the axis of symmetry is:

$x = h$,

where $(h, k)$ is the vertex of the parabola.

---

### **Applications**
1. Identifying the maximum or minimum value of a parabola.
2. Solving optimization problems in physics, engineering, and economics.
3. Graphing quadratic functions accurately. 



## **Understanding Radians of a Circle**

A **radian** is a unit of angular measure based on the radius of a circle. It is used to measure angles in 
mathematics and physics.

---

### **Definition of a Radian**
One radian is the angle subtended at the center of a circle by an arc that is equal in length to the radius of 
the circle.

---

### **Relationship Between Radians and Degrees**
The full circumference of a circle is $2\pi$ times the radius. In terms of angles:
- A full circle measures $360^\circ$ in degrees.
- A full circle measures $2\pi$ radians.

Thus, the conversion between radians and degrees is:

$`1 \text{ radian} = \frac{180^\circ}{\pi} \quad \text{or} \quad 1^\circ = \frac{\pi}{180} \text{ radians}`$.


---

### **Key Radian Measures**
For a circle, the following common angles in degrees and radians are important:

| Degrees $`(^\circ)`$ | Radians $`(\text{rad})`$ |
|----------------------|--------------------------|
| $`0^\circ`$          | $0$                      |
| $`30^\circ`$         | $`\frac{\pi}{6}`$        |
| $`45^\circ`$         | $`\frac{\pi}{4}`$        |
| $`60^\circ`$         | $`\frac{\pi}{3}`$        |
| $`90^\circ`$         | $`\frac{\pi}{2}`$        |
| $`180^\circ`$        | $`\pi`$                  |
| $`270^\circ`$        | $`\frac{3\pi}{2}`$       |
| $`360^\circ`$        | $`2\pi`$                 |

---

### **Converting Between Degrees and Radians**

#### Example 1: Convert $`90^\circ`$ to radians
Using the formula:

$`\text{Radians} = \text{Degrees} \times \frac{\pi}{180}`$,


$`90^\circ \times \frac{\pi}{180} = \frac{\pi}{2}`$.


#### Example 2: Convert $`\frac{\pi}{3}`$ radians to degrees
Using the formula:

$`\text{Degrees} = \text{Radians} \times \frac{180}{\pi}`$,


$`\frac{\pi}{3} \times \frac{180}{\pi} = 60^\circ`$.


---

### **Applications of Radians**
1. **Trigonometry**: Angles in the unit circle and trigonometric functions are often expressed in radians.
2. **Physics**: Angular velocity and rotational motion are measured in radians per second.
3. **Calculus**: Many formulas in calculus, such as derivatives and integrals of trigonometric functions, 
assume angles are measured in radians.



## **Understanding Factorials**

The **factorial** of a non-negative integer $n$, denoted as $n!$, is the product of all positive 
integers from $1$ to $n$. It is defined as:

$`n! = n \times (n-1) \times (n-2) \times \cdots \times 1, \quad \text{for } n \geq 1`$,

with a special case:

$0! = 1$.

---

### **Examples**

1. **Calculate $5!$:**
   
   $`5! = 5 \times 4 \times 3 \times 2 \times 1 = 120`$.
   

2. **Calculate $0!$:**
   By definition:
   
   $0! = 1$.
   

3. **Calculate $7!$:**
   
   $`7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5040`$.
   

---

### **Properties of Factorials**

1. **Recursive Property**:
   
   $`n! = n \times (n-1)!`$
   
   Example:
   
   $`5! = 5 \times 4!`$.
   

2. **Growth**:
   Factorials grow very rapidly with $n$. For example:
   
   $`10! = 3,628,800 \quad \text{and} \quad 20! = 2,432,902,008,176,640,000`$.
   

3. **Division of Factorials**:
   When dividing factorials, many terms cancel out. For example:
   
   $`\frac{6!}{4!} = \frac{6 \times 5 \times 4!}{4!} = 6 \times 5 = 30`$.

---

### **Applications of Factorials**

1. **Combinatorics**: 
   - Counting permutations:
     
     $`P(n, r) = \frac{n!}{(n-r)!}`$.
     
   - Counting combinations:
     
     $`C(n, r) = \frac{n!}{r!(n-r)!}`$.
     

2. **Mathematics**:
   - Factorials appear in series expansions, such as the Taylor series:
     
     $`e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}`$.
     

3. **Probability**:
   - Used in probability distributions like the binomial and Poisson distributions.

4. **Computer Science**:
   - Algorithms for combinatorial problems often rely on factorials.



##  **Quadratic Equations**

A **quadratic equation** is a polynomial equation of degree 2, typically written in the standard form:

$`ax^2 + bx + c = 0`$,

where:
- $a, b, c$ are constants, with $`a \neq 0`$,
- $x$ is the variable.

---

### **Characteristics of Quadratic Equations**

1. **Degree**: The highest power of $x$ is 2.
2. **Shape of the Graph**: The graph of a quadratic equation is a parabola.
   - If $`a > 0`$, the parabola opens upwards.
   - If $`a < 0`$, the parabola opens downwards.

---

### **Methods to Solve Quadratic Equations**

#### 1. **Factoring**
Rewrite the quadratic as a product of two binomials, then solve for $x$. 
Example:

$`x^2 - 5x + 6 = 0`$.

Factoring:

$`(x - 2)(x - 3) = 0`$.

Solutions:

$`x = 2 \quad \text{or} \quad x = 3`$.


#### 2. **Completing the Square**
Rewrite the quadratic in the form $`(x - h)^2 = k`$, then solve for $x$.
Example:

$`x^2 + 6x + 5 = 0`$.

Step 1: Move constant to the other side:

$`x^2 + 6x = -5`$.

Step 2: Add $`\left(\frac{6}{2}\right)^2 = 9`$ to both sides:

$`x^2 + 6x + 9 = 4`$.

Step 3: Factorize:

$`(x + 3)^2 = 4`$.

Step 4: Solve:

$`x + 3 = \pm 2 \quad \implies \quad x = -1 \quad \text{or} \quad x = -5`$.


#### 3. **Quadratic Formula**
For any quadratic equation $`ax^2 + bx + c = 0`$, the solutions are given by:

$`x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}`$.


Example:
Solve $`2x^2 - 4x - 6 = 0`$.

Step 1: Identify coefficients:

$`a = 2, \, b = -4, \, c = -6`$.


Step 2: Substitute into the formula:

$`x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(2)(-6)}}{2(2)}`$.

$`x = \frac{4 \pm \sqrt{16 + 48}}{4}`$.

$`x = \frac{4 \pm \sqrt{64}}{4}`$.


$`x = \frac{4 \pm 8}{4}`$.


Step 3: Solve:

$`x = \frac{4 + 8}{4} = 3 \quad \text{or} \quad x = \frac{4 - 8}{4} = -1`$.


#### 4. **Graphing**
Plot the quadratic function $`y = ax^2 + bx + c`$ and find the points where the graph crosses the $x$-axis. These points correspond to the roots of the equation.

---

### **Discriminant**
The discriminant $`(\Delta)`$ of a quadratic equation is:

$`\Delta = b^2 - 4ac`$.

It determines the nature of the roots:
- If $`(\Delta > 0)`$, there are **two distinct real roots**.
- If $`(\Delta = 0)`$, there is **one real root** (repeated).
- If $`(\Delta < 0)`$, there are **two complex roots**.

---

### **Applications of Quadratic Equations**
1. **Physics**: Projectile motion, finding maximum/minimum heights.
2. **Engineering**: Modeling parabolic structures.
3. **Economics**: Profit optimization problems.
4. **Computer Science**: Simulations and animations.

---

### **Challenge Problem**
Solve:

$`3x^2 + 5x - 2 = 0`$

using the quadratic formula. Let me know if assistance is needed!



## **Vertical Translations of Exponential Growth Functions**

Vertical translations involve shifting the graph of an exponential growth function up or down by adding or subtracting a constant.

---

### **General Form of Exponential Growth Functions**
The standard form of an exponential growth function is:

$`y = a \cdot b^x`$,

where:
- $`a > 0`$ is the initial value,
- $`b > 1`$ is the growth factor,
- $`x`$ is the independent variable.

For a **vertical translation**, a constant $k$ is added or subtracted:

$`y = a \cdot b^x + k`$.


- $`k > 0`$: The graph shifts **up** by $k$ units.
- $`k < 0`$: The graph shifts **down** by $|k|$ units.

---

### **Effect of $k$ on the Graph**

1. **Horizontal Asymptote**:
   - The horizontal asymptote of the function changes from $`y = 0`$ (for the standard form) to $`y = k`$.

2. **Graph Shape**:
   - The overall shape of the exponential growth function remains unchanged (rapid increase as $x$ becomes larger).

---

### **Examples**

#### Example 1:
Function:

$`y = 2 \cdot 3^x + 4`$.


- **Base Function**: $`y = 2 \cdot 3^x`$.
- **Vertical Translation**: The graph is shifted **up** by 4 units.
- **Horizontal Asymptote**: $y = 4$.

#### Example 2:
Function:

$`y = 5 \cdot 2^x - 3`$.


- **Base Function**: $`y = 5 \cdot 2^x`$.
- **Vertical Translation**: The graph is shifted **down** by 3 units.
- **Horizontal Asymptote**: $y = -3$.

---

### **Steps to Identify Vertical Translation**

1. Identify the $k$ value in the equation $`y = a \cdot b^x + k`$.
2. Determine the direction of the shift:
   - $`k > 0`$: Up.
   - $`k < 0`$: Down.
3. Note the new horizontal asymptote:
   - $`y = k`$.

---

### **Graphing Tips**

1. **Base Function**: Start by plotting the base function $`y = a \cdot b^x`$.
2. **Shift**: Apply the vertical translation by shifting all points $k$ units up or down.
3. **Asymptote**: Clearly mark the horizontal asymptote $`y = k`$.

---

### **Applications**

1. **Biology**: Modeling population growth with external factors.
2. **Finance**: Compounding interest with fixed additions or subtractions.
3. **Physics**: Exponential decay with added offsets for energy levels.

---

### **Challenge Problem**
Graph the function:

$`y = 3 \cdot 4^x - 2`$.

- Identify the base function, direction of translation, and new horizontal asymptote.
Let me know your findings!



## **The Natural Logarithm $`(\ln)`$**

The **natural logarithm** is a logarithm with the base $e$, where $`e \approx 2.718`$ (Euler's number). It is denoted as:

$\ln(x)$.

The natural logarithm is the inverse of the exponential function $e^x$, meaning:

$`\ln(e^x) = x \quad \text{and} \quad e^{\ln(x)} = x, \quad \text{for } x > 0`$.


---

### **Key Properties of Natural Logarithms**

1. **Domain**:
   - $`\ln(x)`$ is defined only for $`x > 0`$.

2. **Range**:
   - The range of $`\ln(x)`$ is all real numbers $`(-\infty, \infty)`$.

3. **Logarithmic Identity**:
   - $`\ln(1) = 0`$, because $e^0 = 1$.

4. **Logarithm of $e$**:
   - $`\ln(e) = 1`$, because $`e^1 = e`$.

5. **Logarithmic Multiplication Rule**:
   - $`\ln(ab) = \ln(a) + \ln(b)`$.

6. **Logarithmic Division Rule**:
   - $`\ln\left(\frac{a}{b}\right) = \ln(a) - \ln(b)`$.

7. **Logarithmic Power Rule**:
   - $`\ln(a^b) = b \cdot \ln(a)`$.

---

### **Solving Equations Involving Natural Logarithms**

#### Example 1:
Solve for $x$:

$`\ln(x) = 3`$.

Solution:

$`x = e^3 \quad (\text{since } e^{\ln(x)} = x)`$.

Numerical value:

$`x \approx 20.0855`$.


#### Example 2:
Solve for $x$:

$`e^{\ln(x)} = 10`$.

Solution:

$`x = 10 \quad (\text{because } e^{\ln(x)} = x)`$.


---

### **Graph of the Natural Logarithm**

1. **Shape**:
   - The graph of $`\ln(x)`$ passes through $(1, 0)$ and increases slowly for $x > 1$.
   - It decreases rapidly for $`0 < x < 1`$, approaching $`-\infty`$ as $`x \to 0^+`$.

2. **Asymptote**:
   - The $y$-axis $`(x = 0)`$ is a vertical asymptote.

---

### **Applications of the Natural Logarithm**

1. **Exponential Growth and Decay**:
   - Used in modeling phenomena like population growth, radioactive decay, and interest calculations.

2. **Calculus**:
   - The derivative of $`\ln(x)`$ is:
     
     $`\frac{d}{dx} \ln(x) = \frac{1}{x}`$.

   - The integral of $`1/x`$ is:
     
     $`\int \frac{1}{x} dx = \ln|x| + C`$.
     

3. **Statistics**:
   - Used in log-transformations for data normalization and in probability distributions like the log-normal distribution.

4. **Physics**:
   - Appears in formulas for entropy and thermodynamics.

---


## **Permutation**

A **permutation** refers to the arrangement of a set of items in a specific order. 
It considers the order of elements and is commonly used in combinatorics.

---

### **General Formula for Permutations**

The number of permutations of $n$ items taken $r$ at a time is given by:

$`P(n, r) = \frac{n!}{(n - r)!}`$,

where:
- $n!$ (factorial of $n$) is the product of all positive integers up to $n$,
- $r$ is the number of items chosen,
- $`(n \geq r)`$.

---

### **Key Points**

1. **Order Matters**:
   - In permutations, the order of arrangement is important. For example, arranging $`A, B, C`$ is different from arranging $`C, B, A`$.

2. **All Items Permutated $(r = n)$**:
   - When all $n$ items are arranged:
     
     $`P(n, n) = n!`$.
     

3. **No Items Selected $(r = 0)$**:
   - When $`r = 0`$:
     
     $`P(n, 0) = 1`$.
     

---

### **Examples**

#### Example 1:
Find the number of ways to arrange 4 objects, taking 2 at a time.

Solution:

$`P(4, 2) = \frac{4!}{(4 - 2)!} = \frac{4 \cdot 3 \cdot 2 \cdot 1}{2 \cdot 1} = 12`$.


#### Example 2:
How many ways can the letters of the word **"CAT"** be arranged?

Solution:
- Since all 3 letters are used:

$`P(3, 3) = 3! = 3 \cdot 2 \cdot 1 = 6`$.

Arrangements: $CAT, CTA, ACT, ATC, TAC, TCA$.

---

### **Permutations with Repetition**

If some items are repeated, the total number of distinct permutations is reduced. The formula is:

$`P = \frac{n!}{p_1! \cdot p_2! \cdot \dots \cdot p_k!}`$,

where:
- $`p_1, p_2, \dots, p_k`$ are the frequencies of repeated items.

#### Example:
Find the permutations of the word **"LEVEL"**.

Solution:
- Total letters = 5,
- $E$ appears 2 times, $L$ appears 2 times.

$`P = \frac{5!}{2! \cdot 2!} = \frac{120}{4} = 30`$.


---

### **Applications of Permutations**

1. **Scheduling**:
   - Arranging tasks or events.
2. **Cryptography**:
   - Creating codes and ciphers.
3. **Genetics**:
   - Arranging genetic sequences.
4. **Games and Puzzles**:
   - Solving arrangements of elements.


## **Combinations**

A **combination** refers to selecting items from a set where the order **does not matter**.
It is commonly used in situations where the arrangement is irrelevant.

---

### **General Formula for Combinations**

The number of combinations of $n$ items taken $r$ at a time is given by:

$`C(n, r) = \binom{n}{r} = \frac{n!}{r! \cdot (n - r)!}`$,

where:
- $n!$ is the factorial of $n$,
- $r$ is the number of items chosen,
- $`n \geq r`$.

---

### **Key Points**

1. **Order Does Not Matter**:
   - In combinations, the selection $A, B, C$ is the same as $C, B, A$.

2. **All Items Selected $`(r = n)`$**:
   - If all items are selected:
     
     $`C(n, n) = 1`$.
     

3. **No Items Selected $`(r = 0)`$**:
   - If no items are selected:
     
     $`C(n, 0) = 1`$.
     

4. **Symmetry Property**:
   - $`C(n, r) = C(n, n - r)`$.

---

### **Examples**

#### Example 1:
Find the number of ways to choose 3 items from a set of 5.

Solution:

$`C(5, 3) = \frac{5!}{3! \cdot (5 - 3)!} = \frac{5 \cdot 4 \cdot 3!}{3! \cdot 2!} = \frac{5 \cdot 4}{2} = 10`$.


#### Example 2:
How many ways can a committee of 4 people be formed from a group of 7?

Solution:

$`C(7, 4) = \frac{7!}{4! \cdot (7 - 4)!} = \frac{7 \cdot 6 \cdot 5 \cdot 4!}{4! \cdot 3 \cdot 2 \cdot 1} = \frac{7 \cdot 6 \cdot 5}{3 \cdot 2 \cdot 1} = 35`$.


---

### **Applications of Combinations**

1. **Lottery and Games**:
   - Calculating possible winning combinations.
2. **Team Formation**:
   - Choosing groups or committees.
3. **Probability**:
   - Determining outcomes in experiments where order is irrelevant.
4. **Biology**:
   - Selecting samples for genetic analysis.



## **Distance Between Two Points in Three-Dimensional Cartesian Space**

To calculate the distance between two points $`(x_1, y_1, z_1)`$ and $`(x_2, y_2, z_2)`$ in 3D space, the formula is an extension of the Pythagorean theorem:


$`d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}`$.


---

### **Derivation**
1. In 3D space, the distance between two points is the length of the straight line connecting them.
2. This line can be treated as the hypotenuse of a right-angled triangle formed by the differences in their $x$, $y$, and $z$ coordinates.

---

### **Steps to Calculate**
1. Compute the difference in the $x$-coordinates: $`(x_2 - x_1)`$,
2. Compute the difference in the $y$-coordinates: $`(y_2 - y_1)`$,
3. Compute the difference in the $z$-coordinates: $`(z_2 - z_1)`$,
4. Substitute these values into the formula:
   
   $`d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}`$.
   

---

### **Example**
Find the distance between the points $`(1, 2, 3)`$ and $`(4, 6, 8)`$.

Solution:

$`d = \sqrt{(4 - 1)^2 + (6 - 2)^2 + (8 - 3)^2}`$.


$`d = \sqrt{3^2 + 4^2 + 5^2}`$.


$`d = \sqrt{9 + 16 + 25}`$.


$`d = \sqrt{50}`$.


$`d \approx 7.07`$.


---

### **Applications**
1. **Physics**:
   - Calculating the straight-line distance between objects in space.
2. **Engineering**:
   - Measuring distances in 3D modeling or CAD systems.
3. **Computer Graphics**:
   - Determining distances for rendering and collision detection.
4. **Navigation**:
   - Finding the shortest path between two points in 3D environments.



## **Resultant of a Vector**

The **resultant vector** is the single vector that has the same effect as the combination of two or more vectors.
It is obtained by adding two or more vectors geometrically or algebraically.

---

### **Methods to Find the Resultant Vector**

#### **1. Geometric Method (Head-to-Tail Rule)**:
- Place the tail of the second vector at the head of the first vector.
- Repeat for additional vectors if applicable.
- The resultant vector is the straight line from the tail of the first vector to the head of the last vector.

---

#### **2. Algebraic Method (Component-Wise Addition)**:
Given vectors $`\mathbf{v}_1 = (v_{1x}, v_{1y}, v_{1z})`$ and $`\mathbf{v}_2 = (v_{2x}, v_{2y}, v_{2z})`$, the resultant vector $`\mathbf{R}`$ is:


$`\mathbf{R} = \mathbf{v}_1 + \mathbf{v}_2 = (v_{1x} + v_{2x}, v_{1y} + v_{2y}, v_{1z} + v_{2z})`$.


---

#### **3. Magnitude and Direction**

To calculate the magnitude of the resultant vector in 2D:

$`|\mathbf{R}| = \sqrt{R_x^2 + R_y^2}`$.


For 3D vectors:

$`|\mathbf{R}| = \sqrt{R_x^2 + R_y^2 + R_z^2}`$.


The direction of the resultant in 2D is given by the angle $`\theta`$ relative to the $x$-axis:


$`\theta = \tan^{-1}\left(\frac{R_y}{R_x}\right)`$.


---

### **Example 1: 2D Vectors**
Find the resultant of $`\mathbf{v}_1 = (3, 4)`$ and $`\mathbf{v}_2 = (1, 2)`$.

**Solution**:

$`\mathbf{R} = \mathbf{v}_1 + \mathbf{v}_2 = (3 + 1, 4 + 2) = (4, 6)`$.


Magnitude:

$`|\mathbf{R}| = \sqrt{4^2 + 6^2} = \sqrt{16 + 36} = \sqrt{52} \approx 7.21`$.


Direction:

$`\theta = \tan^{-1}\left(\frac{6}{4}\right) = \tan^{-1}(1.5) \approx 56.31^\circ`$.


---

### **Example 2: 3D Vectors**
Find the resultant of $`\mathbf{v}_1 = (2, -1, 3)`$ and $`\mathbf{v}_2 = (1, 4, -2)`$.

**Solution**:

$`\mathbf{R} = \mathbf{v}_1 + \mathbf{v}_2 = (2 + 1, -1 + 4, 3 - 2) = (3, 3, 1)`$.


Magnitude:

$`|\mathbf{R}| = \sqrt{3^2 + 3^2 + 1^2} = \sqrt{9 + 9 + 1} = \sqrt{19} \approx 4.36`$.


---

### **Applications**
1. **Physics**:
   - Adding forces, velocities, and displacements.
2. **Engineering**:
   - Structural analysis for combined loads.
3. **Navigation**:
   - Calculating resultant motion in wind or current scenarios.
4. **Computer Graphics**:
   - Combining transformations or movements.

Let me know if further clarification or additional examples are needed!



## **Zero Product Rule**
The **Zero Product Rule** is a fundamental principle used to solve quadratic equations that can be factored. 
It states that if the product of two or more terms equals zero, then at least one of the terms must be zero. This is expressed as:


$`ab = 0 \implies a = 0 \, \text{or} \, b = 0`$


### Application to Quadratic Equations
Quadratic equations often take the standard form:


$`ax^2 + bx + c = 0`$


To solve using the Zero Product Rule:
1. **Factorize** the quadratic equation into two binomials, if possible:
   
   $`ax^2 + bx + c = (px + q)(rx + s) = 0`$
   

2. **Set each factor equal to zero**:
   
   $`px + q = 0 \quad \text{or} \quad rx + s = 0`$
   

3. **Solve each equation for $x$**:
   
   $`x = -\frac{q}{p} \quad \text{and} \quad x = -\frac{s}{r}`$
   

### Example
Solve $`x^2 - 5x + 6 = 0`$:

1. **Factorize**: $`x^2 - 5x + 6 = (x - 2)(x - 3)`$
2. **Apply the Zero Product Rule**:
   
   $`x - 2 = 0 \quad \text{or} \quad x - 3 = 0`$
   
3. **Solve**:
   
   $`x = 2 \quad \text{or} \quad x = 3`$
   

The solutions are $x = 2$ and $x = 3$.

This approach is efficient when the quadratic equation is factorable. 
If not, alternative methods such as completing the square or the quadratic formula may be used.



## **Perpendicular Lines in the Coordinate Plane**

In the coordinate plane, **two lines are perpendicular** if the product of their slopes is $-1$. 
This relationship arises because perpendicular lines intersect at a right angle $`(90^\circ)`$.

---

### **Key Points**

#### **1. Slope of a Line**
The slope $(m)$ of a line is calculated as:


$`m = \frac{y_2 - y_1}{x_2 - x_1}`$

Where:
- $`(x_1, y_1)`$ and $`(x_2, y_2)`$ are two points on the line.

#### **2. Condition for Perpendicularity**
Let $m_1$ and $m_2$ be the slopes of two lines. The lines are perpendicular if:


$`m_1 \cdot m_2 = -1`$


This means the slope of one line is the **negative reciprocal** of the other:


$`m_2 = -\frac{1}{m_1}`$

#### **3. Vertical and Horizontal Lines**
- A vertical line has an **undefined slope** (e.g., $x = c$).
- A horizontal line has a slope of $0$ (e.g., $y = c$).
- A vertical line is always perpendicular to a horizontal line.

---

### **Equation of Perpendicular Lines**

#### **Given a Line**
If a line has slope $m_1$, the slope of any line perpendicular to it will be $`m_2 = -\frac{1}{m_1}`$.

#### **Finding the Equation of a Perpendicular Line**
To find the equation of a line perpendicular to another and passing through a specific point $`(x_1, y_1)`$:
1. Calculate the perpendicular slope $`m_2 = -\frac{1}{m_1}`$.
2. Use the point-slope form of a line:
   
   $`y - y_1 = m_2(x - x_1)`$
   

---

### **Examples**

#### **Example 1: Checking Perpendicularity**
Are the lines $y = 2x + 3$ and $`y = -\frac{1}{2}x - 4`$ perpendicular?

1. Slope of first line: $m_1 = 2$.
2. Slope of second line: $`m_2 = -\frac{1}{2}`$.
3. Verify: $`m_1 \cdot m_2 = 2 \cdot -\frac{1}{2} = -1`$.

The lines are perpendicular.

---

#### **Example 2: Finding the Perpendicular Line**
Find the equation of a line perpendicular to $`y = 3x + 1`$ and passing through the point $(2, 5)$.

1. Slope of given line: $m_1 = 3$.
2. Slope of perpendicular line: $`(m_2 = -\frac{1}{3}`$.
3. Use point-slope form:
   
   $`y - 5 = -\frac{1}{3}(x - 2)`$
   
   Simplify:
   
   $`y = -\frac{1}{3}x + \frac{2}{3} + 5`$
   
   
   $`y = -\frac{1}{3}x + \frac{17}{3}`$
   

The equation of the perpendicular line is:

$`y = -\frac{1}{3}x + \frac{17}{3}`$


---

#### Example 3
To find the equation of the line perpendicular to $y = 1$ and passing through the point $(-1, 0)$, 
follow these steps:

---

### Step 1: Understand the Slope of the Given Line
The line $y = 1$ is **horizontal** with a slope of $m = 0$. A line perpendicular to a horizontal
line is **vertical**, meaning it has an **undefined slope**.

---

### Step 2: Equation of a Vertical Line
The equation of a vertical line is always in the form $x = c$, where $c$ is the $x$-coordinate of 
all points on the line.

Since the line passes through $`(-1, 0)`$, the equation of the line is:


$x = -1$

---

### Step 3: Write in Standard Form
The standard form of a linear equation is:


$`Ax + By = C`$


For $x = -1$, rewrite it as:


$`1x + 0y = -1`$


or simply:


$x = -1$

---

### Final Answer
The equation of the line in standard form is:


$x = -1$

Understanding perpendicular lines is essential in geometry, algebra, and applications like graphics and navigation.




## **Radical Equations**

A **radical equation** is an equation in which the variable appears inside a radical, usually a square root, 
cube root, or any higher-order root. Solving radical equations involves isolating the radical expression 
and eliminating the radical by raising both sides of the equation to the appropriate power.

---

### **Steps to Solve a Radical Equation**

1. **Isolate the Radical**:
   - If there is more than one radical term, isolate one of them.

2. **Eliminate the Radical**:
   - Raise both sides of the equation to the power corresponding to the radical. For example:
     - Square root: Raise both sides to the power of 2.
     - Cube root: Raise both sides to the power of 3.

3. **Solve the Resulting Equation**:
   - After eliminating the radical, solve the equation (it may be linear, quadratic, or higher degree).

4. **Check for Extraneous Solutions**:
   - Substituting back into the original equation may reveal "extraneous solutions," which arise from 
   squaring both sides or other operations that introduce invalid results.

---

### **Example 1: Square Root Equation**
Solve:

$`\sqrt{x + 5} = 3`$


**Solution**:
1. Isolate the radical:
   
   $`\sqrt{x + 5} = 3`$
   

2. Eliminate the radical (square both sides):
   
   $`(\sqrt{x + 5})^2 = 3^2`$
   
   
   $`x + 5 = 9`$
   

3. Solve for $x$:
   
   $`x = 9 - 5`$
   
   $x = 4$


4. Check for extraneous solutions:
   Substitute $x = 4$ into the original equation:
   
   $`\sqrt{4 + 5} = \sqrt{9} = 3`$
   
   Valid solution: $x = 4$.

---

### **Example 2: Radical on Both Sides**
Solve:

$`\sqrt{x + 2} = \sqrt{2x - 3}`$


**Solution**:
1. Eliminate the radicals (square both sides):
   
   $`(\sqrt{x + 2})^2 = (\sqrt{2x - 3})^2`$
   
   
   $`x + 2 = 2x - 3`$
   

2. Solve for $x$:
   
   $`2 = x - 3`$
   
   
   $x = 5$


3. Check for extraneous solutions:
   Substitute $x = 5$ into the original equation:
   
   $`\sqrt{5 + 2} = \sqrt{2(5) - 3}`$
   
   
   $`\sqrt{7} = \sqrt{7}`$
   
   Valid solution: $x = 5$.

---

### **Example 3: Quadratic After Eliminating the Radical**
Solve:

$`\sqrt{x} + 4 = x`$


**Solution**:
1. Isolate the radical:
   
   $`\sqrt{x} = x - 4`$


2. Eliminate the radical (square both sides):
   
   $`(\sqrt{x})^2 = (x - 4)^2`$
   
   
   $`x = x^2 - 8x + 16`$
   

3. Rearrange into standard form:
   
   $`x^2 - 9x + 16 = 0`$
   

4. Solve the quadratic equation:
   Use the quadratic formula:
   
   $`x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}, \quad a = 1, b = -9, c = 16`$
   
   
   $`x = \frac{-(-9) \pm \sqrt{(-9)^2 - 4(1)(16)}}{2(1)}`$
   
   
   $`x = \frac{9 \pm \sqrt{81 - 64}}{2}`$

   
   $`x = \frac{9 \pm \sqrt{17}}{2}`$
   

5. Check for extraneous solutions:
   Substitute both solutions back into the original equation to ensure validity.

---

### **Important Notes**
- **Extraneous Solutions**: Always check solutions in the original equation, as squaring both sides can introduce invalid results.
- **Radical Index**: Adjust the power used to eliminate the radical based on its index (e.g., cube root requires cubing both sides).

Understanding radical equations is key to solving various algebraic problems and practical applications 
involving roots.





## **Reflections of Geometric Figures in the Cartesian Plane**

A **reflection** is a transformation that "flips" a geometric figure over a specific line, 
called the **line of reflection**, producing a mirror image. In the Cartesian plane, reflections 
are commonly performed over the **x-axis**, **y-axis**, the line $y = x$, or the line $y = -x$.

---

### **Types of Reflections**

#### 1. **Reflection over the x-axis**
- The x-coordinate stays the same, but the y-coordinate changes its sign.
- **Rule**: $`(x, y) \rightarrow (x, -y)`$.

**Example**:  
If a point $`A(3, 4)`$ is reflected over the x-axis, the new point $A'$ is:

$`(3, 4) \rightarrow (3, -4)`$


---

#### 2. **Reflection over the y-axis**
- The y-coordinate stays the same, but the x-coordinate changes its sign.
- **Rule**: $`(x, y) \rightarrow (-x, y)`$.

**Example**:  
If a point $`B(3, 4)`$ is reflected over the y-axis, the new point $B'$ is:

$`(3, 4) \rightarrow (-3, 4)`$


---

#### 3. **Reflection over the line $y = x$**
- The x-coordinate and y-coordinate are swapped.
- **Rule**: $`(x, y) \rightarrow (y, x)`$.

**Example**:  
If a point $`C(3, 4)`$ is reflected over the line $y = x$, the new point $C'$ is:

$`(3, 4) \rightarrow (4, 3)`$


---

#### 4. **Reflection over the line $y = -x$**
- The x-coordinate and y-coordinate are swapped, and both signs are changed.
- **Rule**: $`(x, y) \rightarrow (-y, -x)`$.

**Example**:  
If a point $D(3, 4)$ is reflected over the line $y = -x$, the new point $D'$ is:

$`(3, 4) \rightarrow (-4, -3)`$


---

### **Summary of Reflection Rules**
| **Line of Reflection** | **Transformation Rule**         |
|----------------------|---------------------------------|
| Over the x-axis      | $`(x, y) \rightarrow (x, -y)`$  |
| Over the y-axis      | $`(x, y) \rightarrow (-x, y)`$  |
| Over $y = x$         | $`(x, y) \rightarrow (y, x)`$   |
| Over $y = -x$        | $`(x, y) \rightarrow (-y, -x)`$ |

---

### **Reflection of Geometric Figures**

To reflect a geometric figure:
1. Reflect each **vertex** of the figure using the appropriate reflection rule.
2. Connect the reflected points to form the reflected image.

**Example: Reflection of a Triangle**  
Given a triangle with vertices $A(1, 2)$, $B(3, 4)$, and $C(5, 0)$:

- **Reflection over the x-axis**:
   - $`A(1, 2) \rightarrow A'(1, -2)`$
   - $`B(3, 4) \rightarrow B'(3, -4)`$
   - $`C(5, 0) \rightarrow C'(5, 0)`$

The reflected triangle has vertices $A'(1, -2)$, $B'(3, -4)$, and $C'(5, 0)$.

---

### **Visual Understanding**
Reflections create **mirror images** of geometric figures across the line of reflection. For example:
- A figure reflected over the x-axis flips vertically.
- A figure reflected over the y-axis flips horizontally.
- A figure reflected over $y = x$ or $y = -x$ is rotated and flipped accordingly.

---

### **Applications**
- Symmetry in design and engineering.
- Computer graphics and image processing.
- Solving geometric problems in mathematics.

Reflections are foundational transformations that preserve **size** and **shape** but change the figure's 
orientation in the Cartesian plane.




## **The Complement of an Event in Probability**

The **complement** of an event in probability refers to all outcomes in the sample space that are not 
part of the specified event. It essentially represents the "opposite" of the event.

---

### **Definition**
If $A$ is an event, then its complement, denoted by $A^c$ or $\neg A$, consists of all 
outcomes in the sample space $S$ that are not in $A$.


$`A^c = S \setminus A`$


- **Sample space $( S )$**: The set of all possible outcomes.
- **Event $( A )$**: A subset of $S$, representing specific outcomes.
- **Complement $( A^c )$**: The set of outcomes in $S$ that are not in $A$.

---

### **Complement Rule**
The probability of the complement of an event is given by:


$`P(A^c) = 1 - P(A)`$


This follows from the fact that:
- $`P(A) + P(A^c) = 1`$, since together they cover the entire sample space.

---

### **Example 1: Tossing a Coin**
- Sample space: $`S = \{ \text{Heads, Tails} \}`$
- Event $A$: Getting Heads $`( A = \{\text{Heads}\} )`$.

The complement of $A$ $( A^c )$ is:

$`A^c = \{\text{Tails}\}`$


If $`P(A) = 0.5`$, then $`P(A^c) = 1 - 0.5 = 0.5`$.

---

### **Example 2: Rolling a Die**
- Sample space: $`S = \{1, 2, 3, 4, 5, 6\}`$
- Event $A$: Rolling an odd number $( A = \{1, 3, 5\} )$.

The complement of $A$ $( A^c )$ is:

$`A^c = \{2, 4, 6\}`$

If $`P(A) = \frac{3}{6} = 0.5`$, then $`P(A^c) = 1 - 0.5 = 0.5`$.

---

### **Key Properties of Complements**
1. **Exclusivity**:
   - $A$ and  $A^c$  are mutually exclusive, meaning they cannot occur simultaneously.
   - $`A \cap A^c = \emptyset`$.

2. **Exhaustiveness**:
   - $`A \cup A^c = S`$, meaning together they include all possible outcomes.

3. **Probability**:
   - $`P(A^c) = 1 - P(A)`$.

---

### **Applications**
1. **Simplifying Probability Calculations**:
   - When calculating the probability of an event is difficult, use its complement instead.
   - Example: Probability of "at least one success" is easier calculated as $`1 - P(\text{no success})`$.

2. **Risk Analysis**:
   - Complement is used to calculate the likelihood of avoiding an undesired outcome.

---

### **Conclusion**
The complement of an event helps to account for all outcomes not included in the original event. 
It is an essential concept in probability, making it easier to work with events and their associated probabilities.





## **Discriminant of a Quadratic Equation**

The **discriminant** of a quadratic equation provides important information about the nature and number 
of the roots of the equation. For a quadratic equation of the form:


$`ax^2 + bx + c = 0 \quad (a \neq 0)`$,


the discriminant $(D)$ is defined as:


$`D = b^2 - 4ac`$


---

### **Role of the Discriminant**

The discriminant determines the nature of the roots of the quadratic equation:

1. **When $D > 0$:**
   - The equation has **two distinct real roots**.
   - If $D$ is a perfect square, the roots are rational; otherwise, they are irrational.

2. **When $D = 0$:**
   - The equation has **exactly one real root** (a repeated or double root).

3. **When $D < 0$:**
   - The equation has **two complex conjugate roots** (no real roots).

---

### **Examples**

#### **1. Positive Discriminant $(D > 0)$**
Equation: $`x^2 - 5x + 6 = 0`$

Here:
- $a = 1$, $b = -5$, $c = 6$.
- Discriminant: 
  
  $`D = (-5)^2 - 4(1)(6) = 25 - 24 = 1`$.

Since $D > 0$, there are two distinct real roots.

---

#### **2. Zero Discriminant $(D = 0)$**
Equation: $`x^2 - 4x + 4 = 0`$

Here:
- $a = 1$, $b = -4$, $c = 4$.
- Discriminant: 
  
  $`D = (-4)^2 - 4(1)(4) = 16 - 16 = 0`$.
  

Since $D = 0$, there is exactly one real root (a double root).

---

#### **3. Negative Discriminant $(D < 0)$**
Equation: $`x^2 + x + 1 = 0`$

Here:
- $a = 1$, $b = 1$, $c = 1$.
- Discriminant:
  
  $`D = (1)^2 - 4(1)(1) = 1 - 4 = -3`$.
  

Since $D < 0$, there are two complex conjugate roots.

---

### **Key Points**
- The discriminant is a single value that gives insight into the roots without solving the quadratic equation.
- It can be used in real-world applications such as physics, engineering, and optimization problems where understanding the behavior of the roots is important. 



## **Horizontal Stretches of Functions**

A **horizontal stretch** of a function occurs when the function's input values are scaled by a factor, 
causing the graph of the function to widen horizontally. This transformation changes how the function 
behaves along the x-axis, while its behavior along the y-axis remains unchanged.

---

### **Definition**
For a given function $f(x)$, a horizontal stretch is represented by:


$`g(x) = f\left(\frac{x}{k}\right)`$,


where:
- $k > 1$: The graph is **stretched** horizontally by a factor of $k$.
- $0 < k < 1$: The graph is **compressed** (squeezed) horizontally by a factor of $k$.

---

### **How It Works**
In $`g(x) = f\left(\frac{x}{k}\right)`$, each input $x$ is replaced by $`\frac{x}{k}`$. This means:
- When $k > 1$, the graph appears wider because each $x$-coordinate is divided by $k$, effectively spreading the graph out.
- When $`0 < k < 1`$, the graph is compressed because each $x$-coordinate is divided by a small fraction, pulling the graph closer together.

---

### **Examples**

#### 1. **Horizontal Stretch**
Given $f(x) = x^2$:
- Apply a horizontal stretch by $k = 2$:  
  
  $`g(x) = f\left(\frac{x}{2}\right) = \left(\frac{x}{2}\right)^2 = \frac{x^2}{4}`$.
  
- The graph of $g(x)$ will be wider compared to $f(x)$.

#### 2. **Horizontal Compression**
Given $`f(x) = x^2`$:
- Apply a horizontal compression by $`k = \frac{1}{2}`$:  
  
  $`g(x) = f\left(\frac{x}{\frac{1}{2}}\right) = f(2x) = (2x)^2 = 4x^2`$.
  
- The graph of $g(x)$ will be narrower compared to $f(x)$.

---

### **Visual Understanding**

#### Original Function $f(x) = x^2$:
- The graph is a parabola centered at the origin.

#### Horizontal Stretch $( k > 1 )$:
- Each point on the graph moves farther from the y-axis. For example, $(1, 1)$ becomes $(2, 1)$ when stretched by $k = 2$.

#### Horizontal Compression $( 0 < k < 1 )$:
- Each point on the graph moves closer to the y-axis. For example, $(1, 1)$ becomes $(0.5, 1)$ when compressed by $`k = \frac{1}{2}`$.

---

### **Key Properties of Horizontal Stretches**
1. **Only x-coordinates are affected**:
   - The y-values remain unchanged, while the x-values are scaled by the factor $k$.

2. **Inverse Relationship**:
   - A horizontal stretch by $k > 1$ is equivalent to dividing x-values by  $k$.
   - A horizontal compression by $0 < k < 1$ is equivalent to multiplying x-values by a factor greater than 1.

---

### **Applications**
- Horizontal stretches are used in modeling situations where the input domain changes while maintaining the general shape of the function.
- Common in physics, engineering, and signal processing to scale time or spatial variables.




## **Modeling Downward Vertical Motion**

Downward vertical motion is a key concept in physics that describes the motion of an object moving 
under the influence of gravity. This type of motion can be modeled using equations from kinematics, 
assuming negligible air resistance.

---

### **Key Equations**
The primary equation for vertical motion is derived from the kinematic equations:


$`h(t) = h_0 - v_0t - \frac{1}{2}gt^2`$

Where:
- $h(t)$: The height of the object at time $t$.
- $h_0$: The initial height of the object (when $t = 0$).
- $v_0$: The initial velocity of the object (positive if upwards, negative if downwards).
- $g$: Acceleration due to gravity $`( g \approx 9.8 \, \text{m/s}^2`$ on Earth).
- $t$: Time in seconds.

---

### **Explanation of Terms**
1. **Initial Height $( h_0 )$**: The starting height of the object above the ground.
2. **Initial Velocity $( v_0 )$**:
   - If $v_0 = 0$, the object starts from rest.
   - If $v_0 > 0$, the object is thrown or projected upwards.
   - If $v_0 < 0$, the object is projected downwards.
3. **Acceleration Due to Gravity $( g )$**:
   - Always acts downward, causing the object to accelerate towards the ground.

---

### **Special Cases**
1. **Free Fall (No Initial Velocity)**:
   If $v_0 = 0$, the equation simplifies to:
   
   $`h(t) = h_0 - \frac{1}{2}gt^2`$.
   

2. **Object Thrown Downwards**:
   If $v_0 < 0$, the term $-v_0t$ becomes larger in magnitude, increasing the speed of descent.

3. **Object Thrown Upwards**:
   The object first rises until its velocity reduces to zero, then falls back under the influence of gravity.

---

### **Example Problem**

#### **Scenario**:
A ball is dropped from a height of $`h_0 = 50 \, \text{m}`$ with no initial velocity. 
How long does it take to hit the ground?

#### **Solution**:
Given:
- $`h_0 = 50 \, \text{m}`$
-  $v_0 = 0$
- $`g = 9.8 \, \text{m/s}^2`$

The equation becomes:

$`0 = h_0 - \frac{1}{2}gt^2`$.


Rearrange to solve for $t$:

$`\frac{1}{2}gt^2 = h_0 \implies t^2 = \frac{2h_0}{g}`$.


Substitute the values:

$`t^2 = \frac{2(50)}{9.8} \approx 10.204`$.



$`t \approx \sqrt{10.204} \approx 3.2 \, \text{seconds}`$.


---

### **Graphical Representation**
- The height $h(t)$ decreases quadratically with time $t$.
- The velocity $`v(t) = -v_0 - gt`$ increases linearly in magnitude, indicating constant acceleration.

---

### **Applications**
1. **Projectile Motion**: To model objects thrown vertically or at an angle.
2. **Physics and Engineering**: Analyzing falling objects or systems under gravitational influence.
3. **Sports**: Studying the motion of balls, javelins, or similar objects.

This framework helps predict motion, impact time, and velocity in practical scenarios.




## **Axis of Symmetry of a Parabola**

The **axis of symmetry** of a parabola is a vertical or horizontal line that divides the parabola 
into two symmetrical halves. It passes through the vertex of the parabola and is a critical feature 
in understanding the parabola's geometry.

---

### **Standard Form of a Parabola**
The equation of a parabola in **standard form** is:


$`y = ax^2 + bx + c`$

- The axis of symmetry is given by the formula:
  
  $`x = -\frac{b}{2a}`$.
  

Here:
- $a$, $b$, and $c$: Coefficients of the quadratic equation.
- $`x = -\frac{b}{2a}`$: The x-coordinate of the vertex and the axis of symmetry.

---

### **Vertex Form of a Parabola**
The equation of a parabola in **vertex form** is:


$`y = a(x - h)^2 + k`$,


where:
- $`(h, k)`$: The vertex of the parabola.
- The axis of symmetry is:
  
  $x = h$.
  

---

### **Direction of the Axis of Symmetry**
1. **For a vertical parabola** $`( y = ax^2 + bx + c )`$:
   - The axis of symmetry is a vertical line, $`x = -\frac{b}{2a}`$.

2. **For a horizontal parabola** $`( x = ay^2 + by + c )`$:
   - The axis of symmetry is a horizontal line, $`y = -\frac{b}{2a}`$.

---

### **Examples**

#### 1. **Find the Axis of Symmetry for $y = 2x^2 + 4x + 1$:**
- Given: $a = 2$, $b = 4$, $c = 1$.
- Use the formula:
  
  $`x = -\frac{b}{2a} = -\frac{4}{2(2)} = -1`$.
  
- The axis of symmetry is $x = -1$.

---

#### 2. **Find the Axis of Symmetry for $y = (x - 3)^2 + 2$ :**
- The equation is in vertex form, $`y = a(x - h)^2 + k`$, where $h = 3$, $k = 2$.
- The axis of symmetry is $x = 3$.

---

### **Graphical Interpretation**
- The axis of symmetry passes through the vertex of the parabola.
- It acts as a mirror line, ensuring that the left and right sides of the parabola are symmetric.

---

### **Key Properties**
1. **Relationship to Vertex**: The axis of symmetry always passes through the vertex of the parabola.
2. **Independent of $c$**: In the standard form $`y = ax^2 + bx + c`$, the axis of symmetry depends only on $a$ and $b$.

---

### **Applications**
1. **Optimization Problems**: Helps in finding the maximum or minimum value of a quadratic function.
2. **Geometry**: Used in analyzing reflective properties of parabolas.
3. **Physics and Engineering**: Understanding trajectories, such as in projectile motion.




## **Trigonometric Ratios**

**Trigonometric ratios** are mathematical relationships between the angles and side lengths of a right triangle. 
These ratios are fundamental in trigonometry and are used to solve problems involving triangles, circles, and periodic phenomena.

---

### **Right Triangle Setup**
For a right triangle:
- The **hypotenuse** is the longest side (opposite the right angle).
- The **adjacent side** is the side next to the given angle $(\theta)$ other than the hypotenuse.
- The **opposite side** is the side opposite to the given angle $(\theta)$.

---

### **Primary Trigonometric Ratios**
1. **Sine $(\sin)$**: 
   
   $`\sin\theta = \frac{\text{Opposite}}{\text{Hypotenuse}}`$
   

2. **Cosine $(\cos)$**: 
   
   $`\cos\theta = \frac{\text{Adjacent}}{\text{Hypotenuse}}`$
   

3. **Tangent $(\tan)$**: 
   
   $`\tan\theta = \frac{\text{Opposite}}{\text{Adjacent}}`$
   

---

### **Reciprocal Trigonometric Ratios**
4. **Cosecant $(\csc)$**: 
   
   $`\csc\theta = \frac{1}{\sin\theta} = \frac{\text{Hypotenuse}}{\text{Opposite}}`$
   

5. **Secant $(\sec)$**: 
   
   $`\sec\theta = \frac{1}{\cos\theta} = \frac{\text{Hypotenuse}}{\text{Adjacent}}`$
   

6. **Cotangent $(\cot)$**: 
   
   $`\cot\theta = \frac{1}{\tan\theta} = \frac{\text{Adjacent}}{\text{Opposite}}`$
   

---

### **Summary Table**

| Ratio              | Definition                          | Formula                                    |
|--------------------|-------------------------------------|--------------------------------------------|
| Sine $(\sin)$      | Opposite ÷ Hypotenuse              | $`\sin\theta = \frac{\text{O}}{\text{H}}`$ |
| Cosine $(\cos)$    | Adjacent ÷ Hypotenuse            | $`\cos\theta = \frac{\text{A}}{\text{H}}`$ |
| Tangent $(\tan)$   | Opposite ÷ Adjacent             | $`\tan\theta = \frac{\text{O}}{\text{A}}`$ |
| Cosecant $(\csc)$  | 1 ÷ Sine                      | $`\csc\theta = \frac{\text{H}}{\text{O}}`$ |
| Secant $(\sec)$    | 1 ÷ Cosine                      | $`\sec\theta = \frac{\text{H}}{\text{A}}`$ |
| Cotangent $(\cot)$ | 1 ÷ Tangent                 | $`\cot\theta = \frac{\text{A}}{\text{O}}`$ |

---

### **Key Relationships**
1. **Pythagorean Identity**:
   
   $`\sin^2\theta + \cos^2\theta = 1`$
   

2. **Tangent and Sine/Cosine**:
   
   $`\tan\theta = \frac{\sin\theta}{\cos\theta}`$
   

3. **Reciprocal Identities**:
   
   $`\csc\theta = \frac{1}{\sin\theta}, \quad \sec\theta = \frac{1}{\cos\theta}, \quad \cot\theta = \frac{1}{\tan\theta}`$.
   

---

### **Example**
#### Given: A right triangle with:
- Opposite = 3
- Adjacent = 4
- Hypotenuse = 5

Find all trigonometric ratios for $\theta$:
- $`\sin\theta = \frac{3}{5}`$
- $`\cos\theta = \frac{4}{5}`$
- $`\tan\theta = \frac{3}{4}`$
- $`\csc\theta = \frac{5}{3}`$
- $`\sec\theta = \frac{5}{4}`$
- $`\cot\theta = \frac{4}{3}`$

---

### **Applications**
1. **Geometry**: Solving right triangles.
2. **Physics**: Analyzing forces, waves, and oscillations.
3. **Engineering**: Modeling periodic behavior.
4. **Astronomy**: Measuring angles in celestial observations. 

These ratios form the foundation for advanced topics like trigonometric equations, transformations, and calculus.



## **Reciprocal trigonometric ratios**

**Reciprocal trigonometric** ratios are derived from the primary trigonometric functions (sine, cosine, and tangent) 
by taking their reciprocals. These ratios are commonly used in various mathematical and engineering applications.

Here are the reciprocal trigonometric ratios:

1. **Cosecant (csc)**: The reciprocal of sine  
   
   $`\csc \theta = \frac{1}{\sin \theta} = \frac{\text{Hypotenuse}}{\text{Opposite side}}`$
   

2. **Secant (sec)**: The reciprocal of cosine  
   
   $`\sec \theta = \frac{1}{\cos \theta} = \frac{\text{Hypotenuse}}{\text{Adjacent side}}`$
   

3. **Cotangent (cot)**: The reciprocal of tangent  
   
   $`\cot \theta = \frac{1}{\tan \theta} = \frac{\cos \theta}{\sin \theta} = \frac{\text{Adjacent side}}{\text{Opposite side}}`$
   

### Relationships to the Unit Circle:
- In the unit circle, where the hypotenuse is 1, these reciprocal ratios are calculated using the coordinates $(x, y)$ of a point on the circle and the angle $\theta$:
  - $`\csc \theta = \frac{1}{y}`$, valid where $y \neq 0$.
  - $`\sec \theta = \frac{1}{x}`$, valid where $x \neq 0$.
  - $`\cot \theta = \frac{x}{y}`$, valid where $y \neq 0$.

### Key Points:
- Reciprocal ratios are undefined when the denominator in the reciprocal calculation equals zero.
- These functions are essential in advanced trigonometry, calculus, and solving equations involving right triangles or periodic functions.



## **special trigonometric ratios**

A **special trigonometric ratios** involves exploring the specific values of trigonometric functions for 
commonly used angles: $0^\circ$, $30^\circ$, $45^\circ$, $60^\circ$, and $90^\circ$. 
These values are often used in mathematics, physics, and engineering due to their simplicity and 
relevance in geometry and calculus.

---

### **Key Special Angles**
The values of trigonometric functions for these angles are often derived from properties of special right triangles:
1. **30°–60°–90° triangle** (Half of an equilateral triangle):
   - Hypotenuse = $2a$, Opposite side of $30^\circ$ = $a$, Adjacent side of $30^\circ$ = $a\sqrt{3}$.
2. **45°–45°–90° triangle** (Isosceles right triangle):
   - Hypotenuse = $a\sqrt{2}$, Legs = $a$.

---

### **Values of Trigonometric Ratios**
| $\theta$   | $\sin \theta$          | $`\cos \theta`$        | $`\tan \theta`$        | $`\csc \theta`$        | $`\sec \theta`$        | $`\cot \theta`$      |
|------------|------------------------|------------------------|------------------------|------------------------|------------------------|----------------------|
| $0^\circ$  | $0$                    | $1$                    | $0$                    | Undefined              | $1$                    | Undefined            |
| $30^\circ$ | $`\frac{1}{2}`$        | $`\frac{\sqrt{3}}{2}`$ | $`\frac{1}{\sqrt{3}}`$ | $2$                    | $`\frac{2}{\sqrt{3}}`$ | $\sqrt{3}$           |
| $45^\circ$ | $`\frac{1}{\sqrt{2}}`$ | $`\frac{1}{\sqrt{2}}`$ | $1$                    | $`\sqrt{2}`$           | $`\sqrt{2}`$           | $1$                  |
| $60^\circ$ | $`\frac{\sqrt{3}}{2}`$ | $`\frac{1}{2}`$        | $\sqrt{3}$             | $`\frac{2}{\sqrt{3}}`$ | $2$                    | $`\frac{1}{\sqrt{3}}`$ |
| $90^\circ$ | $1$                    | $0$                    | Undefined              | $1$                    | Undefined              | $0$                  |

---

### **Special Triangles and Derivations**

#### **30°–60°–90° Triangle**
- **Sine**: For $30^\circ$, $`\sin 30^\circ = \frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{1}{2}`$.
- **Cosine**: For $30^\circ$, $`\cos 30^\circ = \frac{\text{Adjacent}}{\text{Hypotenuse}} = \frac{\sqrt{3}}{2}`$.
- **Tangent**: For $30^\circ$, $`\tan 30^\circ = \frac{\text{Opposite}}{\text{Adjacent}} = \frac{1}{\sqrt{3}}`$.

#### **45°–45°–90° Triangle**
- **Sine and Cosine**: For $45^\circ$, $`\sin 45^\circ = \cos 45^\circ = \frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{1}{\sqrt{2}}`$.
- **Tangent**: For $45^\circ$, $`\tan 45^\circ = \frac{\text{Opposite}}{\text{Adjacent}} = 1`$.

---

### **Reciprocal Relationships**
- **Cosecant**: $`\csc \theta = \frac{1}{\sin \theta}`$.
- **Secant**: $`\sec \theta = \frac{1}{\cos \theta}`$.
- **Cotangent**: $`\cot \theta = \frac{1}{\tan \theta}`$.

---

### **Unit Circle Perspective**
In the unit circle:
- The coordinates of points on the circle represent $`(\cos \theta, \sin \theta)`$.
- Tangent is the slope of the line formed by the terminal side of the angle and the origin.

#### Key Points:
| Angle $(\theta)$ | Coordinates $(x, y)$                         |
|------------------|----------------------------------------------|
| $0^\circ$        | $(1, 0)$                                     |
| $30^\circ$       | $`(\frac{\sqrt{3}}{2}, \frac{1}{2})`$        |
| $45^\circ$       | $`(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})`$ |
| $60^\circ$       | $`(\frac{1}{2}, \frac{\sqrt{3}}{2})`$        |
| $90^\circ$       | $(0, 1)$                                     |

---

### **Applications**
- Used in solving right triangles.
- Fundamental in Fourier analysis and wave theory.
- Appear in optimization problems and integrals in calculus.




## **Domain and Range of Quadratic Functions**
The **domain** and **range** of quadratic functions are essential characteristics in understanding their behavior. 
A quadratic function is typically expressed as:


$`f(x) = ax^2 + bx + c`$


where $a$, $b$, and $c$ are constants, and $a \neq 0$.

---

### **Domain of Quadratic Functions**
- The domain of any quadratic function is all real numbers, $\mathbb{R}$, because there are no restrictions on the values that $x$ can take.
- **Mathematically**:
  
  $`\text{Domain: } (-\infty, \infty)`$
  

---

### **Range of Quadratic Functions**
The range depends on the **vertex** and the **direction** of the parabola (whether it opens upwards or downwards):

1. **Parabola Opens Upward** $(a > 0)$:
   - The vertex is the minimum point of the function.
   - The range includes all values greater than or equal to the $y$-coordinate of the vertex.
   - **Range**:
     
     $`[k, \infty), \quad \text{where } k = f(h) \text{ and } h = -\frac{b}{2a}`$.
     

2. **Parabola Opens Downward** $(a < 0)$:
   - The vertex is the maximum point of the function.
   - The range includes all values less than or equal to the $y$-coordinate of the vertex.
   - **Range**:
     
     $`(-\infty, k], \quad \text{where } k = f(h) \text{ and } h = -\frac{b}{2a}$.
     

---

### **Finding the Vertex**
The vertex $(h, k)$ can be calculated using:

$`h = -\frac{b}{2a}, \quad k = f(h) = a\left(-\frac{b}{2a}\right)^2 + b\left(-\frac{b}{2a}\right) + c`$.


---

### **Examples**
1. $`f(x) = x^2 - 4x + 3`$:
   - $a = 1$, $b = -4$, $c = 3$.
   - Vertex: $`h = -\frac{-4}{2(1)} = 2`$, $`k = f(2) = (2)^2 - 4(2) + 3 = -1`$.
   - **Range**: $`[-1, \infty)`$.

2. $`f(x) = -2x^2 + 4x - 1`$:
   - $a = -2$, $b = 4$, $c = -1$.
   - Vertex: $`h = -\frac{4}{2(-2)} = 1`$, $`k = f(1) = -2(1)^2 + 4(1) - 1 = 1`$.
   - **Range**: $`(-\infty, 1]`$.

---

### Summary
- **Domain**: Always $`(-\infty, \infty)`$.
- **Range**: Depends on the vertex and the direction of the parabola:
  - $`a > 0`$: $[k, \infty)$
  - $a < 0$: $(-\infty, k]$.




## **Exponential Equations Using the Zero-Product Property**
The **Zero-Product Property** is a fundamental principle in algebra that states:

$`\text{If } ab = 0, \text{ then } a = 0 \text{ or } b = 0`$.


This property is commonly used to solve **exponential equations** when they can be expressed as a 
product of terms set equal to zero. Here's how it applies:

---

### **Steps to Solve Exponential Equations Using the Zero-Product Property**

1. **Rewrite the Equation**:
   - Bring all terms to one side of the equation to set it equal to zero.

2. **Factorize the Expression**:
   - If possible, factorize the equation into the product of terms.

3. **Apply the Zero-Product Property**:
   - Set each factor equal to zero.

4. **Solve Each Equation**:
   - Solve for the variable in each equation.

---

### **Example 1: Basic Exponential Equation**
Solve:

$`e^{2x} - 4e^x = 0`$


**Solution**:
1. Rewrite the equation:
   
   $`e^x(e^x - 4) = 0`$

2. Apply the Zero-Product Property:
   
   $`e^x = 0 \quad \text{or} \quad e^x - 4 = 0`$
   

3. Solve each equation:
   - $e^x = 0$: No solution, because $e^x > 0$ for all $x$.
   - $`e^x - 4 = 0`$: $e^x = 4$.

4. Solve for $x$:
   
   $`x = \ln(4)`$
   

**Final Answer**:

$`x = \ln(4)`$


---

### **Example 2: Quadratic Form Exponential Equation**
Solve:

$`2^{2x} - 5 \cdot 2^x + 6 = 0`$


**Solution**:
1. Let $y = 2^x$. Then $`2^{2x} = y^2`$.

2. Rewrite the equation:
   
   $`y^2 - 5y + 6 = 0`$
   

3. Factorize:
   
   $`(y - 2)(y - 3) = 0`$
   

4. Apply the Zero-Product Property:
   
   $`y - 2 = 0 \quad \text{or} \quad y - 3 = 0`$
   

5. Solve for $y$:
   
   $`y = 2 \quad \text{or} \quad y = 3`$
   

6. Recall $y = 2^x$, so:
   
   $`2^x = 2 \quad \text{or} \quad 2^x = 3`$
   

7. Solve for $x$:
   - $2^x = 2$: $x = 1$.
   - $2^x = 3$: $x = \log_2(3)$.

**Final Answer**:

$`x = 1 \quad \text{or} \quad x = \log_2(3)`$

---

### **Key Takeaways**
1. The Zero-Product Property simplifies solving equations where the product of terms equals zero.
2. In exponential equations, factorization often involves substitutions to simplify the equation.
3. Solutions may involve logarithms, as exponential terms are inverses of logarithms.




## **Solving Logarithmic Equations**
Logarithmic equations involve logarithms with unknowns and can be solved by applying logarithmic properties.
Here's an overview of solving these equations:

---

### **Steps to Solve Logarithmic Equations**

1. **Isolate the Logarithmic Term(s)**:
   - Ensure the logarithmic expression is alone on one side of the equation.

2. **Use Logarithmic Properties**:
   - Apply properties of logarithms to simplify the equation:
     - $`\log_b(xy) = \log_b(x) + \log_b(y)`$
     - $`\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)`$
     - $`\log_b(x^n) = n \cdot \log_b(x)`$

3. **Rewrite in Exponential Form**:
   - If the equation has a single logarithm, rewrite it using:
     
     $`\log_b(x) = y \implies x = b^y`$

4. **Solve for the Variable**:
   - Solve the resulting equation after simplifying.

5. **Check for Extraneous Solutions**:
   - Logarithms are only defined for positive arguments. Ensure the solution makes all logarithmic expressions valid.

---

### **Example 1: Single Logarithmic Equation**
Solve:

$`\log_2(x) = 3`$

**Solution**:
1. Rewrite in exponential form:
   
   $`x = 2^3`$

2. Simplify:
   
   $`x = 8`$


**Final Answer**:

$`x = 8`$

---

### **Example 2: Logarithms on Both Sides**
Solve:

$`\log_3(x) = \log_3(5)`$


**Solution**:
1. If the bases are the same, equate the arguments:
   
   $`x = 5`$

**Final Answer**:

$`x = 5`$

---

### **Example 3: Using Logarithmic Properties**
Solve:

$`\log_2(x) + \log_2(x - 3) = 3`$


**Solution**:
1. Apply the product rule:
   
   $`\log_2(x(x - 3)) = 3`$
   

2. Simplify:
   
   $`\log_2(x^2 - 3x) = 3`$


3. Rewrite in exponential form:
   
   $`x^2 - 3x = 2^3`$
   

4. Solve the quadratic equation:
   
   $`x^2 - 3x - 8 = 0`$
   

   Factorize:
   
   $`(x - 4)(x + 2) = 0`$
   

   Solutions:
   
   $`x = 4 \quad \text{or} \quad x = -2`$
   

5. Check for extraneous solutions:
   - $(x = -2)$ is invalid because $`\log_2(x)`$ is undefined for $`x \leq 0`$.
   - $x = 4$ is valid.

**Final Answer**:

$x = 4$

---

### **Example 4: Equation with Different Bases**
Solve:

$`\log_2(x) = \log_3(9)`$


**Solution**:
1. Simplify $`\log_3(9)`$:
   
   $`\log_3(9) = \log_3(3^2) = 2`$
   

2. Rewrite the equation:
   
   $`\log_2(x) = 2`$
   

3. Solve for $x$ using exponential form:
   
   $`x = 2^2 = 4`$
   

**Final Answer**:

$x = 4$

---

### **Key Tips**
1. Logarithmic properties are essential for simplifying equations.
2. Always check the domain $`(x > 0)`$ to avoid extraneous solutions.
3. Rewrite complex logarithms in exponential form to solve effectively.




## **Area of a General Triangle**
The **area of a general triangle** can be computed using several formulas depending on the available
information (e.g., side lengths, base and height, or angles). Below are the most common methods:

---

### **1. Using Base and Height**
If the base $(b)$ and height $(h)$ of the triangle are known:

$`\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}`$

- $b$ is the length of the base.
- $h$ is the perpendicular height from the base to the opposite vertex.

---

### **2. Using Heron's Formula**
If the lengths of all three sides $(a, b, c)$ are known:
1. Compute the semi-perimeter:
   
   $`s = \frac{a + b + c}{2}`$
   

2. Compute the area:
   
   $`\text{Area} = \sqrt{s(s - a)(s - b)(s - c)}`$
   

---

### **3. Using Two Sides and the Included Angle**
If two sides $(a, b)$ and the included angle $`(\theta)`$ are known:

$`\text{Area} = \frac{1}{2} \times a \times b \times \sin(\theta)`$

- $`\theta`$ is the angle between sides $a$ and $b$.

---

### **4. Coordinate Geometry Formula**
If the coordinates of the triangle's vertices are known as $`(x_1, y_1)`$, $`(x_2, y_2)`$, and $`(x_3, y_3)`$:

$`\text{Area} = \frac{1}{2} \left| x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \right|`$


---

### **Examples**

#### **Example 1: Base and Height**
Find the area of a triangle with base $b = 10$ units and height $h = 6$ units:

$`\text{Area} = \frac{1}{2} \times 10 \times 6 = 30 \, \text{square units.}`$

#### **Example 2: Heron's Formula**
Find the area of a triangle with sides $a = 5$, $b = 6$, and $c = 7$:
1. Compute $s$:
   
   $`s = \frac{5 + 6 + 7}{2} = 9`$
   

2. Compute the area:
   
   $`\text{Area} = \sqrt{9(9 - 5)(9 - 6)(9 - 7)} = \sqrt{9 \cdot 4 \cdot 3 \cdot 2} = \sqrt{216} \approx 14.7 \, \text{square units.}`$
   

#### **Example 3: Two Sides and Angle**
Find the area of a triangle with $a = 8$, $b = 10$, and $`\theta = 60^\circ`$:

$`\text{Area} = \frac{1}{2} \times 8 \times 10 \times \sin(60^\circ) = \frac{1}{2} \times 8 \times 10 \times \frac{\sqrt{3}}{2} = 20\sqrt{3} \approx 34.64 \, \text{square units.}`$


---

### **Conclusion**
The appropriate formula depends on the information available about the triangle. Use the one that matches 
the given data for efficient calculation.




## **Consistency and Dependency in Linear Systems**
When analyzing **linear systems of equations**, the concepts of **consistency** and **dependency** 
help determine the nature of solutions the system may have. Here's a breakdown of these concepts:

---

### **1. Consistency in Linear Systems**
A linear system is classified as:

#### **a) Consistent**
- The system has **at least one solution**.
- Can be further divided into:
  - **Unique Solution**: A single solution exists (intersection at a point).
  - **Infinite Solutions**: The equations represent the same line/plane, so they overlap completely.

#### **b) Inconsistent**
- The system has **no solutions**.
- This happens when the equations represent parallel lines or planes that never intersect.

---

### **2. Dependency in Linear Systems**
Dependency refers to whether the equations in the system are related (dependent) or independent.

#### **a) Independent**
- Each equation provides unique information.
- The system has exactly one solution if it is consistent.

#### **b) Dependent**
- At least one equation is a scalar multiple or linear combination of the others.
- The system has infinitely many solutions because the equations describe the same geometric entity 
(e.g., overlapping lines or planes).

---

### **Geometric Interpretation**

- **2 Variables (Lines in a Plane)**:
  - **Consistent and Independent**: Lines intersect at a point (unique solution).
  - **Consistent and Dependent**: Lines are identical (infinite solutions).
  - **Inconsistent**: Lines are parallel and do not intersect (no solution).

- **3 Variables (Planes in Space)**:
  - **Consistent and Independent**: Planes intersect at a single point.
  - **Consistent and Dependent**: Planes overlap or intersect along a line.
  - **Inconsistent**: Planes are parallel or form inconsistent arrangements.

---

### **Example Analysis**

#### **Example 1: Unique Solution**

$`x + y = 3`$

$`2x - y = 1`$

- Solving yields $`x = 1, y = 2`$.
- **Consistent and Independent** (unique solution).

#### **Example 2: Infinite Solutions**
$`x + y = 3`$

$`2x + 2y = 6`$

- The second equation is a multiple of the first.
- **Consistent and Dependent** (infinite solutions).

#### **Example 3: No Solution**

$`x + y = 3`$

$`x + y = 5`$

- The lines are parallel with no intersection.
- **Inconsistent**.

---

### **Summary**
- A system's **consistency** determines if solutions exist.
- A system's **dependency** determines whether the equations provide unique or redundant information.
Understanding these concepts helps identify the type of solutions a linear system has and their geometric interpretation.




  
## **Vertical Translation of an Exponential Decay Function**
A **vertical translation** of an **exponential decay function** involves shifting the graph of the function 
up or down along the $y$-axis. Here's an overview:

---

### **Exponential Decay Function**
The general form of an exponential decay function is:

$`f(x) = a \cdot b^x, \quad \text{where } 0 < b < 1 \text{ and } a > 0`$.

- $a$: Initial value (value of $f(x)$ when $x = 0$).
- $b$: Decay factor (indicates the rate of decay).

---

### **Vertical Translation**
When a constant $k$ is added to or subtracted from the function, the graph is translated vertically:

$`f(x) = a \cdot b^x + k`$

- $k > 0$: The graph shifts **up** by $k$ units.
- $k < 0$: The graph shifts **down** by $|k|$ units.

---

### **Key Characteristics After Translation**
1. **Horizontal Asymptote**:
   - The horizontal asymptote, originally at $y = 0$, shifts to $y = k$.
   - This happens because $k$ is added to all $y$-values of the function.

2. **Decay Behavior**:
   - The function still exhibits exponential decay, but the $y$-values are shifted by $k$.

3. **Domain**:
   - The domain remains all real numbers $`(-\infty, \infty)`$.

4. **Range**:
   - The range changes to:
     
     $`y > k \quad \text{(if \(a > 0\))}`$.
     

---

### **Example**
#### Original Function:

$`f(x) = 2 \cdot (0.5)^x`$

- Decay factor: $b = 0.5$.
- Horizontal asymptote: $y = 0$.
- Range: $y > 0$.

#### Vertical Translation:

$`f(x) = 2 \cdot (0.5)^x + 3`$

- The graph shifts **up** by 3 units.
- New horizontal asymptote: $y = 3$.
- New range: $y > 3$.

---


### **Graphical Representation**
1. The graph of $`f(x) = 2 \cdot (0.5)^x`$ starts at $y = 2$ when $x = 0$ and approaches $y = 0$ as $x \to \infty$.
2. After the translation $(k = 3)$:
   - The graph starts at $y = 5$ when $x = 0$.
   - The horizontal asymptote shifts to $y = 3$.

---

### **Summary**
- Vertical translations adjust the horizontal asymptote and shift the entire graph up or down without changing the domain or the decay rate.
- The new function $`f(x) = a \cdot b^x + k`$ provides a decay model that reflects the additional constant $k$, 
which is common in real-world scenarios like adjusting baseline levels in exponential processes.



  
## **logarithms of exponentiated expressions**
When dealing with **logarithms of exponentiated expressions**, it's important to apply the properties
of logarithms to simplify the expression. Here's how to handle such cases:

---

### **General Expression**
For an expression of the form:

$`\log_b(a^c)`$

where:
- $b$: Base of the logarithm.
- $a$: Argument of the logarithm.
- $c$: Exponent of the argument.

---

### **Key Property**
Using the **power rule of logarithms**, which states:

$`\log_b(a^c) = c \cdot \log_b(a)`$

This allows the exponent $c$ to be brought in front as a coefficient.

---

### **Examples**
#### **Example 1: Simplify $\log_2(8^3)$**
1. Apply the power rule:
   
   $`\log_2(8^3) = 3 \cdot \log_2(8)`$
   

2. Simplify $\log_2(8)$ (since $8 = 2^3$):
   
   $`\log_2(8) = 3`$
   

3. Final result:
   
   $`\log_2(8^3) = 3 \cdot 3 = 9`$
   

---

#### **Example 2: Simplify $`\ln(e^{5x})`$**
1. Use the natural logarithm property:
   
   $`\ln(e^{5x}) = 5x \cdot \ln(e)`$
   

2. Simplify $`\ln(e) = 1`$:
   
   $`\ln(e^{5x}) = 5x`$
   

---

#### **Example 3: Simplify $`\log_{10}(100^2)`$**
1. Apply the power rule:
   
   $`\log_{10}(100^2) = 2 \cdot \log_{10}(100)`$
   

2. Simplify $`\log_{10}(100) = 2`$ (since $`100 = 10^2`$):
   
   $`\log_{10}(100^2) = 2 \cdot 2 = 4`$
   

---

### **Special Cases**
1. **When the base and argument are powers of the same number**:
   
   $`\log_a(a^n) = n`$

   Example: $`\log_3(3^4) = 4`$.

2. **Logarithm of an exponent involving the same base**:
   
   $`\log_b(b^{x+y}) = x + y`$
   
   Example: $`\log_2(2^{3+4}) = 3 + 4 = 7`$.

---

### **Common Mistakes to Avoid**
1. **Not simplifying the logarithm before applying rules**:
   - For example, $`\log_2(64^2)`$ can first simplify $`\log_2(64) = 6`$, then apply the power rule.

2. **Misapplying the base**:
   - Ensure the base of the logarithm matches the context (e.g., natural logarithm $e$, common logarithm $10$, or other bases).

---

### **Conclusion**
The power rule of logarithms $`(\log_b(a^c) = c \cdot \log_b(a))`$ is a fundamental property that simplifies exponentiated logarithmic expressions.
Combine it with other logarithmic properties for efficient calculations.



## **Limits of Power Functions**
### **Limits of Power Functions**
A **power function** is of the form $`f(x) = x^n`$, where $n$ is a real number. Evaluating the limits of power 
functions depends on the behavior of $x$ (as $`x \to \infty`$ , $`x \to -\infty`$, or $`x \to 0`$) and the exponent $n$.


#### **1. As $`x \to \infty`$:**
- If $`n > 0`$, $`x^n \to \infty`$.
- If $`n < 0`$, $`x^n \to 0`$ (because $`x^n = \frac{1}{x^{|n|}}`$).
- If $`n = 0`$, $`x^n = 1`$ (a constant).


#### **2. As $`x \to -\infty`$:**
- If $n > 0$ and $n$ is an **even integer**, $`x^n \to \infty`$ (since negative values squared become positive).
- If $n > 0$ and $n$ is an **odd integer**, $`x^n \to -\infty`$.
- If $n < 0$, $`x^n \to 0`$ (negative or positive doesn't matter as the fraction approaches zero).
- If $n = 0$, $`x^n = 1`$.


#### **3. As \( x \to 0^+ \) or \( x \to 0^- \):**
- If \( n > 0 \), \( x^n \to 0 \).
- If \( n < 0 \), \( x^n \to \infty \) or \( x^n \to -\infty \), depending on the sign of \( x \).

---

### **Examples of Limits for Power Functions**
1. \(\lim_{x \to \infty} x^3 = \infty\) (positive exponent, positive \(x\)).
2. \(\lim_{x \to -\infty} x^4 = \infty\) (even positive exponent, negative \(x\)).
3. \(\lim_{x \to 0^+} x^{-2} = \infty\) (negative exponent, small positive \(x\)).

---

### **Constant Rule for Limits**
The **constant rule for limits** states:
\[
\lim_{x \to c} k = k
\]
where \(k\) is a constant, and \(c\) is any value (finite or infinite). This means the limit of a constant function is the constant itself.

#### **Key Points:**
1. The value of \( x \) has no effect on the outcome since the function is constant.
2. This rule applies regardless of whether \( x \to c \) is finite or infinite.

---

### **Examples of the Constant Rule**
1. \(\lim_{x \to \infty} 5 = 5\).
2. \(\lim_{x \to -\infty} -7 = -7\).
3. \(\lim_{x \to 0} 3 = 3\).

---

### **Combining Power Functions and Constants**
When dealing with combinations of power functions and constants, apply the **sum, product, and quotient rules** in addition to the constant rule.

#### Example:
\[
f(x) = 3x^2 + 5
\]
- \(\lim_{x \to \infty} f(x) = \lim_{x \to \infty} (3x^2) + \lim_{x \to \infty} 5\).
- Using power function and constant rules:
  - \(\lim_{x \to \infty} 3x^2 = \infty\),
  - \(\lim_{x \to \infty} 5 = 5\).
- So, \(\lim_{x \to \infty} f(x) = \infty\).

---

### **Conclusion**
- **Power Functions**: Their limits depend on the value of the exponent \( n \) and the behavior of \( x \).
- **Constant Rule**: The limit of a constant is always the constant itself.
- Use these principles together with algebraic manipulation to evaluate complex limits.



## **Graphing the Square Root Function**
The square root function is a fundamental mathematical function represented by:
\[
f(x) = \sqrt{x}
\]

---

### **Key Characteristics of the Square Root Function**

1. **Domain**:
   - The square root is defined for non-negative values of \(x\).
   - \(\text{Domain: } [0, \infty)\).

2. **Range**:
   - The output of \(\sqrt{x}\) is always non-negative.
   - \(\text{Range: } [0, \infty)\).

3. **Intercept**:
   - The graph passes through the origin: \((0, 0)\).

4. **Increasing Function**:
   - The function is increasing on its entire domain. As \(x\) increases, \(\sqrt{x}\) also increases, but at a decreasing rate.

5. **End Behavior**:
   - As \(x \to \infty\), \(\sqrt{x} \to \infty\).

---

### **Steps to Graph the Function**

1. **Create a Table of Values**:
   Select a few values of \(x\) and compute the corresponding \(f(x) = \sqrt{x}\).

   | \(x\)  | \(f(x) = \sqrt{x}\) |
   |-------|--------------------|
   | \(0\)  | \(0\)              |
   | \(1\)  | \(1\)              |
   | \(4\)  | \(2\)              |
   | \(9\)  | \(3\)              |
   | \(16\) | \(4\)              |

2. **Plot Points**:
   Plot the points \((0, 0)\), \((1, 1)\), \((4, 2)\), \((9, 3)\), and \((16, 4)\) on a graph.

3. **Sketch the Curve**:
   - Connect the points with a smooth curve starting from the origin.
   - The curve should increase gradually, flattening as \(x\) grows larger.

---

### **Transformations of the Square Root Function**
The graph of \(f(x) = \sqrt{x}\) can be transformed using standard transformations:

1. **Vertical Shifts**:
   - \(f(x) = \sqrt{x} + k\): Shift up by \(k\).
   - \(f(x) = \sqrt{x} - k\): Shift down by \(k\).

2. **Horizontal Shifts**:
   - \(f(x) = \sqrt{x - h}\): Shift right by \(h\).
   - \(f(x) = \sqrt{x + h}\): Shift left by \(h\).

3. **Vertical Stretch/Compression**:
   - \(f(x) = a\sqrt{x}\): Stretch vertically if \(a > 1\), compress if \(0 < a < 1\).

4. **Reflection**:
   - \(f(x) = -\sqrt{x}\): Reflect across the \(x\)-axis.

---

### **Example**
Graph \(f(x) = \sqrt{x - 3} + 2\):
1. Start with the base function \(f(x) = \sqrt{x}\).
2. Shift right by 3 (horizontal shift).
3. Shift up by 2 (vertical shift).
4. Plot key points:
   - For \(x = 3\), \(f(3) = \sqrt{3 - 3} + 2 = 2\).
   - For \(x = 4\), \(f(4) = \sqrt{4 - 3} + 2 = 3\).
   - For \(x = 7\), \(f(7) = \sqrt{7 - 3} + 2 = 4\).

Sketch the graph based on these transformations.

---

### **Graphical Summary**
The graph of the square root function starts at the origin, grows slowly, and is defined only for \(x \geq 0\). 
Transformations allow for shifting, stretching, compressing, or reflecting the graph to adapt to real-world applications.




## **Product and Quotient Rule for Limits**

The **Product Rule** and **Quotient Rule** for limits allow us to evaluate limits of expressions involving multiplication or division of functions. These rules are fundamental tools in calculus and analysis.

---

### **1. Product Rule for Limits**

If the limits of two functions \(f(x)\) and \(g(x)\) exist as \(x \to c\), then:
\[
\lim_{x \to c} [f(x) \cdot g(x)] = \left(\lim_{x \to c} f(x)\right) \cdot \left(\lim_{x \to c} g(x)\right)
\]

#### **Key Conditions**:
- Both \(\lim_{x \to c} f(x)\) and \(\lim_{x \to c} g(x)\) must exist and be finite.

#### **Example**:
Evaluate:
\[
\lim_{x \to 2} (x^2 \cdot \sin x)
\]
1. Break the product into individual limits:
   \[
   \lim_{x \to 2} (x^2 \cdot \sin x) = \left(\lim_{x \to 2} x^2\right) \cdot \left(\lim_{x \to 2} \sin x\right)
   \]
2. Compute each limit:
   - \(\lim_{x \to 2} x^2 = 4\)
   - \(\lim_{x \to 2} \sin x = \sin(2)\)
3. Multiply the results:
   \[
   \lim_{x \to 2} (x^2 \cdot \sin x) = 4 \cdot \sin(2)
   \]

---

### **2. Quotient Rule for Limits**

If the limits of \(f(x)\) and \(g(x)\) exist as \(x \to c\) and \(\lim_{x \to c} g(x) \neq 0\), then:
\[
\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\lim_{x \to c} f(x)}{\lim_{x \to c} g(x)}
\]

#### **Key Conditions**:
- \(\lim_{x \to c} f(x)\) and \(\lim_{x \to c} g(x)\) must exist.
- \(\lim_{x \to c} g(x) \neq 0\).

#### **Example**:
Evaluate:
\[
\lim_{x \to 3} \frac{x^2 - 9}{x - 3}
\]
1. Simplify the expression:
   \[
   \frac{x^2 - 9}{x - 3} = \frac{(x - 3)(x + 3)}{x - 3}
   \]
   For \(x \neq 3\), this simplifies to:
   \[
   x + 3
   \]
2. Now, compute the limit:
   \[
   \lim_{x \to 3} (x + 3) = 3 + 3 = 6
   \]

---

### **Indeterminate Forms**
If direct substitution results in forms like \(0 \cdot \infty\), \(\frac{0}{0}\), or \(\frac{\infty}{\infty}\), the rules cannot be directly applied. In such cases, additional techniques (e.g., factoring, rationalizing, or L’Hôpital’s Rule) may be required.

---

### **Summary**

1. **Product Rule**:
   \[
   \lim_{x \to c} [f(x) \cdot g(x)] = \lim_{x \to c} f(x) \cdot \lim_{x \to c} g(x)
   \]

2. **Quotient Rule**:
   \[
   \lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\lim_{x \to c} f(x)}{\lim_{x \to c} g(x)} \quad \text{if } \lim_{x \to c} g(x) \neq 0
   \]

These rules are valid only when the individual limits exist and are finite.




## **Domain and Range of Quadratic Functions**

A quadratic function is of the form:
\[
f(x) = ax^2 + bx + c
\]
where \(a\), \(b\), and \(c\) are constants, and \(a \neq 0\).

---

### **1. Domain of a Quadratic Function**

The domain of a quadratic function is **all real numbers**, because the function is defined for every value of \(x\).

\[
\text{Domain: } (-\infty, \infty)
\]

---

### **2. Range of a Quadratic Function**

The range of a quadratic function depends on its **vertex** and the **direction** in which the parabola opens.

#### **Key Factors**:
- The parabola opens **upward** if \(a > 0\) (minimum point at the vertex).
- The parabola opens **downward** if \(a < 0\) (maximum point at the vertex).

#### **Vertex Formula**:
The vertex of the parabola is given by:
\[
x = -\frac{b}{2a}
\]
Substitute \(x = -\frac{b}{2a}\) into \(f(x)\) to find the corresponding \(y\)-coordinate of the vertex:
\[
y = f\left(-\frac{b}{2a}\right)
\]
This \(y\)-value determines the **minimum** (if \(a > 0\)) or **maximum** (if \(a < 0\)) value of the function.

#### **Range**:
- If \(a > 0\) (opens upward):
  \[
  \text{Range: } [\text{minimum value}, \infty)
  \]
- If \(a < 0\) (opens downward):
  \[
  \text{Range: } (-\infty, \text{maximum value}]
  \]

---

### **Example 1: \(f(x) = x^2 - 4\)**
1. **Domain**:
   - All real numbers: \((- \infty, \infty)\).

2. **Vertex**:
   - \(x = -\frac{b}{2a} = -\frac{0}{2(1)} = 0\).
   - \(y = f(0) = 0^2 - 4 = -4\).

3. **Direction**:
   - \(a = 1 > 0\), so the parabola opens upward.

4. **Range**:
   - Minimum value is \(-4\), so:
     \[
     \text{Range: } [-4, \infty)
     \]

---

### **Example 2: \(f(x) = -2x^2 + 8x - 5\)**
1. **Domain**:
   - All real numbers: \((- \infty, \infty)\).

2. **Vertex**:
   - \(x = -\frac{b}{2a} = -\frac{8}{2(-2)} = 2\).
   - \(y = f(2) = -2(2)^2 + 8(2) - 5 = -8 + 16 - 5 = 3\).

3. **Direction**:
   - \(a = -2 < 0\), so the parabola opens downward.

4. **Range**:
   - Maximum value is \(3\), so:
     \[
     \text{Range: } (-\infty, 3]
     \]

---

### **Conclusion**

- The **domain** of any quadratic function is always \( (-\infty, \infty) \).
- The **range** depends on the vertex and whether the parabola opens upward (\(a > 0\)) or downward (\(a < 0\)). 
Use the vertex formula to determine the extremum (minimum or maximum).





## **Sequences**

A sequence is an ordered list of numbers following a specific rule. Each number in a sequence is called a **term**, and the position of the term in the sequence is its **index**.

---

### **Types of Sequences**

1. **Arithmetic Sequence**:
   - The difference between consecutive terms is constant (called the common difference, \(d\)).
   - General form:
     \[
     a_n = a_1 + (n-1)d
     \]
   - Example: \(2, 5, 8, 11, \ldots\) (\(d = 3\)).

2. **Geometric Sequence**:
   - The ratio between consecutive terms is constant (called the common ratio, \(r\)).
   - General form:
     \[
     a_n = a_1 \cdot r^{n-1}
     \]
   - Example: \(3, 6, 12, 24, \ldots\) (\(r = 2\)).

3. **Harmonic Sequence**:
   - A sequence of reciprocals of an arithmetic sequence.
   - Example: \(1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \ldots\).

4. **Fibonacci Sequence**:
   - Each term is the sum of the two preceding terms.
   - Recursive form:
     \[
     F_1 = 1, \, F_2 = 1, \, F_n = F_{n-1} + F_{n-2} \, \text{for } n \geq 3
     \]
   - Example: \(1, 1, 2, 3, 5, 8, 13, \ldots\).

---

### **Properties of Sequences**

1. **Finite vs. Infinite Sequences**:
   - **Finite sequence**: Has a limited number of terms (e.g., \(2, 4, 6, 8\)).
   - **Infinite sequence**: Has an unlimited number of terms (e.g., \(1, 2, 3, 4, \ldots\)).

2. **Explicit Formula**:
   - Describes the \(n\)-th term directly, such as \(a_n = 2n + 1\).

3. **Recursive Formula**:
   - Defines each term based on previous terms, such as \(a_n = a_{n-1} + 3\), \(a_1 = 2\).

4. **Convergence and Divergence**:
   - A sequence **converges** if its terms approach a specific value as \(n \to \infty\).
   - A sequence **diverges** if its terms grow without bound or oscillate.

---

### **Sum of Sequences**

1. **Arithmetic Series**:
   - Sum of the first \(n\) terms of an arithmetic sequence:
     \[
     S_n = \frac{n}{2} \cdot (a_1 + a_n)
     \]

2. **Geometric Series**:
   - Sum of the first \(n\) terms of a geometric sequence:
     \[
     S_n = a_1 \cdot \frac{1 - r^n}{1 - r}, \, r \neq 1
     \]
   - For an infinite geometric series (\(|r| < 1\)):
     \[
     S = \frac{a_1}{1 - r}
     \]

---

### **Example Problems**

1. **Find the 10th term of an arithmetic sequence \(3, 7, 11, \ldots\):**
   - \(a_1 = 3, \, d = 4\).
   - Use \(a_n = a_1 + (n-1)d\):
     \[
     a_{10} = 3 + (10-1) \cdot 4 = 3 + 36 = 39
     \]

2. **Find the sum of the first 6 terms of the geometric sequence \(2, 6, 18, \ldots\):**
   - \(a_1 = 2, \, r = 3, \, n = 6\).
   - Use \(S_n = a_1 \cdot \frac{1 - r^n}{1 - r}\):
     \[
     S_6 = 2 \cdot \frac{1 - 3^6}{1 - 3} = 2 \cdot \frac{1 - 729}{-2} = 2 \cdot 364 = 728
     \]

---

### **Applications of Sequences**
- Modeling real-world patterns like population growth (geometric sequences).
- Financial calculations, like loan amortization or compound interest.
- Mathematical puzzles, such as finding missing terms in a sequence.

Sequences form the basis for many concepts in calculus, analysis, and applied mathematics.



## **The Real Number System**

The **Real Number System** is a comprehensive classification of numbers used in mathematics, encompassing various subsets of numbers with unique properties. Real numbers include all numbers that can represent a point on a number line.

---

### **Categories of Real Numbers**

1. **Natural Numbers (\( \mathbb{N} \))**:
   - Definition: Counting numbers starting from \(1\).
   - Examples: \(1, 2, 3, 4, \ldots\)
   - Excludes zero and negative numbers.

2. **Whole Numbers**:
   - Definition: Natural numbers including zero.
   - Examples: \(0, 1, 2, 3, \ldots\)

3. **Integers (\( \mathbb{Z} \))**:
   - Definition: Whole numbers and their negatives.
   - Examples: \(\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\)

4. **Rational Numbers (\( \mathbb{Q} \))**:
   - Definition: Numbers that can be expressed as the quotient of two integers (\(\frac{p}{q}\), where \(q \neq 0\)).
   - Examples: \( \frac{1}{2}, -3, 0.75, 5 \)
   - Includes terminating and repeating decimals.

5. **Irrational Numbers**:
   - Definition: Numbers that **cannot** be expressed as a ratio of two integers.
   - Examples: \(\sqrt{2}, \pi, e\)
   - Their decimal expansions are non-repeating and non-terminating.

6. **Real Numbers (\( \mathbb{R} \))**:
   - Definition: The set of all rational and irrational numbers.
   - Includes numbers like \(2, -5, \sqrt{3}, \pi, 0.1\).
   - Can represent any point on the number line.

---

### **Properties of the Real Number System**

1. **Closure**:
   - Addition, subtraction, multiplication, and division (except by 0) of real numbers result in another real number.

2. **Commutative Property**:
   - For addition and multiplication:
     \[
     a + b = b + a \quad \text{and} \quad a \cdot b = b \cdot a
     \]

3. **Associative Property**:
   - For addition and multiplication:
     \[
     (a + b) + c = a + (b + c) \quad \text{and} \quad (a \cdot b) \cdot c = a \cdot (b \cdot c)
     \]

4. **Distributive Property**:
   - Multiplication distributes over addition:
     \[
     a \cdot (b + c) = a \cdot b + a \cdot c
     \]

5. **Identity Elements**:
   - Additive identity: \(0\) (since \(a + 0 = a\)).
   - Multiplicative identity: \(1\) (since \(a \cdot 1 = a\)).

6. **Inverse Elements**:
   - Additive inverse: For any \(a\), there exists \(-a\) such that \(a + (-a) = 0\).
   - Multiplicative inverse: For any \(a \neq 0\), there exists \(1/a\) such that \(a \cdot (1/a) = 1\).

---

### **Visual Representation**

```
Real Numbers (ℝ)
├── Rational Numbers (ℚ)
│   ├── Integers (ℤ)
│   │   ├── Whole Numbers
│   │   │   ├── Natural Numbers (ℕ)
│   ├── Fractions
├── Irrational Numbers
```

---

### **Key Notes**

- **Natural Numbers**: Start from \(1\) (\( \mathbb{N} = \{1, 2, 3, \ldots\}\)).
- **Whole Numbers**: Start from \(0\) (\( \{0, 1, 2, 3, \ldots\}\)).
- **Integers**: Add negative numbers to whole numbers (\( \mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}\)).
- **Rational Numbers**: Includes fractions and decimals that terminate or repeat.
- **Irrational Numbers**: Cannot be written as fractions, such as \(\sqrt{2}\) and \(\pi\).
- **Real Numbers**: Combine all rational and irrational numbers.

The real number system forms the foundation of most mathematical analysis and practical applications.



## **Dilations of Geometric Figures**

**Dilation** is a type of transformation in geometry that enlarges or reduces a geometric figure by a scale factor relative to a fixed point called the **center of dilation**. Dilations produce similar figures, meaning the shape remains the same but the size changes.

---

### **Key Components of Dilations**

1. **Center of Dilation**:
   - A fixed point from which the dilation occurs. 
   - The distances from this point to other points on the figure are multiplied by the scale factor.

2. **Scale Factor (\(k\))**:
   - Determines the degree of enlargement (\(k > 1\)) or reduction (\(0 < k < 1\)).
   - If \(k = 1\), the figure remains unchanged.
   - If \(k < 0\), the figure is reflected across the center along with the dilation.

---

### **Properties of Dilations**

1. **Proportionality**:
   - Corresponding sides of the original figure and the dilated image are proportional by the scale factor \(k\).

2. **Angles**:
   - Corresponding angles in the original figure and the image remain equal.

3. **Shape**:
   - The original figure and its dilation are similar (same shape but different size).

4. **Distance**:
   - The distance from the center of dilation to any point in the image is \(k\) times the distance from the center to the corresponding point in the preimage.

---

### **Mathematical Representation**

For a point \(P(x, y)\) and a center of dilation at the origin \((0, 0)\):
\[
P'(x', y') = (kx, ky)
\]
Where \(P'(x', y')\) is the image of \(P(x, y)\) after dilation.

For a center of dilation at \((h, k)\):
\[
P'(x', y') = \big(h + k(x - h), k(y - k)\big)
\]

---

### **Steps to Perform a Dilation**

1. Identify the center of dilation and the scale factor \(k\).
2. Measure the distance from the center of dilation to each vertex of the figure.
3. Multiply these distances by \(k\) to locate the new points.
4. Connect the new points to form the dilated image.

---

### **Examples**

1. **Dilation from the Origin**:
   - Preimage points: \((2, 3), (4, 5), (6, 1)\).
   - Scale factor: \(k = 2\).
   - Image points: \((4, 6), (8, 10), (12, 2)\).

2. **Reduction with Center at the Origin**:
   - Preimage points: \((6, 8), (12, 16)\).
   - Scale factor: \(k = 0.5\).
   - Image points: \((3, 4), (6, 8)\).

---

### **Applications of Dilations**

1. **Real-Life Scaling**:
   - Creating scale models or blueprints.
   - Zooming in or out on digital images.

2. **Mathematics and Geometry**:
   - Exploring properties of similarity.
   - Understanding transformations in coordinate geometry.

3. **Art and Design**:
   - Creating patterns or designs with repeated scaling.

---

### **Visual Example**

If a triangle with vertices \((1, 2), (3, 4), (5, 6)\) is dilated with a scale factor of \(k = 2\), the vertices of the dilated triangle will be:
\[
(2 \cdot 1, 2 \cdot 2) = (2, 4), \quad (2 \cdot 3, 2 \cdot 4) = (6, 8), \quad (2 \cdot 5, 2 \cdot 6) = (10, 12).
\]

The resulting triangle is twice as large but has the same shape as the original.




## **The Power and Root Rules for Limits**

The **Power Rule** and **Root Rule** for limits are fundamental concepts in calculus that simplify the evaluation of limits involving powers or roots of functions.

---

### **1. The Power Rule for Limits**

If \( \lim_{x \to c} f(x) = L \), where \( L \) is finite, and \( n \) is a positive integer, then:
\[
\lim_{x \to c} [f(x)]^n = [\lim_{x \to c} f(x)]^n = L^n
\]

#### **Examples**:

1. **Basic Example**:
   \[
   \lim_{x \to 2} x^3 = (\lim_{x \to 2} x)^3 = 2^3 = 8
   \]

2. **With a Polynomial Function**:
   \[
   \lim_{x \to 1} (3x^2 + 2)^3 = (\lim_{x \to 1} (3x^2 + 2))^3 = (3(1)^2 + 2)^3 = 5^3 = 125
   \]

---

### **2. The Root Rule for Limits**

If \( \lim_{x \to c} f(x) = L \), where \( L \geq 0 \), and \( n \) is a positive integer, then:
\[
\lim_{x \to c} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to c} f(x)} = \sqrt[n]{L}
\]

#### **Examples**:

1. **Square Root Example**:
   \[
   \lim_{x \to 4} \sqrt{x} = \sqrt{\lim_{x \to 4} x} = \sqrt{4} = 2
   \]

2. **Cube Root Example**:
   \[
   \lim_{x \to 8} \sqrt[3]{x + 1} = \sqrt[3]{\lim_{x \to 8} (x + 1)} = \sqrt[3]{8 + 1} = \sqrt[3]{9}
   \]

---

### **Key Notes and Conditions**

1. **Continuity**:
   - The power and root rules apply because powers and roots are continuous functions for their defined domains.

2. **Domain of \(f(x)\)**:
   - For the root rule, \(f(x) \geq 0\) is required for even roots (like square roots) to ensure the result is real-valued.

3. **Indeterminate Forms**:
   - The rules do not apply directly to indeterminate forms like \(0^0\) or roots of undefined expressions.

---

### **Combined Power and Root Example**

Find:
\[
\lim_{x \to 3} \sqrt[4]{(2x + 1)^3}
\]

Solution:
1. Simplify the expression:
   \[
   \lim_{x \to 3} \sqrt[4]{(2x + 1)^3} = \sqrt[4]{\lim_{x \to 3} (2x + 1)^3}
   \]

2. Apply the Power Rule:
   \[
   \lim_{x \to 3} (2x + 1)^3 = (\lim_{x \to 3} (2x + 1))^3 = (2(3) + 1)^3 = 7^3 = 343
   \]

3. Apply the Root Rule:
   \[
   \sqrt[4]{343}
   \]

The final result is the fourth root of \(343\). If needed, this can be approximated numerically.

---

The **Power Rule** and **Root Rule** for limits provide a straightforward way to handle functions involving 
exponents and radicals, allowing their limits to be evaluated efficiently.




## **Calculating Limits of Rational Functions by Factoring**

When evaluating limits of rational functions, factoring is a common technique used to simplify the function, especially when the limit results in an indeterminate form like \( \frac{0}{0} \). The process often involves canceling common factors to resolve the indeterminate form.

---

### **Steps for Calculating Limits by Factoring**

1. **Substitute the limit point** into the rational function to check for indeterminate forms.
2. **Factorize the numerator and/or denominator** to simplify the expression.
3. **Cancel out common factors** in the numerator and denominator.
4. **Reevaluate the limit** with the simplified expression.

---

### **Example 1: Basic Factoring**

Evaluate:
\[
\lim_{x \to 2} \frac{x^2 - 4}{x - 2}
\]

1. **Substitute \(x = 2\):**
   \[
   \frac{2^2 - 4}{2 - 2} = \frac{0}{0} \quad (\text{indeterminate form})
   \]

2. **Factorize the numerator:**
   \[
   x^2 - 4 = (x - 2)(x + 2)
   \]

   Rewrite the function:
   \[
   \frac{x^2 - 4}{x - 2} = \frac{(x - 2)(x + 2)}{x - 2}
   \]

3. **Cancel common factors:**
   \[
   \frac{(x - 2)(x + 2)}{x - 2} = x + 2 \quad (\text{for } x \neq 2)
   \]

4. **Reevaluate the limit:**
   \[
   \lim_{x \to 2} (x + 2) = 2 + 2 = 4
   \]

**Final Answer: \(4\)**

---

### **Example 2: Factoring Both Numerator and Denominator**

Evaluate:
\[
\lim_{x \to -1} \frac{x^2 + x}{x^2 - 1}
\]

1. **Substitute \(x = -1\):**
   \[
   \frac{(-1)^2 + (-1)}{(-1)^2 - 1} = \frac{0}{0} \quad (\text{indeterminate form})
   \]

2. **Factorize numerator and denominator:**
   - Numerator: \(x^2 + x = x(x + 1)\)
   - Denominator: \(x^2 - 1 = (x - 1)(x + 1)\)

   Rewrite the function:
   \[
   \frac{x^2 + x}{x^2 - 1} = \frac{x(x + 1)}{(x - 1)(x + 1)}
   \]

3. **Cancel common factors:**
   \[
   \frac{x(x + 1)}{(x - 1)(x + 1)} = \frac{x}{x - 1} \quad (\text{for } x \neq -1, x \neq 1)
   \]

4. **Reevaluate the limit:**
   \[
   \lim_{x \to -1} \frac{x}{x - 1} = \frac{-1}{-1 - 1} = \frac{-1}{-2} = \frac{1}{2}
   \]

**Final Answer: \( \frac{1}{2} \)**

---

### **Special Considerations**

1. **Indeterminate Forms**:
   - Factoring resolves \( \frac{0}{0} \), but other forms (like \( \infty/\infty \)) may require different techniques such as dividing by the highest power.

2. **Points of Discontinuity**:
   - Canceling factors in the rational function might remove a discontinuity (a hole) at the limit point, allowing for simplification.

---

### **Example 3: Real-Life Application**

Evaluate:
\[
\lim_{x \to 3} \frac{x^3 - 27}{x^2 - 9}
\]

1. **Substitute \(x = 3\):**
   \[
   \frac{3^3 - 27}{3^2 - 9} = \frac{0}{0} \quad (\text{indeterminate form})
   \]

2. **Factorize numerator and denominator:**
   - Numerator: \(x^3 - 27 = (x - 3)(x^2 + 3x + 9)\) (difference of cubes)
   - Denominator: \(x^2 - 9 = (x - 3)(x + 3)\) (difference of squares)

   Rewrite the function:
   \[
   \frac{x^3 - 27}{x^2 - 9} = \frac{(x - 3)(x^2 + 3x + 9)}{(x - 3)(x + 3)}
   \]

3. **Cancel common factors:**
   \[
   \frac{(x - 3)(x^2 + 3x + 9)}{(x - 3)(x + 3)} = \frac{x^2 + 3x + 9}{x + 3} \quad (\text{for } x \neq 3)
   \]

4. **Reevaluate the limit:**
   \[
   \lim_{x \to 3} \frac{x^2 + 3x + 9}{x + 3} = \frac{3^2 + 3(3) + 9}{3 + 3} = \frac{9 + 9 + 9}{6} = \frac{27}{6} = 4.5
   \]

**Final Answer: \(4.5\)**

---

Using factoring to simplify limits is an essential and straightforward method to handle indeterminate forms in rational functions.





## **Complex Numbers: An Overview**

Complex numbers extend the real number system by including the square root of negative numbers. A complex number is written in the form:

\[
z = a + bi
\]

- \(a\): The **real part** (\(\text{Re}(z) = a\)).
- \(b\): The **imaginary part** (\(\text{Im}(z) = b\)).
- \(i\): The **imaginary unit**, defined as:
  \[
  i^2 = -1
  \]

---

### **Basic Operations with Complex Numbers**

1. **Addition and Subtraction**:
   - Combine real parts and imaginary parts.
   \[
   (a + bi) + (c + di) = (a + c) + (b + d)i
   \]
   \[
   (a + bi) - (c + di) = (a - c) + (b - d)i
   \]

2. **Multiplication**:
   - Use the distributive property and simplify \(i^2 = -1\).
   \[
   (a + bi)(c + di) = (ac - bd) + (ad + bc)i
   \]

3. **Division**:
   - Multiply numerator and denominator by the conjugate of the denominator.
   \[
   \frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
   \]

4. **Conjugate**:
   - The conjugate of \(z = a + bi\) is \( \overline{z} = a - bi \).

5. **Modulus**:
   - The modulus (or magnitude) of \(z = a + bi\) is:
   \[
   |z| = \sqrt{a^2 + b^2}
   \]

---

### **Graphical Representation**

A complex number can be represented on the **complex plane**, with:
- The real part on the horizontal axis.
- The imaginary part on the vertical axis.

This representation is called the **Argand diagram**.

---

### **Polar Form of Complex Numbers**

A complex number \(z = a + bi\) can also be expressed in polar form:
\[
z = r (\cos\theta + i\sin\theta)
\]
- \(r = |z| = \sqrt{a^2 + b^2}\) is the modulus.
- \(\theta = \tan^{-1}\left(\frac{b}{a}\right)\) is the argument (angle).

In shorthand, this is written using Euler's formula:
\[
z = r e^{i\theta}
\]

---

### **Key Properties**

1. **Multiplication in Polar Form**:
   \[
   z_1 \cdot z_2 = r_1r_2 e^{i(\theta_1 + \theta_2)}
   \]

2. **Division in Polar Form**:
   \[
   \frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}
   \]

3. **Power (De Moivre's Theorem)**:
   \[
   z^n = r^n (\cos n\theta + i\sin n\theta)
   \]

4. **Roots of Complex Numbers**:
   To find the \(n\)-th root of a complex number:
   \[
   z_k = r^{1/n} \left(\cos \frac{\theta + 2k\pi}{n} + i\sin \frac{\theta + 2k\pi}{n}\right) \quad \text{for } k = 0, 1, \ldots, n-1
   \]

---

### **Example Problems**

1. **Add \(z_1 = 3 + 4i\) and \(z_2 = 1 - 2i\):**
   \[
   (3 + 4i) + (1 - 2i) = (3 + 1) + (4 - 2)i = 4 + 2i
   \]

2. **Find the modulus of \(z = -1 + i\):**
   \[
   |z| = \sqrt{(-1)^2 + 1^2} = \sqrt{2}
   \]

3. **Multiply \(z_1 = 2e^{i\pi/4}\) and \(z_2 = 3e^{i\pi/6}\):**
   \[
   z_1 \cdot z_2 = (2 \cdot 3)e^{i(\pi/4 + \pi/6)} = 6e^{i5\pi/12}
   \]

---

Complex numbers are fundamental in fields like engineering, physics, and signal processing, 
as they enable elegant solutions to problems involving oscillations, waves, and two-dimensional transformations.





## **Sigma Notation: Summation Symbol**

Sigma notation, represented by the Greek letter \( \Sigma \), is a concise way to write the sum of a sequence of terms. 
It is especially useful when dealing with arithmetic, geometric sequences, or other patterns.

---

### **General Form**

\[
\sum_{k=m}^n f(k)
\]

This means:
- **\(k\):** The index of summation (dummy variable).
- **\(m\):** The lower limit of summation (starting value of \(k\)).
- **\(n\):** The upper limit of summation (ending value of \(k\)).
- **\(f(k)\):** The expression to be summed as \(k\) takes on integer values from \(m\) to \(n\).

The sum expands to:
\[
f(m) + f(m+1) + \cdots + f(n)
\]

---

### **Examples**

1. **Basic Summation**:
   \[
   \sum_{k=1}^4 k = 1 + 2 + 3 + 4 = 10
   \]

2. **Using a Formula**:
   \[
   \sum_{k=1}^3 (k^2 + 1) = (1^2 + 1) + (2^2 + 1) + (3^2 + 1) = 2 + 5 + 10 = 17
   \]

3. **Summing Constants**:
   If \(f(k) = c\), where \(c\) is a constant:
   \[
   \sum_{k=1}^n c = c + c + \cdots + c \quad (\text{\(n\) terms}) = n \cdot c
   \]

---

### **Properties of Sigma Notation**

1. **Linearity**:
   - \(\sum_{k=m}^n [f(k) + g(k)] = \sum_{k=m}^n f(k) + \sum_{k=m}^n g(k)\)
   - \(\sum_{k=m}^n c \cdot f(k) = c \cdot \sum_{k=m}^n f(k)\), where \(c\) is a constant.

2. **Index Shifting**:
   If \(j = k + c\), then:
   \[
   \sum_{k=m}^n f(k) = \sum_{j=m+c}^{n+c} f(j - c)
   \]

---

### **Common Summation Formulas**

1. **Sum of the First \(n\) Positive Integers**:
   \[
   \sum_{k=1}^n k = \frac{n(n+1)}{2}
   \]

2. **Sum of the Squares of the First \(n\) Integers**:
   \[
   \sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}
   \]

3. **Sum of the Cubes of the First \(n\) Integers**:
   \[
   \sum_{k=1}^n k^3 = \left(\frac{n(n+1)}{2}\right)^2
   \]

---

### **Applications**

1. **Arithmetic Series**:
   - General formula for the sum of an arithmetic series:
     \[
     S_n = \frac{n}{2} \cdot (a + l)
     \]
     where \(a\) is the first term, \(l\) is the last term, and \(n\) is the number of terms.

2. **Geometric Series**:
   - General formula for the sum of a geometric series:
     \[
     S_n = a \cdot \frac{1 - r^n}{1 - r} \quad (r \neq 1)
     \]
     where \(a\) is the first term, \(r\) is the common ratio, and \(n\) is the number of terms.

3. **Approximating Areas (Integral Approximation)**:
   Sigma notation is used in Riemann sums to approximate the area under a curve:
   \[
   \sum_{k=1}^n f(x_k) \Delta x
   \]

---

### **Example Problem**

Evaluate:
\[
\sum_{k=1}^5 (2k + 3)
\]

1. Expand the terms:
   \[
   (2(1) + 3) + (2(2) + 3) + (2(3) + 3) + (2(4) + 3) + (2(5) + 3)
   \]

2. Calculate each term:
   \[
   5 + 7 + 9 + 11 + 13
   \]

3. Add:
   \[
   5 + 7 + 9 + 11 + 13 = 45
   \]

**Final Answer: \(45\)**

---

Sigma notation is a powerful mathematical tool for expressing and simplifying sums, 
making it essential in calculus, statistics, and discrete mathematics.




## **Complex Numbers on the Argand Diagram**

The Argand diagram is a geometric representation of complex numbers in the complex plane. In this diagram:
- The **real part** (\(a\)) of a complex number \(z = a + bi\) is plotted on the horizontal axis (x-axis).
- The **imaginary part** (\(b\)) is plotted on the vertical axis (y-axis).

Each complex number corresponds to a unique point in this plane.

---

### **Plotting a Complex Number**

Given \(z = a + bi\):
1. Plot the point \((a, b)\) on the Cartesian plane.
2. The position represents the complex number \(z\).

---

### **Key Features of the Argand Diagram**

1. **Modulus (\(r\))**:
   The modulus of \(z = a + bi\) is the distance from the origin \((0, 0)\) to the point \((a, b)\).
   \[
   r = |z| = \sqrt{a^2 + b^2}
   \]

2. **Argument (\(\theta\))**:
   The argument of \(z = a + bi\) is the angle the line connecting the origin to the point \((a, b)\) makes with the positive x-axis, measured counterclockwise.
   \[
   \theta = \tan^{-1}\left(\frac{b}{a}\right)
   \]

3. **Polar Form**:
   A complex number can also be expressed as:
   \[
   z = r(\cos\theta + i\sin\theta)
   \]
   Or using Euler's formula:
   \[
   z = re^{i\theta}
   \]

4. **Conjugate**:
   The complex conjugate \( \overline{z} \) of \(z = a + bi\) is \(a - bi\). On the Argand diagram, this reflects the point \((a, b)\) across the real axis.

---

### **Example**

Plot \(z = 3 + 4i\) on the Argand diagram:
1. Real part (\(a = 3\)) → Mark \(3\) on the x-axis.
2. Imaginary part (\(b = 4\)) → Mark \(4\) on the y-axis.
3. Plot the point \((3, 4)\).
4. The modulus is:
   \[
   r = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5
   \]
5. The argument is:
   \[
   \theta = \tan^{-1}\left(\frac{4}{3}\right) \approx 53.13^\circ
   \]

The polar form is:
\[
z = 5 \left(\cos 53.13^\circ + i\sin 53.13^\circ \right) = 5e^{i\theta}
\]

---

### **Applications of the Argand Diagram**

1. **Addition and Subtraction**:
   - Represented as vector addition or subtraction on the diagram.

2. **Multiplication and Division**:
   - Multiplication scales and rotates the vector.
   - Division reduces the magnitude and rotates in the opposite direction.

3. **Roots and Powers**:
   - Roots of complex numbers are evenly spaced around the circle with radius equal to the \(n\)-th root of the modulus.

The Argand diagram offers a visual approach to understanding the behavior and properties of complex numbers.




## **The \(n\)-th Term of an Arithmetic Sequence**

An arithmetic sequence is a sequence of numbers where each term after the first is obtained by adding 
a constant difference (\(d\)) to the previous term. 

---

### **General Formula**

The formula for the \(n\)-th term (\(a_n\)) of an arithmetic sequence is:

\[
a_n = a_1 + (n-1)d
\]

Where:
- \(a_n\): The \(n\)-th term.
- \(a_1\): The first term of the sequence.
- \(d\): The common difference between consecutive terms.
- \(n\): The position of the term in the sequence.

---

### **Derivation of the Formula**
1. Start with the sequence: \(a_1, a_1 + d, a_1 + 2d, a_1 + 3d, \dots\).
2. The \(n\)-th term is formed by adding the common difference \(d\) \((n-1)\) times to the first term \(a_1\):
   \[
   a_n = a_1 + (n-1)d
   \]

---

### **Examples**

1. **Find the 10th term of the sequence \(3, 7, 11, 15, \dots\):**
   - \(a_1 = 3\), \(d = 7 - 3 = 4\), \(n = 10\).
   - Using the formula:
     \[
     a_{10} = 3 + (10-1) \cdot 4 = 3 + 36 = 39
     \]

2. **Given the \(n\)-th term formula \(a_n = 5 + 3(n-1)\), find the 5th term:**
   - Substitute \(n = 5\):
     \[
     a_5 = 5 + 3(5-1) = 5 + 12 = 17
     \]

---

### **Applications**

1. **Find Any Term in the Sequence**:
   The formula helps compute terms without listing all preceding terms.

2. **Solve Problems Involving Arithmetic Sequences**:
   - Example: Find the number of terms (\(n\)) in the sequence \(2, 5, 8, \dots, 50\):
     - Use \(a_n = 50\), \(a_1 = 2\), \(d = 3\):
       \[
       50 = 2 + (n-1) \cdot 3
       \]
       \[
       50 - 2 = 3(n-1) \implies 48 = 3(n-1) \implies n-1 = 16 \implies n = 17
       \]

3. **Arithmetic Means**:
   Insert intermediate terms to create an arithmetic sequence.

---

### **Sum of an Arithmetic Sequence**
The \(n\)-th term formula is also used in summing sequences:
\[
S_n = \frac{n}{2} (a_1 + a_n)
\]
Where \(a_n = a_1 + (n-1)d\).

This makes \(a_n\) fundamental in analyzing arithmetic sequences.




## **Recursive Sequences**

A **recursive sequence** is a sequence in which each term is defined in relation to one or more previous terms using a recursive formula. 

---

### **Key Components**

1. **Initial Condition(s):**
   The starting value(s) of the sequence (e.g., \(a_1\), \(a_2\), etc.).

2. **Recursive Formula:**
   A rule or function that defines each term using earlier terms in the sequence.

---

### **General Form**

For a sequence \(\{a_n\}\), the recursive formula is expressed as:
\[
a_n = f(a_{n-1}, a_{n-2}, \dots, a_{n-k})
\]
Where:
- \(a_n\): The current term.
- \(f\): The function defining the relationship.
- \(a_{n-1}, a_{n-2}, \dots\): The previous terms of the sequence.

---

### **Examples of Recursive Sequences**

1. **Arithmetic Sequence**:
   Recursive formula:
   \[
   a_n = a_{n-1} + d, \quad a_1 = c
   \]
   Example:
   - \(a_1 = 3\), \(d = 2\).
   - Sequence: \(3, 5, 7, 9, \dots\).

2. **Geometric Sequence**:
   Recursive formula:
   \[
   a_n = r \cdot a_{n-1}, \quad a_1 = c
   \]
   Example:
   - \(a_1 = 2\), \(r = 3\).
   - Sequence: \(2, 6, 18, 54, \dots\).

3. **Fibonacci Sequence**:
   Recursive formula:
   \[
   a_n = a_{n-1} + a_{n-2}, \quad a_1 = 1, \, a_2 = 1
   \]
   Sequence:
   \[
   1, 1, 2, 3, 5, 8, 13, \dots
   \]

4. **Factorial Sequence**:
   Recursive formula:
   \[
   a_n = n \cdot a_{n-1}, \quad a_1 = 1
   \]
   Example:
   - \(a_1 = 1\), \(n = 2, 3, \dots\).
   - Sequence: \(1, 2, 6, 24, 120, \dots\).

---

### **Advantages of Recursive Sequences**

1. **Compact Representation**:
   Recursive formulas are often shorter and simpler than explicit formulas.

2. **Step-by-Step Generation**:
   Recursive sequences naturally define how terms build upon each other.

3. **Applicability**:
   Many mathematical and computational problems (e.g., dynamic programming) use recursion effectively.

---

### **Finding the Explicit Formula**

To simplify analysis, it is often useful to derive the explicit formula for a recursive sequence:
- **Arithmetic Sequences**:
  Convert \(a_n = a_{n-1} + d\) into:
  \[
  a_n = a_1 + (n-1)d
  \]
- **Geometric Sequences**:
  Convert \(a_n = r \cdot a_{n-1}\) into:
  \[
  a_n = a_1 \cdot r^{n-1}
  \]

---

### **Applications**

1. **Mathematics**:
   - Modeling growth patterns (e.g., population, interest rates).
   - Studying combinatorics (e.g., Fibonacci numbers, Pascal's Triangle).

2. **Computer Science**:
   - Algorithms (e.g., divide and conquer).
   - Dynamic programming (e.g., finding the shortest path).

Recursive sequences are essential for understanding relationships between terms and modeling various phenomena.




## **Magnitude of a Complex Number**

The magnitude (or modulus) of a complex number \(z = a + bi\) is the distance from the origin \((0, 0)\) 
to the point \((a, b)\) in the complex plane. It is a measure of the "size" or absolute value of the complex number.

---

### **Formula**

The magnitude of \(z = a + bi\) is given by:
\[
|z| = \sqrt{a^2 + b^2}
\]
Where:
- \(a\): The real part of \(z\).
- \(b\): The imaginary part of \(z\).

---

### **Derivation**

Using the distance formula in a Cartesian coordinate system:
1. A complex number \(z = a + bi\) corresponds to the point \((a, b)\).
2. The distance from the origin \((0, 0)\) to \((a, b)\) is:
   \[
   \text{Distance} = \sqrt{(a - 0)^2 + (b - 0)^2} = \sqrt{a^2 + b^2}
   \]

---

### **Examples**

1. **Find the magnitude of \(z = 3 + 4i\):**
   \[
   |z| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
   \]

2. **Find the magnitude of \(z = -1 + \sqrt{3}i\):**
   \[
   |z| = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = \sqrt{4} = 2
   \]

3. **For \(z = 5\) (a purely real number):**
   \[
   |z| = \sqrt{5^2 + 0^2} = \sqrt{25} = 5
   \]

4. **For \(z = -7i\) (a purely imaginary number):**
   \[
   |z| = \sqrt{0^2 + (-7)^2} = \sqrt{49} = 7
   \]

---

### **Properties of the Magnitude**

1. **Non-Negativity**:
   \[
   |z| \geq 0, \quad \text{and } |z| = 0 \text{ if and only if } z = 0
   \]

2. **Multiplicative Property**:
   \[
   |z_1 \cdot z_2| = |z_1| \cdot |z_2|
   \]

3. **Division Property**:
   \[
   \left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}, \quad z_2 \neq 0
   \]

4. **Conjugate Property**:
   The magnitude of a complex number and its conjugate are the same:
   \[
   |z| = |\overline{z}|
   \]

5. **Additive Property** (Triangle Inequality):
   \[
   |z_1 + z_2| \leq |z_1| + |z_2|
   \]

---

### **Applications**

1. **Polar Form**:
   The magnitude is used in the polar representation of complex numbers:
   \[
   z = r(\cos\theta + i\sin\theta), \quad r = |z|
   \]

2. **Signal Processing**:
   The magnitude of complex numbers represents amplitude.

3. **Electrical Engineering**:
   Used to analyze impedance in AC circuits.

4. **Geometry**:
   Represents distance in the complex plane.

The magnitude of a complex number is fundamental in mathematics, physics, and engineering for 
analyzing and visualizing complex numbers geometrically.




##  **Multiplication of Complex Numbers**

Multiplication of complex numbers involves combining two complex numbers in the form \( z_1 = a + bi \) and \( z_2 = c + di \), where \( a, b, c, \) and \( d \) are real numbers, and \( i \) is the imaginary unit (\( i^2 = -1 \)).

---

### **Formula**

The product of two complex numbers \( z_1 \) and \( z_2 \) is given by:
\[
z_1 \cdot z_2 = (a + bi)(c + di)
\]
Expanding using the distributive property:
\[
z_1 \cdot z_2 = ac + adi + bci + bdi^2
\]
Simplify using \( i^2 = -1 \):
\[
z_1 \cdot z_2 = (ac - bd) + (ad + bc)i
\]
Thus:
\[
z_1 \cdot z_2 = \text{Real part} + \text{Imaginary part}
\]

---

### **Geometric Interpretation**

In the polar form of complex numbers:
- \( z_1 = r_1(\cos\theta_1 + i\sin\theta_1) \)
- \( z_2 = r_2(\cos\theta_2 + i\sin\theta_2) \)

The product is:
\[
z_1 \cdot z_2 = r_1 r_2 \left[\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\right]
\]

This means:
- The magnitudes (\(r_1\) and \(r_2\)) multiply.
- The angles (\(\theta_1\) and \(\theta_2\)) add.

---

### **Examples**

1. **Multiply \( z_1 = 3 + 2i \) and \( z_2 = 1 + 4i \):**

   Using the formula:
   \[
   z_1 \cdot z_2 = (3)(1) - (2)(4) + [(3)(4) + (2)(1)]i
   \]
   \[
   z_1 \cdot z_2 = 3 - 8 + (12 + 2)i
   \]
   \[
   z_1 \cdot z_2 = -5 + 14i
   \]

2. **Multiply \( z_1 = 2 - 3i \) and \( z_2 = 4 + 5i \):**

   Using the formula:
   \[
   z_1 \cdot z_2 = (2)(4) - (-3)(5) + [(2)(5) + (-3)(4)]i
   \]
   \[
   z_1 \cdot z_2 = 8 + 15 + (10 - 12)i
   \]
   \[
   z_1 \cdot z_2 = 23 - 2i
   \]

---

### **Properties of Multiplication**

1. **Commutative Property**:
   \[
   z_1 \cdot z_2 = z_2 \cdot z_1
   \]

2. **Associative Property**:
   \[
   (z_1 \cdot z_2) \cdot z_3 = z_1 \cdot (z_2 \cdot z_3)
   \]

3. **Distributive Property**:
   \[
   z_1 \cdot (z_2 + z_3) = z_1 \cdot z_2 + z_1 \cdot z_3
   \]

4. **Multiplicative Identity**:
   \[
   z \cdot 1 = z, \quad \text{where } 1 = 1 + 0i
   \]

5. **Conjugate Property**:
   The product of a complex number and its conjugate is a real number:
   \[
   z \cdot \overline{z} = a^2 + b^2, \quad z = a + bi
   \]

---

### **Applications**

1. **Rotation and Scaling**:
   Multiplication in polar form is useful in applications like signal processing, physics, and computer graphics for rotations and scaling in the complex plane.

2. **Electrical Engineering**:
   Used in phasor analysis of AC circuits.

3. **Roots of Unity**:
   Multiplication of complex numbers plays a central role in studying roots of unity and Fourier transforms.

Multiplication of complex numbers is fundamental in mathematics and engineering, 
bridging algebra and geometry through the complex plane.




## **Calculating the Mean of a Sequence Using Sigma Notation**

The mean (or average) of a sequence is calculated by summing all the terms in the sequence and dividing the sum by the total number of terms.

If a sequence is given as \(a_1, a_2, a_3, \dots, a_n\), the mean is:
\[
\text{Mean} = \frac{\text{Sum of terms}}{\text{Number of terms}} = \frac{a_1 + a_2 + \dots + a_n}{n}
\]

---

### **Using Sigma Notation**

Sigma (\(\Sigma\)) notation compactly represents the sum of the sequence:
\[
\sum_{i=1}^n a_i
\]
Where:
- \(i\): The index of summation (starting from 1 in this case).
- \(n\): The total number of terms in the sequence.
- \(a_i\): The \(i\)-th term of the sequence.

Thus, the mean can be written using sigma notation as:
\[
\text{Mean} = \frac{1}{n} \sum_{i=1}^n a_i
\]

---

### **Steps to Calculate the Mean**

1. Write the sequence terms \(a_1, a_2, \dots, a_n\).
2. Represent the sum using \(\sum_{i=1}^n a_i\).
3. Divide the sum by \(n\), the number of terms.

---

### **Examples**

1. **Find the mean of the sequence \(2, 4, 6, 8, 10\):**
   - Total number of terms: \(n = 5\)
   - Sum using sigma notation:
     \[
     \sum_{i=1}^5 a_i = 2 + 4 + 6 + 8 + 10 = 30
     \]
   - Mean:
     \[
     \text{Mean} = \frac{1}{5} \sum_{i=1}^5 a_i = \frac{30}{5} = 6
     \]

2. **Find the mean of the sequence \(a_i = 3i\) for \(i = 1\) to \(4\):**
   - Sequence terms: \(a_1 = 3(1), a_2 = 3(2), a_3 = 3(3), a_4 = 3(4)\)
     \[
     a_1 = 3, \, a_2 = 6, \, a_3 = 9, \, a_4 = 12
     \]
   - Total number of terms: \(n = 4\)
   - Sum using sigma notation:
     \[
     \sum_{i=1}^4 a_i = 3 + 6 + 9 + 12 = 30
     \]
   - Mean:
     \[
     \text{Mean} = \frac{1}{4} \sum_{i=1}^4 a_i = \frac{30}{4} = 7.5
     \]

---

### **Properties**

1. **Scaling**:
   If all terms of the sequence are multiplied by a constant \(c\), the mean is also multiplied by \(c\):
   \[
   \text{Mean of } c \cdot a_i = c \cdot \text{Mean of } a_i
   \]

2. **Additivity**:
   If two sequences are added element-wise, their means are also additive:
   \[
   \text{Mean of } (a_i + b_i) = \text{Mean of } a_i + \text{Mean of } b_i
   \]

3. **Constant Sequence**:
   If all terms are equal to \(k\), the mean is \(k\):
   \[
   \text{Mean} = \frac{1}{n} \sum_{i=1}^n k = k
   \]

---

### **Applications**

1. **Data Analysis**:
   Calculating the average of data points in statistics.

2. **Finance**:
   Determining the average return or expense.

3. **Physics**:
   Finding the average value of measurements.

Sigma notation provides a concise and powerful way to represent and compute the mean of sequences,
especially for larger datasets or algebraically defined terms.



## **Solving Quadratic Equations with Complex Roots**

A quadratic equation is expressed in the standard form:
\[
ax^2 + bx + c = 0
\]
where \(a\), \(b\), and \(c\) are real numbers, and \(a \neq 0\).

---

### **Steps to Solve for Complex Roots**

1. **Use the Quadratic Formula**:
   \[
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   \]

2. **Identify the Discriminant**:
   The discriminant is:
   \[
   \Delta = b^2 - 4ac
   \]
   - If \(\Delta < 0\), the equation has **complex roots**.

3. **Simplify for Complex Roots**:
   - Replace \(\sqrt{-1}\) with \(i\), where \(i\) is the imaginary unit.
   - For \(\Delta < 0\), write:
     \[
     \sqrt{\Delta} = \sqrt{-1 \cdot |\Delta|} = i\sqrt{|\Delta|}
     \]

4. **Write the Solution**:
   Substitute into the quadratic formula:
   \[
   x = \frac{-b \pm i\sqrt{|b^2 - 4ac|}}{2a}
   \]
   This gives two complex roots:
   \[
   x_1 = \frac{-b + i\sqrt{|b^2 - 4ac|}}{2a}, \quad x_2 = \frac{-b - i\sqrt{|b^2 - 4ac|}}{2a}
   \]

---

### **Example 1: Solve \(x^2 + 4x + 5 = 0\)**

1. Identify coefficients:
   - \(a = 1\), \(b = 4\), \(c = 5\)

2. Compute the discriminant:
   \[
   \Delta = b^2 - 4ac = 4^2 - 4(1)(5) = 16 - 20 = -4
   \]

3. Solve for \(x\) using the quadratic formula:
   \[
   x = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{-4 \pm \sqrt{-4}}{2(1)}
   \]

4. Simplify the square root of \(-4\):
   \[
   \sqrt{-4} = i\sqrt{4} = 2i
   \]

5. Write the solutions:
   \[
   x = \frac{-4 \pm 2i}{2}
   \]
   Simplify:
   \[
   x_1 = -2 + i, \quad x_2 = -2 - i
   \]

---

### **Example 2: Solve \(2x^2 + 3x + 7 = 0\)**

1. Identify coefficients:
   - \(a = 2\), \(b = 3\), \(c = 7\)

2. Compute the discriminant:
   \[
   \Delta = b^2 - 4ac = 3^2 - 4(2)(7) = 9 - 56 = -47
   \]

3. Solve for \(x\) using the quadratic formula:
   \[
   x = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{-3 \pm \sqrt{-47}}{2(2)}
   \]

4. Simplify the square root of \(-47\):
   \[
   \sqrt{-47} = i\sqrt{47}
   \]

5. Write the solutions:
   \[
   x = \frac{-3 \pm i\sqrt{47}}{4}
   \]
   Separate into two roots:
   \[
   x_1 = \frac{-3}{4} + \frac{i\sqrt{47}}{4}, \quad x_2 = \frac{-3}{4} - \frac{i\sqrt{47}}{4}
   \]

---

### **Key Points**

1. **Complex roots occur in conjugate pairs**:
   If \(x_1 = p + qi\), then \(x_2 = p - qi\).

2. **Visual Representation**:
   Complex roots can be represented as points in the complex plane with a real and imaginary part.

3. **Applications**:
   - Complex roots appear in physics, engineering, and control systems when analyzing oscillations or stability.

Mastering the process of solving quadratic equations with complex roots is essential 
for understanding higher mathematics and its applications in real-world scenarios.




## **Variance and Standard Deviation**

Variance and standard deviation are measures of **dispersion** that describe how data points in a dataset spread around the mean. 

---

### **Variance**

The variance measures the average squared deviation of data points from the mean.

1. **Population Variance (\(\sigma^2\))**:
   \[
   \sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2
   \]
   Where:
   - \(N\): Total number of data points in the population.
   - \(x_i\): The \(i\)-th data point.
   - \(\mu\): Population mean.

2. **Sample Variance (\(s^2\))**:
   \[
   s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2
   \]
   Where:
   - \(n\): Total number of data points in the sample.
   - \(x_i\): The \(i\)-th data point.
   - \(\bar{x}\): Sample mean.
   - Dividing by \(n-1\) (instead of \(n\)) corrects bias when estimating population variance from a sample.

---

### **Standard Deviation**

The standard deviation is the **square root of the variance**, providing a measure of spread in the same units as the data.

1. **Population Standard Deviation (\(\sigma\))**:
   \[
   \sigma = \sqrt{\sigma^2}
   \]

2. **Sample Standard Deviation (\(s\))**:
   \[
   s = \sqrt{s^2}
   \]

---

### **Steps to Calculate Variance and Standard Deviation**

1. Compute the mean (\(\mu\) or \(\bar{x}\)):
   \[
   \text{Mean} = \frac{\sum x_i}{N} \quad \text{(for population)}, \quad \frac{\sum x_i}{n} \quad \text{(for sample)}.
   \]

2. Subtract the mean from each data point (\(x_i - \mu\) or \(x_i - \bar{x}\)).

3. Square the deviations \((x_i - \mu)^2\).

4. Compute the average of these squared deviations:
   - For population: divide by \(N\).
   - For sample: divide by \(n-1\).

5. Take the square root of the variance to get the standard deviation.

---

### **Example**

Given data: \(2, 4, 6, 8\).

1. **Find the mean**:
   \[
   \mu = \frac{2 + 4 + 6 + 8}{4} = 5
   \]

2. **Compute deviations and their squares**:
   \[
   (x_i - \mu) = [-3, -1, 1, 3], \quad (x_i - \mu)^2 = [9, 1, 1, 9]
   \]

3. **Variance (Population)**:
   \[
   \sigma^2 = \frac{\sum (x_i - \mu)^2}{N} = \frac{9 + 1 + 1 + 9}{4} = \frac{20}{4} = 5
   \]

4. **Standard Deviation (Population)**:
   \[
   \sigma = \sqrt{\sigma^2} = \sqrt{5} \approx 2.24
   \]

5. **Sample Variance**:
   \[
   s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1} = \frac{20}{3} \approx 6.67
   \]

6. **Sample Standard Deviation**:
   \[
   s = \sqrt{s^2} = \sqrt{6.67} \approx 2.58
   \]

---

### **Key Points**

1. **Population vs. Sample**:
   - Use population formulas if working with the entire dataset.
   - Use sample formulas if working with a subset of data to estimate population values.

2. **Interpretation**:
   - A smaller standard deviation indicates data points are closer to the mean.
   - A larger standard deviation indicates data points are more spread out.

3. **Units**:
   - Variance is in squared units of the data.
   - Standard deviation is in the same units as the data.

Variance and standard deviation are foundational concepts in statistics and are widely used in data analysis, 
quality control, and scientific research to understand data variability.




## **The Nth Term of a Geometric Sequence**

A **geometric sequence** (or geometric progression) is a sequence of numbers where each term is obtained by multiplying the previous term by a constant called the **common ratio**, denoted as \(r\).

---

### **Formula for the Nth Term**

The \(n\)-th term of a geometric sequence is given by:

\[
a_n = a_1 \cdot r^{n-1}
\]

Where:
- \(a_n\): The \(n\)-th term of the sequence.
- \(a_1\): The first term of the sequence.
- \(r\): The common ratio (the factor by which each term is multiplied to get the next term).
- \(n\): The position of the term in the sequence (\(n \geq 1\)).

---

### **Steps to Find the Nth Term**

1. Identify the first term (\(a_1\)).
2. Determine the common ratio (\(r\)) by dividing any term by its preceding term:
   \[
   r = \frac{a_2}{a_1} = \frac{a_3}{a_2}, \dots
   \]
3. Substitute \(a_1\), \(r\), and \(n\) into the formula.

---

### **Examples**

#### **Example 1:**
Find the 5th term of the geometric sequence \(2, 6, 18, 54, \dots\).

1. Identify the first term (\(a_1\)):
   \[
   a_1 = 2
   \]
2. Find the common ratio (\(r\)):
   \[
   r = \frac{a_2}{a_1} = \frac{6}{2} = 3
   \]
3. Use the formula:
   \[
   a_5 = a_1 \cdot r^{5-1} = 2 \cdot 3^4
   \]
4. Simplify:
   \[
   a_5 = 2 \cdot 81 = 162
   \]

#### **Example 2:**
Find the 8th term of the geometric sequence where \(a_1 = 5\) and \(r = \frac{1}{2}\).

1. Use the formula:
   \[
   a_8 = a_1 \cdot r^{8-1} = 5 \cdot \left(\frac{1}{2}\right)^7
   \]
2. Simplify:
   \[
   a_8 = 5 \cdot \frac{1}{128} = \frac{5}{128}
   \]

---

### **Properties of Geometric Sequences**

1. **Constant Ratio**:
   Each term is multiplied by \(r\) to get the next term.

2. **Behavior of the Sequence**:
   - If \(|r| > 1\), the terms grow exponentially.
   - If \(0 < |r| < 1\), the terms decrease towards zero.
   - If \(r = -1\), the sequence alternates between two values.

3. **Infinite Geometric Sequences**:
   - For an infinite geometric sequence where \(|r| < 1\), the sum can be calculated using the formula:
     \[
     S = \frac{a_1}{1 - r}
     \]

---

### **Applications**

1. **Population Growth**: Modeling growth where each generation multiplies by a fixed factor.
2. **Finance**: Calculating compound interest.
3. **Physics**: Analyzing exponential decay or growth phenomena.

Understanding the \(n\)-th term formula is crucial for working with sequences and solving real-world problems 
involving exponential patterns.




# **3-Dimensional Shapes**
**3-dimensional shapes**, also known as **solid shapes** or **3D shapes**, are geometric figures that exist in three dimensions: length, width, and height.
They occupy space and have volume. 

Here are some common 3D shapes:

### Polyhedra
* **Cube:** A cube has six square faces, 12 edges, and 8 vertices. 
    * *Example:* A Rubik's Cube
* **Cuboid (Rectangular Prism):** A cuboid has six rectangular faces, 12 edges, and 8 vertices. 
    * *Example:* A brick, a box of cereal
* **Pyramid:** A pyramid has a polygonal base and triangular faces that meet at a common point (apex). 
    * *Example:* The Great Pyramid of Giza, a tetrahedron (a pyramid with a triangular base)
* **Prism:** A prism has two identical polygonal bases connected by rectangular faces. 
    * *Example:* A triangular prism (like a Toblerone chocolate bar), a hexagonal prism (like a honeycomb cell)

### Non-Polyhedra
* **Sphere:** A sphere is a perfectly round 3D object with all points equidistant from the center. 
    * *Example:* A ball, the Earth (approximately)
* **Cylinder:** A cylinder has two parallel circular bases connected by a curved surface. 
    * *Example:* A can of soda, a pipe
* **Cone:** A cone has a circular base and a curved surface that tapers to a point (apex). 
    * *Example:* An ice cream cone, a traffic cone





## **Polyhedron**
A polyhedron is a three-dimensional solid made up of polygons. It has flat faces, straight edges, and vertices. 
For example, a cube, prism, or pyramid are polyhedrons. Cones, spheres, and cylinders are non-polyhedrons 
because their sides are not polygons and they have curved surfaces. The plural of a polyhedron is also 
known as polyhedra.

A polyhedron is a three-dimensional shape enclosed by a finite number of polygonal faces. 
The word "polyhedron" comes from the Greek words "poly" (meaning "many") and "hedra" (meaning "faces"). 

**Key Components of a Polyhedron:**

1. **Faces:** These are the flat, polygonal surfaces that form the "skin" of the polyhedron.
2. **Edges:** These are the line segments where two faces meet.
3. **Vertices:** These are the points where three or more edges intersect.

**Types of Polyhedrons:**

* **Regular Polyhedrons (Platonic Solids):** These have faces that are identical regular polygons. 
There are only five Platonic solids:
    * **Tetrahedron:** 4 triangular faces
    * **Cube:** 6 square faces
    * **Octahedron:** 8 triangular faces
    * **Dodecahedron:** 12 pentagonal faces
    * **Icosahedron:** 20 triangular faces
  
* **Semi-Regular Polyhedrons (Archimedean Solids):** These have faces that are two or more types of regular polygons. Examples include the truncated icosahedron (soccer ball) and the cuboctahedron.
* **Prisms:** These have two parallel, congruent bases connected by parallelogram faces.
* **Pyramids:** These have a polygonal base and triangular faces that meet at a common vertex.

**Euler's Characteristic:**

A fundamental property of convex polyhedrons is described by Euler's characteristic:

**F - E + V = 2**

Where:
* F = number of faces
* E = number of edges
* V = number of vertices

This formula holds true for any convex polyhedron, regardless of its shape or size.

**Applications of Polyhedrons:**

Polyhedrons are found in various fields, including:

* **Geometry and Mathematics:** They are fundamental objects in geometry and are used to study concepts like symmetry, topology, and graph theory.
* **Chemistry:** Many molecules have polyhedral shapes, such as buckminsterfullerene (C60), which resembles a truncated icosahedron.
* **Architecture and Design:** Polyhedrons inspire the design of buildings, structures, and objects due to their unique shapes and properties.
* **Art and Crafts:** Polyhedrons are often used in art and crafts, such as paper models, sculptures, and jewelry.


## **Prism**

Prism is a three-dimensional solid object in which the two ends are identical. It is the combination of the 
flat faces, identical bases and equal cross-sections. The faces of the prism are parallelograms or rectangles 
without the bases. And the bases of the prism could be triangle, square, rectangle or any n-sided polygon. 
For example, a pentagonal prism has two pentagonal bases and 5 rectangular faces.


### Prisms Based on the Alignment of the Identical Bases.
There are two different prisms based on the alignment of the bases named:

- **Right Prism:** A right prism has two flat ends that are perfectly aligned with all the side faces 
in the shape of rectangles.

- **Oblique Prism:** An oblique prism appears to be tilted and the two flat ends are not aligned 
and the side faces are parallelograms.


### Prisms Based on the Shape of the Bases
A prism is named on the basis of the shape obtained by the cross-section of the prism. 
They are further classified as:

- **Triangular Prism:** A prism whose bases are triangle in shape is considered a triangular prism.
- **Square Prism:** A prism whose bases are square in shape is considered a square prism
- **Rectangular prism:** A prism whose bases are rectangle in shape is considered a rectangular prism (a rectangular prism is cuboidal in shape).
- **Pentagonal Prism:** A prism whose bases are pentagon in shape is considered a pentagonal prism.
- **Hexagonal Prisms:** A prism whose bases are hexagon in shape is considered a hexagonal prism.
- **Octagonal Prism:** A prism whose bases are octagon in shape is considered an octagonal prism.
- **Trapezoidal Prism:** A prism whose bases are trapezoid in shape is considered a trapezoidal prism.


## **Pyramids**
These have a polygonal base and triangular faces that meet at a common vertex.

* **Base:** The base of a pyramid is a polygon (a two-dimensional shape with straight sides). This could be a triangle, square, pentagon, or any other polygon.
* **Faces:** The sides of a pyramid are triangular faces that connect the base to a single point at the top.

**Key characteristics of pyramids as polyhedra:**

* **Convex:** The faces of a pyramid do not intersect each other, making it a convex polyhedron.
* **Regular vs. Irregular:**
    * **Regular pyramids:** The base is a regular polygon (all sides and angles are equal), and the triangular faces are congruent isosceles triangles.
    * **Irregular pyramids:** The base is an irregular polygon, or the triangular faces are not congruent.

- A triangular pyramid
- A rectangular pyramid
- A square pyramid
- A pentagonal pyramid
- A hexagonal pyramid
- An octagonal pyramid, etc.


## **A sphere**
A sphere is the set of points with the same distance to a fixed point called the center. 
A sphere is a -dimensional analog of a circle. A hemisphere is half of a sphere.


##  **A cylinder**
A cylinder is a solid shape with two parallel circular bases.
A cylinder is right if the axis that passes through the centers of the circular bases is perpendicular to the bases. Otherwise, the cylinder is oblique.


## **A cone**
A cone is a solid shape with one circular base and one vertex called the apex.
A cone is right if the axis that passes through the center of the circular base and the vertex is perpendicular to the base. Otherwise, the cone is oblique.



## **Factoring Biquadratic Expressions**
**Biquadratic expressions** are polynomials of the form:

```
ax^4 + bx^2 + c
```

where a, b, and c are constants. To factor these, we often employ a technique similar to factoring quadratic expressions.

### Steps to Factor a Biquadratic Expression:

1. **Identify the Biquadratic Expression:** Ensure the expression is in the form `ax^4 + bx^2 + c`.

2. **Substitution (Optional):**
   - Introduce a new variable, often `y`, to simplify the expression. Let `y = x^2`.
   - The biquadratic expression transforms into a quadratic equation in terms of `y`: `ay^2 + by + c`.

3. **Factor the Quadratic Equation:**
   - If the quadratic equation is factorable, find two numbers that add to `b` and multiply to `ac`.
   - Rewrite the middle term using these two numbers.
   - Factor by grouping.

4. **Back-Substitute (if applicable):**
   - Replace `y` with `x^2` in the factored quadratic equation.

5. **Factor Further (if possible):**
   - If the resulting expressions are differences of squares, factor them using the formula `a^2 - b^2 = (a + b)(a - b)`.

### Example:

Factor the biquadratic expression `x^4 - 5x^2 + 4`.

1. **Substitution:** Let `y = x^2`. The expression becomes `y^2 - 5y + 4`.

2. **Factor the Quadratic:** Find two numbers that add to -5 and multiply to 4. These numbers are -1 and -4.
   ```
   y^2 - 5y + 4 = y^2 - y - 4y + 4
                 = y(y - 1) - 4(y - 1)
                 = (y - 1)(y - 4)
   ```

3. **Back-Substitute:** Replace `y` with `x^2`:
   ```
   (y - 1)(y - 4) = (x^2 - 1)(x^2 - 4)
   ```

4. **Factor Further:** Use the difference of squares formula:
   ```
   (x^2 - 1)(x^2 - 4) = (x + 1)(x - 1)(x + 2)(x - 2)
   ```

Therefore, the factored form of `x^4 - 5x^2 + 4` is `(x + 1)(x - 1)(x + 2)(x - 2)`.

### Additional Considerations:

- **Quadratic Formula:** If the quadratic equation obtained after substitution is not easily factorable, use the quadratic formula to find its roots.
- **Synthetic Division:** For more complex biquadratic expressions, synthetic division can be used to find factors.



## **Volumes of Cylinders**

**Understanding the Volume of a Cylinder**

A cylinder is a three-dimensional shape with two parallel circular bases connected by a curved surface. 
The volume of a cylinder represents the amount of space it occupies. 

**The Formula**

The volume of a cylinder is calculated using the following formula:

```
Volume = πr²h
```

Where:
* **π (pi)** is a mathematical constant approximately equal to 3.14159.
* **r** is the radius of the circular base.
* **h** is the height of the cylinder.

**Visualizing the Formula**

Imagine stacking many thin circular disks on top of each other. The radius of each disk is the same as the radius of the cylinder's base.
The height of the cylinder is the total thickness of all the stacked disks. The volume of the cylinder is essentially 
the sum of the volumes of all these individual disks.

**Example**

Let's say we have a cylinder with a radius of 5 cm and a height of 10 cm. To find its volume:

1. **Square the radius:** 5 cm * 5 cm = 25 cm²
2. **Multiply by pi:** 25 cm² * π ≈ 78.54 cm²
3. **Multiply by the height:** 78.54 cm² * 10 cm = 785.4 cm³

Therefore, the volume of the cylinder is approximately 785.4 cubic centimeters.

**Applications of Cylinder Volume**

Understanding cylinder volume has practical applications in various fields, including:

* **Engineering:** Calculating the capacity of tanks, pipes, and other cylindrical structures.
* **Architecture:** Designing buildings and structures with cylindrical components.
* **Manufacturing:** Producing cylindrical objects like cans, bottles, and pipes.




## **Translating Between Explicit and Recursive Formulas for Geometric Sequences**

**Explicit Formula for Geometric Sequences**
The explicit formula calculates the `n-th` term directly:

$`a_n = a_1 * r^(n-1)`$

Where:
	•	`a_n`: The n-th term of the sequence
	•	`a_1`: The first term of the sequence
	•	`r`: The common ratio
	•	`n`: The term number

In function notation, it is written as:

$`f(n) = a_1 * r^(n-1)`$

**Recursive Formula for Geometric Sequences**
The recursive formula defines the sequence in terms of previous terms:

`a_1` = initial term,  
$`a_n = a_(n-1) * r`$ for n >= 2

In function notation, it is written as:

$`f(1) = a_1`$,  
$`f(n+1) = f(n) * r`$ 
for n >= 1


**Translating Between Explicit and Recursive Formulas**
From Recursive to Explicit
1.	Start with the recursive formula:

`a_1 = initial term`,  
$`a_n = a_(n-1) * r`$


2.	Generalize the relationship:

$`a_n = a_1 * r^(n-1)`$

**Example:**
Recursive formula:

`a_1 = 3`,  
$`a_n = a_(n-1) * 2`$

Explicit formula:
$`a_n = 3 * 2^(n-1)`$


**From Explicit to Recursive**
1.	Start with the explicit formula:

$`a_n = a_1 * r^(n-1)`$


2. Set the first term as:

`a_1` = given initial term


3.	Write the recursive relationship:

$`a_n = a_(n-1) * r for n >= 2`$


**Example:**
Explicit formula:

$`a_n = 5 * 3^(n-1)`$

Recursive formula:

`a_1 = 5`,  
$`a_n = a_(n-1) * 3`$


**Translation Using Function Notation**
Recursive to Explicit

Given:

`f(1) = a_1`,  
$`f(n+1) = f(n) * r`$

The explicit formula is:

$`f(n) = a_1 * r^(n-1)`$

Example:

`f(1) = 4`,  
$`f(n+1) = f(n) * 2`$

Explicit:
$`f(n) = 4 * 2^(n-1)`$

Explicit to Recursive
Given:

$`f(n) = a_1 * r^(n-1)`$

The recursive formula is:

$`f(1) = a_1`$,  
$`f(n+1) = f(n) * r`$

Example:

$`f(n) = 6 * 5^(n-1)`$

Recursive:

`f(1) = 6`,  
$`f(n+1) = f(n) * 5`$

**Summary**
- Explicit Formula: Directly computes the ￼`n-th` term without needing previous terms:

$`a_n = a_1 * r^(n-1)`$


•	`Recursive Formula`: Computes each term based on the previous one:

`a_1` = initial term,  
$`a_n = a_(n-1) * r`$ for n >= 2




## **Volume of a Sphere**
The formula for the volume of a sphere is:

$`V = \frac{4}{3} \pi r^3`$

Where:
- $`V`$: Volume of the sphere
- $`r`$: adius of the sphere
- $`\pi`$: Mathematical constant (approximately ￼)

This formula calculates the three-dimensional space occupied by the sphere. 



## **Factoring Polynomials Using the Greatest Common Factor (GCF)**
**Factoring Polynomials Using the Greatest Common Factor (GCF)** is a process of finding the largest 
common factor shared by all terms in the polynomial, and then factoring it out.

### Steps to Factor Using the GCF:

1. **Identify the GCF**:
   - The GCF is the largest number or variable (or both) that divides each term in the polynomial.
   - For each term, identify the common factors (both numerical and variable) that they share.

2. **Factor out the GCF**:
   - Once you’ve identified the GCF, factor it out of the polynomial. This involves dividing each term by the GCF and writing the result inside parentheses.

3. **Simplify**:
   - After factoring out the GCF, simplify the remaining polynomial, if needed.

### Example 1: Polynomial with Numbers

Factor the polynomial:

\[
6x^3 + 9x^2
\]

1. **Identify the GCF**:
   - The GCF of the coefficients 6 and 9 is 3.
   - Both terms contain a variable \( x^2 \), so the GCF is \( 3x^2 \).

2. **Factor out the GCF**:
   - Divide each term by \( 3x^2 \):
   
   \[
   6x^3 + 9x^2 = 3x^2(2x + 3)
   \]

3. **Simplify**:
   - The factored form is \( 3x^2(2x + 3) \).

### Example 2: Polynomial with Variables

Factor the polynomial:

\[
4x^4y^2 + 8x^3y^3
\]

1. **Identify the GCF**:
   - The GCF of the coefficients 4 and 8 is 4.
   - The common powers of \( x \) are \( x^3 \), and the common powers of \( y \) are \( y^2 \). Therefore, the GCF is \( 4x^3y^2 \).

2. **Factor out the GCF**:
   - Divide each term by \( 4x^3y^2 \):

   \[
   4x^4y^2 + 8x^3y^3 = 4x^3y^2(xy + 2y)
   \]

3. **Simplify**:
   - The factored form is \( 4x^3y^2(xy + 2y) \).

### Additional Notes:
- The GCF can be a number, a variable, or both.
- After factoring out the GCF, the remaining polynomial might still be factored further,
but if no further common factors exist, the process is complete.



## **Faces, Vertices, and Edges of Polyhedrons**
The **faces**, **vertices**, and **edges** of polyhedra are fundamental properties used to describe the structure of three-dimensional shapes. Let’s dive deeper into each property:

### **1. Faces (F)**
- **Faces** refer to the flat surfaces of a polyhedron. These surfaces are usually polygons.
- The number and shape of the faces can vary depending on the type of polyhedron.
  
  For example:
  - A **cube** has 6 square faces.
  - A **tetrahedron** has 4 triangular faces.

### **2. Vertices (V)**
- **Vertices** are the corner points where the edges of a polyhedron meet.
- Each vertex is a point in three-dimensional space where several edges converge.

  For example:
  - A **cube** has 8 vertices.
  - A **tetrahedron** has 4 vertices.

### **3. Edges (E)**
- **Edges** are the straight line segments where two faces meet. Each edge is shared by two faces.
  
  For example:
  - A **cube** has 12 edges.
  - A **tetrahedron** has 6 edges.

### **Euler's Polyhedron Formula**
Euler’s formula relates the number of faces (F), vertices (V), and edges (E) of a polyhedron:

\[
V - E + F = 2
\]

This formula holds for any convex polyhedron (a polyhedron where all its faces point outward). 

### **Examples of Common Polyhedra**

1. **Cube** (also known as a regular hexahedron):
   - Faces: 6 (all squares)
   - Vertices: 8
   - Edges: 12

2. **Tetrahedron** (a pyramid with a triangular base):
   - Faces: 4 (all triangles)
   - Vertices: 4
   - Edges: 6

3. **Octahedron** (dual of the cube):
   - Faces: 8 (all triangles)
   - Vertices: 6
   - Edges: 12

4. **Dodecahedron**:
   - Faces: 12 (all regular pentagons)
   - Vertices: 20
   - Edges: 30

5. **Icosahedron**:
   - Faces: 20 (all equilateral triangles)
   - Vertices: 12
   - Edges: 30

### Summary
- **Faces (F)**: The flat surfaces of a polyhedron.
- **Vertices (V)**: The corner points where edges meet.
- **Edges (E)**: The line segments where two faces meet.
- **Euler’s Formula**: \( V - E + F = 2 \), which holds for convex polyhedra.

Each polyhedron has a unique combination of these properties, and understanding how they relate 
to each other provides insight into their geometric structure.



## **Dilations of Figures in the Coordinate Plane**

**Dilation** is a transformation that alters the size of a figure but keeps its shape. It is defined by a **center of dilation** (a fixed point in the plane) and a **scale factor** (a constant ratio that determines the size of the dilation). In a dilation:
- If the scale factor \( k > 1 \), the figure is **enlarged**.
- If \( 0 < k < 1 \), the figure is **reduced**.
- If \( k = 1 \), the figure remains **unchanged**.
- If \( k < 0 \), the figure is both **dilated** and **reflected** about the center.

### **Steps for Performing a Dilation in the Coordinate Plane:**

1. **Identify the center of dilation**:
   The center of dilation is a point \( C(x_C, y_C) \) from which the dilation takes place. This point can be inside, outside, or on the figure.

2. **Apply the scale factor**:
   Each point of the figure is moved along the line connecting it to the center of dilation. The distance from the center to each point is multiplied by the scale factor \( k \).

3. **Dilation of a Point**:
   If a point \( P(x, y) \) is dilated with a scale factor \( k \) and a center of dilation \( C(x_C, y_C) \), the coordinates of the dilated point \( P'(x', y') \) are given by:

   \[
   x' = x_C + k(x - x_C)
   \]
   \[
   y' = y_C + k(y - y_C)
   \]

   In this formula:
   - \( (x, y) \) are the original coordinates of the point,
   - \( (x', y') \) are the coordinates of the dilated point,
   - \( (x_C, y_C) \) are the coordinates of the center of dilation,
   - \( k \) is the scale factor.

4. **Dilation of a Figure**:
   To dilate an entire figure, apply the dilation rule to each vertex (point) of the figure. Once each point is dilated, connect the new points to form the dilated figure.

### **Example: Dilation of a Triangle**

Let’s dilate a triangle with vertices \( A(1, 2) \), \( B(4, 5) \), and \( C(2, 6) \) with a center of dilation at \( O(0, 0) \) and a scale factor \( k = 2 \).

#### Step 1: Apply the formula for each vertex.

For \( A(1, 2) \):
\[
x' = 0 + 2(1 - 0) = 2, \quad y' = 0 + 2(2 - 0) = 4
\]
Thus, \( A'(2, 4) \).

For \( B(4, 5) \):
\[
x' = 0 + 2(4 - 0) = 8, \quad y' = 0 + 2(5 - 0) = 10
\]
Thus, \( B'(8, 10) \).

For \( C(2, 6) \):
\[
x' = 0 + 2(2 - 0) = 4, \quad y' = 0 + 2(6 - 0) = 12
\]
Thus, \( C'(4, 12) \).

#### Step 2: The dilated triangle has vertices \( A'(2, 4) \), \( B'(8, 10) \), and \( C'(4, 12) \).

### **Example with a Negative Scale Factor (Reflection)**

Consider dilating the same triangle \( A(1, 2) \), \( B(4, 5) \), and \( C(2, 6) \) with a center of dilation at \( O(0, 0) \) and a scale factor \( k = -2 \).

#### Step 1: Apply the formula for each vertex.

For \( A(1, 2) \):
\[
x' = 0 + (-2)(1 - 0) = -2, \quad y' = 0 + (-2)(2 - 0) = -4
\]
Thus, \( A'(-2, -4) \).

For \( B(4, 5) \):
\[
x' = 0 + (-2)(4 - 0) = -8, \quad y' = 0 + (-2)(5 - 0) = -10
\]
Thus, \( B'(-8, -10) \).

For \( C(2, 6) \):
\[
x' = 0 + (-2)(2 - 0) = -4, \quad y' = 0 + (-2)(6 - 0) = -12
\]
Thus, \( C'(-4, -12) \).

#### Step 2: The dilated triangle with \( k = -2 \) has vertices \( A'(-2, -4) \), \( B'(-8, -10) \), and \( C'(-4, -12) \).

The figure is not only enlarged but also **reflected** about the origin.

### **Summary**

- **Dilation** involves resizing a figure while maintaining its shape.
- The **center of dilation** is the fixed point from which distances are scaled.
- The **scale factor** determines how much the figure is enlarged or reduced.
- The formula for dilation of a point is:

  \[
  x' = x_C + k(x - x_C), \quad y' = y_C + k(y - y_C)
  \]

- When the scale factor \( k \) is negative, the figure is both **dilated** and **reflected** 
about the center of dilation.




## **Volumes of Rectangular Solids**

The **volume** of a rectangular solid (also known as a rectangular prism) is the amount of space it occupies. It is calculated by multiplying the dimensions of the solid: **length (\( l \))**, **width (\( w \))**, and **height (\( h \))**.

### **Volume Formula**
\[
V = l \cdot w \cdot h
\]

Where:
- \( V \) is the volume,
- \( l \) is the length,
- \( w \) is the width,
- \( h \) is the height.

### **Key Properties**
1. The volume is measured in **cubic units** (e.g., \( \text{cm}^3, \text{m}^3 \), etc.).
2. All dimensions must be in the same unit before calculating the volume.

### **Example 1: Basic Calculation**
Find the volume of a rectangular solid with:
- Length \( l = 5 \, \text{cm} \),
- Width \( w = 3 \, \text{cm} \),
- Height \( h = 4 \, \text{cm} \).

\[
V = 5 \cdot 3 \cdot 4 = 60 \, \text{cm}^3
\]

The volume is \( 60 \, \text{cm}^3 \).

---

### **Example 2: Real-World Problem**
A box has dimensions:
- Length \( l = 2 \, \text{m} \),
- Width \( w = 1.5 \, \text{m} \),
- Height \( h = 0.8 \, \text{m} \).

Find its volume.

\[
V = 2 \cdot 1.5 \cdot 0.8 = 2.4 \, \text{m}^3
\]

The box has a volume of \( 2.4 \, \text{m}^3 \).

---

### **Example 3: Missing Dimension**
If the volume of a rectangular solid is \( V = 120 \, \text{cm}^3 \), and its length and width are:
- \( l = 6 \, \text{cm} \),
- \( w = 4 \, \text{cm} \),

Find the height (\( h \)).

From the formula \( V = l \cdot w \cdot h \), solve for \( h \):

\[
h = \frac{V}{l \cdot w} = \frac{120}{6 \cdot 4} = \frac{120}{24} = 5 \, \text{cm}
\]

The height is \( h = 5 \, \text{cm} \).

---

### **Applications**
- Determining the capacity of storage boxes.
- Measuring the volume of water tanks, fish tanks, or containers.
- Engineering and architectural design.

---

### **Summary**
- The volume of a rectangular solid is calculated as:
  \[
  V = l \cdot w \cdot h
  \]
- Ensure all dimensions are in the same unit before performing calculations.
- The result is expressed in **cubic units**.




## **Closure Properties of Polynomials**

Polynomials exhibit certain closure properties under basic mathematical operations, meaning that applying these operations to polynomials will always result in another polynomial. Here are the key closure properties of polynomials:

---

### **1. Addition**
- **Property**: The sum of two polynomials is always a polynomial.
- **Why?** Adding polynomials combines like terms, and the result will still satisfy the definition of a polynomial (a finite sum of terms with non-negative integer exponents).
  
**Example**:  
\[
P(x) = 2x^3 + 3x^2 + 1, \quad Q(x) = x^3 - 4x + 5
\]
\[
P(x) + Q(x) = (2x^3 + x^3) + 3x^2 + (-4x) + (1 + 5) = 3x^3 + 3x^2 - 4x + 6
\]  
The result is a polynomial.

---

### **2. Subtraction**
- **Property**: The difference of two polynomials is always a polynomial.
- **Why?** Subtracting polynomials is equivalent to adding the opposite, which still combines like terms and satisfies the definition of a polynomial.

**Example**:  
\[
P(x) = x^4 + 2x^2 - 3, \quad Q(x) = x^3 - 5x + 4
\]
\[
P(x) - Q(x) = x^4 - x^3 + 2x^2 + 5x - 3 - 4 = x^4 - x^3 + 2x^2 + 5x - 7
\]  
The result is a polynomial.

---

### **3. Multiplication**
- **Property**: The product of two polynomials is always a polynomial.
- **Why?** Multiplying two polynomials involves distributing terms and combining like terms. The exponents of terms in the resulting polynomial are still non-negative integers.

**Example**:  
\[
P(x) = x^2 + 3x, \quad Q(x) = 2x + 5
\]
\[
P(x) \cdot Q(x) = (x^2 + 3x)(2x + 5) = 2x^3 + 5x^2 + 6x^2 + 15x = 2x^3 + 11x^2 + 15x
\]  
The result is a polynomial.

---

### **4. Division (Quotient and Remainder)**
- **Property**: The division of one polynomial by another **does not always result in a polynomial**. It depends on whether the divisor divides the dividend without leaving a remainder.
- If the result is a polynomial (no remainder), the property holds.
- If there’s a remainder, the result is a rational expression (not a polynomial).

**Example (Exact Division)**:  
\[
P(x) = x^3 + 3x^2 + 3x + 1, \quad Q(x) = x + 1
\]
\[
P(x) \div Q(x) = x^2 + 2x + 1 \quad (\text{a polynomial result})
\]

**Example (Division with Remainder)**:  
\[
P(x) = x^2 + 2, \quad Q(x) = x - 1
\]
\[
P(x) \div Q(x) = x + 1 + \frac{3}{x - 1} \quad (\text{not a polynomial due to the remainder term})
\]

---

### **5. Composition**
- **Property**: The composition of two polynomials is always a polynomial.
- **Why?** Substituting one polynomial into another and simplifying still results in a finite sum of terms with non-negative integer exponents.

**Example**:  
\[
P(x) = x^2 + 2x + 1, \quad Q(x) = 3x - 4
\]
\[
P(Q(x)) = (3x - 4)^2 + 2(3x - 4) + 1 = 9x^2 - 24x + 16 + 6x - 8 + 1 = 9x^2 - 18x + 9
\]  
The result is a polynomial.

---

### **Summary of Closure Properties**
Polynomials are **closed** under:
1. **Addition**  
2. **Subtraction**  
3. **Multiplication**  
4. **Composition**

Polynomials are **not always closed** under:
- **Division** (results may include rational expressions).

Understanding these properties is essential in algebra and higher mathematics, as it ensures predictability 
when performing operations on polynomials.



## **Factoring Cubic Expressions by Grouping**

Factoring cubic expressions by grouping involves rewriting the expression so that it can be separated into groups, where common factors can be factored out. This method is useful for expressions that don't have an immediately apparent factorization.

The general steps are:

---

### **Steps to Factor a Cubic Expression by Grouping**
1. **Rewrite the expression** in groups of two terms (or more, depending on the problem).
2. **Factor out the greatest common factor (GCF)** from each group.
3. If the resulting groups share a common binomial factor, factor it out.
4. Multiply the factors to confirm the original cubic expression.

---

### **Example 1: Basic Factoring by Grouping**
Factor \( x^3 + 3x^2 + x + 3 \).

#### Step 1: Group the terms
\[
x^3 + 3x^2 + x + 3 \quad \Rightarrow \quad (x^3 + 3x^2) + (x + 3)
\]

#### Step 2: Factor out the GCF from each group
\[
x^2(x + 3) + 1(x + 3)
\]

#### Step 3: Factor out the common binomial factor
\[
(x + 3)(x^2 + 1)
\]

The factored form is:
\[
(x + 3)(x^2 + 1)
\]

---

### **Example 2: Slightly Complex Expression**
Factor \( 2x^3 + 3x^2 - 2x - 3 \).

#### Step 1: Group the terms
\[
2x^3 + 3x^2 - 2x - 3 \quad \Rightarrow \quad (2x^3 + 3x^2) - (2x + 3)
\]

#### Step 2: Factor out the GCF from each group
\[
x^2(2x + 3) - 1(2x + 3)
\]

#### Step 3: Factor out the common binomial factor
\[
(2x + 3)(x^2 - 1)
\]

#### Step 4: Fully factor if possible
The second factor, \( x^2 - 1 \), is a difference of squares:
\[
x^2 - 1 = (x - 1)(x + 1)
\]

So, the completely factored form is:
\[
(2x + 3)(x - 1)(x + 1)
\]

---

### **Example 3: Factoring with Coefficients**
Factor \( 6x^3 + 9x^2 + 4x + 6 \).

#### Step 1: Group the terms
\[
6x^3 + 9x^2 + 4x + 6 \quad \Rightarrow \quad (6x^3 + 9x^2) + (4x + 6)
\]

#### Step 2: Factor out the GCF from each group
\[
3x^2(2x + 3) + 2(2x + 3)
\]

#### Step 3: Factor out the common binomial factor
\[
(2x + 3)(3x^2 + 2)
\]

The factored form is:
\[
(2x + 3)(3x^2 + 2)
\]

---

### **Key Tips for Factoring by Grouping**
1. Look for natural groupings in the expression (first two terms, last two terms, etc.).
2. Always check for a **common factor** before starting.
3. After grouping, ensure that the factored terms share a common binomial factor.
4. Simplify further if possible (e.g., difference of squares).

This method is especially helpful for factoring cubic polynomials that don't fit standard patterns
like sum or difference of cubes.



## **Roots of Rational Functions**

A **rational function** is a function of the form:

\[
R(x) = \frac{P(x)}{Q(x)}
\]

Where:
- \( P(x) \) and \( Q(x) \) are polynomials.
- \( Q(x) \neq 0 \) to avoid undefined values.

The **roots of a rational function** are the values of \( x \) for which the numerator \( P(x) = 0 \), provided the denominator \( Q(x) \neq 0 \).

---

### **Steps to Find the Roots of a Rational Function**
1. **Set the numerator equal to zero**:
   \[
   P(x) = 0
   \]
   Solve for \( x \) to find potential roots.
2. **Check for restrictions from the denominator**:
   Exclude any \( x \)-values that make \( Q(x) = 0 \) because these are vertical asymptotes or undefined points, not roots.

---

### **Example 1: Basic Rational Function**
Find the roots of:
\[
R(x) = \frac{x^2 - 4}{x + 3}
\]

#### Step 1: Set the numerator equal to zero
The numerator is \( P(x) = x^2 - 4 \). Solve:
\[
x^2 - 4 = 0
\]
\[
(x - 2)(x + 2) = 0
\]
\[
x = 2 \quad \text{or} \quad x = -2
\]

#### Step 2: Check the denominator
The denominator is \( Q(x) = x + 3 \). Solve:
\[
x + 3 = 0 \quad \Rightarrow \quad x = -3
\]

#### Step 3: Exclude restricted values
Since \( x = -3 \) makes the denominator zero, it is not a root.

**Roots of \( R(x) \): \( x = 2 \) and \( x = -2 \)**.

---

### **Example 2: More Complex Rational Function**
Find the roots of:
\[
R(x) = \frac{x^3 - 2x}{x^2 - 5x + 6}
\]

#### Step 1: Set the numerator equal to zero
The numerator is \( P(x) = x^3 - 2x \). Factor:
\[
x(x^2 - 2) = 0
\]
\[
x = 0 \quad \text{or} \quad x = \pm\sqrt{2}
\]

#### Step 2: Check the denominator
The denominator is \( Q(x) = x^2 - 5x + 6 \). Factor:
\[
x^2 - 5x + 6 = (x - 2)(x - 3)
\]
\[
x = 2 \quad \text{or} \quad x = 3
\]

#### Step 3: Exclude restricted values
The roots of \( P(x) = 0 \) are \( x = 0, \pm\sqrt{2} \). However, \( x = 2 \) and \( x = 3 \) make \( Q(x) = 0 \), so these values are excluded.

**Roots of \( R(x) \): \( x = 0, \pm\sqrt{2} \)**.

---

### **Graphical Interpretation**
- The roots of a rational function correspond to the **x-intercepts** of its graph.
- These are the points where the graph crosses or touches the \( x \)-axis (\( y = 0 \)).
- Values that make \( Q(x) = 0 \) correspond to **vertical asymptotes** or undefined points.

---

### **Summary**
- To find the roots of a rational function, solve \( P(x) = 0 \).
- Exclude any \( x \)-values that make \( Q(x) = 0 \) because the function is undefined at these points.
- Roots represent the x-values where the function equals zero, and they provide critical insights into the function's behavior and graph.





## **Stretches of Geometric Figures**

A **stretch** in geometry is a type of transformation that enlarges or shrinks a figure in one direction (horizontal or vertical) while leaving the other direction unchanged. It changes the shape of the figure but preserves parallelism and collinearity of points.

---

### **Key Characteristics of Stretches**
1. **One-directional scaling**: A stretch affects only one dimension (x or y), unlike dilations, which scale uniformly in all directions.
2. **Proportional scaling**: Distances in the affected direction are multiplied by a constant factor, known as the **stretch factor**.
3. **Shape distortion**: A stretch distorts the figure, often elongating or compressing it.

---

### **Types of Stretches**
1. **Horizontal Stretch**:
   - Scales the figure along the x-axis.
   - Each \( x \)-coordinate is multiplied by a stretch factor \( k \), while \( y \)-coordinates remain unchanged.
   - Transformation rule:
     \[
     (x, y) \to (kx, y)
     \]

2. **Vertical Stretch**:
   - Scales the figure along the y-axis.
   - Each \( y \)-coordinate is multiplied by a stretch factor \( k \), while \( x \)-coordinates remain unchanged.
   - Transformation rule:
     \[
     (x, y) \to (x, ky)
     \]

---

### **Examples**
#### **Horizontal Stretch**
Stretch a triangle with vertices \( A(1, 2) \), \( B(3, 4) \), \( C(5, 0) \) by a factor of \( k = 2 \) along the x-axis.

**Original vertices**:  
\[
A(1, 2), \, B(3, 4), \, C(5, 0)
\]

**Stretched vertices**:  
\[
A'(2, 2), \, B'(6, 4), \, C'(10, 0)
\]

**Transformation**: Multiply each \( x \)-coordinate by 2.

#### **Vertical Stretch**
Stretch a square with vertices \( P(0, 0) \), \( Q(2, 0) \), \( R(2, 2) \), \( S(0, 2) \) by a factor of \( k = 3 \) along the y-axis.

**Original vertices**:  
\[
P(0, 0), \, Q(2, 0), \, R(2, 2), \, S(0, 2)
\]

**Stretched vertices**:  
\[
P'(0, 0), \, Q'(2, 0), \, R'(2, 6), \, S'(0, 6)
\]

**Transformation**: Multiply each \( y \)-coordinate by 3.

---

### **Key Differences from Other Transformations**
1. **Stretch vs. Dilation**:
   - A stretch affects only one dimension, while a dilation scales the figure uniformly in all directions.
   - Stretch factors may be different for horizontal and vertical directions.

2. **Stretch vs. Shear**:
   - A stretch scales coordinates, but a shear shifts coordinates to form a slanted shape without changing lengths in one direction.

---

### **Applications of Stretches**
- Modeling physical distortions (e.g., elongating an object).
- Scaling axes in graphs for better visualization.
- Understanding geometric transformations in computer graphics and design.

Stretches are powerful tools in geometry, allowing for controlled alterations of shapes while maintaining essential relationships between points.




## **Surface Areas of Polyhedrons Using Nets**

A **polyhedron** is a 3D solid with flat polygonal faces, straight edges, and vertices. Examples include cubes, rectangular prisms, pyramids, and other 3D solids. Calculating the surface area of a polyhedron involves summing the areas of all its faces.

A **net** is a 2D representation of a 3D polyhedron, where all the faces are unfolded into a flat layout. Using nets makes it easier to calculate surface area by breaking the problem into smaller, manageable pieces.

---

### **Steps to Calculate Surface Area Using Nets**
1. **Draw or visualize the net**:
   - Identify all the faces of the polyhedron and arrange them in a flat layout.
   - Ensure all faces are accounted for in the net.

2. **Identify the shapes of the faces**:
   - Determine the type of polygon for each face (e.g., rectangles, triangles).

3. **Calculate the area of each face**:
   - Use appropriate area formulas for the shapes (e.g., \( \text{Area of a rectangle} = \text{length} \times \text{width} \)).

4. **Add the areas together**:
   - Sum the areas of all the faces to find the total surface area of the polyhedron.

---

### **Example 1: Surface Area of a Cube**
#### Given:
A cube has side length \( s = 4 \).

#### Step 1: Draw the net of the cube
The net consists of 6 square faces.

#### Step 2: Calculate the area of one face
Each face is a square:
\[
\text{Area of one face} = s^2 = 4^2 = 16
\]

#### Step 3: Add the areas of all faces
\[
\text{Total Surface Area} = 6 \times 16 = 96
\]

The surface area of the cube is:
\[
96 \, \text{square units}
\]

---

### **Example 2: Surface Area of a Rectangular Prism**
#### Given:
A rectangular prism has dimensions \( \text{length} = 5 \), \( \text{width} = 3 \), and \( \text{height} = 2 \).

#### Step 1: Draw the net of the prism
The net consists of:
- 2 rectangles for the top and bottom (\( 5 \times 3 \)),
- 2 rectangles for the front and back (\( 5 \times 2 \)),
- 2 rectangles for the left and right sides (\( 3 \times 2 \)).

#### Step 2: Calculate the area of each type of face
- Top and bottom: \( 2 \times (5 \times 3) = 30 \)
- Front and back: \( 2 \times (5 \times 2) = 20 \)
- Left and right sides: \( 2 \times (3 \times 2) = 12 \)

#### Step 3: Add the areas together
\[
\text{Total Surface Area} = 30 + 20 + 12 = 62
\]

The surface area of the rectangular prism is:
\[
62 \, \text{square units}
\]

---

### **Example 3: Surface Area of a Triangular Pyramid**
#### Given:
A triangular pyramid has:
- A triangular base with base length \( b = 6 \) and height \( h = 4 \),
- 3 triangular lateral faces, each with base \( b = 6 \) and height \( h = 5 \).

#### Step 1: Draw the net of the pyramid
The net consists of:
- 1 triangular base,
- 3 triangular lateral faces.

#### Step 2: Calculate the area of the base
The base is a triangle:
\[
\text{Area of base} = \frac{1}{2} \times b \times h = \frac{1}{2} \times 6 \times 4 = 12
\]

#### Step 3: Calculate the area of the lateral faces
Each lateral face is a triangle:
\[
\text{Area of one lateral face} = \frac{1}{2} \times b \times h = \frac{1}{2} \times 6 \times 5 = 15
\]
The total area of the lateral faces is:
\[
3 \times 15 = 45
\]

#### Step 4: Add the areas together
\[
\text{Total Surface Area} = 12 + 45 = 57
\]

The surface area of the triangular pyramid is:
\[
57 \, \text{square units}
\]

---

### **Formulas for Common Polyhedrons**
1. **Cube**:
   \[
   \text{Surface Area} = 6s^2
   \]
   where \( s \) is the side length.

2. **Rectangular Prism**:
   \[
   \text{Surface Area} = 2lw + 2lh + 2wh
   \]
   where \( l, w, h \) are the length, width, and height.

3. **Triangular Prism**:
   \[
   \text{Surface Area} = \text{Base Area} + \text{Lateral Face Areas}
   \]

4. **Pyramids**:
   \[
   \text{Surface Area} = \text{Base Area} + \text{Sum of Areas of Triangular Faces}
   \]

Using nets simplifies visualization and ensures all faces are included in the surface area calculation.





## **Finding the Common Ratio of a Geometric Sequence Given Two Terms**

In a **geometric sequence**, each term is obtained by multiplying the previous term by a constant 
called the **common ratio**, denoted by \( r \). The general form of a geometric sequence is:

\[
a, ar, ar^2, ar^3, \dots
\]

Where:
- \( a \) is the first term,
- \( r \) is the common ratio.

To find the common ratio given two terms of the sequence, follow these steps:

---

### **Formula to Find the Common Ratio**
If two terms of a geometric sequence are given, say the \( m \)-th term (\( a_m \)) and the \( n \)-th term (\( a_n \)), then the common ratio \( r \) is:

\[
r = \sqrt[k]{\frac{a_n}{a_m}}
\]

Where:
- \( k = n - m \) is the number of terms between \( a_m \) and \( a_n \).

---

### **Steps**
1. Identify the two terms of the sequence, \( a_m \) and \( a_n \), along with their positions \( m \) and \( n \).
2. Calculate the difference \( k = n - m \).
3. Substitute the values of \( a_m \), \( a_n \), and \( k \) into the formula to find \( r \).

---

### **Example 1: Given \( a_2 = 6 \) and \( a_5 = 48 \), find \( r \).**

#### Step 1: Identify terms and their positions
- \( a_2 = 6 \),
- \( a_5 = 48 \),
- \( m = 2 \),
- \( n = 5 \).

#### Step 2: Find the number of terms between \( a_2 \) and \( a_5 \)
\[
k = n - m = 5 - 2 = 3
\]

#### Step 3: Apply the formula
\[
r = \sqrt[3]{\frac{a_5}{a_2}}
\]
\[
r = \sqrt[3]{\frac{48}{6}} = \sqrt[3]{8} = 2
\]

The common ratio is:
\[
r = 2
\]

---

### **Example 2: Given \( a_1 = 4 \) and \( a_4 = 1 \), find \( r \).**

#### Step 1: Identify terms and their positions
- \( a_1 = 4 \),
- \( a_4 = 1 \),
- \( m = 1 \),
- \( n = 4 \).

#### Step 2: Find the number of terms between \( a_1 \) and \( a_4 \)
\[
k = n - m = 4 - 1 = 3
\]

#### Step 3: Apply the formula
\[
r = \sqrt[3]{\frac{a_4}{a_1}}
\]
\[
r = \sqrt[3]{\frac{1}{4}}
\]

The common ratio is:
\[
r = \frac{1}{\sqrt[3]{4}}
\]

---

### **Example 3: General Formula Derivation**

If \( a_m \) and \( a_n \) are terms of the sequence, then:

\[
a_n = a_m \cdot r^k, \quad \text{where } k = n - m
\]

Solve for \( r \):
\[
r^k = \frac{a_n}{a_m}
\]
\[
r = \sqrt[k]{\frac{a_n}{a_m}}
\]

---

### **Key Notes**
- If \( r > 1 \), the sequence grows exponentially.
- If \( 0 < r < 1 \), the sequence decreases exponentially.
- If \( r < 0 \), the sequence alternates between positive and negative terms.

This method works for any two terms of a geometric sequence, provided their positions and values are known.




## **Surface Area of a Sphere**

The **surface area** of a sphere is the total area of its outer surface. 
It is calculated using the following formula:

\[
S = 4 \pi r^2
\]

Where:
- \( S \) is the surface area,
- \( r \) is the radius of the sphere,
- \( \pi \) (pi) is approximately \( 3.14159 \).

---

### **Understanding the Formula**
- The term \( r^2 \) accounts for the square of the radius.
- The \( 4\pi r^2 \) comes from integrating the area of infinitesimally small surface elements over the sphere.

---

### **Example Calculations**
#### **Example 1: Find the surface area of a sphere with radius \( r = 5 \) units.**
\[
S = 4 \pi r^2
\]
Substitute \( r = 5 \):
\[
S = 4 \pi (5)^2 = 4 \pi (25) = 100 \pi
\]
Using \( \pi \approx 3.14159 \):
\[
S \approx 100 \times 3.14159 = 314.16 \, \text{square units.}
\]

#### **Example 2: A sphere has a surface area of \( 154 \pi \) square units. Find its radius.**
Given:
\[
S = 4 \pi r^2 = 154 \pi
\]
Cancel \( \pi \):
\[
4 r^2 = 154
\]
Solve for \( r^2 \):
\[
r^2 = \frac{154}{4} = 38.5
\]
Take the square root:
\[
r = \sqrt{38.5} \approx 6.2 \, \text{units.}
\]

---

### **Key Insights**
1. **Doubling the Radius**:
   If the radius of a sphere is doubled, the surface area increases by a factor of 4. This is because surface area is proportional to the square of the radius.

2. **Halving the Radius**:
   If the radius is halved, the surface area decreases to one-fourth.

---

### **Applications**
- Calculating the amount of material needed to cover a spherical object (e.g., wrapping a ball).
- Determining the paint required for coating spherical surfaces.
- Used in geometry, physics, and engineering problems involving spheres.




## **Dividing Polynomials Using Synthetic Division**

**Synthetic division** is a simplified process for dividing a polynomial by a binomial of the form \( x - c \). It is faster and more efficient than long division for this type of division. 

---

### **Steps for Synthetic Division**
1. **Write the coefficients** of the dividend polynomial:
   - Arrange the terms in descending order of degree.
   - Use \( 0 \) for any missing terms.

2. **Set up the divisor**:
   - If dividing by \( x - c \), write \( c \) (the opposite sign of the constant in the divisor).

3. **Perform the synthetic division**:
   - Bring down the leading coefficient to the bottom row.
   - Multiply the value in the bottom row by \( c \) and place the result in the next column of the top row.
   - Add the values in the column and repeat the process.

4. **Interpret the result**:
   - The last value in the bottom row is the **remainder**.
   - The other values in the bottom row represent the coefficients of the quotient polynomial.

---

### **Example 1: Divide \( 2x^3 + 3x^2 - 4x + 5 \) by \( x - 2 \)**

#### Step 1: Write the coefficients of the dividend:
\[
2, 3, -4, 5
\]

#### Step 2: Write the value of \( c \) (from \( x - 2 \)):
\[
c = 2
\]

#### Step 3: Set up the synthetic division:
\[
\begin{array}{r|rrrr}
2 & 2 & 3 & -4 & 5 \\
  &   & 4 & 14 & 20 \\
\hline
  & 2 & 7 & 10 & 25 \\
\end{array}
\]

- Bring down the \( 2 \) (the leading coefficient).
- Multiply \( 2 \times 2 = 4 \) and add to \( 3 \) to get \( 7 \).
- Multiply \( 7 \times 2 = 14 \) and add to \( -4 \) to get \( 10 \).
- Multiply \( 10 \times 2 = 20 \) and add to \( 5 \) to get \( 25 \).

#### Step 4: Write the result:
- Quotient: \( 2x^2 + 7x + 10 \)
- Remainder: \( 25 \)

The result of the division is:
\[
2x^2 + 7x + 10 + \frac{25}{x - 2}
\]

---

### **Example 2: Divide \( 3x^4 - 2x^3 + x - 7 \) by \( x + 1 \)**

#### Step 1: Write the coefficients of the dividend:
\[
3, -2, 0, 1, -7
\]

#### Step 2: Write the value of \( c \) (from \( x + 1 \)):
\[
c = -1
\]

#### Step 3: Set up the synthetic division:
\[
\begin{array}{r|rrrrr}
-1 & 3 & -2 & 0 & 1 & -7 \\
   &   & -3 & 5 & -5 & 4 \\
\hline
   & 3 & -5 & 5 & -4 & -3 \\
\end{array}
\]

- Bring down the \( 3 \) (the leading coefficient).
- Multiply \( 3 \times -1 = -3 \) and add to \( -2 \) to get \( -5 \).
- Multiply \( -5 \times -1 = 5 \) and add to \( 0 \) to get \( 5 \).
- Multiply \( 5 \times -1 = -5 \) and add to \( 1 \) to get \( -4 \).
- Multiply \( -4 \times -1 = 4 \) and add to \( -7 \) to get \( -3 \).

#### Step 4: Write the result:
- Quotient: \( 3x^3 - 5x^2 + 5x - 4 \)
- Remainder: \( -3 \)

The result of the division is:
\[
3x^3 - 5x^2 + 5x - 4 - \frac{3}{x + 1}
\]

---

### **When to Use Synthetic Division**
- The divisor must be of the form \( x - c \).
- If the divisor is not in this form (e.g., \( 2x - 3 \)), divide by the leading coefficient first.

---

### **Advantages of Synthetic Division**
- Faster and simpler than polynomial long division.
- Requires only basic arithmetic operations.

---

### **Key Notes**
1. **Remainder Theorem**:
   - The remainder when dividing \( P(x) \) by \( x - c \) is \( P(c) \).
2. **Factor Theorem**:
   - If the remainder is \( 0 \), \( x - c \) is a factor of \( P(x) \).

Synthetic division is a powerful and efficient tool for working with polynomials, especially in algebraic 
and calculus contexts.




## **Determining the Index of a Term in a Geometric Sequence**

A **geometric sequence** is a sequence where each term is obtained by multiplying the previous term by a constant, called the **common ratio** (\(r\)). The formula for the \(n\)-th term of a geometric sequence is:

\[
a_n = a_1 \cdot r^{n-1}
\]

Where:
- \(a_n\) is the \(n\)-th term,
- \(a_1\) is the first term,
- \(r\) is the common ratio,
- \(n\) is the index (or position) of the term.

---

### **Finding the Index of a Term**

If you are given:
1. The value of the \(n\)-th term (\(a_n\)),
2. The first term (\(a_1\)),
3. The common ratio (\(r\)),

You can solve for \(n\) using the formula:
\[
n = 1 + \log_r\left(\frac{a_n}{a_1}\right)
\]

This formula comes from solving \(a_n = a_1 \cdot r^{n-1}\) for \(n\).

---

### **Steps to Determine \(n\):**
1. **Write down the geometric sequence formula**:
   \[
   a_n = a_1 \cdot r^{n-1}
   \]

2. **Divide both sides by \(a_1\):**
   \[
   \frac{a_n}{a_1} = r^{n-1}
   \]

3. **Take the logarithm base \(r\) of both sides:**
   \[
   \log_r\left(\frac{a_n}{a_1}\right) = n - 1
   \]

4. **Solve for \(n\):**
   \[
   n = 1 + \log_r\left(\frac{a_n}{a_1}\right)
   \]

---

### **Example 1: Find the index of term \(a_n = 81\) in the sequence \(3, 6, 12, \dots\)**

#### Step 1: Identify the given values
- \(a_1 = 3\),
- \(r = \frac{6}{3} = 2\),
- \(a_n = 81\).

#### Step 2: Use the formula to solve for \(n\)
\[
n = 1 + \log_2\left(\frac{81}{3}\right)
\]

Simplify:
\[
n = 1 + \log_2(27)
\]

#### Step 3: Express \(27\) as a power of \(2\)
\[
27 = 2^{\log_2(27)} \approx 2^{4.7549}
\]

Thus:
\[
n = 1 + 4.7549 = 5.7549
\]

The term \(81\) is close to position \(n = 5.75\).

---



##  **Scatter Plots**

A **scatter plot** is a graphical representation of data points on a two-dimensional Cartesian coordinate system. It is used to observe relationships, 
patterns, and trends between two variables.

---

### **Key Features**
1. **Axes**: 
   - The horizontal axis (\(x\)-axis) represents the independent variable.
   - The vertical axis (\(y\)-axis) represents the dependent variable.

2. **Data Points**:
   - Each point \((x, y)\) on the scatter plot corresponds to a single observation.

3. **Correlation**:
   - Scatter plots can show whether two variables have a positive, negative, or no correlation.

---

### **Steps to Create a Scatter Plot**
1. **Collect Data**:
   - Gather pairs of values for the two variables you want to analyze.
   
2. **Set Axes**:
   - Determine the range and scale for both the \(x\)-axis and \(y\)-axis.

3. **Plot Points**:
   - For each pair of values, mark a point at the corresponding \((x, y)\) location on the graph.

4. **Analyze**:
   - Observe the distribution of points to determine patterns or trends.

---

### **Interpreting Scatter Plots**
- **Positive Correlation**: As \(x\) increases, \(y\) also increases. Points tend to slope upwards.
- **Negative Correlation**: As \(x\) increases, \(y\) decreases. Points tend to slope downwards.
- **No Correlation**: There is no apparent pattern in the points.
- **Outliers**: Data points that fall far from the general trend.

---

### **Example**
#### Data:
| \(x\) (Hours Studied) | \(y\) (Test Scores) |
|-----------------------|---------------------|
| 1                     | 50                  |
| 2                     | 60                  |
| 3                     | 70                  |
| 4                     | 80                  |
| 5                     | 90                  |

#### Scatter Plot:
- The \(x\)-axis represents "Hours Studied."
- The \(y\)-axis represents "Test Scores."
- Plot the points \((1, 50), (2, 60), (3, 70), (4, 80), (5, 90)\).

---

### **Applications**
- **Data Analysis**: Identifying trends or patterns.
- **Statistics**: Examining the correlation between variables.
- **Science and Engineering**: Visualizing experimental results.
- **Business**: Observing sales trends, performance metrics, etc.

---

### **Enhancements**
1. **Trend Line**:
   - Add a line of best fit to quantify the relationship (e.g., linear regression).
2. **Color Coding**:
   - Use colors to group or categorize data points.
3. **Interactive Features**:
   - Enable zooming, hovering, or filtering in digital scatter plots for detailed analysis.

Scatter plots are fundamental tools for visualizing relationships between variables and deriving insights from data.




## **Vertical Asymptotes of Radical Functions**

Vertical asymptotes are vertical lines where a function approaches infinity (\(+\infty\)) or negative infinity (\(-\infty\)) as the input value approaches a certain point. For radical functions, vertical asymptotes often occur due to:

1. **Division by Zero**: A term in the denominator approaches zero.
2. **Domain Restrictions**: The expression under a radical becomes undefined for real numbers (e.g., square root of a negative number).

---

### **Steps to Determine Vertical Asymptotes of Radical Functions**

1. **Identify the Domain**:
   - For a square root (\( \sqrt{f(x)} \)), \( f(x) \geq 0 \).
   - For even roots, ensure the radicand (expression under the root) is non-negative.

2. **Simplify the Function**:
   - If the function has a denominator, determine where the denominator equals zero.

3. **Check the Limits**:
   - Evaluate the behavior of the function as \( x \) approaches values that make the denominator zero or the radicand undefined.

4. **Confirm Vertical Asymptotes**:
   - If the function tends to \( \pm\infty \) as \( x \) approaches a certain value, that value is a vertical asymptote.

---

### **Example 1: Vertical Asymptotes in a Rational Radical Function**

Consider the function:
\[
f(x) = \frac{\sqrt{x}}{x - 3}
\]

#### Step 1: Identify the Domain
- The square root \( \sqrt{x} \) requires \( x \geq 0 \).
- The denominator \( x - 3 \neq 0 \), so \( x \neq 3 \).

Domain: \( x \geq 0 \) and \( x \neq 3 \).

#### Step 2: Check for Vertical Asymptotes
- At \( x = 3 \), the denominator becomes zero.

#### Step 3: Evaluate Limits
\[
\lim_{x \to 3^+} f(x) = \frac{\sqrt{3}}{3 - 3} \to +\infty
\]
\[
\lim_{x \to 3^-} f(x) = \frac{\sqrt{3}}{3 - 3} \to -\infty
\]

#### Conclusion
There is a vertical asymptote at \( x = 3 \).

---

### **Example 2: Vertical Asymptotes in a Pure Radical Function**

Consider the function:
\[
f(x) = \frac{1}{\sqrt{x - 2}}
\]

#### Step 1: Identify the Domain
- The square root \( \sqrt{x - 2} \) requires \( x - 2 > 0 \), so \( x > 2 \).

Domain: \( x > 2 \).

#### Step 2: Check for Vertical Asymptotes
- At \( x = 2 \), the square root \( \sqrt{x - 2} \to 0 \) in the denominator.

#### Step 3: Evaluate Limits
\[
\lim_{x \to 2^+} f(x) = \frac{1}{\sqrt{x - 2}} \to +\infty
\]

#### Conclusion
There is a vertical asymptote at \( x = 2 \).

---

### **Key Notes**
1. **Odd Roots**:
   - Odd roots (e.g., cube roots) have no domain restrictions for the radicand, so vertical asymptotes do not occur due to the root.

2. **Even Roots**:
   - Vertical asymptotes may arise from the radicand becoming zero or negative.

3. **Compound Functions**:
   - For functions combining radicals and rational expressions, carefully analyze both the radicand and the denominator.

---

### **Summary**
To find vertical asymptotes in radical functions:
1. Identify restrictions due to division by zero or undefined radicals.
2. Analyze the function's behavior near the restricted points.
3. Confirm vertical asymptotes where the function approaches \( \pm\infty \).



# An asymptote is a line that a function gets very close to but never touches.


## **The Factor Theorem**

The **Factor Theorem** is a fundamental result in algebra that connects polynomial division, factors, and roots. It states:

---

### **Statement**
If \(f(x)\) is a polynomial:
1. \(x - c\) is a factor of \(f(x)\) **if and only if** \(f(c) = 0\).
2. Conversely, if \(f(c) = 0\), then \(x - c\) is a factor of \(f(x)\).

---

### **Applications**
1. **Checking Factors**: The theorem is used to determine if a given linear expression \(x - c\) is a factor of a polynomial \(f(x)\).
2. **Finding Roots**: If \(f(c) = 0\), \(c\) is a root (or zero) of the polynomial.
3. **Factoring Polynomials**: It helps in breaking down a polynomial into its factors using its roots.

---

### **Example 1: Verify a Factor**
Given \(f(x) = x^3 - 4x^2 + 5x - 2\), check if \(x - 1\) is a factor.

#### Step 1: Substitute \(c = 1\) into \(f(x)\):
\[
f(1) = (1)^3 - 4(1)^2 + 5(1) - 2 = 1 - 4 + 5 - 2 = 0
\]

#### Step 2: Conclusion
Since \(f(1) = 0\), \(x - 1\) is a factor of \(f(x)\).

---

### **Example 2: Factor a Polynomial**
Factor \(f(x) = x^3 - 4x^2 + 5x - 2\) using the Factor Theorem.

#### Step 1: Find a Root
From Example 1, \(x - 1\) is a factor, and \(x = 1\) is a root.

#### Step 2: Divide the Polynomial
Perform synthetic or long division of \(f(x)\) by \(x - 1\) to get:
\[
f(x) = (x - 1)(x^2 - 3x + 2)
\]

#### Step 3: Factor the Quadratic
Factor \(x^2 - 3x + 2\):
\[
x^2 - 3x + 2 = (x - 1)(x - 2)
\]

#### Step 4: Combine Factors
\[
f(x) = (x - 1)^2(x - 2)
\]

---

### **Conclusion**
The Factor Theorem provides a straightforward way to connect roots and factors of a polynomial, 
enabling efficient factoring and root-finding.




## **Determining the Equation of a Trendline**

A trendline represents the general direction of a dataset in a scatter plot. It can be expressed as a linear equation of the form:  
\[
y = mx + b
\]  
where:
- \(m\) is the **slope** of the trendline.
- \(b\) is the **y-intercept** (the value of \(y\) when \(x = 0\)).

---

### **Steps to Determine the Equation**

#### **Step 1: Identify Two Points on the Trendline**
Select two clear points that lie directly on the trendline. For example, let the points be \((x_1, y_1)\) and \((x_2, y_2)\).

#### **Step 2: Calculate the Slope (\(m\))**
The slope is calculated using the formula:
\[
m = \frac{y_2 - y_1}{x_2 - x_1}
\]

#### **Step 3: Use the Slope-Intercept Form**
Substitute the slope (\(m\)) and one of the points (e.g., \((x_1, y_1)\)) into the slope-intercept form of the equation to solve for the y-intercept (\(b\)):

\[
y = mx + b \implies b = y - mx
\]

#### **Step 4: Write the Final Equation**
Using the values of \(m\) and \(b\), write the equation of the trendline as:
\[
y = mx + b
\]

---

### **Example**
Given a scatter plot with a trendline passing through the points \((2, 3)\) and \((4, 7)\), find the equation of the trendline.

#### **Step 1: Calculate the Slope**
\[
m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{7 - 3}{4 - 2} = \frac{4}{2} = 2
\]

#### **Step 2: Find the Y-Intercept**
Using the slope (\(m = 2\)) and the point \((2, 3)\):
\[
b = y - mx = 3 - (2 \cdot 2) = 3 - 4 = -1
\]

#### **Step 3: Write the Equation**
\[
y = 2x - 1
\]

---

### **Graphical Trendline in Software**
If determining from software-generated scatter plots (e.g., Excel, Python), most tools will automatically calculate the trendline equation and display it on the graph.

---

### **Conclusion**
To find the trendline equation, focus on identifying two points, calculating the slope, 
and solving for the y-intercept. The resulting equation reflects the relationship 
between \(x\) and \(y\) in the dataset.





## **Determining the Equation of a Trendline**

A trendline represents the general direction of a dataset in a scatter plot. It can be expressed as a linear equation of the form:  
\[
y = mx + b
\]  
where:
- \(m\) is the **slope** of the trendline.
- \(b\) is the **y-intercept** (the value of \(y\) when \(x = 0\)).

---

### **Steps to Determine the Equation**

#### **Step 1: Identify Two Points on the Trendline**
Select two clear points that lie directly on the trendline. For example, let the points be \((x_1, y_1)\) and \((x_2, y_2)\).

#### **Step 2: Calculate the Slope (\(m\))**
The slope is calculated using the formula:
\[
m = \frac{y_2 - y_1}{x_2 - x_1}
\]

#### **Step 3: Use the Slope-Intercept Form**
Substitute the slope (\(m\)) and one of the points (e.g., \((x_1, y_1)\)) into the slope-intercept form of the equation to solve for the y-intercept (\(b\)):

\[
y = mx + b \implies b = y - mx
\]

#### **Step 4: Write the Final Equation**
Using the values of \(m\) and \(b\), write the equation of the trendline as:
\[
y = mx + b
\]

---

### **Example**
Given a scatter plot with a trendline passing through the points \((2, 3)\) and \((4, 7)\), find the equation of the trendline.

#### **Step 1: Calculate the Slope**
\[
m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{7 - 3}{4 - 2} = \frac{4}{2} = 2
\]

#### **Step 2: Find the Y-Intercept**
Using the slope (\(m = 2\)) and the point \((2, 3)\):
\[
b = y - mx = 3 - (2 \cdot 2) = 3 - 4 = -1
\]

#### **Step 3: Write the Equation**
\[
y = 2x - 1
\]

---

### **Graphical Trendline in Software**
If determining from software-generated scatter plots (e.g., Excel, Python), most tools will automatically calculate the trendline equation and display it on the graph.

---

### **Conclusion**
To find the trendline equation, focus on identifying two points, calculating the slope, 
and solving for the y-intercept. The resulting equation reflects the relationship 
between \(x\) and \(y\) in the dataset.





## **Periodic Functions**

A **periodic function** is a function that repeats its values at regular intervals or cycles. Mathematically, a function \(f(x)\) is periodic if there exists a positive constant \(T\) such that:

\[
f(x + T) = f(x) \quad \text{for all } x \text{ in the domain of } f.
\]

The smallest such positive value of \(T\) is called the **period** of the function.

---

### **Examples of Periodic Functions**

1. **Sine and Cosine Functions:**
   - \(f(x) = \sin(x)\) and \(g(x) = \cos(x)\) have a period of \(2\pi\).
   - This means:
     \[
     \sin(x + 2\pi) = \sin(x), \quad \cos(x + 2\pi) = \cos(x)
     \]

2. **Tangent Function:**
   - \(h(x) = \tan(x)\) has a period of \(\pi\).
   - This means:
     \[
     \tan(x + \pi) = \tan(x)
     \]

3. **Square Wave or Sawtooth Wave:**
   - These are periodic functions often used in signal processing.

---

### **Key Properties**

1. **Repetition:** The function’s values repeat at intervals of \(T\).
2. **Symmetry (sometimes):** Periodic functions often exhibit symmetrical behavior, such as evenness or oddness (e.g., \(\cos(x)\) is even, and \(\sin(x)\) is odd).

---

### **Applications of Periodic Functions**
Periodic functions are widely used in:
1. **Trigonometry**: Modeling wave-like behavior, such as sound waves and light waves.
2. **Physics**: Describing oscillatory motion (e.g., pendulums, springs).
3. **Engineering**: Signal processing, alternating current (AC) circuits.
4. **Astronomy**: Modeling planetary motions.

---

### **Graphical Representation**
- The graph of a periodic function shows repeated cycles.
- The period \(T\) can be measured as the distance between two consecutive points where the function repeats.

---

### **Example**
Given \(f(x) = 3\sin(2x)\), find its period.

#### Step 1: Identify the base period
The sine function \(\sin(x)\) has a period of \(2\pi\).

#### Step 2: Adjust for the coefficient of \(x\)
If \(f(x) = \sin(kx)\), the period is:
\[
T = \frac{2\pi}{k}
\]
Here, \(k = 2\), so:
\[
T = \frac{2\pi}{2} = \pi
\]

---

### **Conclusion**
Periodic functions are essential for understanding repetitive phenomena, and their behavior is 
determined by their period \(T\), symmetry, and application context.




## **Dividing Polynomials by Linear Binomials Using Long Division**

Polynomial long division is a method used to divide a polynomial by another polynomial, often a linear binomial. This process is similar to numerical long division.

---

### **Steps for Polynomial Long Division**

1. **Write the Division in Long Division Format**  
   Place the dividend (the polynomial to be divided) inside the long division symbol and the divisor (the linear binomial) outside.

2. **Divide the First Term**  
   Divide the leading term of the dividend by the leading term of the divisor to determine the first term of the quotient.

3. **Multiply and Subtract**  
   Multiply the entire divisor by the term obtained in the previous step and subtract the result from the dividend.

4. **Bring Down the Next Term**  
   Bring down the next term of the dividend and repeat the process until no terms are left in the dividend.

5. **Write the Final Quotient and Remainder**  
   The quotient will be the result at the top, and any leftover term after subtraction will be the remainder.

---

### **Example**

Divide \(x^3 + 2x^2 - 5x - 6\) by \(x - 2\).

#### **Step 1: Set up the Division**
\[
\frac{x^3 + 2x^2 - 5x - 6}{x - 2}
\]
Write it in long division format:

\[
\begin{array}{r|l}
x - 2 & x^3 + 2x^2 - 5x - 6
\end{array}
\]

#### **Step 2: Divide the Leading Terms**
Divide the leading term of the dividend (\(x^3\)) by the leading term of the divisor (\(x\)):
\[
\frac{x^3}{x} = x^2
\]
Write \(x^2\) in the quotient.

#### **Step 3: Multiply and Subtract**
Multiply \(x^2(x - 2)\):
\[
x^2(x - 2) = x^3 - 2x^2
\]
Subtract this from the dividend:
\[
(x^3 + 2x^2) - (x^3 - 2x^2) = 4x^2
\]

#### **Step 4: Bring Down the Next Term**
Bring down \(-5x\):
\[
4x^2 - 5x
\]

#### **Step 5: Repeat the Process**
Divide \(4x^2\) by \(x\):
\[
\frac{4x^2}{x} = 4x
\]
Write \(+4x\) in the quotient.

Multiply and subtract:
\[
4x(x - 2) = 4x^2 - 8x
\]
\[
(4x^2 - 5x) - (4x^2 - 8x) = 3x
\]

#### **Step 6: Bring Down the Next Term**
Bring down \(-6\):
\[
3x - 6
\]

Divide \(3x\) by \(x\):
\[
\frac{3x}{x} = 3
\]
Write \(+3\) in the quotient.

Multiply and subtract:
\[
3(x - 2) = 3x - 6
\]
\[
(3x - 6) - (3x - 6) = 0
\]

---

### **Final Answer**
The quotient is:
\[
x^2 + 4x + 3
\]

There is no remainder, so:
\[
\frac{x^3 + 2x^2 - 5x - 6}{x - 2} = x^2 + 4x + 3
\]

---

### **Conclusion**
Polynomial long division is a systematic method to divide polynomials. When the divisor is a linear binomial,
the process simplifies to a step-by-step approach of dividing, multiplying, subtracting, 
and bringing down terms until the remainder is determined.





## **Graphing Cubic Curves with Three Distinct Real Roots**

Cubic curves of the form \(f(x) = ax^3 + bx^2 + cx + d\) can have up to three distinct real roots. These roots correspond to the \(x\)-intercepts of the graph, and the shape of the curve is influenced by the sign of \(a\), the coefficient of \(x^3\), and the location of turning points.

---

### **Key Characteristics of Cubic Curves**

1. **Three Distinct Real Roots**: 
   - Denote the roots as \(r_1\), \(r_2\), and \(r_3\), where \(r_1 < r_2 < r_3\).
   - These are the points where \(f(x) = 0\), i.e., where the graph intersects the \(x\)-axis.

2. **End Behavior**: 
   - If \(a > 0\), the curve starts in the lower left (\(x \to -\infty, f(x) \to -\infty\)) and ends in the upper right (\(x \to \infty, f(x) \to \infty\)).
   - If \(a < 0\), the curve starts in the upper left (\(x \to -\infty, f(x) \to \infty\)) and ends in the lower right (\(x \to \infty, f(x) \to -\infty\)).

3. **Turning Points**:
   - A cubic curve with three distinct real roots will have **two turning points** (local maximum and minimum) between the roots.
   - The location of these turning points depends on the derivative \(f'(x)\), which is a quadratic equation.

4. **Sign of Leading Coefficient (\(a\))**:
   - Determines the orientation of the graph (described in end behavior).

---

### **Steps to Graph the Cubic Curve**

1. **Find the Roots**:
   - Solve \(f(x) = 0\) to find the roots \(r_1, r_2, r_3\).

2. **Determine the Turning Points**:
   - Compute the derivative:
     \[
     f'(x) = 3ax^2 + 2bx + c
     \]
   - Solve \(f'(x) = 0\) to find the \(x\)-coordinates of the turning points.
   - Substitute these \(x\)-values into \(f(x)\) to get the corresponding \(y\)-values.

3. **Identify End Behavior**:
   - Use the sign of \(a\) to determine the direction of the tails of the curve.

4. **Plot Key Points**:
   - Plot the roots \((r_1, 0)\), \((r_2, 0)\), and \((r_3, 0)\).
   - Plot the turning points.
   - Optionally, evaluate \(f(x)\) at additional points to refine the graph.

5. **Draw the Curve**:
   - Connect the points with a smooth, continuous curve, ensuring the correct end behavior and turning point locations.

---

### **Example**
Graph \(f(x) = x^3 - 6x^2 + 11x - 6\).

#### **Step 1: Find the Roots**
Solve \(x^3 - 6x^2 + 11x - 6 = 0\) using factoring:
\[
f(x) = (x - 1)(x - 2)(x - 3)
\]
Roots are \(x = 1, 2, 3\).

#### **Step 2: Determine Turning Points**
Compute the derivative:
\[
f'(x) = 3x^2 - 12x + 11
\]
Solve \(f'(x) = 0\) to find:
\[
3x^2 - 12x + 11 = 0 \implies x = \frac{6 \pm \sqrt{4}}{6} = \frac{6 \pm 2}{6}
\]
\[
x = \frac{4}{3}, \quad x = 2.33
\]

#### **Step 3: Evaluate Turning Points**
Substitute into \(f(x)\):
\[
f\left(\frac{4}{3}\right) \approx -0.296, \quad f(2.33) \approx -0.296
\]

#### **Step 4: End Behavior**
Since \(a = 1 > 0\), the curve starts in the lower left and ends in the upper right.

#### **Step 5: Plot and Sketch**
- Plot the roots \((1, 0), (2, 0), (3, 0)\).
- Plot turning points \((4/3, -0.296)\) and \((2.33, -0.296)\).
- Draw a smooth curve passing through these points with the correct end behavior.

---

### **Conclusion**
Cubic curves with three distinct roots have a characteristic "S" shape with two turning points. 
Graphing them involves solving for roots, identifying turning points, and sketching the 
curve with the correct end behavior.




## **Rational Equations with Three Terms**

A **rational equation** is an equation that involves at least one fraction whose numerator or denominator 
contains a variable. Rational equations with three terms typically look like this:

\[
\frac{P(x)}{Q(x)} + \frac{R(x)}{S(x)} = \frac{T(x)}{U(x)}
\]

Where \(P(x)\), \(Q(x)\), \(R(x)\), \(S(x)\), \(T(x)\), and \(U(x)\) are polynomials.

---

### **Steps to Solve Rational Equations**

1. **Find the Least Common Denominator (LCD)**  
   Identify the LCD of all the denominators in the equation. The LCD is the smallest expression that contains all factors of the denominators.

2. **Multiply Through by the LCD**  
   Eliminate the fractions by multiplying every term in the equation by the LCD.

3. **Simplify the Resulting Equation**  
   After eliminating the denominators, simplify the equation. This often leads to a linear, quadratic, or higher-order polynomial equation.

4. **Solve for the Variable**  
   Solve the simplified equation using appropriate techniques (e.g., factoring, quadratic formula).

5. **Check for Extraneous Solutions**  
   Solutions that make any denominator in the original equation zero are invalid and must be excluded.

---

### **Example 1: Simple Rational Equation**
Solve:
\[
\frac{x}{x + 1} + \frac{2}{x - 1} = \frac{3}{x^2 - 1}
\]

#### Step 1: Find the LCD
The denominators are \(x + 1\), \(x - 1\), and \(x^2 - 1\). The LCD is:
\[
x^2 - 1 = (x + 1)(x - 1)
\]

#### Step 2: Multiply Through by the LCD
Multiply every term by \(x^2 - 1\):
\[
(x^2 - 1) \cdot \frac{x}{x + 1} + (x^2 - 1) \cdot \frac{2}{x - 1} = (x^2 - 1) \cdot \frac{3}{x^2 - 1}
\]

Simplify each term:
\[
x(x - 1) + 2(x + 1) = 3
\]

#### Step 3: Simplify the Resulting Equation
Expand and combine like terms:
\[
x^2 - x + 2x + 2 = 3
\]
\[
x^2 + x - 1 = 0
\]

#### Step 4: Solve for \(x\)
Factor or use the quadratic formula:
\[
x = \frac{-1 \pm \sqrt{1^2 - 4(1)(-1)}}{2(1)}
\]
\[
x = \frac{-1 \pm \sqrt{5}}{2}
\]

#### Step 5: Check for Extraneous Solutions
Substitute \(x = \frac{-1 \pm \sqrt{5}}{2}\) into the original equation to ensure no denominator becomes zero. 
Both values are valid.

**Solutions**:
\[
x = \frac{-1 + \sqrt{5}}{2}, \quad x = \frac{-1 - \sqrt{5}}{2}
\]

---

### **Example 2: Equation with Variable Denominators**
Solve:
\[
\frac{2}{x} - \frac{1}{x - 1} = \frac{3}{x(x - 1)}
\]

#### Step 1: Find the LCD
The denominators are \(x\), \(x - 1\), and \(x(x - 1)\). The LCD is:
\[
x(x - 1)
\]

#### Step 2: Multiply Through by the LCD
Multiply every term by \(x(x - 1)\):
\[
x(x - 1) \cdot \frac{2}{x} - x(x - 1) \cdot \frac{1}{x - 1} = x(x - 1) \cdot \frac{3}{x(x - 1)}
\]

Simplify each term:
\[
2(x - 1) - x = 3
\]

#### Step 3: Simplify the Resulting Equation
Expand and combine like terms:
\[
2x - 2 - x = 3
\]
\[
x - 2 = 3
\]
\[
x = 5
\]

#### Step 4: Check for Extraneous Solutions
Verify that \(x = 5\) does not make any denominator zero. It is valid.

**Solution**:
\[
x = 5
\]

---

### **Conclusion**
To solve rational equations:
1. Identify and multiply through by the LCD to eliminate fractions.
2. Solve the resulting equation.
3. Always check for extraneous solutions to ensure validity.




## **Multiplicities of the Roots of Polynomials**

The **multiplicity** of a root of a polynomial is the number of times that root appears as a solution of the polynomial. For a polynomial \(P(x)\), if \((x - r)^k\) is a factor, then \(r\) is a root with multiplicity \(k\).

---

### **Key Properties of Multiplicities**
1. **Simple Roots (Multiplicity = 1):**  
   A root with multiplicity \(1\) is called a simple root. The graph of the polynomial crosses the \(x\)-axis at this root.

2. **Repeated Roots (Multiplicity \(> 1\)):**  
   - **Even Multiplicity:** The graph of the polynomial touches the \(x\)-axis at the root but does not cross it.
   - **Odd Multiplicity (\(> 1\)):** The graph of the polynomial crosses the \(x\)-axis at the root but appears flattened compared to simple roots.

3. **Sum of Multiplicities:**  
   The sum of the multiplicities of all roots equals the degree of the polynomial.

---

### **Examples**

#### Example 1: Identifying Roots and Their Multiplicities  
For the polynomial:
\[
P(x) = (x - 2)^2(x + 1)^3(x - 4)
\]

- Root \(x = 2\):  
  Appears as \((x - 2)^2\), so it has **multiplicity 2**.

- Root \(x = -1\):  
  Appears as \((x + 1)^3\), so it has **multiplicity 3**.

- Root \(x = 4\):  
  Appears as \((x - 4)\), so it has **multiplicity 1**.

---

#### Example 2: Multiplicities and Graph Behavior  
Consider the polynomial:
\[
P(x) = (x - 3)^2(x + 2)
\]

- **Root \(x = 3\):**  
  - Multiplicity: \(2\) (even).  
  - Graph touches the \(x\)-axis at \(x = 3\) but does not cross.

- **Root \(x = -2\):**  
  - Multiplicity: \(1\) (odd).  
  - Graph crosses the \(x\)-axis at \(x = -2\).

---

### **Finding Multiplicities from the Polynomial**
1. **Factored Form:**  
   If the polynomial is in factored form, determine the multiplicity directly from the exponents of the factors.

2. **Non-Factored Form:**  
   For a polynomial not in factored form, first factorize it using techniques such as:
   - Synthetic division
   - Long division
   - Grouping
   - Quadratic formula (if applicable)

3. **Using Derivatives:**  
   If \(r\) is a root of \(P(x)\), and \(P'(r) = 0\), then \(r\) is a root of multiplicity greater than \(1\). The higher-order derivatives can further reveal the multiplicity.

---

#### Example 3: Determine Multiplicity from \(P(x)\)
For \(P(x) = x^3 - 3x^2 + 3x - 1\):
1. Factorize:
   \[
   P(x) = (x - 1)^3
   \]
2. Root \(x = 1\) appears with **multiplicity 3**.

---

### **Conclusion**
- Multiplicities describe how often a root appears in a polynomial.
- They influence the behavior of the graph near the root.
- Analyzing multiplicities helps in graphing, factoring, and solving polynomial equations.




## **Advanced Rational Equations**

Advanced rational equations involve complex algebraic expressions with variables in the numerator and denominator. These problems often include higher-degree polynomials, multiple terms, or nested fractions. Solving these requires a systematic approach to simplify and handle the complexity.

---

### **Steps to Solve Advanced Rational Equations**

1. **Identify and Simplify the Equation**  
   Simplify each term of the equation, if possible. Combine fractions with common denominators where applicable.

2. **Find the Least Common Denominator (LCD)**  
   Determine the least common denominator of all the fractions in the equation.

3. **Eliminate the Denominators**  
   Multiply every term in the equation by the LCD to eliminate fractions. This transforms the rational equation into a polynomial equation.

4. **Simplify the Resulting Polynomial Equation**  
   Expand and simplify the polynomial, then solve for the variable using factoring, the quadratic formula, or other appropriate techniques.

5. **Check for Extraneous Solutions**  
   Substitute the solutions into the original equation to ensure they do not make any denominator zero. Discard any invalid solutions.

---

### **Example 1: Rational Equation with Polynomial Denominators**
Solve:
\[
\frac{x}{x - 1} + \frac{2}{x + 1} = \frac{3x}{x^2 - 1}
\]

#### Step 1: Simplify and Find the LCD  
The denominators are \(x - 1\), \(x + 1\), and \(x^2 - 1\). Since \(x^2 - 1 = (x - 1)(x + 1)\), the LCD is:
\[
x^2 - 1
\]

#### Step 2: Multiply Through by the LCD  
Multiply each term by \(x^2 - 1\):
\[
(x^2 - 1) \cdot \frac{x}{x - 1} + (x^2 - 1) \cdot \frac{2}{x + 1} = (x^2 - 1) \cdot \frac{3x}{x^2 - 1}
\]

Simplify each term:
\[
x(x + 1) + 2(x - 1) = 3x
\]

#### Step 3: Expand and Simplify  
Expand and combine like terms:
\[
x^2 + x + 2x - 2 = 3x
\]
\[
x^2 + 3x - 2 = 3x
\]
\[
x^2 - 2 = 0
\]

#### Step 4: Solve for \(x\)  
Factorize:
\[
x^2 = 2
\]
\[
x = \pm\sqrt{2}
\]

#### Step 5: Check for Extraneous Solutions  
Substitute \(x = \sqrt{2}\) and \(x = -\sqrt{2}\) into the original equation. Both are valid since they do not make any denominator zero.

**Solutions**:
\[
x = \sqrt{2}, \quad x = -\sqrt{2}
\]

---

### **Example 2: Nested Fractions**
Solve:
\[
\frac{\frac{1}{x} + \frac{2}{x + 1}}{\frac{1}{x - 1}} = 3
\]

#### Step 1: Simplify the Numerator and Denominator  
The numerator is:
\[
\frac{1}{x} + \frac{2}{x + 1}
\]
The LCD is \(x(x + 1)\), so:
\[
\frac{1}{x} + \frac{2}{x + 1} = \frac{(x + 1) + 2x}{x(x + 1)} = \frac{3x + 1}{x(x + 1)}
\]

The denominator is:
\[
\frac{1}{x - 1}
\]

The equation becomes:
\[
\frac{\frac{3x + 1}{x(x + 1)}}{\frac{1}{x - 1}} = 3
\]

#### Step 2: Simplify the Complex Fraction  
Multiply by the reciprocal of the denominator:
\[
\frac{3x + 1}{x(x + 1)} \cdot (x - 1) = 3
\]
\[
\frac{(3x + 1)(x - 1)}{x(x + 1)} = 3
\]

#### Step 3: Multiply Through by the LCD  
The LCD is \(x(x + 1)\):
\[
(3x + 1)(x - 1) = 3x(x + 1)
\]

Expand both sides:
\[
3x^2 - 3x + x - 1 = 3x^2 + 3x
\]
\[
3x^2 - 2x - 1 = 3x^2 + 3x
\]
\[
-5x - 1 = 0
\]

#### Step 4: Solve for \(x\)  
\[
x = -\frac{1}{5}
\]

#### Step 5: Check for Extraneous Solutions  
Substitute \(x = -\frac{1}{5}\) into the original equation. It is valid since it does not make any denominator zero.

**Solution**:
\[
x = -\frac{1}{5}
\]

---

### **Advanced Tips**
1. **Handle Higher-Degree Polynomials:** For equations with high-degree polynomials, use synthetic division or numerical methods if factoring is not straightforward.
2. **Use Substitutions:** For complex nested fractions, substitution can simplify the equation.
3. **Graphing Tools:** Visualizing the equation with a graphing tool can help identify roots and verify solutions.
4. **Check Constraints:** Always verify that solutions do not violate domain restrictions.

--- 

These techniques make solving advanced rational equations systematic and manageable.




## **The Rational Roots Theorem**

The **Rational Roots Theorem** is a useful tool for finding all possible rational roots (or zeros) of a polynomial equation with integer coefficients. It provides a systematic way to test for rational solutions without blindly guessing.

---

### **Statement of the Theorem**
For a polynomial:
\[
P(x) = a_nx^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0
\]
where all coefficients \(a_n, a_{n-1}, \dots, a_0\) are integers:

1. Any rational root, if it exists, can be written in the form:
   \[
   \frac{p}{q}
   \]
   where:
   - \(p\) is a factor of the constant term (\(a_0\)).
   - \(q\) is a factor of the leading coefficient (\(a_n\)).

2. The possible rational roots are:
   \[
   \pm \frac{\text{factors of } a_0}{\text{factors of } a_n}
   \]

---

### **Steps to Use the Rational Roots Theorem**

1. **Identify \(a_0\) and \(a_n\):**
   - \(a_0\): The constant term.
   - \(a_n\): The leading coefficient.

2. **List the factors of \(a_0\) (constant term):**  
   Find all positive and negative integers that divide \(a_0\) evenly.

3. **List the factors of \(a_n\) (leading coefficient):**  
   Find all positive and negative integers that divide \(a_n\) evenly.

4. **Form all possible rational roots:**  
   Combine all factors of \(a_0\) (numerators) with all factors of \(a_n\) (denominators).

5. **Test the possible roots:**  
   Substitute each candidate into the polynomial \(P(x)\). A candidate is a root if \(P(x) = 0\).

---

### **Example 1: Simple Polynomial**
Find the rational roots of:
\[
P(x) = 2x^3 - 3x^2 - 2x + 3
\]

1. Identify \(a_0\) and \(a_n\):  
   - \(a_0 = 3\) (constant term).  
   - \(a_n = 2\) (leading coefficient).

2. List factors:  
   - Factors of \(a_0 = 3\): \(\pm 1, \pm 3\).  
   - Factors of \(a_n = 2\): \(\pm 1, \pm 2\).

3. Form all possible rational roots:  
   \[
   \pm \frac{1}{1}, \pm \frac{1}{2}, \pm \frac{3}{1}, \pm \frac{3}{2}
   \]
   Possible roots: \(\pm 1, \pm \frac{1}{2}, \pm 3, \pm \frac{3}{2}\).

4. Test each candidate:  
   Substitute each value into \(P(x)\):
   - \(P(1) = 2(1)^3 - 3(1)^2 - 2(1) + 3 = 0\).  
     \(x = 1\) is a root.

5. Factorize using \(x - 1\):  
   Perform synthetic or long division:
   \[
   P(x) = (x - 1)(2x^2 - x - 3)
   \]

6. Solve the quadratic \(2x^2 - x - 3 = 0\):  
   Factor or use the quadratic formula:
   \[
   2x^2 - x - 3 = (2x + 3)(x - 1)
   \]

Final roots:  
\[
x = 1, x = -\frac{3}{2}, x = 1 \text{ (repeated root)}.
\]

---

### **Example 2: No Rational Roots**
Find the rational roots of:
\[
P(x) = x^3 - 2x + 5
\]

1. Identify \(a_0\) and \(a_n\):  
   - \(a_0 = 5\), \(a_n = 1\).

2. List factors:  
   - Factors of \(a_0 = 5\): \(\pm 1, \pm 5\).  
   - Factors of \(a_n = 1\): \(\pm 1\).

3. Form all possible rational roots:  
   \[
   \pm 1, \pm 5
   \]

4. Test each candidate:  
   Substitute \(x = 1, -1, 5, -5\) into \(P(x)\). None satisfy \(P(x) = 0\).

Conclusion:  
The polynomial \(P(x)\) has no rational roots.

---

### **Applications**
1. **Factoring Polynomials:**  
   After finding a rational root, divide the polynomial to simplify and find other roots.

2. **Finding Integer Roots:**  
   When \(a_n = 1\), all rational roots are integers.

3. **Verifying Roots Numerically:**  
   If a polynomial has no rational roots, use numerical methods (e.g., Newton's method) or graphing tools.

---

The Rational Roots Theorem provides a structured approach for testing possible rational roots,
making it a powerful tool for solving polynomial equations.





##  **Partial Fractions Decomposition**

Partial fractions decomposition is a method used to express a rational function as a sum of simpler fractions. It is particularly useful for integration, solving differential equations, and simplifying complex algebraic expressions.

---

### **Form of a Rational Function**
A rational function is a ratio of two polynomials:
\[
\frac{P(x)}{Q(x)}
\]
where:
- \(P(x)\) is the numerator (a polynomial of degree \(m\)).
- \(Q(x)\) is the denominator (a polynomial of degree \(n\)).

If \(m \geq n\), perform **polynomial long division** first, then decompose the remainder. The focus here is on \(m < n\).

---

### **Steps for Partial Fractions Decomposition**
1. **Factor the Denominator \(Q(x)\):**  
   Break \(Q(x)\) into its irreducible factors over the real numbers (e.g., linear and quadratic factors).

2. **Write the Partial Fractions Setup:**  
   Express \(\frac{P(x)}{Q(x)}\) as a sum of fractions with unknown coefficients. The type of term depends on the factors:
   - For **linear factors** \((x - r)\): Use \(\frac{A}{x - r}\).
   - For **repeated linear factors** \((x - r)^k\): Use \(\frac{A_1}{x - r} + \frac{A_2}{(x - r)^2} + \dots + \frac{A_k}{(x - r)^k}\).
   - For **irreducible quadratic factors** \((ax^2 + bx + c)\): Use \(\frac{Ax + B}{ax^2 + bx + c}\).
   - For **repeated quadratic factors** \((ax^2 + bx + c)^k\): Use \(\frac{A_1x + B_1}{ax^2 + bx + c} + \frac{A_2x + B_2}{(ax^2 + bx + c)^2} + \dots\).

3. **Multiply Through by the Denominator \(Q(x)\):**  
   Eliminate the denominators to obtain a polynomial equation.

4. **Equate Coefficients:**  
   Match the coefficients of corresponding powers of \(x\) on both sides of the equation to solve for the unknowns.

5. **Write the Final Decomposition:**  
   Substitute the solved coefficients back into the partial fractions.

---

### **Example 1: Decompose a Simple Rational Function**
Decompose:
\[
\frac{3x + 5}{(x - 1)(x + 2)}
\]

#### Step 1: Write the Partial Fractions
Since the denominator has two distinct linear factors, write:
\[
\frac{3x + 5}{(x - 1)(x + 2)} = \frac{A}{x - 1} + \frac{B}{x + 2}
\]

#### Step 2: Multiply Through by \((x - 1)(x + 2)\)
\[
3x + 5 = A(x + 2) + B(x - 1)
\]

#### Step 3: Expand and Combine Terms
\[
3x + 5 = Ax + 2A + Bx - B
\]
\[
3x + 5 = (A + B)x + (2A - B)
\]

#### Step 4: Equate Coefficients
Match coefficients of \(x\) and the constant term:
- Coefficient of \(x\): \(A + B = 3\)
- Constant term: \(2A - B = 5\)

Solve the system of equations:
1. \(A + B = 3\)
2. \(2A - B = 5\)

From (1): \(B = 3 - A\).  
Substitute into (2):
\[
2A - (3 - A) = 5
\]
\[
2A - 3 + A = 5
\]
\[
3A = 8 \quad \Rightarrow \quad A = \frac{8}{3}
\]

Substitute \(A = \frac{8}{3}\) into \(B = 3 - A\):
\[
B = 3 - \frac{8}{3} = \frac{9}{3} - \frac{8}{3} = \frac{1}{3}
\]

#### Step 5: Write the Final Decomposition
\[
\frac{3x + 5}{(x - 1)(x + 2)} = \frac{\frac{8}{3}}{x - 1} + \frac{\frac{1}{3}}{x + 2}
\]

---

### **Example 2: Decompose a Repeated Linear Factor**
Decompose:
\[
\frac{2x^2 + 5x + 3}{(x + 1)^2}
\]

#### Step 1: Write the Partial Fractions
For the repeated linear factor \((x + 1)^2\), write:
\[
\frac{2x^2 + 5x + 3}{(x + 1)^2} = \frac{A}{x + 1} + \frac{B}{(x + 1)^2}
\]

#### Step 2: Multiply Through by \((x + 1)^2\)
\[
2x^2 + 5x + 3 = A(x + 1) + B
\]

#### Step 3: Expand and Combine Terms
\[
2x^2 + 5x + 3 = Ax + A + B
\]
\[
2x^2 + 5x + 3 = Ax + (A + B)
\]

#### Step 4: Equate Coefficients
- Coefficient of \(x^2\): \(2 = 0\) (no \(x^2\) term).
- Coefficient of \(x\): \(A = 5\).
- Constant term: \(A + B = 3\).

From \(A = 5\), substitute into \(A + B = 3\):
\[
5 + B = 3 \quad \Rightarrow \quad B = -2
\]

#### Step 5: Write the Final Decomposition
\[
\frac{2x^2 + 5x + 3}{(x + 1)^2} = \frac{5}{x + 1} - \frac{2}{(x + 1)^2}
\]

---

### **Applications**
1. **Integration:**  
   Simplifies rational functions for easier integration.
   \[
   \int \frac{1}{x(x + 1)} \, dx \quad \text{becomes} \quad \int \frac{A}{x} + \frac{B}{x + 1} \, dx
   \]

2. **Solving Differential Equations:**  
   Used in separating variables in first-order differential equations.

3. **Inverse Laplace Transform:**  
   Breaks down Laplace transforms into manageable components.

---

### **Tips for Success**
- Always perform polynomial long division if the degree of the numerator is greater than or equal to the denominator.
- For irreducible quadratic factors, use \(Ax + B\) terms.
- Double-check for repeated roots and assign appropriate powers in the denominator.





## **Union and Intersection of Sets**

Union and intersection are two fundamental operations in set theory that combine or compare elements from two or more sets.

---

### **Union of Sets**
The **union** of two sets combines all elements from both sets, without duplication.  
It is denoted as \( A \cup B \).

#### **Definition**:
\[
A \cup B = \{x \mid x \in A \ \text{or} \ x \in B\}
\]
- \(x\) belongs to \(A \cup B\) if \(x\) is in \(A\), \(B\), or both.

#### **Example**:
If \(A = \{1, 2, 3\}\) and \(B = \{3, 4, 5\}\), then:
\[
A \cup B = \{1, 2, 3, 4, 5\}
\]

---

### **Intersection of Sets**
The **intersection** of two sets includes only the elements that are common to both sets.  
It is denoted as \( A \cap B \).

#### **Definition**:
\[
A \cap B = \{x \mid x \in A \ \text{and} \ x \in B\}
\]
- \(x\) belongs to \(A \cap B\) if \(x\) is in both \(A\) and \(B\).

#### **Example**:
If \(A = \{1, 2, 3\}\) and \(B = \{3, 4, 5\}\), then:
\[
A \cap B = \{3\}
\]

---

### **Key Properties of Union and Intersection**

#### **Union Properties**:
1. **Commutative**:  
   \[
   A \cup B = B \cup A
   \]
2. **Associative**:  
   \[
   (A \cup B) \cup C = A \cup (B \cup C)
   \]
3. **Identity**:  
   \[
   A \cup \emptyset = A
   \]

#### **Intersection Properties**:
1. **Commutative**:  
   \[
   A \cap B = B \cap A
   \]
2. **Associative**:  
   \[
   (A \cap B) \cap C = A \cap (B \cap C)
   \]
3. **Identity**:  
   \[
   A \cap U = A
   \]
   (where \(U\) is the universal set)

#### **Distributive Laws**:
- Union over Intersection:  
  \[
  A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
  \]
- Intersection over Union:  
  \[
  A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
  \]

---

### **Visual Representation with Venn Diagrams**
- **Union** (\(A \cup B\)): The shaded region covers all parts of both sets.
- **Intersection** (\(A \cap B\)): The shaded region only covers the overlapping area of both sets.

---

### **Real-Life Applications**
1. **Union**:  
   Combining lists of items, such as merging contact lists from two sources.
2. **Intersection**:  
   Finding common preferences, such as shared interests between two groups.

By understanding the operations and properties of union and intersection, complex problems in set theory, 
logic, and data analysis can be solved effectively.



## **Graphing Cubic Curves Containing a Double Root**

When graphing a cubic curve containing a double root, the double root creates a specific behavior in the graph: the curve touches the x-axis at the double root but does not cross it. Understanding the behavior and shape of the curve requires analyzing the polynomial equation and its characteristics.

---

### **General Form of a Cubic Polynomial**
A cubic polynomial with a double root can be written as:
\[
y = a(x - r_1)^2(x - r_2)
\]
where:
- \(r_1\) is the **double root**.
- \(r_2\) is the **simple root**.
- \(a\) determines the direction and stretch/compression of the curve.

---

### **Key Characteristics of the Graph**

1. **Double Root Behavior**:
   - At the double root (\(x = r_1\)), the graph **touches the x-axis** and forms a turning point. 
   - The graph does not cross the x-axis at the double root.

2. **Simple Root Behavior**:
   - At the simple root (\(x = r_2\)), the graph crosses the x-axis.

3. **End Behavior**:
   - If \(a > 0\), the graph rises to positive infinity as \(x \to \infty\) and falls to negative infinity as \(x \to -\infty\).
   - If \(a < 0\), the graph falls to negative infinity as \(x \to \infty\) and rises to positive infinity as \(x \to -\infty\).

4. **Turning Points**:
   - A cubic curve can have up to two turning points. One turning point occurs at the double root.

---

### **Steps to Graph the Curve**

1. **Identify the Roots**:
   - Determine the double root (\(r_1\)) and the simple root (\(r_2\)) from the equation.

2. **Plot the Roots**:
   - Mark the double root on the x-axis, where the graph touches but does not cross.
   - Mark the simple root on the x-axis, where the graph crosses.

3. **Analyze the End Behavior**:
   - Use the sign of \(a\) to determine how the graph behaves as \(x \to \pm\infty\).

4. **Find Turning Points**:
   - If needed, compute the derivative to locate turning points:
     \[
     \frac{dy}{dx} = 3a(x - r_1)(x - r_2) + 2a(x - r_1)^2
     \]
   - Solve \(\frac{dy}{dx} = 0\) to find the x-coordinates of the turning points.

5. **Sketch the Curve**:
   - Draw the graph, ensuring it touches the x-axis at the double root, crosses at the simple root, and follows the end behavior.

---

### **Example**
Graph the cubic curve:
\[
y = (x - 1)^2(x + 2)
\]

#### Step 1: Identify the Roots
- Double root: \(x = 1\)
- Simple root: \(x = -2\)

#### Step 2: Analyze the End Behavior
- Since the coefficient of \(x^3\) (leading term) is positive, the graph rises to \(+\infty\) as \(x \to \infty\) and falls to \(-\infty\) as \(x \to -\infty\).

#### Step 3: Plot Key Points
- The graph touches the x-axis at \(x = 1\) (double root).
- The graph crosses the x-axis at \(x = -2\) (simple root).

#### Step 4: Find Turning Points
Compute the derivative:
\[
\frac{dy}{dx} = 3(x - 1)^2 + 2(x - 1)(x + 2)
\]
Solve \(\frac{dy}{dx} = 0\) to find critical points.

#### Step 5: Sketch the Curve
- Start from \(-\infty\), crossing the x-axis at \(x = -2\).
- The graph rises, touches the x-axis at \(x = 1\), forms a turning point, and rises to \(+\infty\).

---

### **Key Observations**
1. The double root causes the graph to "bounce off" or touch the x-axis.
2. The simple root is where the curve transitions between positive and negative y-values.
3. The relative steepness and shape depend on the value of \(a\).




## **Dividing Polynomials by Manipulating Rational Expressions**

Dividing polynomials often involves expressing the division as a rational expression and simplifying it using algebraic techniques. These techniques include factoring, canceling common terms, and splitting the rational expression into simpler components.

---

### **Steps for Dividing Polynomials**

1. **Write the Division as a Rational Expression**:
   A polynomial division problem can be written as:
   \[
   \frac{P(x)}{Q(x)}
   \]
   where \(P(x)\) is the dividend and \(Q(x)\) is the divisor.

2. **Factor Both Polynomials** (if possible):
   Break both the numerator and the denominator into their factored forms.

3. **Simplify the Expression**:
   - Cancel out common factors between the numerator and denominator.
   - Ensure that \(Q(x) \neq 0\), as division by zero is undefined.

4. **Perform Long Division (if needed)**:
   - If the degree of \(P(x)\) is greater than or equal to \(Q(x)\), perform polynomial long division to simplify the expression.
   - The result will often be expressed as a combination of a quotient and a remainder:
     \[
     \frac{P(x)}{Q(x)} = \text{Quotient} + \frac{\text{Remainder}}{Q(x)}
     \]

---

### **Techniques**

#### **1. Factoring and Simplifying**
Example:  
Divide \(P(x) = x^3 - 3x^2 - 4x + 12\) by \(Q(x) = x^2 - 4\).

**Solution**:
- Factor both polynomials:
  \[
  P(x) = (x^2 - 4)(x - 3), \quad Q(x) = (x - 2)(x + 2)
  \]
- Write as a rational expression:
  \[
  \frac{P(x)}{Q(x)} = \frac{(x^2 - 4)(x - 3)}{(x - 2)(x + 2)}
  \]
- Simplify by canceling \(x^2 - 4 = (x - 2)(x + 2)\):
  \[
  \frac{P(x)}{Q(x)} = x - 3
  \]

#### **2. Polynomial Long Division**
Example:  
Divide \(P(x) = x^3 + 2x^2 - x - 2\) by \(Q(x) = x^2 - 1\).

**Solution**:
- Perform long division:
  1. Divide the leading term of \(P(x)\) (\(x^3\)) by the leading term of \(Q(x)\) (\(x^2\)) to get \(x\).
  2. Multiply \(Q(x)\) by \(x\): \(x(x^2 - 1) = x^3 - x\).
  3. Subtract: \(x^3 + 2x^2 - x - 2 - (x^3 - x) = 2x^2 - 2\).
  4. Divide \(2x^2\) by \(x^2\): \(+2\).
  5. Multiply \(Q(x)\) by \(2\): \(2(x^2 - 1) = 2x^2 - 2\).
  6. Subtract: \(2x^2 - 2 - (2x^2 - 2) = 0\).

**Quotient**:
\[
x + 2
\]

---

#### **3. Splitting Rational Expressions**
Example:  
Simplify \(\frac{x^3 + x^2}{x^2 - x}\).

**Solution**:
- Factor both numerator and denominator:
  \[
  \frac{x^3 + x^2}{x^2 - x} = \frac{x^2(x + 1)}{x(x - 1)}
  \]
- Simplify:
  \[
  \frac{x^3 + x^2}{x^2 - x} = \frac{x(x + 1)}{x - 1}, \quad x \neq 0
  \]

---

### **Key Points to Remember**
1. **Check for Undefined Values**:
   Always ensure the denominator \(Q(x) \neq 0\), and note restrictions on \(x\) after simplifying.

2. **Use Factoring Where Possible**:
   Factoring simplifies the division and reduces the risk of computational errors.

3. **Long Division When Necessary**:
   If the numerator’s degree is higher than the denominator’s, use long division to express the result as a quotient and remainder.

4. **Interpret the Result**:
   Simplified rational expressions can often reveal asymptotic behavior or discontinuities in functions.





##  **Combining Reflections with Other Graph Transformations**

Graph transformations include translations, reflections, stretches, and compressions. When combining these transformations, the sequence and type of operations determine the resulting graph's behavior.

---

### **Key Transformations**
1. **Reflections**:
   - Reflection across the x-axis: Replace \(f(x)\) with \(-f(x)\).
   - Reflection across the y-axis: Replace \(f(x)\) with \(f(-x)\).

2. **Other Transformations**:
   - Vertical stretch/compression: Replace \(f(x)\) with \(a \cdot f(x)\), where \(a > 1\) stretches and \(0 < a < 1\) compresses.
   - Horizontal stretch/compression: Replace \(f(x)\) with \(f(bx)\), where \(b > 1\) compresses and \(0 < b < 1\) stretches.
   - Vertical translation: Replace \(f(x)\) with \(f(x) + k\).
   - Horizontal translation: Replace \(f(x)\) with \(f(x - h)\).

---

### **Combining Reflections with Other Transformations**

When combining reflections with other transformations, the graph undergoes multiple changes based on the order of operations. Here’s how to combine these effects:

1. **Reflection and Translation**:
   - Reflect first, then translate.
   - Example: Start with \(f(x)\), reflect it across the x-axis (\(-f(x)\)), then translate it upward by 3 units (\(-f(x) + 3\)).

2. **Reflection and Stretch/Compression**:
   - Apply the stretch or compression before the reflection.
   - Example: Start with \(f(x)\), vertically stretch it by a factor of 2 (\(2f(x)\)), then reflect it across the x-axis (\(-2f(x)\)).

3. **Reflection and Horizontal Transformations**:
   - Reflect across the y-axis and adjust horizontally.
   - Example: Start with \(f(x)\), reflect it across the y-axis (\(f(-x)\)), then translate it right by 4 units (\(f(-(x - 4))\)).

---

### **Order of Operations**
The general sequence of transformations is:
1. Handle horizontal transformations (\(f(x - h)\), \(f(bx)\)).
2. Apply reflections (\(f(-x)\), \(-f(x)\)).
3. Perform vertical transformations (\(a \cdot f(x)\), \(f(x) + k\)).

---

### **Examples**

#### **1. Combine Reflection Across the X-Axis and Vertical Translation**
Transform \(f(x) = x^2\) by reflecting across the x-axis and translating up 2 units:
- Reflection: \(-f(x) = -x^2\)
- Translation: \(-x^2 + 2\)

Resulting equation: \(y = -x^2 + 2\)

---

#### **2. Combine Reflection Across the Y-Axis and Horizontal Stretch**
Transform \(f(x) = \sqrt{x}\) by reflecting across the y-axis and stretching horizontally by a factor of 2:
- Reflection: \(f(-x) = \sqrt{-x}\)
- Horizontal stretch: \(f(-x/2) = \sqrt{-x/2}\)

Resulting equation: \(y = \sqrt{-x/2}\)

---

#### **3. Combine Multiple Transformations**
Transform \(f(x) = x^3\) by reflecting across the x-axis, stretching vertically by a factor of 3, and translating left by 1 unit:
- Reflection: \(-f(x) = -x^3\)
- Vertical stretch: \(-3f(x) = -3x^3\)
- Horizontal translation: \(-3f(x + 1) = -3(x + 1)^3\)

Resulting equation: \(y = -3(x + 1)^3\)

---

### **Graphing Tips**
1. Apply transformations in sequence to visualize the graph’s evolution.
2. Use test points to confirm the graph’s behavior after each transformation.
3. Be consistent with the signs of transformations, especially when combining reflections and translations.






##  **Computing Probabilities for Compound Events Using Venn Diagrams**

Venn diagrams are powerful tools for visualizing relationships and calculating probabilities for compound events in probability theory. These events may involve unions (\(A \cup B\)), intersections (\(A \cap B\)), or complements (\(A^c\)).

---

### **Key Concepts**

1. **Union (\(A \cup B\))**:
   - Represents all outcomes in \(A\) **or** \(B\) (or both).
   - Probability formula:
     \[
     P(A \cup B) = P(A) + P(B) - P(A \cap B)
     \]

2. **Intersection (\(A \cap B\))**:
   - Represents all outcomes in **both** \(A\) and \(B\).
   - Probability formula:
     \[
     P(A \cap B) = P(A) + P(B) - P(A \cup B)
     \]

3. **Complement (\(A^c\))**:
   - Represents all outcomes **not in \(A\)**.
   - Probability formula:
     \[
     P(A^c) = 1 - P(A)
     \]

4. **Mutually Exclusive Events**:
   - \(A\) and \(B\) are mutually exclusive if \(P(A \cap B) = 0\).

---

### **Steps to Compute Probabilities Using Venn Diagrams**

1. **Draw the Venn Diagram**:
   - Create circles for each event and label them.
   - Overlap circles to show intersections where events occur together.

2. **Assign Probabilities**:
   - Divide the sample space into regions and label each with its corresponding probability (e.g., \(P(A \cap B)\), \(P(A \cap B^c)\)).

3. **Apply Formulas**:
   - Use the union, intersection, and complement formulas to calculate probabilities.

4. **Verify Completeness**:
   - Ensure all regions in the sample space add up to 1.

---

### **Examples**

#### **1. Compute \(P(A \cup B)\):**
Suppose:
- \(P(A) = 0.4\),
- \(P(B) = 0.3\),
- \(P(A \cap B) = 0.1\).

**Solution**:
Using the formula for union:
\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]
\[
P(A \cup B) = 0.4 + 0.3 - 0.1 = 0.6
\]

---

#### **2. Compute \(P(A^c \cap B)\):**
Suppose:
- \(P(A) = 0.5\),
- \(P(B) = 0.4\),
- \(P(A \cap B) = 0.2\).

**Solution**:
1. Complement of \(A\): \(P(A^c) = 1 - P(A) = 1 - 0.5 = 0.5\).
2. Use the total probability:
   \[
   P(A^c \cap B) = P(B) - P(A \cap B)
   \]
   \[
   P(A^c \cap B) = 0.4 - 0.2 = 0.2
   \]

---

#### **3. Verify Using a Venn Diagram**
If the sample space is divided into regions based on \(A\) and \(B\), assign:
- \(P(A \cap B) = 0.2\),
- \(P(A \cap B^c) = 0.3\),
- \(P(A^c \cap B) = 0.2\),
- \(P(A^c \cap B^c) = 0.3\).

**Verification**:
- Total sample space = \(P(A \cap B) + P(A \cap B^c) + P(A^c \cap B) + P(A^c \cap B^c)\):
  \[
  0.2 + 0.3 + 0.2 + 0.3 = 1
  \]

---

### **Tips**
- Always label the regions in the Venn diagram clearly.
- Double-check calculations, especially for intersections and complements.
- Ensure probabilities sum to 1, reflecting the total sample space.





##  **Graph Transformations of Square Root Functions**

The square root function, \( f(x) = \sqrt{x} \), is a common base function. Transformations can shift, stretch, compress, or reflect its graph. These transformations can be expressed in a general form:

\[
g(x) = a \cdot \sqrt{b(x - h)} + k
\]

Each parameter (\(a\), \(b\), \(h\), and \(k\)) introduces a specific transformation.

---

### **Types of Transformations**

#### **1. Horizontal Shifts (\(h\))**
- If \(h > 0\): The graph shifts **right** by \(h\) units.
- If \(h < 0\): The graph shifts **left** by \(|h|\) units.
- Transformation: \(g(x) = \sqrt{x - h}\).

#### **2. Vertical Shifts (\(k\))**
- If \(k > 0\): The graph shifts **up** by \(k\) units.
- If \(k < 0\): The graph shifts **down** by \(|k|\) units.
- Transformation: \(g(x) = \sqrt{x} + k\).

#### **3. Vertical Stretch/Compression (\(a\))**
- If \(a > 1\): The graph is **stretched vertically**.
- If \(0 < a < 1\): The graph is **compressed vertically**.
- If \(a < 0\): The graph is **reflected across the x-axis** and also stretched/compressed.
- Transformation: \(g(x) = a \cdot \sqrt{x}\).

#### **4. Horizontal Stretch/Compression (\(b\))**
- If \(b > 1\): The graph is **compressed horizontally**.
- If \(0 < b < 1\): The graph is **stretched horizontally**.
- If \(b < 0\): The graph is **reflected across the y-axis** and also stretched/compressed.
- Transformation: \(g(x) = \sqrt{b \cdot x}\).

---

### **Combined Transformations**

Transformations are often combined, as shown in the general form:
\[
g(x) = a \cdot \sqrt{b(x - h)} + k
\]

#### **Order of Operations**
1. Apply horizontal transformations (\(x - h\), \(b(x - h)\)).
2. Perform vertical transformations (\(a \cdot \sqrt{x}\), \(\sqrt{x} + k\)).

---

### **Examples**

#### **1. Horizontal Shift**
Transform \(f(x) = \sqrt{x}\) to \(g(x) = \sqrt{x - 3}\):
- The graph shifts **right** by 3 units.

#### **2. Vertical Stretch and Shift**
Transform \(f(x) = \sqrt{x}\) to \(g(x) = 2\sqrt{x} + 1\):
- Vertical stretch by a factor of 2.
- Shift up by 1 unit.

#### **3. Reflection and Horizontal Compression**
Transform \(f(x) = \sqrt{x}\) to \(g(x) = -\sqrt{2x}\):
- Reflect across the x-axis.
- Compress horizontally by a factor of \(\sqrt{2}\).

#### **4. Combined Transformations**
Transform \(f(x) = \sqrt{x}\) to \(g(x) = -3\sqrt{0.5(x + 4)} - 2\):
- Reflect across the x-axis.
- Vertical stretch by a factor of 3.
- Horizontal stretch by a factor of \(\sqrt{2}\).
- Shift left by 4 units.
- Shift down by 2 units.

---

### **Graphing Tips**
1. Identify the base function \(f(x) = \sqrt{x}\).
2. Apply transformations step by step:
   - Horizontal shifts/compressions.
   - Vertical reflections/stretches/shifts.
3. Plot key points (e.g., vertex and additional points to the right of the vertex).
4. Use symmetry when applicable to verify the shape.

By understanding each parameter's role, transformations of square root functions can be visualized 
and graphed accurately.





##  **Properties of Transformed Square Root Functions**

The square root function \( f(x) = \sqrt{x} \) has a standard set of properties. When transformed using the general equation:

\[
g(x) = a \cdot \sqrt{b(x - h)} + k
\]

its properties change based on the parameters \(a\), \(b\), \(h\), and \(k\). Here's how the transformations affect key properties:

---

### **1. Domain**
The domain of \(g(x)\) is the set of input values (\(x\)) for which the function is defined.

- **Base Function**: \( \text{Domain of } f(x) = \sqrt{x} \) is \([0, \infty)\).
- **Transformed Function**: 
  - The horizontal shift (\(h\)) and horizontal stretch/compression (\(b\)) affect the domain:
    \[
    \text{Domain: } x \geq h \text{ when } b > 0, \quad x \leq h \text{ when } b < 0.
    \]

---

### **2. Range**
The range is the set of output values (\(g(x)\)).

- **Base Function**: \( \text{Range of } f(x) = \sqrt{x} \) is \([0, \infty)\).
- **Transformed Function**: 
  - The vertical shift (\(k\)) and vertical stretch/compression (\(a\)) affect the range:
    \[
    \text{Range: } g(x) \geq k \text{ when } a > 0, \quad g(x) \leq k \text{ when } a < 0.
    \]

---

### **3. End Behavior**
The end behavior describes how the function behaves as \(x \to \infty\).

- **Base Function**: As \(x \to \infty\), \(f(x) \to \infty\).
- **Transformed Function**: 
  - For \(g(x) = a \cdot \sqrt{b(x - h)} + k\):
    \[
    \text{As } x \to \infty, \, g(x) \to k + \infty \text{ if } a > 0, \quad g(x) \to k - \infty \text{ if } a < 0.
    \]

---

### **4. Symmetry**
- The base square root function \(f(x) = \sqrt{x}\) has no symmetry (neither even nor odd).
- Transformed functions also typically lack symmetry unless \(g(x)\) is centered on a symmetric domain (rare for square root functions).

---

### **5. Intercepts**
- **x-Intercept**: Set \(g(x) = 0\) and solve for \(x\):
  \[
  0 = a \cdot \sqrt{b(x - h)} + k \implies x = h - \frac{k^2}{a^2b} \text{ (if \(k \neq 0\))}.
  \]
- **y-Intercept**: Set \(x = 0\) and solve for \(g(x)\):
  \[
  g(0) = a \cdot \sqrt{b(0 - h)} + k \text{ (defined if \(h \leq 0\))}.
  \]

---

### **6. Increasing/Decreasing Behavior**
- The square root function is always increasing for its domain.
- A reflection across the x-axis (\(a < 0\)) makes the function always decreasing for its domain.

---

### **7. Vertex**
The "starting point" of the transformed square root function is \((h, k)\), determined by the horizontal (\(h\)) and vertical (\(k\)) shifts.

---

### **8. Shape and Orientation**
- The shape is determined by the stretch/compression factor \(|a|\) and \(|b|\).
  - \(a > 1\): Vertically stretched.
  - \(0 < a < 1\): Vertically compressed.
  - \(b > 1\): Horizontally compressed.
  - \(0 < b < 1\): Horizontally stretched.
- Reflections:
  - \(a < 0\): Reflects across the x-axis.
  - \(b < 0\): Reflects across the y-axis.

---

### **Example**
For \(g(x) = 2\sqrt{3(x - 4)} - 5\):
- Domain: \(x \geq 4\),
- Range: \(g(x) \geq -5\),
- Vertex: \((4, -5)\),
- x-Intercept: Solve \(2\sqrt{3(x - 4)} - 5 = 0\),
- y-Intercept: \(g(0) = 2\sqrt{3(0 - 4)} - 5 \text{ (undefined)}\).





## **Graphing Cubic Curves Containing One Distinct Real Root**

A cubic equation with one distinct real root and two complex conjugate roots can be expressed in the general form:

\[
f(x) = a(x - r_1)(x^2 + px + q)
\]

Here:
- \(r_1\) is the distinct real root.
- \(x^2 + px + q\) represents the irreducible quadratic factor corresponding to the two complex roots.
- \(a\) is the leading coefficient that affects the vertical stretch/compression and orientation of the graph.

---

### **Key Characteristics of Such Cubic Curves**
1. **One Real Root:**
   - The real root (\(r_1\)) is where the curve intersects the x-axis.

2. **Two Complex Conjugate Roots:**
   - These roots do not appear as x-intercepts, but their influence is reflected in the curve's overall shape (smooth turning points).

3. **End Behavior:**
   - As \(x \to \infty\), \(f(x) \to \infty\) if \(a > 0\), or \(f(x) \to -\infty\) if \(a < 0\).
   - As \(x \to -\infty\), \(f(x) \to -\infty\) if \(a > 0\), or \(f(x) \to \infty\) if \(a < 0\).

4. **Symmetry:**
   - The curve generally lacks symmetry unless the equation is specifically structured to exhibit it (e.g., centered at the origin).

---

### **Steps to Graph the Curve**

1. **Find the Real Root:**
   - Solve \(f(x) = 0\) to find \(r_1\).

2. **Identify the Quadratic Factor:**
   - Analyze \(x^2 + px + q\) to understand the curve's turning behavior.

3. **Determine End Behavior:**
   - Evaluate the sign and magnitude of \(a\).

4. **Plot Key Points:**
   - Include the real root, \(f(0)\) (y-intercept), and additional points near the real root to capture the shape.

5. **Sketch the Curve:**
   - Use the above information to smoothly connect the real root and turning points while respecting the end behavior.

---

### **Example**
Graph the cubic curve \(f(x) = (x - 1)(x^2 + 4x + 5)\):

1. **Distinct Real Root:** \(x = 1\) (where \(f(x) = 0\)).
2. **Quadratic Factor:** \(x^2 + 4x + 5\) has complex roots \(-2 \pm i\), contributing smooth turning behavior.
3. **End Behavior:** As \(x \to \infty\), \(f(x) \to \infty\); as \(x \to -\infty\), \(f(x) \to -\infty\).
4. **Key Points:**
   - \(f(0) = (0 - 1)(0^2 + 4(0) + 5) = -5\).
   - Evaluate additional points like \(f(-1)\), \(f(2)\), etc.

---

### **Graph Features**
- A single x-intercept at \(x = 1\).
- A smooth curve influenced by the complex roots, with one peak and one trough.
- End behavior follows the leading coefficient \(a = 1\).

This approach ensures an accurate sketch of cubic curves with one distinct real root.





##  **Limits of Exponential Functions**

Exponential functions take the general form:

\[
f(x) = a \cdot b^x
\]

where:
- \(a\) is a constant (the initial value or vertical stretch factor),
- \(b\) is the base of the exponential (typically \(b > 0\) and \(b \neq 1\)).

The behavior of limits for exponential functions depends on the value of \(b\) and whether \(x\) approaches \(\infty\) or \(-\infty\).

---

### **1. Exponential Growth (\(b > 1\))**
For \(f(x) = a \cdot b^x\) with \(b > 1\):
- **As \(x \to \infty\):**
  \[
  \lim_{x \to \infty} a \cdot b^x = \infty \quad \text{(if \(a > 0\)) or \(-\infty\) (if \(a < 0\))}.
  \]
- **As \(x \to -\infty\):**
  \[
  \lim_{x \to -\infty} a \cdot b^x = 0 \quad \text{(exponentially approaches 0)}.
  \]

Example:
\[
f(x) = 2 \cdot 3^x
\]
- As \(x \to \infty\), \(f(x) \to \infty\).
- As \(x \to -\infty\), \(f(x) \to 0^+\).

---

### **2. Exponential Decay (\(0 < b < 1\))**
For \(f(x) = a \cdot b^x\) with \(0 < b < 1\):
- **As \(x \to \infty\):**
  \[
  \lim_{x \to \infty} a \cdot b^x = 0 \quad \text{(decays to zero)}.
  \]
- **As \(x \to -\infty\):**
  \[
  \lim_{x \to -\infty} a \cdot b^x = \infty \quad \text{(if \(a > 0\)) or \(-\infty\) (if \(a < 0\))}.
  \]

Example:
\[
f(x) = 5 \cdot (0.5)^x
\]
- As \(x \to \infty\), \(f(x) \to 0^+\).
- As \(x \to -\infty\), \(f(x) \to \infty\).

---

### **3. Special Base (\(b = e\))**
For the natural exponential function \(f(x) = a \cdot e^x\):
- The growth or decay properties are similar, depending on \(a\):
  - **As \(x \to \infty\):**
    \[
    \lim_{x \to \infty} a \cdot e^x = \infty \quad \text{(if \(a > 0\)) or \(-\infty\) (if \(a < 0\))}.
    \]
  - **As \(x \to -\infty\):**
    \[
    \lim_{x \to -\infty} a \cdot e^x = 0.
    \]

---

### **4. Horizontal Asymptote**
In all cases, when exponential functions decay (as \(x \to -\infty\) for \(b > 1\), or \(x \to \infty\) for \(0 < b < 1\)), they approach a horizontal asymptote:
\[
y = 0.
\]

---

### **Summary Table**

| Base \(b\)            | \(x \to \infty\)           | \(x \to -\infty\)        |
|------------------------|---------------------------|--------------------------|
| \(b > 1\)             | \(\infty\) (or \(-\infty\)) | \(0^+\)                 |
| \(0 < b < 1\)         | \(0^+\)                   | \(\infty\) (or \(-\infty\)) |
| \(b = e\)             | Growth like \(b > 1\)     | Same as \(b > 1\)        |





## **Properties of Transformed Exponential Functions**

Exponential functions can be transformed in various ways, and these transformations affect their shape, position, and behavior. The general form of a transformed exponential function is:

\[
f(x) = a \cdot b^{k(x - h)} + c
\]

Here:
- \(a\): Vertical stretch/compression and reflection.
- \(b\): Base of the exponential function (\(b > 0\) and \(b \neq 1\)).
- \(k\): Horizontal stretch/compression and reflection.
- \(h\): Horizontal shift.
- \(c\): Vertical shift.

---

### **Key Transformations and Their Effects**

#### **1. Vertical Stretch/Compression and Reflection (\(a\))**
- \(a > 1\): The graph stretches vertically (steeper growth/decay).
- \(0 < a < 1\): The graph compresses vertically (flatter growth/decay).
- \(a < 0\): The graph reflects across the x-axis.

#### **2. Horizontal Stretch/Compression and Reflection (\(k\))**
- \(k > 1\): The graph compresses horizontally (growth/decay is faster).
- \(0 < k < 1\): The graph stretches horizontally (growth/decay is slower).
- \(k < 0\): The graph reflects across the y-axis.

#### **3. Horizontal Shift (\(h\))**
- \(h > 0\): The graph shifts \(h\) units to the right.
- \(h < 0\): The graph shifts \(|h|\) units to the left.

#### **4. Vertical Shift (\(c\))**
- \(c > 0\): The graph shifts \(c\) units up.
- \(c < 0\): The graph shifts \(|c|\) units down.

---

### **Properties of the Transformed Function**

1. **Domain:**
   The domain of any exponential function remains:
   \[
   (-\infty, \infty)
   \]

2. **Range:**
   The range depends on the vertical shift (\(c\)) and reflection (\(a\)):
   - If \(a > 0\): \((c, \infty)\)
   - If \(a < 0\): \((-\infty, c)\)

3. **Horizontal Asymptote:**
   The horizontal asymptote shifts with \(c\):
   \[
   y = c
   \]

4. **End Behavior:**
   The end behavior depends on \(a\), \(b\), and \(k\):
   - If \(a > 0\) and \(b > 1\): \(f(x) \to \infty\) as \(x \to \infty\), and \(f(x) \to c\) as \(x \to -\infty\).
   - If \(a < 0\): The behavior is reversed.

---

### **Example Transformations**

1. **Original Function:**
   \(f(x) = 2^x\)

2. **Transformation 1:**
   \(f(x) = 2 \cdot 2^x - 3\)
   - Vertical stretch by a factor of 2.
   - Shifted 3 units down.
   - Range: \((-3, \infty)\).
   - Horizontal asymptote: \(y = -3\).

3. **Transformation 2:**
   \(f(x) = -2^{x - 1} + 4\)
   - Reflected across the x-axis.
   - Shifted 1 unit right and 4 units up.
   - Range: \((-\infty, 4)\).
   - Horizontal asymptote: \(y = 4\).

---

### **Graphing Strategy**
1. Start with the basic exponential graph \(b^x\).
2. Apply transformations in this order:
   - Horizontal shift (\(h\)),
   - Stretch/compression/reflection (\(a\) and \(k\)),
   - Vertical shift (\(c\)).
3. Mark the horizontal asymptote, shifted points, and key features like the y-intercept.

This approach ensures a clear understanding and accurate graph of any transformed exponential function.





## **Finding Equations of Perpendicular Lines**

When two lines are perpendicular, the product of their slopes is \(-1\). If the slope of one line is \(m_1\), then the slope of the line perpendicular to it is:

\[
m_2 = -\frac{1}{m_1}, \quad \text{provided \(m_1 \neq 0\).}
\]

If one line is vertical (\(m_1 = \infty\)), the perpendicular line is horizontal (\(m_2 = 0\)), and vice versa.

---

### **Steps to Find the Equation of a Perpendicular Line**

1. **Find the slope of the given line:**
   - If the line is given in slope-intercept form (\(y = mx + b\)), the slope is \(m\).
   - If the line is given in standard form (\(Ax + By = C\)), rewrite it as \(y = mx + b\) or use:
     \[
     m = -\frac{A}{B}.
     \]

2. **Determine the slope of the perpendicular line:**
   - Use the relationship:
     \[
     m_{\text{perpendicular}} = -\frac{1}{m}.
     \]

3. **Use the point-slope formula to write the equation:**
   - If the perpendicular line passes through a point \((x_1, y_1)\), use:
     \[
     y - y_1 = m_{\text{perpendicular}}(x - x_1).
     \]

4. **Simplify the equation:**
   - Rearrange into slope-intercept form (\(y = mx + b\)) or standard form (\(Ax + By = C\)) as needed.

---

### **Examples**

#### **Example 1:**
Find the equation of the line perpendicular to \(y = 2x + 3\) and passing through the point \((4, 1)\).

1. Slope of the given line: \(m = 2\).
2. Slope of the perpendicular line:
   \[
   m_{\text{perpendicular}} = -\frac{1}{2}.
   \]
3. Use the point-slope formula:
   \[
   y - 1 = -\frac{1}{2}(x - 4).
   \]
4. Simplify:
   \[
   y - 1 = -\frac{1}{2}x + 2 \quad \Rightarrow \quad y = -\frac{1}{2}x + 3.
   \]

#### **Example 2:**
Find the equation of the line perpendicular to \(3x - 4y = 8\) and passing through the point \((-2, 5)\).

1. Rewrite the given line in slope-intercept form:
   \[
   -4y = -3x + 8 \quad \Rightarrow \quad y = \frac{3}{4}x - 2.
   \]
   The slope is \(m = \frac{3}{4}\).
2. Slope of the perpendicular line:
   \[
   m_{\text{perpendicular}} = -\frac{1}{m} = -\frac{1}{\frac{3}{4}} = -\frac{4}{3}.
   \]
3. Use the point-slope formula:
   \[
   y - 5 = -\frac{4}{3}(x + 2).
   \]
4. Simplify:
   \[
   y - 5 = -\frac{4}{3}x - \frac{8}{3} \quad \Rightarrow \quad y = -\frac{4}{3}x + \frac{7}{3}.
   \]

---

### **Key Notes**
- The perpendicular slope is always the negative reciprocal of the original slope.
- Be cautious when dealing with horizontal (\(m = 0\)) and vertical lines (\(m = \infty\)).
- Simplify equations into the desired form for clarity.



##  **Covariance: Definition and Explanation**

Covariance is a statistical measure that quantifies the relationship between two random variables, indicating how changes in one variable are associated with changes in the other. It measures the degree to which two variables vary together.

---

### **Formula for Covariance**

Given two random variables \(X\) and \(Y\), with \(n\) data points, the covariance is calculated as:

\[
\text{Cov}(X, Y) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu_X)(y_i - \mu_Y)
\]

Where:
- \(x_i\): The \(i\)-th value of \(X\),
- \(y_i\): The \(i\)-th value of \(Y\),
- \(\mu_X\): The mean of \(X\),
- \(\mu_Y\): The mean of \(Y\),
- \(n\): The number of data points.

For a sample, the formula becomes:

\[
\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{X})(y_i - \bar{Y})
\]

Where:
- \(\bar{X}\) and \(\bar{Y}\): Sample means of \(X\) and \(Y\).

---

### **Interpreting Covariance**
- **Positive Covariance:** Indicates that as \(X\) increases, \(Y\) also tends to increase (and vice versa).
- **Negative Covariance:** Indicates that as \(X\) increases, \(Y\) tends to decrease (and vice versa).
- **Zero Covariance:** Suggests no linear relationship between \(X\) and \(Y\).

However, the magnitude of covariance is not standardized, so it’s difficult to assess the strength of the relationship using covariance alone.

---

### **Relation to Correlation**
Correlation is a standardized version of covariance that ranges between \(-1\) and \(1\). It is given by:

\[
\text{Corr}(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}
\]

Where:
- \(\sigma_X\) and \(\sigma_Y\): Standard deviations of \(X\) and \(Y\).

---

### **Example Calculation**

Suppose we have two variables \(X = [1, 2, 3]\) and \(Y = [4, 5, 6]\).

1. Calculate the means:
   \[
   \mu_X = \frac{1 + 2 + 3}{3} = 2, \quad \mu_Y = \frac{4 + 5 + 6}{3} = 5
   \]

2. Compute deviations from the mean:
   \[
   (x_i - \mu_X) = [-1, 0, 1], \quad (y_i - \mu_Y) = [-1, 0, 1]
   \]

3. Compute the product of deviations:
   \[
   (x_i - \mu_X)(y_i - \mu_Y) = [1, 0, 1]
   \]

4. Compute covariance (for the population):
   \[
   \text{Cov}(X, Y) = \frac{1}{3} \sum (x_i - \mu_X)(y_i - \mu_Y) = \frac{1}{3}(1 + 0 + 1) = \frac{2}{3}
   \]

---

### **Applications of Covariance**
1. **Portfolio Optimization:** Used to assess how asset prices move together.
2. **Statistics:** Determines relationships between variables in regression and other analyses.
3. **Machine Learning:** Helps in feature selection and data preprocessing.

Covariance is a foundational concept in statistics and data analysis, essential for understanding relationships between variables.





##  **The Connection Between Variance and Covariance**

Variance and covariance are closely related concepts in statistics, both describing how data values spread and relate to each other. Covariance generalizes the idea of variance to describe relationships between two variables, while variance specifically measures the spread of a single variable.

---

### **Variance as a Special Case of Covariance**

The variance of a single variable \(X\) is the covariance of \(X\) with itself. Mathematically:

\[
\text{Var}(X) = \text{Cov}(X, X)
\]

From the covariance formula:

\[
\text{Cov}(X, Y) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu_X)(y_i - \mu_Y),
\]

when \(Y = X\):

\[
\text{Var}(X) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu_X)^2.
\]

This demonstrates that variance measures how a variable varies with itself.

---

### **Key Insights**
1. **Variance is Self-Covariance:**
   - Variance quantifies the spread of a single variable around its mean.
   - Covariance extends this idea to measure how two variables change together.

2. **Relationship in Multivariable Contexts:**
   - In a multivariable setting, the covariance matrix is a generalization of variance and covariance. For variables \(X_1, X_2, \dots, X_n\), the covariance matrix contains variances along the diagonal and covariances off-diagonal:
     \[
     \Sigma =
     \begin{bmatrix}
     \text{Var}(X_1) & \text{Cov}(X_1, X_2) & \cdots & \text{Cov}(X_1, X_n) \\
     \text{Cov}(X_2, X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2, X_n) \\
     \vdots & \vdots & \ddots & \vdots \\
     \text{Cov}(X_n, X_1) & \text{Cov}(X_n, X_2) & \cdots & \text{Var}(X_n)
     \end{bmatrix}.
     \]

3. **Interpretation of Variance and Covariance:**
   - **Variance:** Measures the extent to which values of a variable deviate from its mean.
   - **Covariance:** Measures the extent to which two variables move together.

---

### **Example: Variance and Covariance**

Suppose \(X = [1, 2, 3]\) and \(Y = [2, 4, 6]\).

#### **Variance:**
1. Mean of \(X\): \(\mu_X = \frac{1 + 2 + 3}{3} = 2\).
2. Variance of \(X\):
   \[
   \text{Var}(X) = \frac{1}{3} \sum (x_i - \mu_X)^2 = \frac{1}{3}[(1-2)^2 + (2-2)^2 + (3-2)^2] = \frac{1}{3}[1 + 0 + 1] = \frac{2}{3}.
   \]

#### **Covariance:**
1. Mean of \(Y\): \(\mu_Y = \frac{2 + 4 + 6}{3} = 4\).
2. Covariance:
   \[
   \text{Cov}(X, Y) = \frac{1}{3} \sum (x_i - \mu_X)(y_i - \mu_Y) = \frac{1}{3}[(-1)(-2) + (0)(0) + (1)(2)] = \frac{1}{3}(2 + 0 + 2) = \frac{4}{3}.
   \]

---

### **Conclusion**
- **Variance:** Focuses on the spread of one variable.
- **Covariance:** Expands this to the relationship between two variables.
- Covariance forms the basis for many statistical concepts, such as correlation and the covariance matrix in multivariate statistics.






## **Factorials in Variable Expressions**

Factorials are a mathematical operation denoted by \(n!\) (read as "n factorial"). For a positive integer \(n\), the factorial is defined as:

\[
n! = n \cdot (n-1) \cdot (n-2) \cdot \dots \cdot 2 \cdot 1
\]

For special cases:
\[
0! = 1
\]

Factorials often appear in variable expressions, particularly in combinations, permutations, and series expansions. Understanding how to manipulate factorials in variable expressions is crucial for solving problems in algebra, probability, and calculus.

---

### **Common Manipulations of Factorials in Variable Expressions**

1. **Simplifying Factorials:**
   Factorials can be simplified using the recursive definition:
   \[
   n! = n \cdot (n-1)!
   \]
   For example:
   \[
   \frac{n!}{(n-1)!} = n
   \]

2. **Factorial Expansions:**
   Expand factorials to cancel terms in fractions:
   \[
   \frac{n!}{(n-k)!} = n \cdot (n-1) \cdot (n-2) \cdot \dots \cdot (n-k+1)
   \]
   This is often used in permutations:
   \[
   P(n, k) = \frac{n!}{(n-k)!}
   \]

3. **Expressions Involving Factorials:**
   Combine and simplify factorials by canceling common terms:
   \[
   \frac{(n+1)!}{n!} = n+1
   \]

4. **Factorials in Binomial Coefficients:**
   Factorials are used in the binomial coefficient:
   \[
   \binom{n}{k} = \frac{n!}{k!(n-k)!}
   \]

---

### **Examples**

#### **Example 1: Simplify a Fraction with Factorials**
Simplify:
\[
\frac{(n+2)!}{n!}
\]

Solution:
\[
(n+2)! = (n+2)(n+1)n!
\]
\[
\frac{(n+2)!}{n!} = (n+2)(n+1)
\]

#### **Example 2: Simplify a Binomial Coefficient**
Simplify:
\[
\binom{n+2}{2}
\]

Solution:
\[
\binom{n+2}{2} = \frac{(n+2)!}{2!(n+2-2)!} = \frac{(n+2)(n+1)n!}{2! \cdot n!}
\]
\[
= \frac{(n+2)(n+1)}{2}
\]

#### **Example 3: Solve an Equation Involving Factorials**
Solve for \(n\):
\[
\frac{n!}{(n-2)!} = 30
\]

Solution:
\[
\frac{n!}{(n-2)!} = n \cdot (n-1) \cdot (n-2)! / (n-2)! = n(n-1)
\]
\[
n(n-1) = 30
\]
Solve the quadratic equation:
\[
n^2 - n - 30 = 0
\]
\[
(n-6)(n+5) = 0
\]
\[
n = 6 \quad (\text{reject } n = -5, \text{factorials are non-negative}).
\]

---

### **Applications of Factorials**
1. **Combinatorics:**
   - Permutations: \(P(n, k) = \frac{n!}{(n-k)!}\)
   - Combinations: \(\binom{n}{k} = \frac{n!}{k!(n-k)!}\)

2. **Series Expansions:**
   - Factorials appear in Taylor series and Maclaurin series:
     \[
     e^x = \sum_{n=0}^\infty \frac{x^n}{n!}
     \]

3. **Probability:**
   - Counting outcomes in arrangements and selections.

Factorials are foundational in many areas of mathematics and their manipulation is an essential skill.





## **Solving Exponential Equations with Different Bases Using Logarithms**

When solving exponential equations where the bases are different and cannot be rewritten to have the same base, logarithms are used as a tool to simplify and solve the equations.

---

### **Steps to Solve Exponential Equations with Logarithms**

1. **Write the Equation:**
   Start with the given exponential equation:
   \[
   a^x = b
   \]
   or
   \[
   a^{f(x)} = b
   \]

2. **Take the Logarithm of Both Sides:**
   Apply logarithms to both sides of the equation. You can use natural logarithms (\(\ln\)) or common logarithms (\(\log\)):
   \[
   \log(a^x) = \log(b)
   \]
   Using the property of logarithms \(\log(a^x) = x \cdot \log(a)\), rewrite the equation:
   \[
   x \cdot \log(a) = \log(b)
   \]

3. **Solve for \(x\):**
   Rearrange to isolate \(x\):
   \[
   x = \frac{\log(b)}{\log(a)}
   \]

4. **Substitute Values (if needed):**
   Plug in the values of \(a\) and \(b\) and calculate the result using a calculator.

---

### **Examples**

#### **Example 1: Solve \(2^x = 16\)**
1. Take \(\log\) of both sides:
   \[
   \log(2^x) = \log(16)
   \]

2. Use the logarithmic property:
   \[
   x \cdot \log(2) = \log(16)
   \]

3. Solve for \(x\):
   \[
   x = \frac{\log(16)}{\log(2)}
   \]

4. Simplify using \(\log(16) = \log(2^4) = 4 \cdot \log(2)\):
   \[
   x = \frac{4 \cdot \log(2)}{\log(2)} = 4
   \]

---

#### **Example 2: Solve \(3^{2x-1} = 5\)**
1. Take \(\log\) of both sides:
   \[
   \log(3^{2x-1}) = \log(5)
   \]

2. Apply the logarithmic property:
   \[
   (2x-1) \cdot \log(3) = \log(5)
   \]

3. Expand and solve for \(x\):
   \[
   2x \cdot \log(3) - \log(3) = \log(5)
   \]
   \[
   2x \cdot \log(3) = \log(5) + \log(3)
   \]
   \[
   x = \frac{\log(5) + \log(3)}{2 \cdot \log(3)}
   \]

---

#### **Example 3: Solve \(4^{x+1} = 7^{2x-3}\)**
1. Take \(\ln\) of both sides:
   \[
   \ln(4^{x+1}) = \ln(7^{2x-3})
   \]

2. Apply the logarithmic property:
   \[
   (x+1) \cdot \ln(4) = (2x-3) \cdot \ln(7)
   \]

3. Expand:
   \[
   x \cdot \ln(4) + \ln(4) = 2x \cdot \ln(7) - 3 \cdot \ln(7)
   \]

4. Group terms with \(x\) on one side:
   \[
   x \cdot \ln(4) - 2x \cdot \ln(7) = -\ln(4) - 3 \cdot \ln(7)
   \]

5. Factor out \(x\):
   \[
   x \cdot (\ln(4) - 2 \cdot \ln(7)) = -\ln(4) - 3 \cdot \ln(7)
   \]

6. Solve for \(x\):
   \[
   x = \frac{-\ln(4) - 3 \cdot \ln(7)}{\ln(4) - 2 \cdot \ln(7)}
   \]

---

### **Key Logarithmic Properties Used**
1. \(\log(a^x) = x \cdot \log(a)\)
2. \(\log(ab) = \log(a) + \log(b)\)
3. \(\log(a/b) = \log(a) - \log(b)\)

---

### **Applications**
1. **Exponential Growth and Decay:**
   Solving population growth, radioactive decay, or compound interest problems.
2. **Physics and Engineering:**
   Analyzing waveforms, oscillations, and energy dissipation.
3. **Logarithmic Scales:**
   Used in decibel measurements, Richter scale, and pH calculations.


   

##  **Combining Graph Transformations of Reciprocal Functions**

The reciprocal function, in its basic form, is:

\[
f(x) = \frac{1}{x}
\]

This function has key characteristics:
- It is undefined at \(x = 0\) (vertical asymptote).
- It has a horizontal asymptote at \(y = 0\).
- The graph is symmetric about the origin (odd function).

When graph transformations are applied to \(f(x) = \frac{1}{x}\), the resulting function takes the form:

\[
f(x) = \frac{a}{b(x - h)} + k
\]

Here:
- \(a\): Vertical stretch/compression and reflection about the \(x\)-axis.
- \(b\): Horizontal stretch/compression and reflection about the \(y\)-axis.
- \(h\): Horizontal shift.
- \(k\): Vertical shift.

---

### **Types of Transformations**

1. **Vertical Stretch/Compression and Reflection:**
   - \(a > 1\): Vertical stretch.
   - \(0 < a < 1\): Vertical compression.
   - \(a < 0\): Reflects the graph about the \(x\)-axis.

2. **Horizontal Stretch/Compression and Reflection:**
   - \(b > 1\): Horizontal compression.
   - \(0 < b < 1\): Horizontal stretch.
   - \(b < 0\): Reflects the graph about the \(y\)-axis.

3. **Horizontal Shift:**
   - \(h > 0\): Shifts the graph to the right by \(h\).
   - \(h < 0\): Shifts the graph to the left by \(|h|\).

4. **Vertical Shift:**
   - \(k > 0\): Shifts the graph up by \(k\).
   - \(k < 0\): Shifts the graph down by \(|k|\).

---

### **Steps to Combine Transformations**

1. **Start with the Basic Graph:**
   Begin with the graph of \(f(x) = \frac{1}{x}\).

2. **Apply Horizontal and Vertical Shifts:**
   - Shift the graph horizontally by \(h\).
   - Shift the graph vertically by \(k\).

   The vertical and horizontal asymptotes move to \(x = h\) and \(y = k\), respectively.

3. **Apply Reflections and Stretches/Compressions:**
   - If \(a\) or \(b\) are negative, reflect the graph.
   - Apply any stretching or compressing transformations.

4. **Plot Key Points and Asymptotes:**
   Identify how the transformations affect specific points on the graph and redraw the asymptotes.

---

### **Example**

#### **Transform \(f(x) = \frac{1}{x}\) to \(f(x) = -\frac{2}{x+3} + 4\):**

1. **Horizontal Shift:**
   \(x + 3\) shifts the graph left by 3. The vertical asymptote moves to \(x = -3\).

2. **Vertical Shift:**
   \(+4\) shifts the graph up by 4. The horizontal asymptote moves to \(y = 4\).

3. **Reflection About the \(x\)-Axis:**
   The negative sign in \(-\frac{2}{x+3}\) reflects the graph about the \(x\)-axis.

4. **Vertical Stretch:**
   The factor \(2\) stretches the graph vertically, making it steeper.

**Final Adjustments:**
- Vertical asymptote: \(x = -3\).
- Horizontal asymptote: \(y = 4\).
- The graph is flipped and stretched due to the transformations.

---

### **Applications**
- **Physics:** Reciprocal relationships like \(V = \frac{1}{R}\) in electrical circuits.
- **Economics:** Diminishing returns or inverse proportionality.
- **Statistics:** Reciprocal transformations to linearize data.

By combining transformations carefully, the shape and behavior of reciprocal functions can be tailored 
to fit a wide range of scenarios.




## 





























































































































