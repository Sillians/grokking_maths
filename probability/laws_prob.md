## **Laws of Probability**

Probability theory follows fundamental laws that help determine the likelihood of events occurring. 
These laws provide a framework for solving probability problems systematically.

---

### **1. The Probability Range Law**
For any event $`A`$, the probability must be between 0 and 1:

$`0 \leq P(A) \leq 1`$

- $`P(A) = 0`$ means $A$ is impossible.
- $`P(A) = 1`$ means $A$ is certain.

---

### **2. The Law of Complementation**
The probability of an event **not occurring** (denoted as $`A^c`$ or $\neg A$) is:

$`P(A^c) = 1 - P(A)`$

Example: If the probability of rain today is 0.7, then the probability of no rain is:

$`1 - 0.7 = 0.3`$

---

### **3. The Addition Law (Union of Events)**
For two events $A$ and $B$:

$`P(A \cup B) = P(A) + P(B) - P(A \cap B)`$

- If $A$ and $B$ are **mutually exclusive** (disjoint, meaning $`P(A \cap B) = 0`$ ), then:

$`P(A \cup B) = P(A) + P(B)`$

Example: Probability of rolling a 2 or a 4 on a fair die:

$`P(2) + P(4) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}`$

---

### **4. The Multiplication Law (Intersection of Events)**
For two **independent** events $A$ and $B$:

$`P(A \cap B) = P(A) \cdot P(B)`$

Example: Probability of flipping two heads in two coin tosses:

$`P(H) \times P(H) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}`$

For **dependent** events:

$`P(A \cap B) = P(A) \cdot P(B | A)`$

where $`P(B | A)`$ is the probability of $B$ occurring given that $A$ has occurred.

---

### **5. The Law of Total Probability**
If $`B_1, B_2, \dots, B_n`$ are **mutually exclusive** and **exhaustive** events (they cover all possible outcomes), then:

$`P(A) = P(A | B_1) P(B_1) + P(A | B_2) P(B_2) + \dots + P(A | B_n) P(B_n)`$

Example: If a factory produces 60% of its products from machine $M_1$ and 40% from machine $M_2$, 
and the defect rates are 2% and 5% respectively, then the probability of getting a defective product is:

$`P(D) = P(D | M_1) P(M_1) + P(D | M_2) P(M_2)`$

$`= (0.02 \times 0.6) + (0.05 \times 0.4) = 0.012 + 0.02 = 0.032`$

---

### **6. Bayes' Theorem (Conditional Probability)**
If $A$ and $B$ are two events, the probability of $A$ occurring given $B$ has occurred is:

$`P(A | B) = \frac{P(B | A) P(A)}{P(B)}`$

This helps in revising probabilities when new information is available.

Example: If a medical test is 99% accurate and the disease affects 1 in 10,000 people, 
Bayes' theorem helps find the true probability that a positive test result means a person has the disease.

---

### **7. The Law of Conditional Probability**
The probability of event $A$ occurring given $B$ has already occurred is:

$`P(A | B) = \frac{P(A \cap B)}{P(B)}`$

Example: If 30% of students play soccer and 10% play soccer and basketball, then the probability 
that a student plays basketball given that they play soccer is:


$`P(B | S) = \frac{P(B \cap S)}{P(S)} = \frac{0.1}{0.3} = \frac{1}{3}`$

---

### **8. The Multiplication Rule for Conditional Probability**
For any two events:


$`P(A \cap B) = P(A | B) P(B)`$


This is useful in problems involving sequential events.

Example: The probability of drawing two aces in a row from a deck of 52:


$`P(A_1 \cap A_2) = P(A_1) \times P(A_2 | A_1)`$

$`= \frac{4}{52} \times \frac{3}{51} = \frac{1}{221}`$

---

### **Conclusion**
These probability laws form the backbone of statistical reasoning, decision-making, and machine learning. 
Mastering them enables solving complex probability problems efficiently.