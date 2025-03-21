# **Interpreting a Piecewise Function**

A **piecewise function** is a function that is defined by different expressions based on the input value. 
It allows for different behaviors over different domains. 

---

### **1. Structure of a Piecewise Function**
A piecewise function is written as:

$`f(x) = \begin{cases} \text{Expression 1}, & \text{if } x \text{ is in domain 1} \\ \text{Expression 2}, & \text{if } x \text{ is in domain 2} \\ \vdots & \vdots \end{cases}`$

Each piece is valid for a specific range of $x$, which is explicitly stated.

---

### **2. Steps to Interpret a Piecewise Function**
1. **Identify the Different Expressions**  
   - Each expression represents a specific rule for the function over a certain interval.

2. **Examine the Domain for Each Piece**  
   - Check which values of $x$ correspond to which expressions.

3. **Evaluate Function Values**  
   - To find $f(a)$ for some $a$, determine which interval $a$ falls into and use the corresponding expression.

4. **Check for Continuity or Discontinuity**  
   - If the function "jumps" from one value to another at a boundary, it is discontinuous there.
   - If the function smoothly transitions between pieces, it is continuous.

---

### **3. Example Interpretation**
Consider:

$`f(x) = \begin{cases}  x^2, & \text{if } x < 0 \\ 2x + 1, & \text{if } 0 \leq x < 3 \\ 7, & \text{if } x \geq 3 \end{cases}`$

- **For $`x < 0`$**: The function follows $`f(x) = x^2`$, meaning it's quadratic.  
- **For $`0 \leq x < 3`$**: The function follows $`f(x) = 2x + 1`$, a linear equation.  
- **For $`x \geq 3`$**: The function is constant at $`f(x) = 7`$.  

To evaluate specific values:
- $`f(-2) = (-2)^2 = 4`$
- $`f(1) = 2(1) + 1 = 3`$
- $`f(3) = 7`$

Checking continuity:
- At $`x = 0`$:  
  - Left-hand limit $`\lim\limits_{x \to 0^-} f(x) = 0^2 = 0`$
  - Right-hand limit $`\lim\limits_{x \to 0^+} f(x) = 2(0) + 1 = 1`$
  - Since limits don’t match, **discontinuous at \( x = 0 \)**.

- At $`x = 3`$:  
  - Left-hand limit $`\lim\limits_{x \to 3^-} f(x) = 2(3) + 1 = 7`$  
  - Right-hand limit $`\lim\limits_{x \to 3^+} f(x) = 7`$ 
  - Limits match, so **continuous at \( x = 3 \)**.

---

### **4. Real-World Applications**
- **Tax brackets**: Different tax rates apply to different income ranges.  
- **Shipping costs**: Fees vary based on package weight.  
- **Speed limits**: Vary depending on location (e.g., highway vs. city).  

Piecewise functions allow for **modeling different behaviors** depending on the input, making them crucial in applied mathematics.