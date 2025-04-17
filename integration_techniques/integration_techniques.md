## **Integration Techniques: Deep Dive with Explanations and Examples**

---

### **1. Substitution (u-substitution)**

**Purpose**: Simplifies integration by changing variables.

**Idea**: If an integral contains a function and its derivative, substitute the inner 
function with a new variable.

**Formula**:

$`\int f(g(x))g'(x) \, dx = \int f(u) \, du`$

**Example**:

$`\int 2x \cdot \cos(x^2) \, dx`$

Let $`u = x^2 \Rightarrow du = 2x \, dx`$. The integral becomes:

$`\int \cos(u) \, du = \sin(u) + C = \sin(x^2) + C`$


---

### **2. Integration by Parts**

**Purpose**: Integrates products of functions.

**Formula**:

$`\int u \, dv = uv - \int v \, du`$

**Example**:

$`\int x e^x \, dx`$

Let $`u = x, \ dv = e^x dx \Rightarrow du = dx, \ v = e^x`$

$`\int x e^x \, dx = x e^x - \int e^x dx = x e^x - e^x + C`$

---

### **3. Trigonometric Integrals**

**Purpose**: Deals with powers or products of trig functions.

**Useful identities**:

- $`\boxed{\sin^2(x) = \frac{1 - \cos(2x)}{2}}`$
- $`\boxed{\cos^2(x) = \frac{1 + \cos(2x)}{2}}`$
- $`\boxed{\sin(2x) = 2\sin(x)\cos(x)}`$
- $`\boxed{\cos(2x) = \cos^2(x) - \sin^2(x)}`$

**Examples**:

- $`\int \sin^2(x) \, dx`$

  Using identity:  
  
  $`\sin^2(x) = \frac{1 - \cos(2x)}{2}`$
  

  Steps:  
  
  $`\int \sin^2(x) \, dx = \int \frac{1 - \cos(2x)}{2} \, dx = \frac{x}{2} - \frac{\sin(2x)}{4} + C`$

  

---

### **4. Trigonometric Substitution**

**Purpose**: Used with square roots involving quadratics.

**Substitutions**:

- $`\sqrt{a^2 - x^2} \Rightarrow x = a\sin\theta`$
- $`\sqrt{a^2 + x^2} \Rightarrow x = a\tan\theta`$
- $`\sqrt{x^2 - a^2} \Rightarrow x = a\sec\theta`$

**Example**:

$`\int \frac{1}{\sqrt{4 - x^2}} \, dx \Rightarrow x = 2\sin\theta \Rightarrow dx = 2\cos\theta \, d\theta`$


$`\int \frac{1}{\sqrt{4 - 4\sin^2\theta}} \cdot 2\cos\theta \, d\theta = \int d\theta = \theta + C \Rightarrow \sin^{-1}(x/2) + C`$


---

### **5. Partial Fraction Decomposition**

**Purpose**: Breaks rational functions into simpler terms.

**Example**:

$`\int \frac{1}{x^2 - 1} \, dx = \int \left(\frac{1}{2(x - 1)} - \frac{1}{2(x + 1)}\right) dx`$


$`= \frac{1}{2} \ln|x - 1| - \frac{1}{2} \ln|x + 1| + C`$


---

### **6. Completing the Square**

**Purpose**: Simplifies integrals involving quadratics.

**Example**:

$`\int \frac{1}{x^2 + 4x + 5} \, dx \Rightarrow \int \frac{1}{(x + 2)^2 + 1} \, dx`$


$`= \tan^{-1}(x + 2) + C`$

---

### **7. Numerical Integration**

**Purpose**: Approximate the value of a definite integral when exact methods are hard.

**Methods**:

- **Trapezoidal Rule**:

  $`\int_a^b f(x) \, dx \approx \frac{b - a}{2}(f(a) + f(b))`$

- **Simpson's Rule**:
  
  $`\int_a^b f(x) \, dx \approx \frac{b - a}{6} [f(a) + 4f(\frac{a+b}{2}) + f(b)]`$
  

---

### **8. Improper Integrals**

**Purpose**: Evaluates integrals with infinite limits or discontinuities.

**Example**:

$`\int_1^\infty \frac{1}{x^2} \, dx = \lim_{t \to \infty} \int_1^t x^{-2} \, dx = \lim_{t \to \infty} [-x^{-1}]_1^t = 1`$


---

### **9. Integration by Table or CAS**

**Purpose**: For complex integrals without elementary antiderivatives.

**Tools**:

- Use integration tables
- Symbolic software: WolframAlpha, SymPy, MATLAB

---

Each technique is a tool for a specific class of problems. Selecting the correct method requires analyzing the structure of the integrand.

