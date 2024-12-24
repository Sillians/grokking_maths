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




## **Domain and Range of Quadratic Functions
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
















































































































































































































































































































