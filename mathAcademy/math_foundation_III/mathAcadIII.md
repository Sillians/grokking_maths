## Mathematical Foundations III


For more Details about Math Academy:

- [mathacademy.com](https://mathacademy.com/learn)

- [News Ycombinator 41534847](https://news.ycombinator.com/item?id=41534847)

- [News Ycombinator 36073631](https://news.ycombinator.com/item?id=36073631)


## Content
### 1. Sequences and Series
### 2. Inequalities
### 3. Parameter & Polar Coordinates
### 4. Conic Sections
### 5. Trigonometry
### 6. Complex Numbers
### 7. Limits and Continuity
### 8. Differentiation
### 9. Definite Integrals
### 10. Integration Techniques
### 11. Contextual Applications of Calculus
### 12. Differential Equations
### 13. Vectors
### 14. Linear Algebra
### 15. Probability.




## **Implicit Differentiatione**  

Implicit differentiation is a technique used to find the derivative of a function when **it is not explicitly solved for one variable in terms of another**. 
This is especially useful for equations where **solving for y in terms of x is difficult or impossible**.  

#### **🔹 When to Use Implicit Differentiation?**  
- When a function is **not given explicitly** as \( y = f(x) \).  
- When it's easier to differentiate **both sides of the equation** rather than solving for \( y \).  
- When working with curves like **circles, ellipses, or complex equations**.  

---

### **1️⃣ Key Concept: Differentiating Both Sides**
Given an equation involving **both \( x \) and \( y \)**, apply **differentiation to both sides**, treating \( y \) as an **implicit function of \( x \)**.  

- **Differentiate \( x \) normally.**  
- **Differentiate \( y \) using the Chain Rule**, multiplying by \( \frac{dy}{dx} \) (since \( y \) is a function of \( x \)).  

#### **Example 1: Differentiating \( x^2 + y^2 = 25 \)**  
1. Differentiate both sides:  
   \[
   \frac{d}{dx} (x^2 + y^2) = \frac{d}{dx} (25)
   \]
2. Apply derivatives:  
   \[
   2x + 2y \frac{dy}{dx} = 0
   \]
3. Solve for \( \frac{dy}{dx} \):  
   \[
   \frac{dy}{dx} = -\frac{x}{y}
   \]  

This is the derivative of a **circle** \( x^2 + y^2 = 25 \).

---

### **2️⃣ Chain Rule in Implicit Differentiation**
Since \( y \) is **implicitly defined**, we apply the **chain rule** whenever differentiating a term involving \( y \).  

#### **Example 2: Differentiating \( x^3 + y^3 = 9xy \)**  
1. Differentiate both sides:  
   \[
   \frac{d}{dx} (x^3) + \frac{d}{dx} (y^3) = \frac{d}{dx} (9xy)
   \]
2. Apply derivatives:
   \[
   3x^2 + 3y^2 \frac{dy}{dx} = 9 \left( x \frac{dy}{dx} + y \right)
   \]
3. Solve for \( \frac{dy}{dx} \):  
   \[
   3y^2 \frac{dy}{dx} - 9x \frac{dy}{dx} = 9y - 3x^2
   \]
   \[
   \frac{dy}{dx} (3y^2 - 9x) = 9y - 3x^2
   \]
   \[
   \frac{dy}{dx} = \frac{9y - 3x^2}{3y^2 - 9x}
   \]

---

### **3️⃣ Higher-Order Implicit Differentiation**
For second derivatives (\( \frac{d^2y}{dx^2} \)), differentiate implicitly **again**.

#### **Example 3: Finding \( \frac{d^2y}{dx^2} \) for \( x^2 + y^2 = 1 \)**  
1. First derivative:  
   \[
   2x + 2y \frac{dy}{dx} = 0
   \]
   \[
   \frac{dy}{dx} = -\frac{x}{y}
   \]
2. Differentiate again using the **quotient rule**:  
   \[
   \frac{d}{dx} \left( -\frac{x}{y} \right)
   \]
   Using the quotient rule:
   \[
   \frac{d^2y}{dx^2} = -\frac{y(1) - x\frac{dy}{dx}}{y^2}
   \]
   Substituting \( \frac{dy}{dx} = -\frac{x}{y} \),
   \[
   \frac{d^2y}{dx^2} = -\frac{y - x(-x/y)}{y^2}
   \]
   \[
   = -\frac{y + x^2/y}{y^2}
   \]
   \[
   = -\frac{y^2 + x^2}{y^3}
   \]

---

### **4️⃣ Applications of Implicit Differentiation**
- **Tangents & Normals to Curves:**  
  - Find slopes of curves without solving explicitly for \( y \).  
- **Physics & Related Rates:**  
  - Problems involving motion (e.g., **circle expansion, volume changes**).  
- **Curvature & Second Derivatives:**  
  - Helps compute **concavity and inflection points**.  

---

### **5️⃣ Summary**
✅ Differentiate both sides while treating \( y \) as a function of \( x \).  
✅ Use the **chain rule** when differentiating terms involving \( y \).  
✅ Solve for \( \frac{dy}{dx} \) explicitly.  
✅ For second derivatives, differentiate **implicitly again**.  

Implicit differentiation is a **powerful tool** for handling equations where solving for \( y \) is difficult, 
making it essential in **calculus, physics, and engineering**.





## **Dot Product of a Vector Using Angle and Magnitude**  

The **dot product** (or **scalar product**) of two vectors quantifies their alignment by measuring how much one vector projects onto another. 
When using the **angle** between vectors and their **magnitudes**, the dot product has a straightforward geometric interpretation.

---

### **🔹 1. Formula for the Dot Product Using Angle and Magnitude**  
Given two vectors **\( \mathbf{A} \)** and **\( \mathbf{B} \)** with magnitudes \( |\mathbf{A}| \) and \( |\mathbf{B}| \), the dot product is defined as:

\[
\mathbf{A} \cdot \mathbf{B} = |\mathbf{A}| |\mathbf{B}| \cos\theta
\]

where:  
- \( \theta \) is the **angle** between \( \mathbf{A} \) and \( \mathbf{B} \) (measured from \( 0^\circ \) to \( 180^\circ \)),  
- \( |\mathbf{A}| \) and \( |\mathbf{B}| \) are the **magnitudes (lengths)** of the vectors,  
- \( \cos\theta \) determines how much the vectors point in the same direction.  

---

### **🔹 2. Interpretation of the Dot Product**
- If \( \theta = 0^\circ \), then \( \cos(0) = 1 \), and  
  \[
  \mathbf{A} \cdot \mathbf{B} = |\mathbf{A}| |\mathbf{B}|
  \]
  (Vectors are perfectly aligned in the same direction).  
- If \( \theta = 90^\circ \), then \( \cos(90^\circ) = 0 \), so  
  \[
  \mathbf{A} \cdot \mathbf{B} = 0
  \]
  (Vectors are perpendicular, meaning no projection onto each other).  
- If \( \theta = 180^\circ \), then \( \cos(180^\circ) = -1 \), so  
  \[
  \mathbf{A} \cdot \mathbf{B} = - |\mathbf{A}| |\mathbf{B}|
  \]
  (Vectors are completely opposite in direction).  

---

### **🔹 3. Step-by-Step Calculation**
#### **Example 1: Compute \( \mathbf{A} \cdot \mathbf{B} \) Using Magnitudes and Angle**  
Let:  
- \( |\mathbf{A}| = 5 \),  
- \( |\mathbf{B}| = 7 \),  
- \( \theta = 60^\circ \).  

Using the dot product formula:

\[
\mathbf{A} \cdot \mathbf{B} = (5)(7) \cos(60^\circ)
\]

Since \( \cos 60^\circ = \frac{1}{2} \):

\[
\mathbf{A} \cdot \mathbf{B} = (5)(7) \times \frac{1}{2}
\]

\[
= 35 \times 0.5 = 17.5
\]

Thus, \( \mathbf{A} \cdot \mathbf{B} = 17.5 \).

---

### **🔹 4. Alternative: Computing the Angle from the Dot Product**
If the dot product and magnitudes are known, the angle \( \theta \) can be found using:

\[
\cos\theta = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}
\]

#### **Example 2: Finding the Angle Between Vectors**
Given:  
- \( \mathbf{A} \cdot \mathbf{B} = 20 \),  
- \( |\mathbf{A}| = 4 \),  
- \( |\mathbf{B}| = 6 \).  

Solve for \( \theta \):

\[
\cos\theta = \frac{20}{(4)(6)}
\]

\[
= \frac{20}{24} = \frac{5}{6}
\]

Taking the inverse cosine:

\[
\theta = \cos^{-1} \left( \frac{5}{6} \right)
\]

Using a calculator:

\[
\theta \approx 33.56^\circ
\]

---

### **🔹 5. Applications of the Dot Product**
The dot product is widely used in:  
✅ **Physics:** Work done by a force is calculated as \( W = \mathbf{F} \cdot \mathbf{d} \), where \( \mathbf{F} \) is force and \( \mathbf{d} \) is displacement.  
✅ **Computer Graphics:** Used to determine lighting, shading, and angles between surfaces.  
✅ **Machine Learning & Neural Networks:** Measures cosine similarity, which helps in text similarity, recommendation systems, and clustering.  
✅ **Geometry & Engineering:** Finds angles between vectors in structural analysis.  

---

### **🔹 6. Summary**
✅ **Formula:** \( \mathbf{A} \cdot \mathbf{B} = |\mathbf{A}| |\mathbf{B}| \cos\theta \)  
✅ **Key Cases:**  
- \( \theta = 0^\circ \Rightarrow \) Maximum alignment (positive dot product).  
- \( \theta = 90^\circ \Rightarrow \) Perpendicular vectors (dot product = 0).  
- \( \theta = 180^\circ \Rightarrow \) Opposite vectors (negative dot product).  
✅ **Finding \( \theta \):** Use \( \cos\theta = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|} \).  

This method provides a **powerful tool for understanding vector relationships in physics, engineering, and machine learning**.




## **Sum and Difference Formulas for Sine**  

The **sum and difference formulas** for sine allow us to compute the sine of the sum or difference of two angles. 
These formulas are fundamental in trigonometry and are used in various applications, including physics, 
engineering, and signal processing.

---

### **🔹 1. Formulas**  
For two angles \( A \) and \( B \):

#### **Sum Formula for Sine**
\[
\sin(A + B) = \sin A \cos B + \cos A \sin B
\]

#### **Difference Formula for Sine**
\[
\sin(A - B) = \sin A \cos B - \cos A \sin B
\]

---

### **🔹 2. Derivation Using the Unit Circle**  
The sum and difference formulas can be derived using the unit circle, rotations, or Euler’s formula. A common geometric proof involves representing sine and cosine in terms of right triangles and using the properties of angles in the unit circle.

---

### **🔹 3. Applications and Examples**  

#### **Example 1: Compute \( \sin 75^\circ \) Using the Sum Formula**  
Since \( 75^\circ = 45^\circ + 30^\circ \), use:

\[
\sin(45^\circ + 30^\circ) = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ
\]

Using known values:

\[
\sin 45^\circ = \frac{\sqrt{2}}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2}, \quad \cos 45^\circ = \frac{\sqrt{2}}{2}, \quad \sin 30^\circ = \frac{1}{2}
\]

\[
\sin 75^\circ = \left( \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} \right) + \left( \frac{\sqrt{2}}{2} \times \frac{1}{2} \right)
\]

\[
= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}
\]

---

#### **Example 2: Compute \( \sin 15^\circ \) Using the Difference Formula**  
Since \( 15^\circ = 45^\circ - 30^\circ \), use:

\[
\sin(45^\circ - 30^\circ) = \sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ
\]

Using known values:

\[
\sin 15^\circ = \left( \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} \right) - \left( \frac{\sqrt{2}}{2} \times \frac{1}{2} \right)
\]

\[
= \frac{\sqrt{6}}{4} - \frac{\sqrt{2}}{4} = \frac{\sqrt{6} - \sqrt{2}}{4}
\]

---

### **🔹 4. Summary**
✅ **Sum Formula:** \( \sin(A + B) = \sin A \cos B + \cos A \sin B \)  
✅ **Difference Formula:** \( \sin(A - B) = \sin A \cos B - \cos A \sin B \)  
✅ **Used for:**  
- Calculating trigonometric values for non-standard angles  
- Simplifying trigonometric expressions  
- Solving physics and engineering problems  

These formulas are **powerful tools** in trigonometry and frequently appear in calculus, Fourier analysis, and wave mechanics.






## **Sum and Difference Formulas for Sine**  

The **sum and difference formulas** for sine allow us to compute the sine of the sum or difference of two angles. 
These formulas are fundamental in trigonometry and are used in various applications, including physics, 
engineering, and signal processing.

---

### **🔹 1. Formulas**  
For two angles \( A \) and \( B \):

#### **Sum Formula for Sine**
\[
\sin(A + B) = \sin A \cos B + \cos A \sin B
\]

#### **Difference Formula for Sine**
\[
\sin(A - B) = \sin A \cos B - \cos A \sin B
\]

---

### **🔹 2. Derivation Using the Unit Circle**  
The sum and difference formulas can be derived using the unit circle, rotations, or Euler’s formula. A common geometric proof involves representing sine and cosine in terms of right triangles and using the properties of angles in the unit circle.

---

### **🔹 3. Applications and Examples**  

#### **Example 1: Compute \( \sin 75^\circ \) Using the Sum Formula**  
Since \( 75^\circ = 45^\circ + 30^\circ \), use:

\[
\sin(45^\circ + 30^\circ) = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ
\]

Using known values:

\[
\sin 45^\circ = \frac{\sqrt{2}}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2}, \quad \cos 45^\circ = \frac{\sqrt{2}}{2}, \quad \sin 30^\circ = \frac{1}{2}
\]

\[
\sin 75^\circ = \left( \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} \right) + \left( \frac{\sqrt{2}}{2} \times \frac{1}{2} \right)
\]

\[
= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}
\]

---

#### **Example 2: Compute \( \sin 15^\circ \) Using the Difference Formula**  
Since \( 15^\circ = 45^\circ - 30^\circ \), use:

\[
\sin(45^\circ - 30^\circ) = \sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ
\]

Using known values:

\[
\sin 15^\circ = \left( \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} \right) - \left( \frac{\sqrt{2}}{2} \times \frac{1}{2} \right)
\]

\[
= \frac{\sqrt{6}}{4} - \frac{\sqrt{2}}{4} = \frac{\sqrt{6} - \sqrt{2}}{4}
\]

---

### **🔹 4. Summary**
✅ **Sum Formula:** \( \sin(A + B) = \sin A \cos B + \cos A \sin B \)  
✅ **Difference Formula:** \( \sin(A - B) = \sin A \cos B - \cos A \sin B \)  
✅ **Used for:**  
- Calculating trigonometric values for non-standard angles  
- Simplifying trigonometric expressions  
- Solving physics and engineering problems  

These formulas are **powerful tools** in trigonometry and frequently appear in calculus, Fourier analysis, 
and wave mechanics.




## **Calculating Velocity for Straight-Line Motion Using Differentiation.**

### 1. **Basic Concepts**

### **Displacement and Velocity**
- **Displacement, \( s(t) \):**  
  The function \( s(t) \) represents the position (or displacement) of an object along a straight line at time \( t \). It tells you where the object is located relative to a reference point.
  
- **Instantaneous Velocity, \( v(t) \):**  
  Instantaneous velocity is defined as the derivative of the displacement function with respect to time:
  \[
  v(t) = \frac{ds(t)}{dt}.
  \]
  This gives the object's velocity at a specific moment in time.

- **Average Velocity:**  
  Over an interval \([t_1, t_2]\), the average velocity is:
  \[
  v_{\text{avg}} = \frac{s(t_2) - s(t_1)}{t_2 - t_1}.
  \]
  Differentiation, however, gives the instantaneous rate of change, which is more precise when the displacement function is continuous and differentiable.

---

### 2. **Why Use Differentiation?**

Differentiation provides the slope of the tangent line to the curve \( s(t) \) at any given point \( t \). This slope represents the instantaneous velocity—indicating not only the speed (the magnitude of the velocity) but also the direction of motion (positive for one direction and negative for the opposite).

---

### 3. **Step-by-Step Process**

### **Step 1: Start with the Displacement Function**

Suppose you are given a displacement function, for example:
\[
s(t) = 5t^2 + 3t + 2.
\]
This function tells you the position of the object at any time \( t \).

### **Step 2: Differentiate the Displacement Function**

Apply the rules of differentiation to \( s(t) \):
- The derivative of \( 5t^2 \) with respect to \( t \) is \( 10t \).
- The derivative of \( 3t \) is \( 3 \).
- The derivative of the constant \( 2 \) is \( 0 \).

Thus, the instantaneous velocity is:
\[
v(t) = s'(t) = 10t + 3.
\]

### **Step 3: Interpret the Result**

- **At \( t = 0 \):**  
  \( v(0) = 10(0) + 3 = 3 \) units per time interval (e.g., meters per second).  
  This means the object starts with an initial velocity of 3 m/s.

- **For \( t > 0 \):**  
  The velocity increases linearly with time. For example, at \( t = 2 \):
  \[
  v(2) = 10(2) + 3 = 23 \, \text{units/time}.
  \]

---

### 4. **Graphical Insight**

- **Displacement Curve:**  
  Plotting \( s(t) \) against \( t \) gives you a curve that shows how the object’s position changes over time.

- **Tangent Line and Slope:**  
  At any point \( t = a \) on the displacement curve, the slope of the tangent line represents \( v(a) \). Drawing the tangent line visually confirms the instantaneous rate of change.

- **Velocity Curve:**  
  Plotting \( v(t) \) against \( t \) (i.e., \( 10t + 3 \)) gives a straight line, which makes it easy to see how velocity changes over time.

---

### 5. **Real-World Applications**

- **Physics and Engineering:**  
  Understanding instantaneous velocity is critical in mechanics, where it is used to determine how objects move, accelerate, or decelerate.

- **Motion Analysis:**  
  In kinematics, differentiating the displacement function gives insights into an object’s behavior—useful for trajectory planning, vehicle dynamics, and more.

- **Optimization and Control:**  
  In control systems, knowing the exact rate of change (velocity) helps in designing systems that can react appropriately to changes in motion.

---

### 6. **Summary**

- **Definition:**  
  Instantaneous velocity \( v(t) \) is the derivative of the displacement function \( s(t) \).
- **Calculation:**  
  Given \( s(t) = 5t^2 + 3t + 2 \), we differentiate term by term to get \( v(t) = 10t + 3 \).
- **Interpretation:**  
  The resulting function \( v(t) \) provides the speed and direction of the object at any given time \( t \).
- **Graphical Analysis:**  
  The slope of the tangent to the displacement curve corresponds to the instantaneous velocity.

By mastering differentiation and understanding its physical interpretation, you can effectively analyze and predict the behavior of objects in straight-line motion.





## **Simplifying Expressions Using Basic Trigonometric Identities**

### **1. Fundamental Trigonometric Identities**
Before simplifying expressions, it's essential to recall the basic identities:

### **Reciprocal Identities**
\[
\sin \theta = \frac{1}{\csc \theta}, \quad \cos \theta = \frac{1}{\sec \theta}, \quad \tan \theta = \frac{1}{\cot \theta}
\]

\[
\csc \theta = \frac{1}{\sin \theta}, \quad \sec \theta = \frac{1}{\cos \theta}, \quad \cot \theta = \frac{1}{\tan \theta}
\]

### **Pythagorean Identities**
\[
\sin^2 \theta + \cos^2 \theta = 1
\]

\[
1 + \tan^2 \theta = \sec^2 \theta
\]

\[
1 + \cot^2 \theta = \csc^2 \theta
\]

### **Quotient Identities**
\[
\tan \theta = \frac{\sin \theta}{\cos \theta}, \quad \cot \theta = \frac{\cos \theta}{\sin \theta}
\]

### **Even-Odd Identities**
\[
\sin(-\theta) = -\sin \theta, \quad \cos(-\theta) = \cos \theta, \quad \tan(-\theta) = -\tan \theta
\]

\[
\csc(-\theta) = -\csc \theta, \quad \sec(-\theta) = \sec \theta, \quad \cot(-\theta) = -\cot \theta
\]

---

### **2. Strategies for Simplifying Trigonometric Expressions**
To simplify an expression, follow these steps:

1. **Rewrite using basic identities** (convert sec, csc, cot, tan into sine and cosine).
2. **Find common denominators** if needed.
3. **Factor expressions** (if possible).
4. **Apply Pythagorean identities** to reduce terms.
5. **Cancel common terms** when applicable.

---

### **3. Examples of Simplifications**
### **Example 1: Simplify \( \frac{\sin \theta}{\cos \theta} + \frac{\cos \theta}{\sin \theta} \)**

**Step 1: Rewrite using Quotient Identities**
\[
\frac{\sin \theta}{\cos \theta} = \tan \theta, \quad \frac{\cos \theta}{\sin \theta} = \cot \theta
\]

So, the given expression becomes:
\[
\tan \theta + \cot \theta
\]

**Step 2: Express Everything in Terms of \(\sin \theta\) and \(\cos \theta\)**
\[
\frac{\sin \theta}{\cos \theta} + \frac{\cos \theta}{\sin \theta}
\]

**Step 3: Find Common Denominator**
\[
\frac{\sin^2 \theta + \cos^2 \theta}{\sin \theta \cos \theta}
\]

Using the **Pythagorean Identity** \( \sin^2 \theta + \cos^2 \theta = 1 \), we get:

\[
\frac{1}{\sin \theta \cos \theta}
\]

Thus, the simplified form is:

\[
\frac{1}{\sin \theta \cos \theta}
\]

---

### **Example 2: Simplify \( \frac{1 - \cos^2 \theta}{\sin \theta} \)**

**Step 1: Apply the Pythagorean Identity**  
Since \( 1 - \cos^2 \theta = \sin^2 \theta \), we substitute:

\[
\frac{\sin^2 \theta}{\sin \theta}
\]

**Step 2: Cancel Common Terms**
\[
\sin \theta
\]

Thus, the simplified expression is:

\[
\sin \theta
\]

---

### **Example 3: Simplify \( \frac{\cot \theta - 1}{1 - \tan \theta} \)**

**Step 1: Express Everything in Terms of \(\tan \theta\)**
\[
\cot \theta = \frac{1}{\tan \theta}
\]

Substituting this:

\[
\frac{\frac{1}{\tan \theta} - 1}{1 - \tan \theta}
\]

**Step 2: Get a Common Denominator in the Numerator**
\[
\frac{\frac{1 - \tan \theta}{\tan \theta}}{1 - \tan \theta}
\]

**Step 3: Rewrite as a Fraction**
Since division by a fraction is multiplication by its reciprocal:

\[
\frac{1 - \tan \theta}{\tan \theta} \times \frac{1}{1 - \tan \theta}
\]

Cancel out \( 1 - \tan \theta \):

\[
\frac{1}{\tan \theta}
\]

**Step 4: Recognize the Result**
Since \( \frac{1}{\tan \theta} = \cot \theta \), we conclude:

\[
\cot \theta
\]

---

### **4. Summary of Key Techniques**
- Convert everything into sine and cosine.
- Use fundamental identities to replace terms.
- Factor expressions when needed.
- Cancel out common terms.
- Apply Pythagorean identities strategically.

By mastering these techniques, complex trigonometric expressions can be efficiently simplified, 
making calculations easier in various mathematical and engineering applications.






## **Approximating Areas With the Left Riemann Sum**  

The **Left Riemann Sum** is a method for approximating the area under a curve (integral)
by summing up the areas of rectangles. The left endpoints of subintervals determine the height of each rectangle.  


#### **Formula**  
If a function \( f(x) \) is defined on an interval \([a, b]\) and divided into \( n \) subintervals of equal width \( \Delta x \), the Left Riemann Sum is:  

\[
L_n = \sum_{i=0}^{n-1} f(x_i) \Delta x
\]

where:  
- \( \Delta x = \frac{b - a}{n} \) is the width of each subinterval,  
- \( x_i = a + i\Delta x \) (starting points of each rectangle),  
- \( f(x_i) \) gives the height of the rectangle using the **left endpoint** of each subinterval.  

#### **Steps to Approximate Area Using the Left Riemann Sum**  
1. **Divide the interval** \([a, b]\) into \( n \) equal subintervals.  
2. **Determine the left endpoints** \( x_0, x_1, ..., x_{n-1} \).  
3. **Evaluate \( f(x) \) at each left endpoint** to get rectangle heights.  
4. **Compute the sum** of all rectangle areas using the formula above.  

#### **Example**  
Approximate the area under \( f(x) = x^2 \) on \( [0,2] \) using \( n = 4 \).  

1. Interval: \([0,2]\), so \( \Delta x = \frac{2-0}{4} = 0.5 \).  
2. Left endpoints: \( x_0 = 0 \), \( x_1 = 0.5 \), \( x_2 = 1 \), \( x_3 = 1.5 \).  
3. Function values:  
   - \( f(0) = 0^2 = 0 \)  
   - \( f(0.5) = (0.5)^2 = 0.25 \)  
   - \( f(1) = 1^2 = 1 \)  
   - \( f(1.5) = (1.5)^2 = 2.25 \)  
4. Compute the sum:  

\[
L_4 = (0 + 0.25 + 1 + 2.25) \times 0.5 = 1.75
\]

Thus, the **Left Riemann Sum approximation** for this integral is **1.75**.  

#### **Observations**  
- The Left Riemann Sum tends to **underestimate** the area for increasing functions.  
- It tends to **overestimate** the area for decreasing functions.  
- Increasing \( n \) improves accuracy, approaching the actual integral value.





## **Simplifying Expressions Using the Pythagorean Identity**  

The **Pythagorean Identities** in trigonometry are fundamental equations derived from the Pythagorean theorem.
They allow the simplification of trigonometric expressions and are given as:  

1. **Primary Identity:**  
   \[
   \sin^2\theta + \cos^2\theta = 1
   \]
2. **Derived Forms:**  
   \[
   1 + \tan^2\theta = \sec^2\theta
   \]
   \[
   1 + \cot^2\theta = \csc^2\theta
   \]

#### **Steps for Simplification**  
1. **Recognize terms** in the given expression that match any Pythagorean identity.  
2. **Substitute** the identity to simplify the expression.  
3. **Factor or rewrite** terms to reduce complexity.  
4. **Cancel out** common factors when possible.  

#### **Examples**  

**Example 1:** Simplify \( 1 - \sin^2\theta \).  
- Using \( \sin^2\theta + \cos^2\theta = 1 \), solve for \( \cos^2\theta \):  
  \[
  \cos^2\theta = 1 - \sin^2\theta
  \]
- So, \( 1 - \sin^2\theta = \cos^2\theta \).  

**Example 2:** Simplify \( \sec^2\theta - \tan^2\theta \).  
- Using \( 1 + \tan^2\theta = \sec^2\theta \), rewrite it as:  
  \[
  \sec^2\theta - \tan^2\theta = 1
  \]  

**Example 3:** Simplify \( \frac{1}{\csc^2\theta} + \frac{1}{\cot^2\theta} \).  
- Using \( \csc^2\theta = 1 + \cot^2\theta \), rewrite:  
  \[
  \frac{1}{\csc^2\theta} + \frac{1}{\cot^2\theta} = \frac{1}{1+\cot^2\theta} + \frac{1}{\cot^2\theta}
  \]  
- Further simplification depends on rewriting in terms of \( \sin\theta \) and \( \cos\theta \).  

Using Pythagorean identities effectively simplifies trigonometric expressions, making calculations more manageable.





## **Alternate Forms of the Pythagorean Identity**  

The **Pythagorean Identity** is a fundamental trigonometric equation derived from the Pythagorean Theorem. 
The standard form is:  

\[
\sin^2 \theta + \cos^2 \theta = 1
\]  

This identity holds for all values of \(\theta\) and forms the basis for deriving alternative trigonometric relationships.

---

### **Deriving Alternate Forms**  

By dividing the standard identity by either \(\sin^2\theta\) or \(\cos^2\theta\), we obtain two additional useful forms:

1. **Dividing by \( \cos^2 \theta \):**  

\[
\frac{\sin^2 \theta}{\cos^2 \theta} + \frac{\cos^2 \theta}{\cos^2 \theta} = \frac{1}{\cos^2 \theta}
\]

Since \( \frac{\sin \theta}{\cos \theta} = \tan \theta \) and \( \frac{1}{\cos \theta} = \sec \theta \), we get:

\[
\tan^2 \theta + 1 = \sec^2 \theta
\]

2. **Dividing by \( \sin^2 \theta \):**  

\[
\frac{\sin^2 \theta}{\sin^2 \theta} + \frac{\cos^2 \theta}{\sin^2 \theta} = \frac{1}{\sin^2 \theta}
\]

Using \( \frac{\cos \theta}{\sin \theta} = \cot \theta \) and \( \frac{1}{\sin \theta} = \csc \theta \), we get:

\[
1 + \cot^2 \theta = \csc^2 \theta
\]

---

### **Summary of Pythagorean Identities**
1. **Standard Form:**  
   \[
   \sin^2 \theta + \cos^2 \theta = 1
   \]
2. **Tan-Sec Identity:**  
   \[
   \tan^2 \theta + 1 = \sec^2 \theta
   \]
3. **Cot-Csc Identity:**  
   \[
   1 + \cot^2 \theta = \csc^2 \theta
   \]

---

### **Applications of Pythagorean Identities**  

- **Simplifying Trigonometric Expressions** – Used in calculus, algebraic manipulations, and solving integrals.  
- **Proving Other Identities** – A fundamental building block in trigonometric proofs.  
- **Solving Trigonometric Equations** – Helps find unknown angles and function values.  
- **Physics & Engineering** – Used in wave mechanics, oscillations, and AC circuit analysis.  

These identities form the backbone of trigonometric relationships and are essential for advanced 
applications in math and science.




## **Rates of Change in Applied Contexts**  

Rates of change describe how a quantity changes concerning another quantity, often time. 
In applied contexts, these are used in physics, economics, biology, and engineering to model real-world phenomena.

---

### **1. Definition of Rate of Change**  

The rate of change of a function \( f(x) \) over an interval \([a, b]\) is given by:

\[
\frac{\Delta y}{\Delta x} = \frac{f(b) - f(a)}{b - a}
\]

This represents the **average rate of change (AROC)** over the interval. It is the slope of the secant line connecting two points on the curve.

If we take the limit as \( \Delta x \to 0 \), we obtain the **instantaneous rate of change (IROC)**, which is given by the derivative:

\[
f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}
\]

This is the slope of the tangent line to the curve at \( x \), representing the rate at which \( f(x) \) is changing at that exact point.

---

### **2. Types of Rates of Change in Applications**  

#### **(a) Velocity and Acceleration (Physics)**
- **Velocity:** The rate of change of displacement \( s(t) \) with respect to time \( t \).  
  \[
  v(t) = \frac{ds}{dt}
  \]
- **Acceleration:** The rate of change of velocity with respect to time.  
  \[
  a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}
  \]

#### **(b) Population Growth (Biology & Demography)**
- If \( P(t) \) is the population at time \( t \), the growth rate is given by:
  \[
  P'(t) = k P(t)
  \]
  where \( k \) is a growth constant (exponential growth or decay model).

#### **(c) Marginal Cost & Revenue (Economics)**
- **Marginal cost:** The rate of change of total cost \( C(x) \) with respect to the number of items produced \( x \).
  \[
  C'(x) = \frac{dC}{dx}
  \]
- **Marginal revenue:** The derivative of the revenue function \( R(x) \), which measures how revenue changes with an additional unit sold.

#### **(d) Reaction Rates (Chemistry)**
- The rate of change of concentration of a reactant \( [A] \) in a chemical reaction is given by:
  \[
  \text{Rate} = -\frac{d[A]}{dt}
  \]
  where a negative sign indicates the concentration is decreasing.

#### **(e) Flow Rate (Engineering & Fluid Mechanics)**
- If \( V(t) \) represents volume at time \( t \), the flow rate is given by:
  \[
  Q = \frac{dV}{dt}
  \]
  which measures how quickly fluid is moving.

---

### **3. Interpreting Positive and Negative Rates of Change**
- **Positive rate of change:** The quantity is increasing.
- **Negative rate of change:** The quantity is decreasing.
- **Zero rate of change:** No change is occurring at that moment.

---

### **4. Applications in Real Life**
- **Predicting stock prices** in finance.
- **Measuring drug concentration decay** in medicine.
- **Determining how fast a car needs to slow down** in automotive engineering.
- **Calculating optimal production levels** in economics.

Understanding rates of change helps in making predictions, optimizing processes, and solving complex real-world problems.




## **Calculating Limits of Radical Functions Using Conjugate Multiplication**  

When evaluating limits involving square roots, direct substitution may lead to an **indeterminate form** (e.g., \( \frac{0}{0} \)). 
In such cases, the **conjugate multiplication** method is useful to simplify the expression and find the limit.

---

### **1. Why Use Conjugate Multiplication?**  
- Radical expressions often create indeterminate forms.
- Multiplying by the conjugate removes the radical in the numerator or denominator.
- It helps in algebraic simplification, allowing the limit to be evaluated.

---

### **2. Steps for Conjugate Multiplication Method**  

For a limit of the form:

\[
\lim_{x \to a} \frac{\text{expression with a square root}}{\text{another expression}}
\]

**Step 1:** Identify the conjugate.  
If the expression contains \( \sqrt{f(x)} \pm g(x) \), its conjugate is \( \sqrt{f(x)} \mp g(x) \).  

**Step 2:** Multiply the numerator and denominator by the conjugate.  
This applies the **difference of squares** identity:

\[
(a - b)(a + b) = a^2 - b^2
\]

which eliminates the square root in the numerator.

**Step 3:** Simplify the expression.  
This often results in a factor that cancels out the problematic term.

**Step 4:** Evaluate the limit after simplification.

---

### **3. Example Problem**  
Evaluate:

\[
\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}
\]

#### **Step 1: Identify the issue**
Substituting \( x = 4 \):

\[
\frac{\sqrt{4} - 2}{4 - 4} = \frac{2 - 2}{0} = \frac{0}{0}
\]

which is an indeterminate form.

#### **Step 2: Multiply by the conjugate**
The conjugate of \( \sqrt{x} - 2 \) is \( \sqrt{x} + 2 \), so multiply by:

\[
\frac{\sqrt{x} + 2}{\sqrt{x} + 2}
\]

\[
\lim_{x \to 4} \frac{(\sqrt{x} - 2)(\sqrt{x} + 2)}{(x - 4)(\sqrt{x} + 2)}
\]

#### **Step 3: Apply the difference of squares**
\[
\sqrt{x}^2 - 2^2 = x - 4
\]

\[
\lim_{x \to 4} \frac{x - 4}{(x - 4)(\sqrt{x} + 2)}
\]

#### **Step 4: Cancel and evaluate**
\[
\lim_{x \to 4} \frac{1}{\sqrt{x} + 2}
\]

Substituting \( x = 4 \):

\[
\frac{1}{\sqrt{4} + 2} = \frac{1}{2 + 2} = \frac{1}{4}
\]

Thus, 

\[
\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4} = \frac{1}{4}
\]

---

### **4. Summary of Key Points**
- Use conjugate multiplication to simplify limits involving square roots.
- The difference of squares helps remove the radical.
- Cancel the problematic term and evaluate the simplified limit.
- This method is especially useful when direct substitution gives \( \frac{0}{0} \).






## **The Double-Angle Formula for Sine**  

The **double-angle formula for sine** expresses \( \sin(2\theta) \) in terms of \( \sin(\theta) \) and \( \cos(\theta) \), 
which is useful in trigonometric simplifications, calculus, and physics applications.  

\[
\sin(2\theta) = 2\sin\theta\cos\theta
\]

---

### **1. Derivation of the Formula**  
Using the **sum formula for sine**:  

\[
\sin(A + B) = \sin A \cos B + \cos A \sin B
\]

Let \( A = B = \theta \), so:

\[
\sin(2\theta) = \sin(\theta + \theta) = \sin\theta \cos\theta + \cos\theta \sin\theta
\]

Since both terms are the same, we simplify:

\[
\sin(2\theta) = 2\sin\theta\cos\theta
\]

---

### **2. Applications of the Formula**  

#### **(a) Expressing Products of Sine and Cosine**  
If a function contains \( 2\sin\theta\cos\theta \), it can be rewritten as \( \sin(2\theta) \).

Example:  
\[
2\sin(30^\circ)\cos(30^\circ) = \sin(60^\circ) = \frac{\sqrt{3}}{2}
\]

#### **(b) Solving Trigonometric Equations**  
Example: Solve \( \sin(2\theta) = \frac{1}{2} \).  

Using the double-angle identity:

\[
2\sin\theta\cos\theta = \frac{1}{2}
\]

Solving for \( \theta \):

\[
\sin\theta\cos\theta = \frac{1}{4}
\]

Using identities or solving numerically, we determine \( \theta \).

#### **(c) Differentiation and Integration**  
In calculus, the identity simplifies integrals and derivatives involving sine and cosine.

Example:  
\[
\int \sin(2x) dx
\]

Using the identity:

\[
\int 2\sin x\cos x dx
\]

which simplifies using substitution.

---

### **3. Alternative Forms Using Pythagorean Identities**  
Since \( \cos^2\theta = 1 - \sin^2\theta \), an alternative form is:

\[
\sin(2\theta) = 2\sin\theta\sqrt{1 - \sin^2\theta}
\]

Alternatively, using \( \sin^2\theta = 1 - \cos^2\theta \):

\[
\sin(2\theta) = 2\sqrt{1 - \cos^2\theta} \cos\theta
\]

These forms help when rewriting expressions in different contexts.

---

### **4. Summary**
- The **double-angle identity** simplifies trigonometric expressions.
- Used in **equation solving, calculus, and physics**.
- Alternative forms exist using **Pythagorean identities**.

This formula is crucial in both theoretical and applied mathematics.





## **Evaluating Limits at Infinity by Comparing Relative Magnitudes of Functions**

When evaluating **limits at infinity**, a useful technique is to compare the **relative growth rates**
(magnitudes) of different functions. This method helps determine whether a function approaches zero, 
a finite number, or infinity as \( x \to \infty \) or \( x \to -\infty \).

---

### **Key Growth Rates of Common Functions** (from slowest to fastest)
1. **Logarithmic Functions:** \( \log x \)  
2. **Polynomial Functions:** \( x^n \) (higher powers grow faster)  
3. **Exponential Functions:** \( a^x \) (for \( a > 1 \), grows faster than polynomials)  
4. **Factorial Functions:** \( n! \)  
5. **Power Tower (Double Exponentials):** \( a^{a^x} \)  

For comparison:  
\[
\log x \ll x^n \ll a^x \ll x! \ll a^{a^x}
\]
as \( x \to \infty \).

---

### **Limit Evaluation Using Relative Magnitudes**
1. **Compare degrees of polynomials** (when dividing polynomials):
   - If the degree of the numerator **is greater**, the limit goes to **infinity**.
   - If the degree of the denominator **is greater**, the limit is **zero**.
   - If the degrees are equal, the limit is the **ratio of the leading coefficients**.

   **Example:**
   \[
   \lim_{x \to \infty} \frac{x^3 + 5x}{2x^3 - 7} = \frac{1}{2}
   \]

2. **Compare polynomial and exponential functions:**
   - **Exponentials grow faster** than polynomials, so terms like \( e^x \) dominate.
   
   **Example:**
   \[
   \lim_{x \to \infty} \frac{x^5}{e^x} = 0
   \]
   since \( e^x \) grows much faster than \( x^5 \).

3. **Compare logarithmic and polynomial functions:**
   - **Polynomials always grow faster** than logarithms.
   
   **Example:**
   \[
   \lim_{x \to \infty} \frac{\log x}{x} = 0
   \]
   since \( x \) grows much faster than \( \log x \).

---

### **Conclusion**
To evaluate limits at infinity:
- Identify the dominant term in the function.
- Compare the relative magnitudes using the hierarchy of function growth rates.
- Use simplifications like dividing by the highest power in fractions or L'Hôpital’s Rule if needed.




## **Extending Polynomial Identities to the Complex Numbers**  

Polynomial identities that hold for real numbers also extend naturally to **complex numbers** due to the
fundamental properties of complex arithmetic. Here’s how and why these identities hold in the complex domain.  

---

### **1. Closure Under Addition and Multiplication**  
The set of complex numbers \( \mathbb{C} \) is **closed** under addition and multiplication, 
meaning that if \( z_1 \) and \( z_2 \) are complex, then:  

\[
z_1 + z_2 \in \mathbb{C}, \quad z_1 \cdot z_2 \in \mathbb{C}
\]
This ensures that polynomial identities remain valid when extended to complex numbers.  

---

### **2. Polynomial Identities in \( \mathbb{C} \)**  
#### **(a) Binomial Theorem**  
For any integer \( n \), the **binomial expansion** holds for complex numbers:  
\[
(z_1 + z_2)^n = \sum_{k=0}^{n} \binom{n}{k} z_1^{n-k} z_2^k
\]
since exponentiation and multiplication behave the same way in \( \mathbb{C} \).  

#### **(b) Difference of Squares**  
For any complex numbers \( z_1, z_2 \):  
\[
z_1^2 - z_2^2 = (z_1 - z_2)(z_1 + z_2)
\]  
This identity remains valid because complex numbers follow the same distributive, associative, and commutative properties as real numbers.  

#### **(c) Factorization of Polynomials**  
The **Factor Theorem** extends to complex numbers: If \( P(x) \) is a polynomial and \( P(c) = 0 \) for some complex number \( c \), then \( (x - c) \) is a factor of \( P(x) \).  

For example,  
\[
x^2 + 1 = (x - i)(x + i)
\]  
demonstrates that factoring extends naturally to the complex plane.  

---

### **3. Fundamental Theorem of Algebra**  
A critical extension to complex numbers is that **every non-constant polynomial with complex coefficients has a root in \( \mathbb{C} \)**.  

For instance, the polynomial \( x^2 + 1 = 0 \) has no real solutions but has complex solutions:  
\[
x = \pm i
\]  
This guarantees that every polynomial can be factored completely over \( \mathbb{C} \), unlike in \( \mathbb{R} \).  

---

### **4. Application to Roots of Unity**  
The identity  
\[
x^n - 1 = (x - 1)(x - \omega)(x - \omega^2) \dots (x - \omega^{n-1})
\]  
where \( \omega = e^{2\pi i / n} \) represents the **n-th roots of unity**, extends naturally to complex numbers, allowing the decomposition of polynomials into their fundamental components.  

---

### **Conclusion**  
Polynomial identities remain valid in \( \mathbb{C} \) due to closure, factorization rules, 
and the Fundamental Theorem of Algebra. Extending them allows deeper insights into roots, 
factorization, and complex analysis.  





## **Graphing Strict Two-Variable Linear Inequalities**  

Graphing strict two-variable linear inequalities involves shading the appropriate region in a coordinate 
plane based on a given inequality. Here’s a step-by-step guide to the process:  

---

### **1. Understanding a Linear Inequality**  
A two-variable linear inequality has the general form:  
\[
ax + by < c, \quad ax + by > c, \quad ax + by \leq c, \quad \text{or} \quad ax + by \geq c
\]  
where:  
- \( a, b, c \) are real numbers.  
- \( x \) and \( y \) are variables.  
- The inequality sign (\(<\), \(>\), \(\leq\), \(\geq\)) determines the type of boundary and shading.  

A **strict inequality** (\(<\) or \(>\)) means the boundary line **is not included** (dashed line).  
A **non-strict inequality** (\(\leq\) or \(\geq\)) means the boundary line **is included** (solid line).  

---

### **2. Graphing Steps**  
#### **Step 1: Rewrite in Slope-Intercept Form (if necessary)**  
Convert the inequality into slope-intercept form (\(y = mx + b\)) to easily identify the slope \(m\) and the y-intercept \(b\).  
For example, given \( 2x + 3y < 6 \):  
\[
3y < -2x + 6
\]  
\[
y < -\frac{2}{3}x + 2
\]  
Now, the slope is \( -\frac{2}{3} \) and the y-intercept is \(2\).  

#### **Step 2: Draw the Boundary Line**  
- Replace the inequality sign with an **equals sign** and graph the line.  
- **Use a dashed line** for \( < \) or \( > \) (since the points on the line are not included in the solution).  
- **Use a solid line** for \( \leq \) or \( \geq \) (since the points on the line are included).  

For \( y < -\frac{2}{3}x + 2 \), plot the y-intercept at \( (0,2) \) and use the slope to find another point (\(3,0\)), then draw a **dashed** line.  

#### **Step 3: Shade the Correct Region**  
- **Pick a test point** (e.g., \( (0,0) \)) and substitute into the inequality.  
- If it **satisfies** the inequality, shade the region **containing that point**.  
- If it **does not satisfy** the inequality, shade the **opposite region**.  

For \( y < -\frac{2}{3}x + 2 \), test \( (0,0) \):  
\[
0 < -\frac{2}{3}(0) + 2
\]  
\[
0 < 2
\]  
Since this is **true**, shade the region **below** the dashed line.  

---

### **3. Example Graph**  
For \( y > 2x - 3 \):  
- Graph \( y = 2x - 3 \) with a **dashed line**.  
- Pick \( (0,0) \), check \( 0 > 2(0) - 3 \Rightarrow 0 > -3 \) (true).  
- Shade the region **above** the line.  

---

### **Key Points to Remember**  
✅ Dashed line for strict inequalities (\(<\) or \(>\)).  
✅ Solid line for non-strict inequalities (\(\leq\) or \(\geq\)).  
✅ Use a test point to determine shading.  
✅ The shaded region represents all solutions.  





## **Expressing an Arithmetic Series in Sigma Notation**  

An **arithmetic series** is the sum of the terms in an **arithmetic sequence**, where each term increases 
(or decreases) by a common difference \( d \). The sum of an arithmetic series can be represented
using **sigma notation** (∑ notation).  

---

### **1. General Formula for an Arithmetic Sequence**  
An arithmetic sequence has the form:  
\[
a, a + d, a + 2d, a + 3d, \dots, a + (n-1)d
\]  
where:  
- \( a \) = first term  
- \( d \) = common difference  
- \( n \) = number of terms  

The **nth** term is given by:  
\[
a_n = a + (n-1)d
\]  

---

### **2. Expressing an Arithmetic Series in Sigma Notation**  
The sum of the first \( n \) terms of an arithmetic series can be written in sigma notation as:  
\[
\sum_{k=1}^{n} \left[ a + (k-1)d \right]
\]  
where:  
- \( k \) is the index of summation, starting from 1.  
- \( a + (k-1)d \) represents the general term of the sequence.  
- \( n \) is the total number of terms.  

---

### **3. Example**  
Consider the arithmetic series:  
\[
3 + 7 + 11 + 15 + 19
\]  
Here:  
- \( a = 3 \)  
- \( d = 4 \)  
- \( n = 5 \)  

The general term is:  
\[
a_k = 3 + (k-1) \cdot 4
\]  

In sigma notation, the series is expressed as:  
\[
\sum_{k=1}^{5} \left( 3 + (k-1) \cdot 4 \right)
\]  

---

### **4. Simplifying the Sigma Expression**  
If the series follows a simple linear pattern, the expression inside the summation can often be rewritten in a more compact form.  

For example, the arithmetic series:  
\[
2 + 5 + 8 + 11 + 14 + 17
\]  
can be expressed as:  
\[
\sum_{k=1}^{6} (2 + (k-1) \cdot 3)
\]  
which simplifies to:  
\[
\sum_{k=1}^{6} (3k - 1)
\]  

---

### **Key Takeaways**  
✅ Identify the **first term** \( a \) and **common difference** \( d \).  
✅ Use the formula \( a_k = a + (k-1)d \) for the general term.  
✅ Use the sigma notation:  
   \[
   \sum_{k=1}^{n} [a + (k-1)d]
   \]  
✅ If possible, simplify the expression inside the summation.  





## **Finding the Sum of an Arithmetic Series**  

An **arithmetic series** is the sum of the terms in an **arithmetic sequence**, where each term follows 
a pattern of adding a common difference \( d \).  

---

### **1. Formula for the Sum of an Arithmetic Series**  
The sum of the first \( n \) terms of an arithmetic series is given by the formula:  

\[
S_n = \frac{n}{2} (a + l)
\]

or equivalently,  

\[
S_n = \frac{n}{2} \left[ 2a + (n-1)d \right]
\]

where:  
- \( S_n \) = sum of the first \( n \) terms  
- \( n \) = number of terms  
- \( a \) = first term  
- \( l \) = last term (when known)  
- \( d \) = common difference  

---

### **2. Example 1: Using the First and Last Term**  
Find the sum of the arithmetic series:  
\[
3 + 7 + 11 + 15 + 19
\]  
Here:  
- \( a = 3 \)  
- \( l = 19 \)  
- \( n = 5 \)  

Using the sum formula:  
\[
S_5 = \frac{5}{2} (3 + 19)
\]
\[
S_5 = \frac{5}{2} \times 22 = \frac{110}{2} = 55
\]  

---

### **3. Example 2: Using the First Term and Common Difference**  
Find the sum of the first 10 terms of an arithmetic sequence where \( a = 4 \) and \( d = 6 \).  

First, find the 10th term using:  
\[
a_n = a + (n-1)d
\]  
\[
a_{10} = 4 + (10-1) \cdot 6 = 4 + 54 = 58
\]  

Now, use the sum formula:  
\[
S_{10} = \frac{10}{2} (4 + 58)
\]  
\[
S_{10} = 5 \times 62 = 310
\]  

---

### **Key Takeaways**  
✅ Use \( S_n = \frac{n}{2} (a + l) \) if the last term is known.  
✅ Use \( S_n = \frac{n}{2} \left[ 2a + (n-1)d \right] \) if only \( a \) and \( d \) are given.  
✅ Always check if the sequence follows a constant difference before applying the formula.  





## **Graphing Curves Defined Parametrically**  

Parametric equations represent curves by defining both the \( x \)- and \( y \)-coordinates 
as functions of a third variable, called the **parameter** (often \( t \)). Instead of a 
single equation in terms of \( x \) and \( y \), parametric equations are given as:  


\[
x = f(t), \quad y = g(t), \quad t \in \text{interval}
\]  

where \( t \) represents an independent variable, controlling the motion along the curve.

---

### **1. Steps to Graph a Parametric Curve**  

1. **Create a Table of Values**  
   - Choose several values of \( t \).  
   - Compute corresponding \( x \) and \( y \) values.  
   - Record the ordered pairs \( (x, y) \).  

2. **Plot the Points**  
   - Mark the points on the coordinate plane.  
   - Indicate the direction of increasing \( t \) with arrows.  

3. **Eliminate the Parameter (Optional)**  
   - Solve for \( t \) in one equation and substitute into the other.  
   - Obtain a Cartesian equation in terms of \( x \) and \( y \).  
   - This helps visualize the standard form of the curve.  

---

### **2. Example: A Parametric Circle**  

Consider the parametric equations:  
\[
x = 3\cos t, \quad y = 3\sin t, \quad 0 \leq t \leq 2\pi
\]  

- Compute values for key points:  

| \( t \)  | \( x = 3\cos t \) | \( y = 3\sin t \) | \( (x, y) \) |
|------|----------------|----------------|------------|
| \( 0 \)    | 3              | 0              | (3,0)       |
| \( \frac{\pi}{2} \) | 0              | 3              | (0,3)       |
| \( \pi \)  | -3             | 0              | (-3,0)      |
| \( \frac{3\pi}{2} \) | 0              | -3             | (0,-3)      |
| \( 2\pi \)  | 3              | 0              | (3,0)       |

- **Plot the points** and **connect them smoothly** to form a circle.  
- **Find Cartesian equation** by eliminating \( t \):  

\[
\cos t = \frac{x}{3}, \quad \sin t = \frac{y}{3}
\]  
\[
\cos^2 t + \sin^2 t = 1 \Rightarrow \left(\frac{x}{3}\right)^2 + \left(\frac{y}{3}\right)^2 = 1
\]  
\[
x^2 + y^2 = 9
\]  

Thus, the parametric equations describe a **circle centered at (0,0) with radius 3**.

---

### **3. Example: Parametric Parabola**  

\[
x = t^2, \quad y = 2t, \quad -3 \leq t \leq 3
\]  

- Solve for \( t \):  
  \[
  t = \frac{y}{2}
  \]  
  - Substitute into \( x \):  
  \[
  x = \left(\frac{y}{2}\right)^2 = \frac{y^2}{4}
  \]  
  - The Cartesian equation is:  
  \[
  x = \frac{y^2}{4}
  \]  
  - This is a **sideways parabola**.

---

### **Key Takeaways**  
✅ **Parametric equations** describe curves using an independent parameter \( t \).  
✅ **Graphing involves** making a table, plotting points, and drawing the curve.  
✅ **Eliminating \( t \)** can convert parametric equations to Cartesian form.  
✅ **Directionality matters**—arrows indicate how the curve is traced as \( t \) increases.  





## **Differentiating Parametric Curves**  

When a curve is expressed in **parametric form** as:  
\[
x = f(t), \quad y = g(t)
\]  
where \( t \) is the parameter, the derivative of \( y \) with respect to \( x \) is
found using the **chain rule**.

#### **1. First Derivative: \( \frac{dy}{dx} \)**
The derivative of \( y \) with respect to \( x \) is given by:
\[
\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}
\]
provided that \( \frac{dx}{dt} \neq 0 \).  

#### **2. Second Derivative: \( \frac{d^2y}{dx^2} \)**
To find the second derivative, use:
\[
\frac{d^2y}{dx^2} = \frac{d}{dt} \left( \frac{dy}{dx} \right) \div \frac{dx}{dt}
\]

#### **Example**
Consider the parametric equations:
\[
x = t^2 + 1, \quad y = t^3 - t
\]
1. Compute \( \frac{dx}{dt} \) and \( \frac{dy}{dt} \):
   \[
   \frac{dx}{dt} = 2t, \quad \frac{dy}{dt} = 3t^2 - 1
   \]
2. Compute \( \frac{dy}{dx} \):
   \[
   \frac{dy}{dx} = \frac{3t^2 - 1}{2t}
   \]

This gives the slope of the curve at any point \( t \).

### **Differentiating Parametric Curves: Examples with \( \sin 2t \) and \( \sin^2 t \)**  

#### **Example 1: Differentiating \( \sin 2t \)**  
We differentiate \( y = \sin 2t \) using the chain rule:

\[
\frac{dy}{dt} = \cos 2t \cdot \frac{d}{dt}(2t) = 2\cos 2t
\]

#### **Example 2: Differentiating \( \sin^2 t \)**  
Using the chain rule:

\[
\frac{d}{dt} (\sin^2 t) = 2\sin t \cdot \cos t = \sin 2t
\]

(using the double-angle identity \( 2\sin t \cos t = \sin 2t \)).

#### **Example 3: Parametric Differentiation**
Given:
\[
x = \cos 2t, \quad y = \sin^2 t
\]

1. Compute \( \frac{dx}{dt} \) and \( \frac{dy}{dt} \):

   \[
   \frac{dx}{dt} = -2\sin 2t
   \]

   \[
   \frac{dy}{dt} = \sin 2t
   \]

2. Compute \( \frac{dy}{dx} \):

   \[
   \frac{dy}{dx} = \frac{\sin 2t}{-2\sin 2t} = -\frac{1}{2}
   \]

Thus, the tangent to the parametric curve has a slope of \( -\frac{1}{2} \).

#### **Geometric Interpretation**
- \( \frac{dy}{dx} \) represents the **slope** of the tangent to the curve.
- \( \frac{d^2y}{dx^2} \) determines **concavity** (curvature).

By using these derivatives, we can analyze **tangents, normals, concavity, and inflection points** 
of parametric curves.





## **Calculating Acceleration for Straight-Line Motion Using Differentiation**  

In straight-line motion, **acceleration** is the rate of change of velocity with respect to time. 
It is obtained by differentiating the velocity function.  

#### **1. Definitions and Key Formulas**  
- **Position function:** \( s(t) \) gives the displacement of an object at time \( t \).  
- **Velocity function:** \( v(t) = \frac{ds}{dt} \) is the first derivative of position, representing the rate of change of displacement.  
- **Acceleration function:** \( a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2} \) is the second derivative of position, representing the rate of change of velocity.  

#### **2. Example 1: Basic Acceleration Calculation**  
Given the position function:

\[
s(t) = 4t^3 - 3t^2 + 2t - 5
\]

1. Differentiate \( s(t) \) to find velocity:

   \[
   v(t) = \frac{ds}{dt} = 12t^2 - 6t + 2
   \]

2. Differentiate \( v(t) \) to find acceleration:

   \[
   a(t) = \frac{dv}{dt} = 24t - 6
   \]

Thus, the acceleration at any time \( t \) is given by \( a(t) = 24t - 6 \).  

#### **3. Example 2: Acceleration at a Specific Time**  
Find the acceleration at \( t = 2 \):

\[
a(2) = 24(2) - 6 = 48 - 6 = 42
\]

So, the acceleration at \( t = 2 \) is \( 42 \) units per second squared.

#### **4. Interpretation in Motion Analysis**  
- If \( a(t) > 0 \), velocity is increasing (speeding up).  
- If \( a(t) < 0 \), velocity is decreasing (slowing down).  
- If \( a(t) = 0 \), velocity is constant (no acceleration).  

This method applies to **kinematics** in physics, engineering, and machine learning models 
involving motion prediction.





## **The Double-Angle Formula for Cosine**  

#### **1. Definition of the Double-Angle Formula for Cosine**  
The double-angle formula for cosine expresses \( \cos(2\theta) \) in terms of \( \cos(\theta) \)
and \( \sin(\theta) \). It is derived from the sum formula for cosine:

\[
\cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)
\]

Using the Pythagorean identity \( \sin^2(\theta) = 1 - \cos^2(\theta) \) and \( \cos^2(\theta) = 1 - \sin^2(\theta) \), we obtain two alternative forms:

\[
\cos(2\theta) = 2\cos^2(\theta) - 1
\]

\[
\cos(2\theta) = 1 - 2\sin^2(\theta)
\]

Thus, the three equivalent forms of the double-angle formula for cosine are:

\[
\cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)
\]

\[
\cos(2\theta) = 2\cos^2(\theta) - 1
\]

\[
\cos(2\theta) = 1 - 2\sin^2(\theta)
\]

---

#### **2. Derivation of the Formula**  
Using the sum formula for cosine:

\[
\cos(A + B) = \cos A \cos B - \sin A \sin B
\]

Setting \( A = B = \theta \):

\[
\cos(2\theta) = \cos(\theta) \cos(\theta) - \sin(\theta) \sin(\theta)
\]

\[
\cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)
\]

By substituting \( \sin^2(\theta) = 1 - \cos^2(\theta) \):

\[
\cos(2\theta) = \cos^2(\theta) - (1 - \cos^2(\theta))
\]

\[
\cos(2\theta) = 2\cos^2(\theta) - 1
\]

Similarly, substituting \( \cos^2(\theta) = 1 - \sin^2(\theta) \):

\[
\cos(2\theta) = (1 - \sin^2(\theta)) - \sin^2(\theta)
\]

\[
\cos(2\theta) = 1 - 2\sin^2(\theta)
\]

---

#### **3. Applications of the Double-Angle Formula**  

- **Trigonometric simplifications**  
  Useful in reducing higher-degree trigonometric expressions.  

- **Solving trigonometric equations**  
  Converts equations involving \( \cos(2\theta) \) into forms involving only \( \cos(\theta) \) or \( \sin(\theta) \).  

- **Integration and differentiation**  
  Often appears in calculus problems when simplifying trigonometric integrals and derivatives.  

- **Fourier Analysis and Signal Processing**  
  Helps in analyzing waveforms and harmonic frequencies.  

---

#### **4. Example Problems**  

**Example 1: Evaluating \( \cos(2\theta) \) Given \( \cos(\theta) = \frac{3}{5} \)**  
Using \( \cos(2\theta) = 2\cos^2(\theta) - 1 \):

\[
\cos(2\theta) = 2 \left(\frac{3}{5}\right)^2 - 1
\]

\[
\cos(2\theta) = 2 \times \frac{9}{25} - 1
\]

\[
\cos(2\theta) = \frac{18}{25} - \frac{25}{25}
\]

\[
\cos(2\theta) = -\frac{7}{25}
\]

---

**Example 2: Using the Formula to Solve an Equation**  
Solve for \( \theta \) if \( \cos(2\theta) = \frac{1}{2} \).

Using \( \cos(2\theta) = 2\cos^2(\theta) - 1 \):

\[
\frac{1}{2} = 2\cos^2(\theta) - 1
\]

\[
\frac{3}{2} = 2\cos^2(\theta)
\]

\[
\cos^2(\theta) = \frac{3}{4}
\]

\[
\cos(\theta) = \pm\frac{\sqrt{3}}{2}
\]

Solving for \( \theta \):

\[
\theta = \pm\frac{\pi}{6} + 2k\pi, \quad k \in \mathbb{Z}
\]

---

The double-angle formula for cosine is essential in trigonometry, calculus, and real-world applications 
like physics and engineering.





## **Introduction to Ellipses**  

An **ellipse** is a fundamental conic section, representing the set of all points in a plane where the sum of the 
distances from two fixed points (called **foci**) is constant. It generalizes the concept of a circle, stretching it into an oval-like shape.

---

### **1. Standard Equation of an Ellipse**  
The standard form of an ellipse depends on its orientation:

1. **Horizontal Major Axis:**  
   \[
   \frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
   \]
   - Center: \( (h, k) \)  
   - Major axis along the **x-axis**  
   - \( a \) is the **semi-major axis** (longer radius)  
   - \( b \) is the **semi-minor axis** (shorter radius)  
   - The foci are located at \( (h \pm c, k) \), where \( c^2 = a^2 - b^2 \)

2. **Vertical Major Axis:**  
   \[
   \frac{(x - h)^2}{b^2} + \frac{(y - k)^2}{a^2} = 1
   \]
   - Major axis along the **y-axis**  
   - The foci are at \( (h, k \pm c) \), where \( c^2 = a^2 - b^2 \)

---

### **2. Key Features of an Ellipse**  
- **Vertices**: Endpoints of the major axis (\( \pm a \) from the center).  
- **Co-vertices**: Endpoints of the minor axis (\( \pm b \) from the center).  
- **Foci**: Fixed points inside the ellipse that determine its shape, positioned at distance \( c \) from the center.  
- **Eccentricity** \( e \): Defines how "stretched" the ellipse is:  
  \[
  e = \frac{c}{a}, \quad 0 \leq e < 1
  \]  
  The closer \( e \) is to 1, the more elongated the ellipse.  

---

### **3. Derivation Using the Distance Formula**  
An ellipse is defined as the locus of all points where the sum of distances to the two foci is constant, say \( 2a \):  
\[
d_1 + d_2 = 2a
\]
Using the **distance formula**, this leads to the standard equation.

---

### **4. Applications of Ellipses**  
- **Physics & Astronomy**: Planetary orbits around the Sun follow elliptical paths (Kepler’s First Law).  
- **Engineering**: Elliptical mirrors and satellite dish designs optimize signal reflection.  
- **Architecture**: Elliptical arches distribute weight efficiently.  

---

### **5. Example Problem**  
**Find the foci of the ellipse**  
\[
\frac{x^2}{25} + \frac{y^2}{9} = 1
\]
- Here, \( a^2 = 25 \Rightarrow a = 5 \), and \( b^2 = 9 \Rightarrow b = 3 \).
- The foci are found using \( c^2 = a^2 - b^2 \):
  \[
  c^2 = 25 - 9 = 16 \Rightarrow c = 4
  \]
- Since the major axis is along the **x-axis**, the foci are at:
  \[
  (\pm 4, 0)
  \]

---

### **Conclusion**  
Ellipses are fundamental in geometry, physics, and engineering. Understanding their 
properties allows for deeper insights into orbital mechanics, acoustics, and optics.





## **Introduction to Matrices**  

A **matrix** is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. Matrices are 
fundamental in linear algebra and are widely used in various fields, including engineering, physics, computer science, and machine learning.  

---

### **1. Definition and Notation**  
A matrix is typically represented as:  
\[
A = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}
\]
where:
- \( A \) is the matrix.
- \( a_{ij} \) represents the element in the **i-th row** and **j-th column**.
- The size of the matrix is denoted as **\( m \times n \) (rows × columns)**.

---

### **2. Types of Matrices**  
- **Square Matrix**: A matrix with the same number of rows and columns (\( m = n \)).  
- **Row Matrix**: A matrix with a single row (\( 1 \times n \)).  
- **Column Matrix**: A matrix with a single column (\( m \times 1 \)).  
- **Zero Matrix (\( O \))**: A matrix where all elements are zero.  
- **Identity Matrix (\( I \))**: A square matrix with 1s on the diagonal and 0s elsewhere:  
  \[
  I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
  \]
- **Diagonal Matrix**: A square matrix where all off-diagonal elements are zero.  
- **Symmetric Matrix**: A square matrix where \( A^T = A \) (i.e., it is equal to its transpose).  

---

### **3. Matrix Operations**  
#### **(a) Addition and Subtraction**  
For two matrices \( A \) and \( B \) of the same size \( m \times n \):  
\[
(A + B)_{ij} = A_{ij} + B_{ij}, \quad (A - B)_{ij} = A_{ij} - B_{ij}
\]

#### **(b) Scalar Multiplication**  
Multiplying a matrix by a scalar \( k \):  
\[
(kA)_{ij} = k \cdot A_{ij}
\]

#### **(c) Matrix Multiplication**  
For an \( m \times n \) matrix \( A \) and an \( n \times p \) matrix \( B \), their product \( C = AB \) is an \( m \times p \) matrix where:  
\[
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
\]
Matrix multiplication is **not commutative** (\( AB \neq BA \) in general).

#### **(d) Transpose of a Matrix**  
The **transpose** of a matrix \( A \), denoted as \( A^T \), is obtained by swapping rows and columns:  
\[
(A^T)_{ij} = A_{ji}
\]

#### **(e) Determinant of a Square Matrix**  
For a \( 2 \times 2 \) matrix:  
\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \quad \det(A) = ad - bc
\]

For a \( 3 \times 3 \) matrix, the determinant is computed using expansion along a row or column.

#### **(f) Inverse of a Matrix**  
For a square matrix \( A \), its inverse \( A^{-1} \) (if it exists) satisfies:  
\[
A A^{-1} = A^{-1} A = I
\]
For a \( 2 \times 2 \) matrix:  
\[
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}, \quad \text{if } \det(A) \neq 0
\]

---

### **4. Applications of Matrices**  
- **Linear Equations**: Used to solve systems of equations using Gaussian elimination or matrix inversion.  
- **Computer Graphics**: Used for transformations like rotation, scaling, and translation.  
- **Machine Learning**: Essential for representing and processing large datasets, especially in deep learning.  
- **Physics & Engineering**: Used in quantum mechanics, signal processing, and structural analysis.  

---

### **5. Example Problem**  
**Find the product of matrices**  
\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}
\]
\[
AB = \begin{bmatrix} (1 \cdot 2 + 2 \cdot 1) & (1 \cdot 0 + 2 \cdot 3) \\ (3 \cdot 2 + 4 \cdot 1) & (3 \cdot 0 + 4 \cdot 3) \end{bmatrix}
\]
\[
= \begin{bmatrix} 4 & 6 \\ 10 & 12 \end{bmatrix}
\]

---

### **Conclusion**  
Matrices are powerful mathematical tools used across various disciplines. Mastering their operations, properties, 
and applications is fundamental in algebra, data science, physics, and artificial intelligence.






## **Conditional Probabilities from Venn Diagrams**  

Conditional probability is the probability of an event occurring given that another event has already occurred. 
Venn diagrams provide a visual way to understand these relationships.  

---

### **1. Conditional Probability Formula**  
For two events \( A \) and \( B \), the conditional probability of \( A \) given \( B \), denoted as \( P(A | B) \), is:

\[
P(A | B) = \frac{P(A \cap B)}{P(B)}
\]

where:  
- \( P(A \cap B) \) is the probability that both \( A \) and \( B \) occur (the intersection of \( A \) and \( B \) in the Venn diagram).  
- \( P(B) \) is the probability that \( B \) occurs.  

Similarly, the probability of \( B \) given \( A \) is:

\[
P(B | A) = \frac{P(A \cap B)}{P(A)}
\]

---

### **2. Understanding Conditional Probability with Venn Diagrams**  
A Venn diagram typically consists of:  
- A universal set (represented by a rectangle).  
- Two or more circles representing different events.  
- Overlapping areas showing intersections (joint probabilities).  

By shading the **relevant portion of the diagram**, we can visually determine conditional probabilities.

#### **Example 1: Probability of A Given B**  
Suppose a Venn diagram shows:  
- \( P(A) = 0.4 \)  
- \( P(B) = 0.5 \)  
- \( P(A \cap B) = 0.2 \)  

Using the formula:

\[
P(A | B) = \frac{P(A \cap B)}{P(B)} = \frac{0.2}{0.5} = 0.4
\]

This means that **if event \( B \) has occurred, there is a 40% chance that event \( A \) also occurs**.

---

### **3. Conditional Probability of Complements Using Venn Diagrams**  
The probability of **not** \( A \) occurring given that \( B \) has occurred is:

\[
P(A' | B) = \frac{P(B) - P(A \cap B)}{P(B)}
\]

Using the previous values:

\[
P(A' | B) = \frac{0.5 - 0.2}{0.5} = \frac{0.3}{0.5} = 0.6
\]

This means **if \( B \) has occurred, there is a 60% chance that \( A \) does not occur**.

---

### **4. Conditional Probability and Independence in Venn Diagrams**  
Two events \( A \) and \( B \) are **independent** if:

\[
P(A | B) = P(A) \quad \text{or} \quad P(B | A) = P(B)
\]

This means that knowing whether \( B \) occurs does not change the probability of \( A \). In a Venn diagram, 
independence is observed when the proportion of overlap is equal to the individual probabilities of each event.

---

### **5. Application: Real-World Example with Venn Diagrams**  
Consider a survey where people are asked if they **exercise regularly (A)** and **eat healthy (B)**. The probabilities are:

- \( P(A) = 0.6 \)  
- \( P(B) = 0.7 \)  
- \( P(A \cap B) = 0.4 \)  

From the Venn diagram, we calculate:

\[
P(A | B) = \frac{P(A \cap B)}{P(B)} = \frac{0.4}{0.7} \approx 0.57
\]

\[
P(B | A) = \frac{P(A \cap B)}{P(A)} = \frac{0.4}{0.6} \approx 0.67
\]

Thus, **if a person eats healthy, there is a 57% chance they also exercise regularly**.

---

### **Key Takeaways**  
- **Venn diagrams** help visualize conditional probabilities by highlighting relevant regions.  
- **Conditional probability formula** is \( P(A | B) = P(A \cap B) / P(B) \).  
- **Complements** are calculated using \( P(A' | B) = 1 - P(A | B) \).  
- **Independence** occurs when \( P(A | B) = P(A) \), meaning knowing \( B \) does not affect \( A \).  
- **Real-world problems** involving surveys, medical tests, and risk assessments can be analyzed using these principles.  






## **Adding and Subtracting Matrices**  

Matrix addition and subtraction are fundamental operations in linear algebra with applications in data science, 
engineering, and physics. These operations are straightforward but require careful adherence to dimension compatibility rules.

---

### **1. Conditions for Adding and Subtracting Matrices**  
Two matrices can be **added or subtracted** if they have the **same dimensions** (same number of rows and columns). 
If one matrix is \( m \times n \), the other must also be \( m \times n \).

For matrices **\( A \) and \( B \)** of the same size:

\[
A + B = [a_{ij}] + [b_{ij}] = [a_{ij} + b_{ij}]
\]

\[
A - B = [a_{ij}] - [b_{ij}] = [a_{ij} - b_{ij}]
\]

Each element in the resulting matrix is found by adding or subtracting corresponding elements in \( A \) and \( B \).

---

### **2. Matrix Addition Example**  
Given two matrices:

\[
A = \begin{bmatrix} 2 & 4 \\ 6 & 8 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & 3 \\ 5 & 7 \end{bmatrix}
\]

Compute:

\[
A + B = \begin{bmatrix} 2+1 & 4+3 \\ 6+5 & 8+7 \end{bmatrix} = \begin{bmatrix} 3 & 7 \\ 11 & 15 \end{bmatrix}
\]

---

### **3. Matrix Subtraction Example**  
Using the same matrices:

\[
A - B = \begin{bmatrix} 2-1 & 4-3 \\ 6-5 & 8-7 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
\]

---

### **4. Properties of Matrix Addition and Subtraction**  
1. **Commutative Property**: \( A + B = B + A \)  
2. **Associative Property**: \( (A + B) + C = A + (B + C) \)  
3. **Additive Identity**: The **zero matrix** \( 0 \) satisfies \( A + 0 = A \).  
4. **Additive Inverse**: \( A + (-A) = 0 \), where \( -A \) is obtained by negating each element in \( A \).  

---

### **5. Special Cases**  
- **Adding/Subtracting Different-Sized Matrices**: Not possible unless dimensions match.
- **Adding/Subtracting a Scalar**: Not allowed; only elementwise scalar addition is possible via scalar multiplication.

---

### **6. Applications of Matrix Addition and Subtraction**  
- **Economics**: Computing total revenue or cost changes.  
- **Graphics Processing**: Image blending and transformations.  
- **Physics & Engineering**: Combining forces or electrical currents.  

Matrix addition and subtraction serve as the foundation for more advanced operations 
like matrix multiplication and transformations.






## **The Determinant of a \(2 \times 2\) Matrix**  

The **determinant** of a \(2 \times 2\) matrix provides a scalar value that gives insights into the 
matrix’s properties, such as **invertibility**, **area scaling**, and **geometric transformations**. 
It is widely used in **linear algebra**, **physics**, **computer graphics**, and **machine learning**.

---

### **1. Definition of the Determinant**  
For a \(2 \times 2\) matrix:

\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\]

The determinant, denoted as \( \det(A) \) or \( |A| \), is calculated as:

\[
\det(A) = ad - bc
\]

This is a simple computation that takes the product of the diagonal elements and subtracts the product of the off-diagonal elements.

---

### **2. Example Calculation**  
Given:

\[
A = \begin{bmatrix} 3 & 5 \\ 2 & 7 \end{bmatrix}
\]

Compute the determinant:

\[
\det(A) = (3 \times 7) - (5 \times 2) = 21 - 10 = 11
\]

Thus, \( \det(A) = 11 \).

---

### **3. Geometric Interpretation**  
In **2D transformations**, the determinant represents the **scaling factor of area** under the transformation defined by \( A \).  
- If \( |\det(A)| > 1 \), the transformation **expands** the area.  
- If \( 0 < |\det(A)| < 1 \), the transformation **shrinks** the area.  
- If \( \det(A) = 0 \), the transformation **collapses** the space (dependent vectors).  

For example, if a parallelogram is formed by two column vectors of \( A \), its area is \( |\det(A)| \).

---

### **4. Properties of Determinants in \(2 \times 2\) Matrices**  
1. **Invertibility**:  
   - If \( \det(A) \neq 0 \), \( A \) is **invertible**.  
   - If \( \det(A) = 0 \), \( A \) is **singular** (non-invertible).  

2. **Determinant of Identity Matrix**:  
   \[
   \det\left(\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \right) = 1
   \]
   The identity matrix has a determinant of 1, meaning it preserves volume.

3. **Effect of Row Operations**:  
   - Swapping two rows **negates** the determinant.  
   - Multiplying a row by \( k \) **scales** the determinant by \( k \).  

4. **Product Rule**:  
   \[
   \det(AB) = \det(A) \cdot \det(B)
   \]

---

### **5. Special Cases**  
1. **Zero Determinant Example (Singular Matrix):**  
   \[
   B = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}
   \]
   \[
   \det(B) = (2 \times 2) - (4 \times 1) = 4 - 4 = 0
   \]
   Since \( \det(B) = 0 \), \( B \) is singular and not invertible.

2. **Negative Determinant:**  
   If \( \det(A) < 0 \), the transformation includes a **reflection**.

---

### **6. Applications of the Determinant**  
- **Solving Systems of Linear Equations** (Cramer's Rule)  
- **Eigenvalues & Eigenvectors** (Characteristic Equation)  
- **Transformations in Computer Graphics** (Scaling, Rotation, Shearing)  
- **Physics & Engineering** (Analyzing stability in systems)  

The determinant is a fundamental concept that helps in understanding matrix behavior, 
transformation effects, and system solutions.






## **Integrating Algebraic Functions Using Substitution**  

#### **1. Introduction to Substitution Method**
Substitution is a powerful technique used to evaluate integrals, especially when the function contains a composite expression. 
The method is based on reversing the chain rule of differentiation.

The key idea is to replace a complex expression with a new variable, simplifying the integral into a basic form that can be easily evaluated.

#### **2. General Formula for Substitution**
If an integral has the form:

\[
I = \int f(g(x)) g'(x) \,dx
\]

we introduce a substitution:

\[
u = g(x) \quad \text{so that} \quad du = g'(x)dx
\]

Rewriting the integral in terms of \( u \):

\[
I = \int f(u) \, du
\]

which can now be integrated easily.

#### **3. Example Applications**
##### **Example 1: Power Function**
Evaluate:

\[
\int (x^2 + 3)^5 \cdot 2x \,dx
\]

- Let \( u = x^2 + 3 \), then \( du = 2x \,dx \).
- Substituting:

  \[
  \int u^5 \, du
  \]

- Integrating:

  \[
  \frac{u^6}{6} + C
  \]

- Substituting back \( u = x^2 + 3 \):

  \[
  \frac{(x^2 + 3)^6}{6} + C
  \]

##### **Example 2: Rational Function**
Evaluate:

\[
\int \frac{x}{x^2 + 1} \,dx
\]

- Let \( u = x^2 + 1 \), so \( du = 2x \,dx \).
- Rewrite \( x \,dx \) as \( \frac{du}{2} \).
- Substituting:

  \[
  \int \frac{du}{2u}
  \]

- Evaluating:

  \[
  \frac{1}{2} \ln |u| + C
  \]

- Substituting back \( u = x^2 + 1 \):

  \[
  \frac{1}{2} \ln |x^2 + 1| + C
  \]

#### **4. Summary**
- Identify an inner function \( g(x) \) whose derivative is present in the integral.
- Set \( u = g(x) \), then differentiate to get \( du = g'(x)dx \).
- Rewrite the integral in terms of \( u \), integrate, and substitute back.

This method simplifies complex algebraic functions into more manageable forms, making integration straightforward.





## **Equations of a Hyperbola Centered at the Origin**  

#### **1. Introduction to Hyperbolas**  
A **hyperbola** is the set of all points \((x, y)\) in a plane where the absolute difference of the 
distances to two fixed points, called the **foci**, is constant. Unlike ellipses, hyperbolas have two 
separate branches.

The **standard form** of a hyperbola depends on the orientation of its transverse axis 
(the axis along which the two branches extend).

---

#### **2. Standard Equations of a Hyperbola**  

If the hyperbola is centered at the origin \((0,0)\), its equation takes one of two forms:

1. **Horizontal Hyperbola (opens left and right):**  
   \[
   \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
   \]
   - The transverse axis is along the **x-axis**.
   - The foci are at \( (\pm c, 0) \), where \( c^2 = a^2 + b^2 \).
   - The vertices are at \( (\pm a, 0) \).

2. **Vertical Hyperbola (opens up and down):**  
   \[
   \frac{y^2}{a^2} - \frac{x^2}{b^2} = 1
   \]
   - The transverse axis is along the **y-axis**.
   - The foci are at \( (0, \pm c) \), where \( c^2 = a^2 + b^2 \).
   - The vertices are at \( (0, \pm a) \).

In both cases, **asymptotes** are given by:

\[
y = \pm \frac{b}{a} x
\]

which act as guiding lines that the hyperbola approaches but never touches.

---

#### **3. Key Components of a Hyperbola**
- **Center**: \((0,0)\) (since it's centered at the origin).
- **Vertices**: Located at \( (\pm a, 0) \) for a horizontal hyperbola and \( (0, \pm a) \) for a vertical hyperbola.
- **Foci**: Located at \( (\pm c, 0) \) for a horizontal hyperbola and \( (0, \pm c) \) for a vertical hyperbola, where \( c^2 = a^2 + b^2 \).
- **Asymptotes**: Diagonal lines that guide the branches of the hyperbola.

---

#### **4. Example Problems**
##### **Example 1: Graphing a Horizontal Hyperbola**
Find the center, foci, vertices, and asymptotes for the hyperbola:

\[
\frac{x^2}{9} - \frac{y^2}{16} = 1
\]

**Solution:**  
- **Standard form**: \( \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \)  
- \( a^2 = 9 \) → \( a = 3 \)  
- \( b^2 = 16 \) → \( b = 4 \)  
- \( c^2 = a^2 + b^2 = 9 + 16 = 25 \) → \( c = 5 \)  
- **Vertices**: \( (\pm 3, 0) \)  
- **Foci**: \( (\pm 5, 0) \)  
- **Asymptotes**: \( y = \pm \frac{b}{a}x = \pm \frac{4}{3}x \)  

##### **Example 2: Identifying a Vertical Hyperbola**
Determine whether the equation represents a hyperbola:

\[
\frac{y^2}{4} - \frac{x^2}{9} = 1
\]

**Solution:**  
- The \( y^2 \) term is positive, meaning it is a **vertical hyperbola**.
- **Vertices**: \( (0, \pm 2) \)  
- **Foci**: \( (0, \pm \sqrt{4 + 9}) = (0, \pm \sqrt{13}) \)  
- **Asymptotes**: \( y = \pm \frac{2}{3}x \)  

---

#### **5. Summary**
- **A horizontal hyperbola** has a positive \( x^2 \)-term and opens left and right.
- **A vertical hyperbola** has a positive \( y^2 \)-term and opens up and down.
- **The equation always follows** \( \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \) or \( \frac{y^2}{a^2} - \frac{x^2}{b^2} = 1 \).
- **Asymptotes** help sketch accurate graphs.

This deep dive covers the essentials of hyperbolas centered at the origin, including equations, graphing, and key properties.





## **Integrating Linear Rational Functions Using Substitution**  

#### **1. Understanding Linear Rational Functions**  
A **linear rational function** is a fraction where the numerator is a constant or a linear expression, 
and the denominator is also a linear expression. It generally takes the form:

\[
\int \frac{1}{ax + b} \, dx
\]

where \( a \) and \( b \) are constants.

---

#### **2. General Formula for Integration**  
The integral of a linear rational function can be solved using **u-substitution**, where we let:

\[
u = ax + b
\]

Then, differentiating both sides:

\[
du = a \, dx \quad \Rightarrow \quad dx = \frac{du}{a}
\]

Substituting into the integral:

\[
\int \frac{1}{ax + b} \, dx = \int \frac{1}{u} \cdot \frac{du}{a}
\]

Since \( \int \frac{1}{u} \, du = \ln |u| \), we get:

\[
\frac{1}{a} \ln |ax + b| + C
\]

where \( C \) is the constant of integration.

Thus, the **general formula** is:

\[
\int \frac{1}{ax + b} \, dx = \frac{1}{a} \ln |ax + b| + C
\]

---

#### **3. Example Problems**
##### **Example 1: Basic Integration**
Evaluate:

\[
\int \frac{1}{3x + 5} \, dx
\]

**Solution:**  
Let \( u = 3x + 5 \), so \( du = 3dx \) or \( dx = \frac{du}{3} \).  
Rewriting the integral:

\[
\int \frac{1}{3x + 5} \, dx = \int \frac{1}{u} \cdot \frac{du}{3}
\]

\[
= \frac{1}{3} \int \frac{1}{u} \, du
\]

\[
= \frac{1}{3} \ln |u| + C
\]

Substituting back \( u = 3x + 5 \):

\[
\frac{1}{3} \ln |3x + 5| + C
\]

---

##### **Example 2: Applying the Formula Directly**
Find:

\[
\int \frac{1}{7x - 2} \, dx
\]

Using the formula:

\[
\frac{1}{a} \ln |ax + b| + C
\]

where \( a = 7 \) and \( b = -2 \):

\[
\frac{1}{7} \ln |7x - 2| + C
\]

---

#### **4. More General Case: Integrating \( \frac{f'(x)}{f(x)} \)**  
A more general integral of a linear rational function is:

\[
\int \frac{f'(x)}{f(x)} \, dx = \ln |f(x)| + C
\]

which applies when the numerator is the derivative of the denominator.  

##### **Example 3: Variable Numerator**  
Evaluate:

\[
\int \frac{4}{4x + 7} \, dx
\]

Here, let \( u = 4x + 7 \), so \( du = 4dx \). Then:

\[
\int \frac{4}{4x + 7} \, dx = \int \frac{du}{u} = \ln |u| + C
\]

Substituting back:

\[
\ln |4x + 7| + C
\]

---

#### **5. Summary**
- The **general formula** for integrating linear rational functions is:

  \[
  \int \frac{1}{ax + b} \, dx = \frac{1}{a} \ln |ax + b| + C
  \]

- If the numerator is the derivative of the denominator, use:

  \[
  \int \frac{f'(x)}{f(x)} \, dx = \ln |f(x)| + C
  \]

- **Substitution (u-substitution)** is the key method for solving these integrals.






## **The Multiplication Law for Conditional Probability**  

#### **1. Definition and Formula**  
The multiplication law of conditional probability expresses the probability of two events occurring 
together in terms of conditional probability:  

\[
P(A \cap B) = P(A | B) P(B)
\]

Alternatively, it can also be written as:

\[
P(A \cap B) = P(B | A) P(A)
\]

This formula follows directly from the definition of conditional probability:

\[
P(A | B) = \frac{P(A \cap B)}{P(B)}
\]

Multiplying both sides by \( P(B) \) gives:

\[
P(A \cap B) = P(A | B) P(B)
\]

Similarly, using \( P(B | A) = \frac{P(A \cap B)}{P(A)} \), we get the second form.

#### **2. Intuition Behind the Formula**  
The formula tells us that the probability of **both** \( A \) and \( B \) occurring is found by:  
1. First calculating the probability of one event (e.g., \( B \) happening first).  
2. Then multiplying it by the probability of the other event occurring **given that the first event has already happened**.

#### **3. Example 1: Drawing Cards**  
Suppose we randomly draw two cards from a standard deck of 52. What is the probability that the first card is an ace and the second is also an ace?

- \( P(A_1) \) (probability of drawing an ace first) = \( \frac{4}{52} \).
- \( P(A_2 | A_1) \) (probability of drawing an ace second **given** the first was an ace) = \( \frac{3}{51} \).

By the multiplication law:

\[
P(A_1 \cap A_2) = P(A_1) P(A_2 | A_1) = \frac{4}{52} \times \frac{3}{51} = \frac{12}{2652} \approx 0.0045.
\]

#### **4. Example 2: Medical Testing**  
Suppose a disease affects 5% of a population. A test correctly identifies a diseased person 90% of the time and gives a false positive 2% of the time. What is the probability that a randomly selected person tests positive?

Using the law of total probability:

\[
P(T) = P(T | D) P(D) + P(T | D^c) P(D^c),
\]

where:
- \( P(T | D) = 0.9 \) (test positive given disease),
- \( P(D) = 0.05 \) (having disease),
- \( P(T | D^c) = 0.02 \) (false positive rate),
- \( P(D^c) = 0.95 \) (not having disease).

Thus:

\[
P(T) = (0.9 \times 0.05) + (0.02 \times 0.95) = 0.045 + 0.019 = 0.064.
\]

#### **5. Special Case: Independent Events**  
If \( A \) and \( B \) are **independent**, then \( P(A | B) = P(A) \), meaning that knowing \( B \) has occurred does not change the probability of \( A \).  

Thus, the multiplication rule simplifies to:

\[
P(A \cap B) = P(A) P(B).
\]

Example:  
If we roll two fair dice, the probability of rolling a 3 on the first die and a 5 on the second is:

\[
P(3 \cap 5) = P(3) P(5) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}.
\]

#### **6. Key Takeaways**
- The multiplication rule helps compute the probability of **joint events** occurring.
- The conditional probability accounts for **new information** by adjusting probabilities.
- **Independence simplifies** the multiplication rule since \( P(A | B) = P(A) \).
- Useful in real-world applications like **medical diagnosis, reliability testing, and risk assessment**.

This principle forms the foundation of **Bayes' Theorem**, which reverses conditional probabilities 
based on given evidence.




## **Integration Using Substitution**  

#### **1. Introduction to Substitution Method**  
The **substitution method** (also called **u-substitution**) is a powerful technique in integration 
that simplifies complex functions by transforming them into easier forms. It is analogous to 
the **chain rule** in differentiation, but in reverse.  

#### **2. General Formula**  
If an integral is of the form:  

\[
\int f(g(x)) g'(x) \, dx
\]

We make the substitution:  

\[
u = g(x) \quad \Rightarrow \quad du = g'(x) dx.
\]

This transforms the integral into:

\[
\int f(u) \, du.
\]

After integrating, we substitute \( u \) back in terms of \( x \).  

---

#### **3. Example 1: Basic Substitution**  
Evaluate:  

\[
\int 2x (x^2 + 1)^5 \, dx.
\]

**Step 1: Choose a substitution**  
Let:

\[
u = x^2 + 1 \quad \Rightarrow \quad du = 2x dx.
\]

**Step 2: Transform the integral**  
Since \( du = 2x dx \), we rewrite the integral as:

\[
\int u^5 \, du.
\]

**Step 3: Integrate**  

\[
\frac{u^6}{6} + C.
\]

**Step 4: Substitute \( u = x^2 + 1 \) back**  

\[
\frac{(x^2 + 1)^6}{6} + C.
\]

---

#### **4. Example 2: Trigonometric Substitution**  
Evaluate:

\[
\int \frac{\cos x}{\sin x} \, dx.
\]

**Step 1: Choose a substitution**  
Let:

\[
u = \sin x \quad \Rightarrow \quad du = \cos x \, dx.
\]

**Step 2: Transform the integral**  
Since \( du = \cos x \, dx \), the integral becomes:

\[
\int \frac{du}{u}.
\]

**Step 3: Integrate**  
This is a standard logarithmic integral:

\[
\ln |u| + C.
\]

**Step 4: Substitute \( u = \sin x \) back**  

\[
\ln |\sin x| + C.
\]

---

#### **5. Example 3: Definite Integral Using Substitution**  
Evaluate:

\[
\int_0^1 3(x^2 + 1)^2 x \, dx.
\]

**Step 1: Choose a substitution**  
Let:

\[
u = x^2 + 1 \quad \Rightarrow \quad du = 2x dx.
\]

Rearrange to match the integral:

\[
\frac{du}{2} = x dx.
\]

**Step 2: Change limits**  
- When \( x = 0 \), \( u = 0^2 + 1 = 1 \).
- When \( x = 1 \), \( u = 1^2 + 1 = 2 \).

**Step 3: Transform the integral**  

\[
\int_1^2 3u^2 \cdot \frac{du}{2}.
\]

\[
\frac{3}{2} \int_1^2 u^2 \, du.
\]

**Step 4: Integrate**  

\[
\frac{3}{2} \times \frac{u^3}{3} \Bigg|_1^2.
\]

\[
\frac{1}{2} \left( 2^3 - 1^3 \right).
\]

\[
\frac{1}{2} (8 - 1) = \frac{7}{2}.
\]

---

#### **6. Key Takeaways**
- **Substitution simplifies integrals** by transforming complex functions into standard forms.
- **Trigonometric substitution** is useful for integrals involving square roots or trigonometric expressions.
- **Definite integrals require changing limits** when substituting.
- **Pattern recognition** helps in selecting the right \( u \).

This technique is fundamental in solving integrals that appear in calculus, physics, and engineering applications.





## **The Complex Conjugate**  

#### **1. Introduction to Complex Conjugates**  
In complex number theory, the **complex conjugate** of a complex number is obtained by changing the 
sign of its imaginary part. It plays a crucial role in various mathematical and engineering applications, 
including simplifying expressions, solving equations, and working with complex functions.  

---

#### **2. Definition of the Complex Conjugate**  
If a complex number is given as:

\[
z = a + bi
\]

where:
- \( a \) is the **real part**,
- \( b \) is the **imaginary part**,

then its **complex conjugate** is:

\[
\overline{z} = a - bi.
\]

---

#### **3. Geometric Interpretation**  
On the complex plane:
- The complex number \( z = a + bi \) is represented as a point \((a, b)\).
- Its conjugate \( \overline{z} = a - bi \) is the **reflection of \( z \) across the real axis**.

This means the real part stays the same, while the imaginary part is negated.

---

#### **4. Properties of the Complex Conjugate**  
The complex conjugate has several important properties:

1. **Conjugate of a Sum**  
   \[
   \overline{(z_1 + z_2)} = \overline{z_1} + \overline{z_2}
   \]

2. **Conjugate of a Product**  
   \[
   \overline{(z_1 z_2)} = \overline{z_1} \cdot \overline{z_2}
   \]

3. **Conjugate of a Quotient**  
   \[
   \overline{\left(\frac{z_1}{z_2}\right)} = \frac{\overline{z_1}}{\overline{z_2}}, \quad \text{for } z_2 \neq 0.
   \]

4. **Conjugate of a Power**  
   \[
   \overline{(z^n)} = (\overline{z})^n.
   \]

5. **Multiplication of a Complex Number by its Conjugate**  
   \[
   z \cdot \overline{z} = (a + bi)(a - bi) = a^2 + b^2.
   \]
   This is always a real number.

---

#### **5. Using the Complex Conjugate to Compute the Modulus**  
The modulus (or absolute value) of a complex number is:

\[
|z| = \sqrt{a^2 + b^2}.
\]

Since:

\[
z \cdot \overline{z} = a^2 + b^2,
\]

we can compute the modulus as:

\[
|z| = \sqrt{z \cdot \overline{z}}.
\]

---

#### **6. Rationalizing Complex Denominators**  
When dividing by a complex number, we use the conjugate to simplify the expression.

For example, simplify:

\[
\frac{1}{2 + 3i}.
\]

**Step 1: Multiply by the conjugate**  
The conjugate of \( 2 + 3i \) is \( 2 - 3i \), so we multiply both numerator and denominator:

\[
\frac{1}{2 + 3i} \times \frac{2 - 3i}{2 - 3i}.
\]

**Step 2: Expand the denominator**  

\[
(2 + 3i)(2 - 3i) = 4 - 9i^2 = 4 + 9 = 13.
\]

**Step 3: Expand the numerator**  

\[
1 \cdot (2 - 3i) = 2 - 3i.
\]

**Step 4: Write the final result**  

\[
\frac{2 - 3i}{13} = \frac{2}{13} - \frac{3}{13}i.
\]

---

#### **7. Application of Complex Conjugates**
- **Solving complex equations**: Used to find roots of polynomials with real coefficients.
- **Electrical engineering**: Used in AC circuit analysis.
- **Quantum mechanics**: Appears in wave functions and probability amplitudes.
- **Signal processing**: Used in Fourier transforms and filter design.

---

#### **8. Summary**
- The complex conjugate of \( z = a + bi \) is \( \overline{z} = a - bi \).
- It reflects a complex number across the real axis.
- Multiplying a complex number by its conjugate results in a real number.
- The modulus can be computed using the conjugate.
- It helps in simplifying complex fractions and rationalizing denominators.

Understanding the complex conjugate is essential for working with complex numbers in various 
mathematical and applied fields.





## **Equations of Hyperbolas Centered at a General Point**  

A **hyperbola** is the set of all points where the absolute difference of distances from two fixed points (foci) is constant.
When centered at a general point **\((h, k)\)** instead of the origin, the equations adjust accordingly.

---

### **1. Standard Equations of a Hyperbola**  

For a hyperbola centered at \((h, k)\), the general form depends on its orientation:

#### **(a) Horizontal Hyperbola**
If the transverse axis (the axis along which the foci and vertices lie) is **horizontal**, the equation is:

\[
\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1
\]

- **Vertices**: \((h \pm a, k)\)  
- **Foci**: \((h \pm c, k)\), where \( c = \sqrt{a^2 + b^2} \)  
- **Asymptotes**: \( y - k = \pm \frac{b}{a} (x - h) \)  

---

#### **(b) Vertical Hyperbola**
If the transverse axis is **vertical**, the equation is:

\[
\frac{(y - k)^2}{a^2} - \frac{(x - h)^2}{b^2} = 1
\]

- **Vertices**: \((h, k \pm a)\)  
- **Foci**: \((h, k \pm c)\), where \( c = \sqrt{a^2 + b^2} \)  
- **Asymptotes**: \( y - k = \pm \frac{a}{b} (x - h) \)  

---

### **2. Key Parameters**  
- \( a \): Distance from center to **vertices**.  
- \( b \): Controls the asymptotes’ slopes.  
- \( c \): Distance from center to **foci**, found using:

  \[
  c = \sqrt{a^2 + b^2}
  \]

- **Eccentricity**:  

  \[
  e = \frac{c}{a}, \quad e > 1
  \]

  The greater the **eccentricity**, the more "stretched" the hyperbola.

---

### **3. Graphing a Hyperbola Centered at \((h, k)\)**  
1. Identify **center** \((h, k)\).  
2. Plot **vertices** by moving \( a \) units along the transverse axis.  
3. Plot **foci** by moving \( c \) units along the transverse axis.  
4. Sketch **asymptotes** through \( (h, k) \) with slopes \( \pm \frac{b}{a} \) (horizontal) or \( \pm \frac{a}{b} \) (vertical).  
5. Draw the hyperbola opening outward along the transverse axis.

---

### **Example Problem**
Find the equation of a hyperbola centered at \( (3, -2) \) with **vertices at** \( (7, -2) \) and \( (-1, -2) \), and asymptotes with slope \( \pm \frac{4}{3} \).

#### **Step 1: Identify \( a \) and \( b \)**  
- The **center** is at \( (h, k) = (3, -2) \).  
- The **vertices** are \( (h \pm a, k) \), so:  

  \[
  a = 7 - 3 = 4
  \]

- Given asymptote slope **\( \pm \frac{4}{3} \)**, we know:

  \[
  \frac{b}{a} = \frac{4}{3} \Rightarrow b = \frac{4}{3} \times 4 = 4
  \]

#### **Step 2: Write the Equation**
Since the transverse axis is **horizontal**, use:

\[
\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1
\]

Substituting \( (h, k) = (3, -2) \), \( a^2 = 16 \), and \( b^2 = 16 \):

\[
\frac{(x - 3)^2}{16} - \frac{(y + 2)^2}{16} = 1
\]

This is the equation of the hyperbola.

---

### **Conclusion**
Hyperbolas centered at a general point \( (h, k) \) follow the same rules as those centered at the origin but shift accordingly. 
Understanding the relationships between \( a \), \( b \), and \( c \) helps in identifying key elements such as vertices, foci, and asymptotes, 
making it easier to graph and analyze these curves.




## **Independent and Dependent Events in Probability**  

In probability theory, events are classified as **independent** or **dependent** based on whether the 
occurrence of one event affects the probability of another.

---

### **1. Independent Events**  
Two events **\( A \)** and **\( B \)** are **independent** if the occurrence of one does **not** affect the probability of the other.

#### **Mathematical Definition:**  
Events \( A \) and \( B \) are independent if:

\[
P(A \cap B) = P(A) \cdot P(B)
\]

This means the probability of both events occurring together is simply the product of their individual probabilities.

#### **Examples of Independent Events:**  
- Rolling a die and flipping a coin: The result of the die does not affect the coin toss.  
- Drawing a card from a deck, replacing it, and drawing again: Since the first card is replaced, the second draw is unaffected.  

---

### **2. Dependent Events**  
Two events **\( A \)** and **\( B \)** are **dependent** if the occurrence of one affects the probability of the other.

#### **Mathematical Definition:**  
Events \( A \) and \( B \) are dependent if:

\[
P(A \cap B) \neq P(A) \cdot P(B)
\]

Instead, the probability of **\( B \) given \( A \)** is expressed using conditional probability:

\[
P(B | A) = \frac{P(A \cap B)}{P(A)}
\]

Thus, the probability of both occurring is:

\[
P(A \cap B) = P(A) \cdot P(B | A)
\]

#### **Examples of Dependent Events:**  
- Drawing a card **without replacement**: The probability of drawing a second red card changes after drawing the first.  
- Choosing a student randomly from a class and then choosing another without replacing them: The second selection is affected by the first.

---

### **Key Difference:**  
- **Independent Events:** The outcome of one event does not change the probability of the other.  
- **Dependent Events:** The outcome of one event affects the probability of the other.

Understanding this distinction is crucial in probability calculations, especially in real-world scenarios 
like risk assessment, game theory, and machine learning.






## **Independent Events in Probability**  

#### **Definition of Independent Events**  
Two events, \( A \) and \( B \), are **independent** if the occurrence of one event does not affect 
the probability of the other occurring. Mathematically, events \( A \) and \( B \) are independent if:

\[
P(A \cap B) = P(A) \cdot P(B)
\]

This formula generalizes to multiple events. If \( A_1, A_2, ..., A_n \) are independent, then:

\[
P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_1) \cdot P(A_2) \cdots P(A_n)
\]

This means that the probability of all events occurring together is simply the product of their individual probabilities.

---

### **Key Properties of Independent Events**
1. **Multiplication Rule**  
   - If \( A \) and \( B \) are independent:
     \[
     P(A \cap B) = P(A) \cdot P(B)
     \]
   - If three events \( A, B, C \) are independent:
     \[
     P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)
     \]

2. **Conditional Probability of Independent Events**  
   - For independent events, knowing that one has occurred does not change the probability of the other occurring:
     \[
     P(A | B) = P(A)
     \]
     \[
     P(B | A) = P(B)
     \]
   - This confirms that \( A \) and \( B \) do not influence each other.

---

### **Examples of Independent Events**
#### **Example 1: Tossing Two Coins**  
- Let \( A \) be the event of getting **Heads on the first coin**.
- Let \( B \) be the event of getting **Tails on the second coin**.

Since each coin flip is independent, we calculate:

\[
P(A) = \frac{1}{2}, \quad P(B) = \frac{1}{2}
\]

The probability of both occurring together:

\[
P(A \cap B) = P(A) \cdot P(B) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}
\]

#### **Example 2: Rolling a Die and Flipping a Coin**
- Let \( A \) be the event of rolling a **4** on a six-sided die:  
  \[
  P(A) = \frac{1}{6}
  \]
- Let \( B \) be the event of flipping a **Heads** on a fair coin:  
  \[
  P(B) = \frac{1}{2}
  \]

Since rolling a die does not affect a coin flip:

\[
P(A \cap B) = P(A) \cdot P(B) = \frac{1}{6} \times \frac{1}{2} = \frac{1}{12}
\]

---

### **Independent vs. Dependent Events**
| Feature            | Independent Events | Dependent Events |
|--------------------|-------------------|------------------|
| Definition        | The occurrence of one event does not affect the probability of the other. | The occurrence of one event affects the probability of the other. |
| Formula          | \( P(A \cap B) = P(A) \cdot P(B) \) | \( P(A \cap B) = P(A) \cdot P(B | A) \) |
| Example          | Rolling a die and flipping a coin | Drawing cards **without replacement** from a deck |

---

### **Checking for Independence**
To verify if events \( A \) and \( B \) are independent, check:

\[
P(A \cap B) = P(A) \cdot P(B)
\]

If this equation holds, \( A \) and \( B \) are independent. Otherwise, they are dependent.

#### **Example: Are These Events Independent?**
A fair six-sided die is rolled:
- Let \( A \) be the event of rolling an **even number** (\{2,4,6\}).
- Let \( B \) be the event of rolling a **number greater than 3** (\{4,5,6\}).

Compute probabilities:

\[
P(A) = \frac{3}{6} = \frac{1}{2}, \quad P(B) = \frac{3}{6} = \frac{1}{2}
\]

Find \( P(A \cap B) \), the probability of rolling an even number **greater than 3** (\{4,6\}):

\[
P(A \cap B) = \frac{2}{6} = \frac{1}{3}
\]

Compare:

\[
P(A) \cdot P(B) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}
\]

Since \( P(A \cap B) \neq P(A) \cdot P(B) \), these events are **not independent**.

---

### **Conclusion**
Independent events in probability follow the multiplication rule, and one event occurring does 
not influence the probability of the other. Recognizing independence is crucial in probability calculations, 
statistical inference, and machine learning applications.





## **Special Properties of the Complex Conjugate**  

#### **Definition of the Complex Conjugate**  
For a complex number \( z = a + bi \), where \( a, b \) are real numbers and \( i = \sqrt{-1} \), 
its **complex conjugate** is denoted as:

\[
\overline{z} = a - bi
\]

This operation reflects \( z \) across the real axis in the complex plane.

---

### **Special Properties of the Complex Conjugate**

#### **1. Conjugate of a Sum**
For two complex numbers \( z_1 \) and \( z_2 \):

\[
\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}
\]

✔ **Proof:**  
Let \( z_1 = a + bi \) and \( z_2 = c + di \), then:

\[
z_1 + z_2 = (a+c) + (b+d)i
\]

Taking the conjugate:

\[
\overline{z_1 + z_2} = (a+c) - (b+d)i = \overline{z_1} + \overline{z_2}
\]

---

#### **2. Conjugate of a Product**
For two complex numbers \( z_1 \) and \( z_2 \):

\[
\overline{z_1 \cdot z_2} = \overline{z_1} \cdot \overline{z_2}
\]

✔ **Proof:**  
Using \( z_1 = a + bi \) and \( z_2 = c + di \):

\[
z_1 \cdot z_2 = (a + bi)(c + di) = (ac - bd) + (ad + bc)i
\]

Taking the conjugate:

\[
\overline{z_1 \cdot z_2} = (ac - bd) - (ad + bc)i
\]

Now computing \( \overline{z_1} \cdot \overline{z_2} \):

\[
\overline{z_1} = a - bi, \quad \overline{z_2} = c - di
\]

\[
\overline{z_1} \cdot \overline{z_2} = (a - bi)(c - di) = (ac - bd) - (ad + bc)i
\]

Since both expressions are equal:

\[
\overline{z_1 \cdot z_2} = \overline{z_1} \cdot \overline{z_2}
\]

---

#### **3. Conjugate of a Quotient**
For two complex numbers \( z_1 \) and \( z_2 \neq 0 \):

\[
\overline{\left( \frac{z_1}{z_2} \right)} = \frac{\overline{z_1}}{\overline{z_2}}
\]

✔ **Proof:**  
Let \( z_1 = a + bi \) and \( z_2 = c + di \), then:

\[
\frac{z_1}{z_2} = \frac{(a + bi)}{(c + di)}
\]

Multiply by the conjugate of the denominator:

\[
\frac{(a + bi)(c - di)}{(c + di)(c - di)}
\]

\[
= \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
\]

Taking the conjugate:

\[
\overline{\frac{z_1}{z_2}} = \frac{(ac + bd) - (bc - ad)i}{c^2 + d^2}
\]

Now, computing \( \frac{\overline{z_1}}{\overline{z_2}} \):

\[
\frac{\overline{z_1}}{\overline{z_2}} = \frac{(a - bi)}{(c - di)}
\]

Multiplying numerator and denominator by \( c + di \):

\[
= \frac{(a - bi)(c + di)}{(c - di)(c + di)}
\]

\[
= \frac{(ac + bd) - (ad - bc)i}{c^2 + d^2}
\]

Since both expressions match:

\[
\overline{\left( \frac{z_1}{z_2} \right)} = \frac{\overline{z_1}}{\overline{z_2}}
\]

---

#### **4. Modulus and Conjugate Relationship**
The modulus of a complex number is:

\[
|z| = \sqrt{a^2 + b^2}
\]

The modulus remains the same under conjugation:

\[
|\overline{z}| = |z|
\]

✔ **Proof:**  
Since \( \overline{z} = a - bi \):

\[
|\overline{z}| = \sqrt{a^2 + (-b)^2} = \sqrt{a^2 + b^2} = |z|
\]

Thus, taking the conjugate does not change the magnitude.

---

#### **5. Conjugate and Reciprocal Relationship**
For \( z \neq 0 \):

\[
\overline{\left( \frac{1}{z} \right)} = \frac{1}{\overline{z}}
\]

✔ **Proof:**  
Using the property:

\[
\frac{1}{z} = \frac{\overline{z}}{|z|^2}
\]

Taking the conjugate:

\[
\overline{\left(\frac{1}{z}\right)} = \overline{\left(\frac{\overline{z}}{|z|^2}\right)} = \frac{\overline{\overline{z}}}{|z|^2} = \frac{z}{|z|^2} = \frac{1}{\overline{z}}
\]

---

#### **6. Sum of a Complex Number and Its Conjugate**
\[
z + \overline{z} = 2a
\]

✔ **Proof:**  
\[
(a + bi) + (a - bi) = 2a
\]

The imaginary part cancels out, leaving only the real part.

---

#### **7. Product of a Complex Number and Its Conjugate**
\[
z \cdot \overline{z} = |z|^2
\]

✔ **Proof:**  
\[
(a + bi)(a - bi) = a^2 - (bi)^2 = a^2 + b^2 = |z|^2
\]

---

### **Geometric Interpretation**
- The complex conjugate \( \overline{z} \) reflects \( z \) across the real axis.
- The magnitude \( |z| \) represents the distance from the origin.
- The product \( z \cdot \overline{z} \) gives the square of the modulus, meaning it captures the squared Euclidean norm.

---

### **Conclusion**
The complex conjugate has key algebraic and geometric properties that make it fundamental in complex analysis, 
quantum mechanics, and engineering. It preserves modulus, interacts predictably under arithmetic operations, 
and provides a straightforward way to compute reciprocals of complex numbers.





## **Dividing Complex Numbers**  

#### **Definition**
Given two complex numbers:  

\[
z_1 = a + bi, \quad z_2 = c + di, \quad z_2 \neq 0
\]

The division of \( z_1 \) by \( z_2 \) is defined as:

\[
\frac{z_1}{z_2}
\]

To simplify this expression, we use the **conjugate method**, which eliminates the imaginary part 
from the denominator.

---

### **Step-by-Step Process for Division**

#### **Step 1: Multiply by the Conjugate of the Denominator**
The conjugate of \( z_2 = c + di \) is:

\[
\overline{z_2} = c - di
\]

Multiplying the numerator and denominator by \( \overline{z_2} \):

\[
\frac{z_1}{z_2} = \frac{(a + bi)}{(c + di)} \times \frac{(c - di)}{(c - di)}
\]

Since \( \frac{c - di}{c - di} = 1 \), this does not change the value of the expression.

---

#### **Step 2: Expand the Numerator and Denominator**

Using the distributive property:

\[
(a + bi)(c - di) = ac - adi + bci - bdi^2
\]

Since \( i^2 = -1 \), we get:

\[
= ac - adi + bci + bd
\]

Rearrange terms:

\[
= (ac + bd) + (bc - ad)i
\]

Now, expand the denominator:

\[
(c + di)(c - di) = c^2 - (di)^2 = c^2 - d^2i^2 = c^2 + d^2
\]

Since \( i^2 = -1 \), the denominator becomes:

\[
c^2 + d^2
\]

---

#### **Step 3: Express in Standard Form**
\[
\frac{z_1}{z_2} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
\]

Splitting into real and imaginary parts:

\[
\frac{z_1}{z_2} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2} i
\]

Thus, the quotient of two complex numbers is another complex number in the form:

\[
\frac{z_1}{z_2} = x + yi
\]

where:

\[
x = \frac{ac + bd}{c^2 + d^2}, \quad y = \frac{bc - ad}{c^2 + d^2}
\]

---

### **Example Calculation**
#### **Example 1: Compute \( \frac{3 + 4i}{1 - 2i} \)**

1. **Find the conjugate of the denominator**:  
   The denominator is \( 1 - 2i \), so its conjugate is \( 1 + 2i \).

2. **Multiply numerator and denominator by the conjugate**:

   \[
   \frac{(3 + 4i)(1 + 2i)}{(1 - 2i)(1 + 2i)}
   \]

3. **Expand the numerator**:

   \[
   (3 + 4i)(1 + 2i) = 3 \cdot 1 + 3 \cdot 2i + 4i \cdot 1 + 4i \cdot 2i
   \]

   \[
   = 3 + 6i + 4i + 8i^2
   \]

   Since \( i^2 = -1 \), we get:

   \[
   = 3 + 6i + 4i - 8 = -5 + 10i
   \]

4. **Expand the denominator**:

   \[
   (1 - 2i)(1 + 2i) = 1 - 4i^2 = 1 + 4 = 5
   \]

5. **Divide by the denominator**:

   \[
   \frac{-5 + 10i}{5} = -1 + 2i
   \]

**Final Answer:**  
\[
\frac{3 + 4i}{1 - 2i} = -1 + 2i
\]

---

### **Special Properties of Division in Complex Numbers**
1. **Dividing by a Real Number**:  
   If \( z = a + bi \) and \( k \) is a real number:

   \[
   \frac{z}{k} = \frac{a}{k} + \frac{b}{k}i
   \]

   This simply scales both real and imaginary parts.

2. **Dividing by a Purely Imaginary Number**:  
   If \( z_2 = bi \), then:

   \[
   \frac{a + bi}{bi} = \frac{a + bi}{bi} \times \frac{-i}{-i} = \frac{(-ai - b) i}{b^2}
   \]

   Since \( i^2 = -1 \), this simplifies to:

   \[
   \frac{-ai - b}{b^2}i = \frac{-b}{b^2} + \frac{-a}{b^2}i = -\frac{b}{b^2} - \frac{a}{b^2}i
   \]

   Which simplifies further.

3. **Dividing a Complex Number by Itself**:  
   Since \( z \cdot \overline{z} = |z|^2 \), the division simplifies to:

   \[
   \frac{z}{z} = 1
   \]

   as long as \( z \neq 0 \).

---

### **Geometric Interpretation**
- Division of complex numbers can be seen as **scaling and rotating** in the complex plane.
- The magnitude (modulus) of the quotient is:

  \[
  \left| \frac{z_1}{z_2} \right| = \frac{|z_1|}{|z_2|}
  \]

  meaning the magnitudes divide.

- The argument (angle) of the quotient is:

  \[
  \arg \left(\frac{z_1}{z_2}\right) = \arg(z_1) - \arg(z_2)
  \]

  meaning the angle is **subtracted**.

---

### **Conclusion**
Dividing complex numbers involves multiplying by the conjugate of the denominator to eliminate the imaginary part.
This results in a new complex number whose real and imaginary components can be computed separately. 
The division process has both algebraic and geometric significance, making it an essential tool in complex analysis, 
signal processing, and engineering applications.







## **The Sum of a Finite Geometric Series**

#### **Definition**
A **geometric series** is a sum of terms where each term is obtained by multiplying the previous one by a fixed number 
called the **common ratio** \( r \). A **finite geometric series** has a fixed number of terms.

#### **General Form of a Finite Geometric Series**
A geometric series with **first term** \( a \), **common ratio** \( r \), and **\( n \) terms** is:

\[
S_n = a + ar + ar^2 + ar^3 + \dots + ar^{n-1}
\]

---

### **1. Formula for the Sum of a Finite Geometric Series**
The sum of the first \( n \) terms of a geometric series is given by:

\[
S_n = \frac{a(1 - r^n)}{1 - r}, \quad \text{for } r \neq 1.
\]

Where:
- \( S_n \) = sum of the first \( n \) terms,
- \( a \) = first term,
- \( r \) = common ratio,
- \( n \) = number of terms.

---

### **2. Derivation of the Formula**
To derive the sum formula, start with the series:

\[
S_n = a + ar + ar^2 + \dots + ar^{n-1}
\]

Multiply both sides by \( r \):

\[
r S_n = ar + ar^2 + ar^3 + \dots + ar^n
\]

Now subtract the two equations:

\[
S_n - r S_n = a - ar^n
\]

Factor out \( S_n \):

\[
S_n (1 - r) = a (1 - r^n)
\]

Divide by \( (1 - r) \) (for \( r \neq 1 \)):

\[
S_n = \frac{a(1 - r^n)}{1 - r}
\]

---

### **3. Special Cases**
#### **(i) When \( r = 1 \)**
If \( r = 1 \), all terms are the same, so the sum is simply:

\[
S_n = n \cdot a
\]

#### **(ii) When \( |r| < 1 \) and \( n \to \infty \)**
If the series extends infinitely and \( |r| < 1 \), the sum approaches:

\[
S_{\infty} = \frac{a}{1 - r}
\]

This is the formula for an **infinite geometric series**.

---

### **4. Example Calculations**
#### **Example 1: Find the sum of the series**
\[
3 + 6 + 12 + 24 + 48
\]
Here:
- \( a = 3 \),
- \( r = \frac{6}{3} = 2 \),
- \( n = 5 \).

Using the formula:

\[
S_5 = \frac{3(1 - 2^5)}{1 - 2} = \frac{3(1 - 32)}{1 - 2} = \frac{3(-31)}{-1} = 93.
\]

#### **Example 2: Find the sum of the series**
\[
5 + \frac{5}{2} + \frac{5}{4} + \frac{5}{8}
\]
Here:
- \( a = 5 \),
- \( r = \frac{1}{2} \),
- \( n = 4 \).

Using the formula:

\[
S_4 = \frac{5(1 - (1/2)^4)}{1 - 1/2} = \frac{5(1 - 1/16)}{1/2} = \frac{5(15/16)}{1/2} = \frac{75}{8} = 9.375.
\]

---

### **5. Applications**
- **Finance**: Computing compound interest.
- **Physics**: Modeling repeated decay processes.
- **Computer Science**: Analyzing recursive algorithms.
- **Economics**: Calculating depreciation over time.

---

### **6. Conclusion**
The sum of a finite geometric series is efficiently computed using:

\[
S_n = \frac{a(1 - r^n)}{1 - r}, \quad r \neq 1.
\]

Understanding this formula helps in various fields, from finance to physics, where repeated growth or decay occurs.






## **Expressing Rational Functions with Repeated Factors as Sums of Partial Fractions**

#### **1. Understanding Partial Fractions Decomposition**
Partial fraction decomposition is a method used to break down a complex rational function into simpler fractions. This technique is particularly 
useful for integration and solving differential equations.

For a rational function of the form:

\[
\frac{P(x)}{Q(x)}
\]

where \( P(x) \) and \( Q(x) \) are polynomials, and \( \deg P(x) < \deg Q(x) \), we express \( \frac{P(x)}{Q(x)} \) as a sum of simpler rational expressions.

When the denominator \( Q(x) \) has **repeated factors**, special handling is required.

---

#### **2. Types of Partial Fractions and Repeated Factors**
For a rational function with repeated linear or quadratic factors in the denominator, we follow these rules:

1. **Repeated Linear Factors**: If the denominator contains a repeated linear factor \( (x - a)^n \), we must include **separate fractions for each power** of the factor:

   \[
   \frac{P(x)}{(x - a)^n} = \frac{A_1}{x - a} + \frac{A_2}{(x - a)^2} + \dots + \frac{A_n}{(x - a)^n}
   \]

2. **Repeated Irreducible Quadratic Factors**: If the denominator contains a repeated irreducible quadratic factor \( (x^2 + bx + c)^n \), we express the decomposition as:

   \[
   \frac{P(x)}{(x^2 + bx + c)^n} = \frac{Ax + B}{x^2 + bx + c} + \frac{Cx + D}{(x^2 + bx + c)^2} + \dots + \frac{Yx + Z}{(x^2 + bx + c)^n}
   \]

Each fraction has a numerator of one degree lower than the corresponding denominator.

---

#### **3. Step-by-Step Decomposition Process**
To express a rational function as a sum of partial fractions:

1. **Factor the Denominator**: Identify if the denominator contains repeated linear or quadratic factors.
2. **Set Up Partial Fractions**: Write the appropriate fractions as per the factorization.
3. **Multiply by the Denominator**: Multiply both sides by the original denominator to eliminate fractions.
4. **Expand and Group Terms**: Expand and match terms on both sides.
5. **Solve for Coefficients**: Solve the system of equations to find unknown constants.

---

#### **4. Example 1: Repeated Linear Factors**
Decompose:

\[
\frac{5x + 2}{(x - 1)^2 (x + 2)}
\]

**Step 1: Factor the denominator**
\[
(x - 1)^2 (x + 2)
\]

**Step 2: Set up the decomposition**
\[
\frac{5x + 2}{(x - 1)^2 (x + 2)} = \frac{A}{x - 1} + \frac{B}{(x - 1)^2} + \frac{C}{x + 2}
\]

**Step 3: Multiply by the denominator**
\[
5x + 2 = A(x - 1)(x + 2) + B(x + 2) + C(x - 1)^2
\]

**Step 4: Expand and collect like terms**
\[
5x + 2 = A(x^2 + x - 2) + B(x + 2) + C(x^2 - 2x + 1)
\]

**Step 5: Solve for A, B, and C**
Expanding and matching coefficients gives a system of equations to solve.

---

#### **5. Example 2: Repeated Quadratic Factor**
Decompose:

\[
\frac{x^2 + 3x + 5}{(x^2 + 1)^2}
\]

**Step 1: Factor the denominator**
\[
(x^2 + 1)^2
\]

**Step 2: Set up the decomposition**
\[
\frac{x^2 + 3x + 5}{(x^2 + 1)^2} = \frac{Ax + B}{x^2 + 1} + \frac{Cx + D}{(x^2 + 1)^2}
\]

**Step 3: Multiply by the denominator**
\[
x^2 + 3x + 5 = (Ax + B)(x^2 + 1) + (Cx + D)
\]

**Step 4: Expand and collect like terms**
\[
Ax^3 + Ax + Bx^2 + B + Cx + D = x^2 + 3x + 5
\]

**Step 5: Solve for A, B, C, and D**
Matching coefficients results in a system of equations to determine the unknowns.

---

#### **6. Summary**
- **Repeated linear factors** require separate terms for each power.
- **Repeated quadratic factors** require numerators with an extra variable (Ax + B).
- Multiply, expand, and match coefficients to solve for unknowns.

This method is essential for integration and solving equations in calculus and differential equations.







## **Introduction to Polar Coordinates**  

Polar coordinates provide an alternative to Cartesian coordinates for representing points in a plane. 
Instead of using **(x, y)**, polar coordinates use **(r, θ)**, where:  

- **r** is the radial distance from the origin (the pole).  
- **θ** (theta) is the angle measured from the positive x-axis, usually in radians or degrees.  

### **1. Relationship Between Cartesian and Polar Coordinates**  
To convert between the two coordinate systems:  

- **From Polar to Cartesian:**  
  \[
  x = r\cos\theta
  \]
  \[
  y = r\sin\theta
  \]
  
- **From Cartesian to Polar:**  
  \[
  r = \sqrt{x^2 + y^2}
  \]
  \[
  \theta = \tan^{-1} \left(\frac{y}{x}\right)
  \]
  (Adjust **θ** based on quadrant placement.)

### **2. Understanding the Polar Plane**  
- The **radial coordinate** \( r \) can be positive or negative. A negative \( r \) reflects the point across the origin.  
- The **angle** \( \theta \) can have multiple representations:  
  - **Standard**: \( \theta \) measured counterclockwise from the positive x-axis.  
  - **Negative Angles**: Measured clockwise.  
  - **Equivalent Angles**: Since angles repeat every \( 2\pi \) radians (or 360°), adding or subtracting \( 2\pi \) does not change the location.  

### **3. Plotting Points in Polar Coordinates**  
Each point in the polar system can have multiple equivalent representations due to the periodic nature of angles.  
Example: The point \( (3, \frac{\pi}{4}) \) is the same as:  
- \( (3, \frac{\pi}{4} + 2\pi) \)  
- \( (-3, \frac{5\pi}{4}) \)  

### **4. Graphing Polar Equations**  
Common polar curves include:  
- **Circles**: \( r = a \) (a circle centered at the origin with radius \( a \)).  
- **Lines**: \( \theta = \theta_0 \) (a straight line passing through the origin).  
- **Lemniscates**: \( r^2 = a^2 \cos 2\theta \) (figure-eight curves).  
- **Cardioids**: \( r = a(1 + \cos\theta) \) (heart-shaped curves).  

### **5. Applications of Polar Coordinates**  
- Used in **physics** for rotational motion and wave functions.  
- Applied in **engineering** for modeling circular and spiral patterns.  
- Essential in **calculus** for evaluating integrals in circular regions.  






## **Converting from Polar Coordinates to Cartesian Coordinates**  

Polar coordinates \((r, \theta)\) provide an alternative to Cartesian coordinates \((x, y)\) for representing 
points in a plane. To convert from polar to Cartesian, we use trigonometric relationships derived from a 
right triangle.

---

### **1. Conversion Formulas**  
Given a point in polar form **\((r, \theta)\)**, the corresponding Cartesian coordinates \((x, y)\) 
are found using:

\[
x = r \cos \theta
\]

\[
y = r \sin \theta
\]

These formulas come from the fact that in a right triangle:
- \( r \) is the hypotenuse.
- \( \theta \) is the angle with the positive x-axis.
- The adjacent side to \( \theta \) is \( x = r\cos\theta \).
- The opposite side to \( \theta \) is \( y = r\sin\theta \).

---

### **2. Examples of Conversion**  

#### **Example 1: Convert \( (4, 60^\circ) \) to Cartesian coordinates.**  
Using the formulas:

\[
x = 4 \cos 60^\circ = 4 \times \frac{1}{2} = 2
\]

\[
y = 4 \sin 60^\circ = 4 \times \frac{\sqrt{3}}{2} = 2\sqrt{3}
\]

So, the Cartesian coordinates are:

\[
(2, 2\sqrt{3})
\]

---

#### **Example 2: Convert \( (5, \frac{\pi}{4}) \) to Cartesian coordinates.**  
Since \( \frac{\pi}{4} = 45^\circ \):

\[
x = 5 \cos 45^\circ = 5 \times \frac{\sqrt{2}}{2} = \frac{5\sqrt{2}}{2}
\]

\[
y = 5 \sin 45^\circ = 5 \times \frac{\sqrt{2}}{2} = \frac{5\sqrt{2}}{2}
\]

So, the Cartesian coordinates are:

\[
\left(\frac{5\sqrt{2}}{2}, \frac{5\sqrt{2}}{2}\right)
\]

---

### **3. Handling Negative \( r \) Values**  
A negative \( r \) reflects the point across the origin. If \( (r, \theta) \) is given but \( r \) is negative, rewrite it as:

\[
(-r, \theta + \pi)
\]

Example:  
Convert \( (-3, 30^\circ) \) to Cartesian coordinates.  
First, rewrite it as \( (3, 30^\circ + 180^\circ) = (3, 210^\circ) \).  

\[
x = 3 \cos 210^\circ = 3 \times \left(-\frac{\sqrt{3}}{2}\right) = -\frac{3\sqrt{3}}{2}
\]

\[
y = 3 \sin 210^\circ = 3 \times \left(-\frac{1}{2}\right) = -\frac{3}{2}
\]

So, the Cartesian coordinates are:

\[
\left(-\frac{3\sqrt{3}}{2}, -\frac{3}{2}\right)
\]

---

### **4. Quadrant Considerations**  
- If \( \theta \) is in **Quadrant I** (\( 0^\circ \) to \( 90^\circ \)), both \( x \) and \( y \) are **positive**.  
- If \( \theta \) is in **Quadrant II** (\( 90^\circ \) to \( 180^\circ \)), \( x \) is **negative** and \( y \) is **positive**.  
- If \( \theta \) is in **Quadrant III** (\( 180^\circ \) to \( 270^\circ \)), both \( x \) and \( y \) are **negative**.  
- If \( \theta \) is in **Quadrant IV** (\( 270^\circ \) to \( 360^\circ \)), \( x \) is **positive** and \( y \) is **negative**.  

---

### **5. Applications of Conversion**  
- **Physics**: Used in rotational motion, electromagnetism, and wave functions.  
- **Engineering**: Applied in robotics, radar systems, and fluid mechanics.  
- **Computer Graphics**: Helps in rendering curves and objects in different coordinate systems.  






## **Writing Sums of Trigonometric Functions in Amplitude-Phase Form**  

#### **1. Understanding Amplitude-Phase Form**  
A sum of two sine or cosine functions of the same frequency can be rewritten as a single sinusoidal 
function with an amplitude and a phase shift. The general transformation follows:  


\[
a \cos x + b \sin x = R \cos(x - \phi)
\]

or equivalently,

\[
a \cos x + b \sin x = R \sin(x + \theta)
\]

where:  
- \( R \) is the **amplitude**, given by:  
  \[
  R = \sqrt{a^2 + b^2}
  \]
- \( \phi \) (or \( \theta \)) is the **phase shift**, determined by:  
  \[
  \tan \phi = \frac{b}{a}
  \]

---

#### **2. Deriving the Formula**  
Using the cosine angle identity:

\[
\cos (x - \phi) = \cos x \cos \phi + \sin x \sin \phi
\]

Multiplying both sides by \( R \):

\[
R \cos (x - \phi) = R \cos \phi \cos x + R \sin \phi \sin x
\]

Comparing with \( a \cos x + b \sin x \), we equate coefficients:

\[
R \cos \phi = a, \quad R \sin \phi = b
\]

Dividing the equations:

\[
\tan \phi = \frac{b}{a}
\]

And solving for \( R \):

\[
R = \sqrt{a^2 + b^2}
\]

---

#### **3. Example Calculation**  

**Example 1:** Express \( 3\cos x + 4\sin x \) in amplitude-phase form.  

1. Compute \( R \):

   \[
   R = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
   \]

2. Compute \( \phi \):

   \[
   \tan \phi = \frac{4}{3}
   \]

   Using inverse tangent:

   \[
   \phi = \tan^{-1} \left(\frac{4}{3}\right) \approx 53.13^\circ
   \]

3. Rewrite the function:

   \[
   3\cos x + 4\sin x = 5 \cos(x - 53.13^\circ)
   \]

---

**Example 2:** Express \( -2\cos x + 5\sin x \) in amplitude-phase form.  

1. Compute \( R \):

   \[
   R = \sqrt{(-2)^2 + 5^2} = \sqrt{4 + 25} = \sqrt{29}
   \]

2. Compute \( \phi \):

   \[
   \tan \phi = \frac{5}{-2} = -2.5
   \]

   Using inverse tangent:

   \[
   \phi = \tan^{-1}(-2.5) \approx -68.2^\circ
   \]

3. Rewrite the function:

   \[
   -2\cos x + 5\sin x = \sqrt{29} \cos(x + 68.2^\circ)
   \]

---

#### **4. Applications**  
- **Signal Processing**: Used to simplify oscillatory signals in physics and engineering.  
- **Electrical Circuits**: Helps in analyzing AC waveforms.  
- **Harmonic Motion**: Common in physics problems involving oscillations.  

This method allows rewriting trigonometric sums into a more intuitive sinusoidal form, 
making calculations and interpretations easier.





## 
































































































































































































































