## **Introduction to Probability:**

### **1. Random Experiment**
- A **random experiment** is an action or process that leads to one of many possible outcomes.
- Examples:
  - **Flipping a coin:** Outcomes → Heads, Tails.
  - **Rolling a die:** Outcomes → 1, 2, 3, 4, 5, 6.
  - **Exam marks:** Outcomes → Any number from 0 to 100.
- The list of possible outcomes must be **exhaustive** (cover all possibilities) and **mutually exclusive** (no overlap).

---

### **2. Sample Space**
- The **sample space (S)** is the set of all possible outcomes of a random experiment.
- Notation:  
  \[
  S = \{O_1, O_2, O_3, \dots\}
  \]
- Example:  
  - Rolling a die: \( S = \{1,2,3,4,5,6\} \).

---

### **3. Events**
- A **simple event** is a single outcome from the sample space.
- An **event** is a collection of one or more simple events.
- Example: Rolling a die
  - **Simple Event:** Getting a 3 → \( \{3\} \).
  - **Event:** Rolling an even number → \( \{2,4,6\} \).

---

### **4. Assigning Probabilities**
- **Requirements for probabilities:**
  1. \( P(O_i) \geq 0 \) (Probabilities are non-negative).
  2. \( P(S) = 1 \) (The sum of probabilities of all outcomes equals 1).
  3. For disjoint events \( A \) and \( B \):  
     \[
     P(A \cup B) = P(A) + P(B)
     \]

- **Three Approaches to Assigning Probabilities:**
  1. **Classical Approach:** Assumes all outcomes are equally likely.
  2. **Relative-Frequency Approach:** Based on past data or repeated experiments.
  3. **Subjective Approach:** Based on belief or judgment (e.g., betting, stock predictions).

---

### **5. Probability Calculation Approaches**
#### **A. Classical Approach (Axiomatic Approach)**
- If an experiment has \( n \) simple outcomes, each has a probability of \( 1/n \).
- Example:
  - Rolling a fair die: Each outcome has \( P(O_i) = \frac{1}{6} \).

#### **B. Relative-Frequency Approach**
- Probabilities are estimated based on past experiments.
- Formula:
  \[
  P(A) = \lim_{n \to \infty} \frac{n_A}{n}
  \]
  where \( n_A \) is the number of times event \( A \) occurs in \( n \) trials.
- Example: If a die is rolled 100 times and lands on "1" exactly 15 times,  
  \[
  P(1) \approx \frac{15}{100} = 0.15.
  \]

#### **C. Subjective Approach**
- Probability is based on personal belief rather than objective data.
- Example:
  - Probability of a specific horse winning a race.
  - Probability of a stock increasing in price.

---

### **6. Basic Probability Rules**
#### **A. Complement Rule**
- The probability of an event NOT occurring:
  \[
  P(A^c) = 1 - P(A)
  \]
- Example:  
  - Rolling a die: \( P(3) = \frac{1}{6} \), so \( P(\text{not 3}) = 1 - \frac{1}{6} = \frac{5}{6} \).

#### **B. Addition Rule (Union)**
- If \( A \) and \( B \) are any two events:
  \[
  P(A \cup B) = P(A) + P(B) - P(A \cap B)
  \]
- If \( A \) and \( B \) are **mutually exclusive**, then \( P(A \cap B) = 0 \), so:
  \[
  P(A \cup B) = P(A) + P(B)
  \]

#### **C. Conditional Probability**
- The probability of event \( A \) occurring **given that** event \( B \) has already occurred:
  \[
  P(A | B) = \frac{P(A \cap B)}{P(B)}
  \]
- Example:  
  - Drawing an Ace from a deck given that the card drawn is a Spade.
  - \( P(\text{Spade Ace} | \text{Ace}) = \frac{1/52}{4/52} = \frac{1}{4} \).

#### **D. Multiplication Rule**
- The probability of **both** events \( A \) and \( B \) occurring:
  \[
  P(A \cap B) = P(A | B) P(B)
  \]
  or equivalently:
  \[
  P(A \cap B) = P(B | A) P(A)
  \]
- Example:  
  - Probability of drawing two Aces in a row from a shuffled deck:
    \[
    P(A_1 \cap A_2) = P(A_1) \times P(A_2 | A_1) = \frac{4}{52} \times \frac{3}{51} = \frac{1}{221}.
    \]

#### **E. Independence of Events**
- Two events \( A \) and \( B \) are independent if:
  \[
  P(A | B) = P(A)
  \]
  or equivalently:
  \[
  P(A \cap B) = P(A) P(B)
  \]
- Example:
  - Drawing two cards **with replacement** (the probability remains unchanged).

---

### **7. Bayes' Theorem**
- Used to update probabilities based on new information.
- Formula:
  \[
  P(B_i | A) = \frac{P(A | B_i) P(B_i)}{\sum_{j=1}^{k} P(A | B_j) P(B_j)}
  \]
- Example:  
  - Given a student answered a multiple-choice question correctly, what is the probability they actually knew the answer?

---

### **8. Applications of Probability**
- **Gambling and Betting**
- **Machine Learning and Data Science** (Bayesian models, Naïve Bayes classifier)
- **Stock Market Predictions**
- **Medical Testing (False Positives and Negatives)**

---

### **Summary**
1. **Fundamental concepts** (sample spaces, events, probability assignment).
2. **Probability rules** (complement rule, addition rule, conditional probability, multiplication rule, independence).
3. **Three approaches to probability** (classical, relative-frequency, subjective).
4. **Advanced concepts** like Bayes' theorem and probability trees.










