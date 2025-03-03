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





## **Writing Geometric Series in Sigma Notation**  

A **geometric series** is a sum of terms where each term is obtained by multiplying the previous 
one by a constant ratio. **Sigma notation (∑)** provides a compact way to represent these sums.

---

### **🔹 General Formula for a Geometric Series in Sigma Notation**  
A geometric series can be written as:  

\[
S_n = a + ar + ar^2 + ar^3 + \dots + ar^{n-1}
\]

Using **sigma notation**, this becomes:

\[
S_n = \sum_{k=0}^{n-1} ar^k
\]

where:  
- \( a \) = first term  
- \( r \) = common ratio  
- \( n \) = number of terms  
- \( k \) = index of summation (starting from 0)

---

### **🔹 Examples**
#### **1️⃣ Finite Geometric Series Example**
Write the sum **\( 3 + 6 + 12 + 24 + 48 \)** in sigma notation.

👉 Identify parameters:  
- First term: \( a = 3 \)  
- Common ratio: \( r = \frac{6}{3} = 2 \)  
- Number of terms: \( n = 5 \)  

Using the formula:

\[
\sum_{k=0}^{4} 3(2)^k
\]

---

#### **2️⃣ Infinite Geometric Series Example**
An infinite geometric series **\( 5 + \frac{5}{2} + \frac{5}{4} + \frac{5}{8} + \dots \)** can be written as:

\[
\sum_{k=0}^{\infty} 5\left(\frac{1}{2}\right)^k
\]

✅ **Converges if** \( |r| < 1 \), using:

\[
S_{\infty} = \frac{a}{1 - r}
\]

---

### **🔹 Special Cases**
1. **Geometric Series Starting from \( k=1 \)**:  
   If a series starts from \( k=1 \), rewrite it as:

   \[
   \sum_{k=1}^{n} ar^{k-1}
   \]

2. **Changing the First Term**:  
   If the first term isn't at \( k=0 \), adjust the exponent accordingly.

---

### **🔹 Summary**
| **Case** | **Sigma Notation** |
|------------|--------------------|
| Finite Series | \( \sum_{k=0}^{n-1} ar^k \) |
| Infinite Series (\( |r| < 1 \)) | \( \sum_{k=0}^{\infty} ar^k \) |
| Starting at \( k=1 \) | \( \sum_{k=1}^{n} ar^{k-1} \) |

🚀 **Key Takeaway**: Geometric series are easy to express using sigma notation, making it useful for 
compact representation and further calculations.




## **The Polar Form of a Complex Number**  

A **complex number** \( z \) can be expressed in both **rectangular (Cartesian)** and **polar forms**. 
The **polar form** is particularly useful for multiplication, division, and finding roots of complex numbers.

---

### **🔹 Rectangular vs. Polar Form**  
A complex number in **rectangular form** is:  
\[
z = x + iy
\]  
where:  
- \( x \) = real part  
- \( y \) = imaginary part  
- \( i \) = imaginary unit (\( i^2 = -1 \))

In **polar form**, the same number is expressed as:  
\[
z = r (\cos \theta + i \sin \theta)
\]  
or using **Euler’s formula**:  
\[
z = r e^{i\theta}
\]  
where:  
- \( r = |z| = \sqrt{x^2 + y^2} \) (modulus or magnitude)  
- \( \theta = \tan^{-1} \left(\frac{y}{x}\right) \) (argument or phase angle)  

---

### **🔹 Conversion Between Forms**
#### **1️⃣ Rectangular to Polar**  
Given \( z = x + iy \):  
- Compute **magnitude**:  
  \[
  r = \sqrt{x^2 + y^2}
  \]
- Compute **angle** \( \theta \) (principal argument):  
  \[
  \theta = \tan^{-1} \left(\frac{y}{x}\right)
  \]

Then, write:
\[
z = r (\cos \theta + i \sin \theta) = r e^{i\theta}
\]

👉 **Example:** Convert \( z = 1 + i\sqrt{3} \) to polar form.  
- \( r = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{4} = 2 \)  
- \( \theta = \tan^{-1} \left(\frac{\sqrt{3}}{1}\right) = \frac{\pi}{3} \)  

So,  
\[
z = 2 e^{i\pi/3}
\]

---

#### **2️⃣ Polar to Rectangular**  
Given \( z = r e^{i\theta} \), expand using Euler’s formula:  
\[
z = r (\cos \theta + i \sin \theta)
\]

👉 **Example:** Convert \( z = 4e^{i\pi/4} \) to rectangular form.  
- \( x = 4 \cos (\pi/4) = 4 \times \frac{\sqrt{2}}{2} = 2\sqrt{2} \)  
- \( y = 4 \sin (\pi/4) = 4 \times \frac{\sqrt{2}}{2} = 2\sqrt{2} \)  

So,  
\[
z = 2\sqrt{2} + i 2\sqrt{2}
\]

---

### **🔹 Applications of Polar Form**
1. **Multiplication & Division**:  
   - **Multiplication**:  
     \[
     z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)}
     \]
   - **Division**:  
     \[
     \frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}
     \]

2. **Powers & Roots (De Moivre’s Theorem)**:  
   - **Powers**:  
     \[
     z^n = r^n e^{i n \theta}
     \]
   - **Roots**:  
     \[
     z_k = r^{1/n} e^{i (\theta + 2k\pi)/n}, \quad k = 0,1,\dots, n-1
     \]

---

### **🔹 Summary**
| **Form** | **Expression** |
|----------|--------------|
| Rectangular | \( x + iy \) |
| Polar | \( r (\cos \theta + i \sin \theta) \) |
| Exponential | \( r e^{i\theta} \) |
| Magnitude | \( r = \sqrt{x^2 + y^2} \) |
| Argument | \( \theta = \tan^{-1} (y/x) \) |

🚀 **Key Takeaway**: The polar form is extremely useful for simplifying operations like multiplication, 
division, and root calculations of complex numbers.






## **Convergence of a Geometric Sequence**  

#### **1. Definition of a Geometric Sequence**  
A geometric sequence (or geometric progression) is a sequence where each term is obtained by 
multiplying the previous term by a constant ratio, denoted as \( r \). It has the general form:  


\[
a, ar, ar^2, ar^3, \dots
\]

where:  
- \( a \) is the first term.  
- \( r \) is the common ratio.  

#### **2. When Does a Geometric Sequence Converge?**  
A sequence **converges** if it approaches a finite limit as \( n \to \infty \). The behavior of a geometric sequence depends on the common ratio \( r \):  

1. **If \( |r| < 1 \), the sequence converges**  
   - As \( n \to \infty \), the terms \( ar^n \) approach **zero** because multiplying by a small number repeatedly makes the terms shrink.
   - Example: \( 2, 1, 0.5, 0.25, 0.125, \dots \) with \( r = \frac{1}{2} \) converges to 0.

2. **If \( |r| \geq 1 \), the sequence diverges**  
   - When \( r > 1 \), the terms grow indefinitely (\( \to \infty \)).
   - When \( r < -1 \), the terms oscillate between large positive and negative values (does not settle to a single limit).
   - Example: \( 2, 4, 8, 16, 32, \dots \) with \( r = 2 \) diverges to \( \infty \).

#### **3. Limit of a Geometric Sequence**  
For a geometric sequence with common ratio \( |r| < 1 \), the limit of the general term as \( n \to \infty \) is:

\[
\lim_{n \to \infty} ar^n = 0
\]

Thus, all geometric sequences with \( |r| < 1 \) converge to **zero**.

#### **4. Example Problems**
**Example 1:** Does the geometric sequence \( 5, 2.5, 1.25, 0.625, \dots \) converge?  
- \( a = 5 \), \( r = \frac{1}{2} \), and \( |r| < 1 \).  
- Since the ratio is less than 1, the sequence **converges** to 0.

**Example 2:** Does the sequence \( 3, 6, 12, 24, \dots \) converge?  
- \( a = 3 \), \( r = 2 \), and \( |r| > 1 \).  
- The sequence grows infinitely large, so it **diverges**.

#### **5. Key Takeaways**  
- If \( |r| < 1 \), the sequence **converges** to 0.  
- If \( |r| \geq 1 \), the sequence **diverges**.  
- Geometric sequences play an essential role in series, finance (compound interest), and signal processing.  






## **Sum of a Finite Geometric Series Given in Sigma Notation**

#### **1. Understanding the Sigma Notation for a Geometric Series**
A **geometric series** is a sum of terms in a geometric sequence, where each term is obtained by 
multiplying the previous term by a constant ratio \( r \). A **finite geometric series** has a 
limited number of terms.

The general form of a **finite geometric series** using **sigma notation** is:

\[
\sum_{k=m}^{n} a r^k
\]

where:
- \( a \) is the **first term** of the series,
- \( r \) is the **common ratio**,
- \( k \) is the **index of summation**, running from \( m \) to \( n \).

#### **2. Formula for the Sum of a Finite Geometric Series**
The sum of the first \( N \) terms of a geometric series is given by:

\[
S_N = a \frac{1 - r^N}{1 - r}, \quad \text{for } r \neq 1
\]

where:
- \( S_N \) is the sum of the first \( N \) terms,
- \( a \) is the first term,
- \( r \) is the common ratio,
- \( N \) is the number of terms in the series.

If the index \( k \) starts at \( m \) instead of \( 0 \), then the formula adapts as:

\[
S = a r^m \frac{1 - r^{(n-m+1)}}{1 - r}, \quad \text{for } r \neq 1
\]

#### **3. Example Calculations**
##### **Example 1: Basic Finite Geometric Series**
Evaluate:

\[
\sum_{k=0}^{4} 3(2)^k
\]

**Solution:**
- \( a = 3 \),  
- \( r = 2 \),  
- Number of terms: \( N = 4 - 0 + 1 = 5 \).

Using the sum formula:

\[
S_5 = 3 \frac{1 - 2^5}{1 - 2}
\]

\[
= 3 \frac{1 - 32}{1 - 2} = 3 \times \frac{-31}{-1} = 3 \times 31 = 93
\]

Thus, the sum is **93**.

##### **Example 2: Geometric Series with a Different Starting Index**
Evaluate:

\[
\sum_{k=2}^{5} 4(3)^k
\]

**Solution:**
- \( a = 4 \),  
- \( r = 3 \),  
- Number of terms: \( N = 5 - 2 + 1 = 4 \).

Using the adapted sum formula:

\[
S = 4(3^2) \frac{1 - 3^4}{1 - 3}
\]

\[
= 4(9) \times \frac{1 - 81}{1 - 3}
\]

\[
= 36 \times \frac{-80}{-2} = 36 \times 40 = 1440
\]

Thus, the sum is **1440**.

#### **4. Special Cases**
1. **If \( r = 1 \):**  
   The series becomes arithmetic because each term is the same. The sum simplifies to:

   \[
   S_N = aN
   \]

2. **Negative or Fractional \( r \):**  
   The same formula applies, but terms alternate signs (for negative \( r \)) or decrease in magnitude (for \( 0 < r < 1 \)).

#### **5. Conclusion**
- **Identify** the first term \( a \), common ratio \( r \), and number of terms \( N \).
- **Apply** the geometric sum formula accordingly.
- **Adjust** for different starting indices in sigma notation.

This method efficiently evaluates finite geometric series without manually summing each term.





## **Euler's Formula**

#### **1. Introduction to Euler’s Formula**
Euler’s formula is one of the most profound and beautiful equations in mathematics, linking complex numbers, 
trigonometry, and exponentials. It is given by:

\[
e^{ix} = \cos x + i \sin x
\]

where:
- \( e \) is the base of the natural logarithm,
- \( i \) is the imaginary unit (\( i^2 = -1 \)),
- \( x \) is a real number (usually representing an angle in radians),
- \( \cos x \) and \( \sin x \) are the trigonometric functions.

This formula establishes a deep connection between exponential functions and trigonometry.

---

#### **2. Derivation of Euler’s Formula**
Euler’s formula can be derived using the Maclaurin series expansions of \( e^x \), \( \cos x \), and \( \sin x \).

##### **Step 1: Maclaurin Series Expansions**
The Taylor series expansions for these functions are:

1. **Exponential function:**
   \[
   e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + \dots
   \]

2. **Sine function:**
   \[
   \sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots
   \]

3. **Cosine function:**
   \[
   \cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots
   \]

##### **Step 2: Substituting \( x = ix \) in \( e^x \)**
If we replace \( x \) with \( ix \) in the Maclaurin series for \( e^x \), we get:

\[
e^{ix} = 1 + ix + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!} + \frac{(ix)^5}{5!} + \dots
\]

Expanding the powers of \( i \):

\[
e^{ix} = 1 + ix - \frac{x^2}{2!} - i \frac{x^3}{3!} + \frac{x^4}{4!} + i \frac{x^5}{5!} - \dots
\]

Rearranging real and imaginary terms:

\[
e^{ix} = \left( 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots \right) + i \left( x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots \right)
\]

Recognizing these as the series for cosine and sine:

\[
e^{ix} = \cos x + i \sin x
\]

Thus, we have derived Euler’s formula.

---

#### **3. Special Cases of Euler’s Formula**
##### **Case 1: Euler’s Identity**
Setting \( x = \pi \) in Euler’s formula:

\[
e^{i\pi} = \cos \pi + i \sin \pi
\]

Since \( \cos \pi = -1 \) and \( \sin \pi = 0 \), this simplifies to:

\[
e^{i\pi} + 1 = 0
\]

This is known as **Euler’s identity**, often considered one of the most beautiful equations in mathematics as it relates five fundamental constants: \( e, i, \pi, 1, \) and \( 0 \).

##### **Case 2: Relation to the Unit Circle**
For any real number \( x \), Euler’s formula states:

\[
e^{ix} = \cos x + i \sin x
\]

This describes a point on the **unit circle** in the complex plane, where \( \cos x \) is the real part and \( \sin x \) is the imaginary part.

---

#### **4. Applications of Euler’s Formula**
##### **1. Complex Number Representation**
Euler’s formula provides a way to express complex numbers in **polar form**:

\[
z = r e^{i\theta}
\]

where:
- \( r = |z| \) is the magnitude (modulus) of \( z \),
- \( \theta = \arg(z) \) is the argument (angle) of \( z \).

##### **2. De Moivre’s Theorem**
Euler’s formula leads to **De Moivre’s Theorem**:

\[
(\cos x + i \sin x)^n = e^{inx} = \cos(nx) + i \sin(nx)
\]

This is useful in **computing powers and roots of complex numbers**.

##### **3. Fourier Analysis**
Euler’s formula is fundamental in Fourier analysis, where signals are represented as sums of exponential functions:

\[
f(t) = \sum c_n e^{i n t}
\]

This is widely used in **signal processing, quantum mechanics, and engineering**.

##### **4. Differential Equations**
Many differential equations, especially in **physics and engineering**, have solutions involving exponentials of imaginary numbers, which can be rewritten using Euler’s formula.

---

#### **5. Conclusion**
- **Euler’s formula** bridges complex numbers, trigonometry, and exponentials.
- **It is derived** using the Taylor series expansions of \( e^x, \sin x, \) and \( \cos x \).
- **Euler’s identity** \( e^{i\pi} + 1 = 0 \) is a special case.
- **The formula is crucial** in complex number operations, Fourier analysis, and engineering applications.

This equation stands as one of the most elegant and fundamental relationships in mathematics.







# **Infinite Series and Partial Sums**  

#### **1. Introduction to Infinite Series**  
An **infinite series** is the sum of infinitely many terms of a sequence:

\[
S = a_1 + a_2 + a_3 + \dots = \sum_{n=1}^{\infty} a_n
\]

where \( a_n \) represents the terms of the sequence. The sum of the first \( N \) terms is called the **partial sum**.

---

#### **2. Partial Sums and Convergence**  
The **\( N \)th partial sum** of an infinite series is:

\[
S_N = \sum_{n=1}^{N} a_n = a_1 + a_2 + \dots + a_N
\]

To determine whether an infinite series **converges** or **diverges**, we examine the limit:

\[
\lim_{N \to \infty} S_N = S
\]

- If \( S_N \) approaches a finite value \( S \), the series **converges**.
- If \( S_N \) grows without bound or oscillates indefinitely, the series **diverges**.

---

#### **3. Common Types of Infinite Series**  

##### **1. Geometric Series**
A geometric series has the form:

\[
\sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ar^3 + \dots
\]

where \( a \) is the first term and \( r \) is the common ratio.  
- The sum of the first \( N \) terms (partial sum) is:

  \[
  S_N = a \frac{1 - r^N}{1 - r}, \quad r \neq 1
  \]

- The **infinite sum** (if \( |r| < 1 \)) is:

  \[
  S = \frac{a}{1 - r}, \quad \text{for } |r| < 1
  \]

- If \( |r| \geq 1 \), the series **diverges**.

##### **2. Harmonic Series**
The harmonic series is:

\[
\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots
\]

Although the terms decrease, the series **diverges** to infinity.

##### **3. p-Series**
A **p-series** is of the form:

\[
\sum_{n=1}^{\infty} \frac{1}{n^p}
\]

- It **converges** if \( p > 1 \).
- It **diverges** if \( p \leq 1 \).

##### **4. Alternating Series**
An alternating series has terms that switch signs, such as:

\[
\sum_{n=1}^{\infty} (-1)^n a_n
\]

A special case is the **alternating harmonic series**:

\[
\sum_{n=1}^{\infty} \frac{(-1)^n}{n}
\]

which **converges** conditionally.

---

#### **4. Tests for Convergence**  
To determine if a series converges, several tests are used:

1. **Divergence Test**: If \( \lim_{n \to \infty} a_n \neq 0 \), then \( \sum a_n \) **diverges**.
2. **Geometric Series Test**: Converges if \( |r| < 1 \).
3. **p-Series Test**: Converges if \( p > 1 \).
4. **Integral Test**: If \( f(x) \) is decreasing and positive, then:

   \[
   \sum a_n \text{ and } \int f(x)dx \text{ have the same behavior}
   \]

5. **Comparison Test**: If \( 0 \leq a_n \leq b_n \) and \( \sum b_n \) converges, then \( \sum a_n \) converges.
6. **Limit Comparison Test**: If \( \lim_{n\to\infty} \frac{a_n}{b_n} = C \) (a finite, positive constant), and \( \sum b_n \) converges, then \( \sum a_n \) converges.
7. **Alternating Series Test**: If the sequence decreases and its limit is zero, then the alternating series **converges**.
8. **Ratio Test**: If \( \lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| < 1 \), the series converges absolutely.
9. **Root Test**: If \( \lim_{n\to\infty} \sqrt[n]{|a_n|} < 1 \), the series converges absolutely.

---

#### **5. Absolute vs. Conditional Convergence**  
- A series **converges absolutely** if \( \sum |a_n| \) converges.
- If \( \sum |a_n| \) diverges but \( \sum a_n \) converges, it **converges conditionally**.

---

#### **6. Applications of Infinite Series**  
- **Taylor and Maclaurin Series** approximate functions using infinite series.
- **Fourier Series** represents periodic functions.
- **Physics and Engineering** use series in wave analysis and quantum mechanics.
- **Computer Science** relies on series for numerical approximations.

---

### **Conclusion**
Infinite series play a crucial role in mathematics and applications. Understanding **partial sums**, 
**convergence tests**, and **special series types** helps determine whether a series has a finite sum or diverges.






## **Upward and Downward Opening Parabolas**  

#### **1. Introduction to Parabolas**  
A **parabola** is a U-shaped curve that represents a quadratic function. It is defined by the equation:

\[
y = ax^2 + bx + c
\]

where:  
- \( a \) determines the **direction** and **width** of the parabola.
- \( b \) controls the **horizontal shift**.
- \( c \) represents the **y-intercept**.

The **vertex** of the parabola is its highest or lowest point, depending on whether it opens **upward** or **downward**.

---

#### **2. Direction of Opening**  
The direction of a parabola is determined by the **sign of the leading coefficient** \( a \):  

- If \( a > 0 \), the parabola **opens upward** (like a U).  
- If \( a < 0 \), the parabola **opens downward** (like an inverted U).  

🔹 **Example 1: Upward Opening Parabola**  
\[
y = 2x^2 - 4x + 1
\]
Since \( a = 2 > 0 \), the parabola opens **upward**.

🔹 **Example 2: Downward Opening Parabola**  
\[
y = -3x^2 + 6x - 2
\]
Since \( a = -3 < 0 \), the parabola opens **downward**.

---

#### **3. Key Features of a Parabola**  
##### **(a) Vertex**  
The **vertex** is the turning point of the parabola, given by:

\[
x = \frac{-b}{2a}
\]

Substituting \( x \) into the equation finds \( y \), giving the vertex \( (h, k) \).

##### **(b) Axis of Symmetry**  
A vertical line that passes through the vertex:

\[
x = \frac{-b}{2a}
\]

##### **(c) Y-Intercept**  
Occurs where \( x = 0 \):

\[
y = c
\]

##### **(d) X-Intercepts (Roots/Zeros)**  
Solve \( ax^2 + bx + c = 0 \) using:
- **Factoring** (if possible)
- **Quadratic formula**:

  \[
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
  \]

---

#### **4. Graphing a Parabola**
1. **Find the vertex** \( (h, k) \).
2. **Draw the axis of symmetry** \( x = h \).
3. **Find the y-intercept** \( (0, c) \).
4. **Find x-intercepts**, if they exist.
5. **Plot additional points** for accuracy.
6. **Sketch the curve**, ensuring symmetry.

---

#### **5. Applications of Parabolas**
- **Physics**: Projectile motion follows a parabolic trajectory.
- **Engineering**: Parabolic reflectors in antennas and headlights.
- **Economics**: Quadratic cost and revenue functions.

---

### **Conclusion**
Upward-opening parabolas occur when \( a > 0 \), while downward-opening parabolas occur when \( a < 0 \). 
The vertex, axis of symmetry, and intercepts provide key insights into their behavior and graphing.







## **Expressing Rational Functions with Irreducible Quadratic Factors as Sums of Partial Fractions**  

#### **1. Introduction to Partial Fractions**  
Partial fraction decomposition is a technique used to break down a **rational function** 
(a fraction where both the numerator and denominator are polynomials) into simpler fractions 
that are easier to integrate or manipulate.  

For a rational function of the form:  

\[
\frac{P(x)}{Q(x)}
\]

where **\( P(x) \)** is the numerator and **\( Q(x) \)** is the denominator, we express it as a sum of simpler fractions.

---

#### **2. Types of Factors in the Denominator**  
Before decomposing, analyze \( Q(x) \), which can contain:  
1. **Linear factors** (e.g., \( (x - a) \))  
2. **Irreducible quadratic factors** (e.g., \( x^2 + bx + c \), which cannot be factored further over real numbers)  

This discussion focuses on rational functions with **irreducible quadratic factors**.

---

#### **3. Decomposition When the Denominator Contains Irreducible Quadratic Factors**  
If \( Q(x) \) has irreducible quadratic factors, each quadratic term contributes a fraction of the form:

\[
\frac{Ax + B}{ax^2 + bx + c}
\]

where:  
- \( A \) and \( B \) are **unknown coefficients** to be determined.  
- \( ax^2 + bx + c \) is an **irreducible quadratic factor** in the denominator.  

---

#### **4. Step-by-Step Decomposition**  
##### **Step 1: Factor the Denominator**  
Ensure that \( Q(x) \) is completely factored into linear and irreducible quadratic terms.  

##### **Step 2: Set Up Partial Fractions**  
For each **irreducible quadratic factor** \( ax^2 + bx + c \), include a fraction:

\[
\frac{Ax + B}{ax^2 + bx + c}
\]

For any **linear factor** \( (x - d) \), include a fraction:

\[
\frac{C}{x - d}
\]

##### **Step 3: Multiply Both Sides by the Denominator**  
Multiply both sides by the **least common denominator (LCD)** to eliminate fractions.

##### **Step 4: Expand and Collect Like Terms**  
Expand both sides and group terms based on powers of \( x \).

##### **Step 5: Solve for Coefficients**  
Solve for \( A, B, C, \) etc., using:
- **Coefficient comparison**: Match coefficients of corresponding powers of \( x \).
- **Substituting values**: Choose values of \( x \) to simplify calculations.

---

#### **5. Example: Decomposing a Rational Function**  
**Problem:**  
Decompose the function:

\[
\frac{x^3 + 2x^2 + 3}{(x-1)(x^2 + x + 1)}
\]

##### **Step 1: Factor the Denominator**  
The denominator is already factored into a **linear factor** \( (x - 1) \) and an **irreducible quadratic factor** \( (x^2 + x + 1) \).

##### **Step 2: Set Up Partial Fractions**  
Since \( x - 1 \) is a linear factor, assign:

\[
\frac{A}{x - 1}
\]

Since \( x^2 + x + 1 \) is an irreducible quadratic factor, assign:

\[
\frac{Bx + C}{x^2 + x + 1}
\]

Thus, the equation is:

\[
\frac{x^3 + 2x^2 + 3}{(x-1)(x^2 + x + 1)} = \frac{A}{x - 1} + \frac{Bx + C}{x^2 + x + 1}
\]

##### **Step 3: Multiply by the LCD**  
Multiply both sides by \( (x - 1)(x^2 + x + 1) \) to clear fractions:

\[
x^3 + 2x^2 + 3 = A(x^2 + x + 1) + (Bx + C)(x - 1)
\]

##### **Step 4: Expand Both Sides**  
Expand both terms:

\[
x^3 + 2x^2 + 3 = A(x^2 + x + 1) + Bx^2 - Bx + Cx - C
\]

\[
= Ax^2 + Ax + A + Bx^2 - Bx + Cx - C
\]

\[
= (A + B)x^2 + (A - B + C)x + (A - C)
\]

##### **Step 5: Solve for Coefficients**  
Comparing coefficients with \( x^3 + 2x^2 + 3 \):

- **\( x^3 \) term:** No \( x^3 \) on the right side, so **\( A + B = 1 \)**.  
- **\( x^2 \) term:** \( A + B = 1 \) and must match \( 2x^2 \), so **\( A + B = 2 \)**.  
- **\( x \) term:** \( A - B + C = 0 \).  
- **Constant term:** \( A - C = 3 \).

Solving:

1. \( A + B = 2 \)  
2. \( A - B + C = 0 \)  
3. \( A - C = 3 \)  

From equation (3):  
\[
C = A - 3
\]

Substituting into equation (2):  
\[
A - B + (A - 3) = 0
\]
\[
2A - B - 3 = 0
\]
\[
2A - B = 3
\]

Now solving the system:

- \( A + B = 2 \)
- \( 2A - B = 3 \)

Adding both equations:

\[
3A = 5 \Rightarrow A = \frac{5}{3}
\]

Substituting into \( A + B = 2 \):

\[
\frac{5}{3} + B = 2
\]

\[
B = 2 - \frac{5}{3} = \frac{6}{3} - \frac{5}{3} = \frac{1}{3}
\]

Using \( C = A - 3 \):

\[
C = \frac{5}{3} - 3 = \frac{5}{3} - \frac{9}{3} = -\frac{4}{3}
\]

##### **Step 6: Final Decomposition**  
\[
\frac{x^3 + 2x^2 + 3}{(x-1)(x^2 + x + 1)} = \frac{5/3}{x-1} + \frac{(1/3)x - 4/3}{x^2 + x + 1}
\]

---

### **6. Applications of Partial Fractions**
- **Integration**: Decomposing fractions into simpler terms makes them easier to integrate.
- **Laplace Transforms**: Used in engineering and physics to analyze systems.
- **Algebraic Manipulation**: Simplifies complex expressions.

---

### **Conclusion**
When dealing with irreducible quadratic factors, each factor contributes a **linear numerator** in the 
partial fraction decomposition. By setting up the equation, clearing fractions, and solving for unknowns, 
the rational function is rewritten as a sum of simpler fractions.






## **Writing an Infinite Geometric Series in Sigma Notation**  

#### **1. Introduction to Geometric Series**  
A **geometric series** is a sum of terms where each term is obtained by multiplying the previous 
term by a constant ratio \( r \). It takes the general form:

\[
S = a + ar + ar^2 + ar^3 + \dots
\]

where:  
- \( a \) is the **first term**,  
- \( r \) is the **common ratio**,  
- The series continues indefinitely for an **infinite geometric series**.

---

#### **2. Sigma Notation for Infinite Geometric Series**  
The **sigma notation** (\( \sum \)) is a compact way to represent sums. The general form of an infinite geometric series in sigma notation is:

\[
\sum_{n=0}^{\infty} ar^n
\]

where:  
- The **lower index** \( n=0 \) indicates that the summation starts at \( n=0 \).  
- The **upper index** \( \infty \) represents an infinite number of terms.  
- \( ar^n \) is the general term of the series.  

**Example:**  

The infinite geometric series  

\[
3 + 6 + 12 + 24 + 48 + \dots
\]

has:  
- First term: \( a = 3 \)  
- Common ratio: \( r = 2 \)  

It can be written in sigma notation as:

\[
\sum_{n=0}^{\infty} 3(2)^n
\]

---

#### **3. Convergence of an Infinite Geometric Series**  
An **infinite geometric series** **converges** if \( |r| < 1 \) and **diverges** if \( |r| \geq 1 \).  

When \( |r| < 1 \), the sum of the infinite geometric series is given by:

\[
S = \frac{a}{1 - r}
\]

where:  
- \( a \) is the first term,  
- \( r \) is the common ratio, with \( |r| < 1 \).  

**Example:**  

The infinite geometric series:

\[
5 + 2.5 + 1.25 + 0.625 + \dots
\]

has:  
- First term: \( a = 5 \)  
- Common ratio: \( r = 0.5 \)  

Sigma notation:

\[
\sum_{n=0}^{\infty} 5(0.5)^n
\]

Sum of the series:

\[
S = \frac{5}{1 - 0.5} = \frac{5}{0.5} = 10
\]

---

### **4. Conclusion**  
An **infinite geometric series** in **sigma notation** is written as:

\[
\sum_{n=0}^{\infty} ar^n
\]

where \( a \) is the first term and \( r \) is the common ratio. The series converges 
when \( |r| < 1 \) and diverges otherwise.







## **Scalar Multiplication of Matrices**

#### **Definition**
Scalar multiplication of a matrix involves multiplying each element of the matrix by a single constant 
(called a scalar). If \( A \) is an \( m \times n \) matrix and \( k \) is a scalar, the result of 
multiplying \( k \) by \( A \) is another \( m \times n \) matrix where each element is the product 
of \( k \) and the corresponding element in \( A \).

Mathematically, if:

\[
A = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}
\]

then:

\[
kA = \begin{bmatrix} k a_{11} & k a_{12} & \dots & k a_{1n} \\ k a_{21} & k a_{22} & \dots & k a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ k a_{m1} & k a_{m2} & \dots & k a_{mn} \end{bmatrix}
\]

#### **Properties of Scalar Multiplication**
1. **Distributive Property Over Matrix Addition**  
   \[
   k(A + B) = kA + kB
   \]
   where \( A \) and \( B \) are matrices of the same size.

2. **Associative Property of Scalars**  
   \[
   (k_1 k_2) A = k_1 (k_2 A)
   \]
   where \( k_1, k_2 \) are scalars.

3. **Identity Property**  
   \[
   1 \cdot A = A
   \]
   Multiplying a matrix by 1 leaves it unchanged.

4. **Zero Property**  
   \[
   0 \cdot A = 0
   \]
   Multiplying a matrix by 0 results in the zero matrix.

5. **Multiplication with Negative Scalars**  
   \[
   (-1)A = -A
   \]
   Multiplying a matrix by \(-1\) negates each element of the matrix.

#### **Example Calculation**
Given:

\[
A = \begin{bmatrix} 2 & -3 \\ 4 & 5 \end{bmatrix}
\]

Multiply by scalar \( k = 3 \):

\[
3A = \begin{bmatrix} 3(2) & 3(-3) \\ 3(4) & 3(5) \end{bmatrix} = \begin{bmatrix} 6 & -9 \\ 12 & 15 \end{bmatrix}
\]

#### **Applications**
- **Image Processing**: Adjusting brightness in grayscale images.
- **Economics & Finance**: Scaling financial models and market indices.
- **Physics & Engineering**: Transforming physical quantities in equations.

Scalar multiplication is fundamental in linear algebra and serves as a building block for more advanced 
operations like matrix-vector multiplication and transformations.





## **Addition and Scalar Multiplication of Cartesian Vectors in 3D**

#### **Definition of a 3D Cartesian Vector**
A **Cartesian vector** in three-dimensional space is represented as:

\[
\mathbf{v} = (v_x, v_y, v_z)
\]

where \( v_x, v_y, v_z \) are the components along the \( x \)-, \( y \)-, and \( z \)-axes, respectively. 
Vectors can be written in component form:

\[
\mathbf{v} = v_x \hat{i} + v_y \hat{j} + v_z \hat{k}
\]

where \( \hat{i}, \hat{j}, \hat{k} \) are unit vectors along the \( x \)-, \( y \)-, and \( z \)-axes.

---

## **1. Vector Addition in 3D**
### **Definition**
The sum of two vectors \( \mathbf{a} = (a_x, a_y, a_z) \) and \( \mathbf{b} = (b_x, b_y, b_z) \) is found by adding corresponding components:

\[
\mathbf{a} + \mathbf{b} = (a_x + b_x, a_y + b_y, a_z + b_z)
\]

or in unit vector notation:

\[
\mathbf{a} + \mathbf{b} = (a_x + b_x) \hat{i} + (a_y + b_y) \hat{j} + (a_z + b_z) \hat{k}
\]

### **Properties of Vector Addition**
1. **Commutative Property**:  
   \[
   \mathbf{a} + \mathbf{b} = \mathbf{b} + \mathbf{a}
   \]
2. **Associative Property**:  
   \[
   (\mathbf{a} + \mathbf{b}) + \mathbf{c} = \mathbf{a} + (\mathbf{b} + \mathbf{c})
   \]
3. **Identity Element**: The zero vector \( \mathbf{0} = (0,0,0) \) satisfies:
   \[
   \mathbf{a} + \mathbf{0} = \mathbf{a}
   \]
4. **Inverse Element**: The negative vector \( -\mathbf{a} = (-a_x, -a_y, -a_z) \) satisfies:
   \[
   \mathbf{a} + (-\mathbf{a}) = \mathbf{0}
   \]

### **Example**
Given:

\[
\mathbf{a} = (2, -1, 3), \quad \mathbf{b} = (4, 5, -2)
\]

Find \( \mathbf{a} + \mathbf{b} \):

\[
(2, -1, 3) + (4, 5, -2) = (2+4, -1+5, 3+(-2)) = (6, 4, 1)
\]

---

## **2. Scalar Multiplication of a Vector in 3D**
### **Definition**
Multiplying a vector \( \mathbf{a} = (a_x, a_y, a_z) \) by a scalar \( k \) scales each component:

\[
k \mathbf{a} = (k a_x, k a_y, k a_z)
\]

or in unit vector notation:

\[
k \mathbf{a} = (k a_x) \hat{i} + (k a_y) \hat{j} + (k a_z) \hat{k}
\]

### **Properties of Scalar Multiplication**
1. **Distributive Property Over Vector Addition**:  
   \[
   k (\mathbf{a} + \mathbf{b}) = k \mathbf{a} + k \mathbf{b}
   \]
2. **Distributive Property Over Scalar Addition**:  
   \[
   (k_1 + k_2) \mathbf{a} = k_1 \mathbf{a} + k_2 \mathbf{a}
   \]
3. **Associative Property**:  
   \[
   (k_1 k_2) \mathbf{a} = k_1 (k_2 \mathbf{a})
   \]
4. **Multiplication by 1**:  
   \[
   1 \mathbf{a} = \mathbf{a}
   \]
5. **Multiplication by 0**:  
   \[
   0 \mathbf{a} = \mathbf{0}
   \]

### **Example**
Given:

\[
\mathbf{a} = (3, -2, 5), \quad k = -2
\]

Find \( k\mathbf{a} \):

\[
-2(3, -2, 5) = (-6, 4, -10)
\]

---

## **Applications of Vector Addition and Scalar Multiplication**
- **Physics**: Force, velocity, and acceleration calculations.
- **Computer Graphics**: Transformations and animations.
- **Robotics**: Path planning and motion control.
- **Engineering**: Structural analysis and electromagnetism.

These operations form the foundation of vector algebra, which extends to more advanced topics 
like dot and cross products.





## **Finding the Sum of an Infinite Geometric Series**

---

### **1. Definition of an Infinite Geometric Series**
A **geometric series** is a sum of terms where each term is a constant multiple of the previous one. 
In general, a geometric series has the form:

\[
S = a + ar + ar^2 + ar^3 + \dots
\]

where:
- \( a \) is the **first term**,
- \( r \) is the **common ratio**, and
- The series continues indefinitely.

If \( |r| < 1 \), the series **converges** to a finite sum. Otherwise, the series **diverges** (sum approaches \( \infty \) or does not settle at a finite value).

---

### **2. Sum Formula for an Infinite Geometric Series**
When \( |r| < 1 \), the sum of an infinite geometric series is given by:

\[
S_{\infty} = \frac{a}{1 - r}
\]

This formula is derived from the finite sum formula of a geometric series:

\[
S_n = \frac{a(1 - r^n)}{1 - r}
\]

Taking the limit as \( n \to \infty \), if \( |r| < 1 \), then \( r^n \to 0 \), simplifying to:

\[
S_{\infty} = \frac{a}{1 - r}
\]

---

### **3. Conditions for Convergence**
- The series **converges** only if \( |r| < 1 \).
- If \( |r| \geq 1 \), the series **diverges** (sum approaches infinity or oscillates indefinitely).

---

### **4. Examples**
#### **Example 1: Finding the Sum of a Convergent Series**
Find the sum of the infinite geometric series:

\[
3 + 2.4 + 1.92 + 1.536 + \dots
\]

**Solution:**
- First term: \( a = 3 \)
- Common ratio: \( r = \frac{2.4}{3} = 0.8 \)
- Since \( |r| = 0.8 < 1 \), the series converges.

Using the formula:

\[
S_{\infty} = \frac{3}{1 - 0.8} = \frac{3}{0.2} = 15
\]

#### **Example 2: Identifying a Divergent Series**
Determine whether the series \( 5 + 10 + 20 + 40 + \dots \) converges.

**Solution:**
- First term: \( a = 5 \)
- Common ratio: \( r = \frac{10}{5} = 2 \)
- Since \( |r| = 2 > 1 \), the series **diverges**.

Thus, there is no finite sum.

---

### **5. Applications of Infinite Geometric Series**
1. **Finance**: Calculating the present value of perpetuities.
2. **Physics**: Modeling wave reflections and decay processes.
3. **Computer Science**: Algorithms involving recurrence relations.
4. **Engineering**: Signal processing and control systems.

Understanding infinite geometric series is fundamental in various fields, providing a powerful 
tool for modeling real-world scenarios.





## **The Transpose of a Matrix**
---

### **1. Definition of the Transpose**
The **transpose** of a matrix \( A \), denoted as \( A^T \), is obtained by flipping the matrix over 
its **main diagonal** (from top-left to bottom-right). This operation swaps the **rows** and **columns** 
of the matrix.

Formally, if \( A = [a_{ij}] \) is an \( m \times n \) matrix, its transpose \( A^T \) is an \( n \times m \) 
matrix where:

\[
(A^T)_{ij} = A_{ji}
\]

This means:
- The **first row** of \( A \) becomes the **first column** of \( A^T \).
- The **second row** of \( A \) becomes the **second column** of \( A^T \), and so on.

---

### **2. Example of Matrix Transposition**
#### **Example 1:**
Given the matrix:

\[
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\]

The transpose is:

\[
A^T =
\begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix}
\]

Here, the **rows of \( A \) became columns in \( A^T \)**.

---

### **3. Properties of the Transpose**
1. **Double Transposition**: \( (A^T)^T = A \)  
   - Taking the transpose twice returns the original matrix.

2. **Transpose of a Sum**: \( (A + B)^T = A^T + B^T \)  
   - The transpose of a sum is the sum of the transposes.

3. **Transpose of a Product**: \( (AB)^T = B^T A^T \)  
   - The transpose of a product reverses the order of multiplication.

4. **Transpose of a Scalar Multiple**: \( (\alpha A)^T = \alpha A^T \)  
   - A scalar factor remains unchanged.

5. **Symmetric Matrices**: A matrix is **symmetric** if \( A^T = A \).  

6. **Skew-Symmetric Matrices**: A matrix is **skew-symmetric** if \( A^T = -A \).

---

### **4. Special Cases**
#### **Square Matrices**
For a square matrix (same number of rows and columns), the transpose does not change the size of the matrix but can change its properties (e.g., making it symmetric).

#### **Column and Row Vectors**
- A **column vector** (size \( m \times 1 \)) transposes into a **row vector** (size \( 1 \times m \)).
- A **row vector** (size \( 1 \times n \)) transposes into a **column vector** (size \( n \times 1 \)).

Example:
\[
\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}^T =
\begin{bmatrix} 4 & 5 & 6 \end{bmatrix}
\]

---

### **5. Applications of Matrix Transposition**
- **Linear Algebra**: Used in vector spaces and transformations.
- **Machine Learning**: Essential in operations like covariance matrices and backpropagation.
- **Computer Graphics**: Used in transformations and projections.
- **Signal Processing**: Applied in Fourier transforms and filtering.

Understanding matrix transposition is fundamental for working with data structures, mathematical modeling,
and various computational applications.





## **Calculating the Dot Product Using Components**  

---

### **1. Definition of the Dot Product**  
The **dot product** (also called the **scalar product**) of two vectors \( \mathbf{a} \) and \( \mathbf{b} \) 
is a mathematical operation that results in a **scalar** (a single number). It is defined as:

\[
\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \|\mathbf{b}\| \cos \theta
\]

where:
- \( \|\mathbf{a}\| \) and \( \|\mathbf{b}\| \) are the magnitudes (lengths) of the vectors.
- \( \theta \) is the angle between the two vectors.
- \( \cos \theta \) determines how much one vector points in the direction of the other.

---

### **2. Dot Product Using Components**  
Given two vectors in **component form**:

\[
\mathbf{a} = (a_1, a_2, a_3)
\]
\[
\mathbf{b} = (b_1, b_2, b_3)
\]

the dot product is computed as:

\[
\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3
\]

For **2D vectors** \( \mathbf{a} = (a_1, a_2) \) and \( \mathbf{b} = (b_1, b_2) \), the formula simplifies to:

\[
\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2
\]

---

### **3. Example Calculations**
#### **Example 1: 2D Vectors**  
Let:

\[
\mathbf{a} = (3, -2), \quad \mathbf{b} = (4, 5)
\]

\[
\mathbf{a} \cdot \mathbf{b} = (3)(4) + (-2)(5) = 12 - 10 = 2
\]

#### **Example 2: 3D Vectors**  
Let:

\[
\mathbf{a} = (1, -3, 2), \quad \mathbf{b} = (4, 0, -2)
\]

\[
\mathbf{a} \cdot \mathbf{b} = (1)(4) + (-3)(0) + (2)(-2)
\]

\[
= 4 + 0 - 4 = 0
\]

Since the result is **zero**, the vectors are **orthogonal** (perpendicular to each other).

---

### **4. Properties of the Dot Product**  
1. **Commutativity**:  
   \[
   \mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}
   \]

2. **Distributive Property**:  
   \[
   \mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}
   \]

3. **Scalar Multiplication**:  
   \[
   (c\mathbf{a}) \cdot \mathbf{b} = c (\mathbf{a} \cdot \mathbf{b})
   \]

4. **Dot Product with Itself** (Magnitude Squared):  
   \[
   \mathbf{a} \cdot \mathbf{a} = \|\mathbf{a}\|^2
   \]

---

### **5. Application of the Dot Product**  
- **Checking Orthogonality**: If \( \mathbf{a} \cdot \mathbf{b} = 0 \), the vectors are perpendicular.
- **Projection of a Vector**:  
  The scalar projection of \( \mathbf{a} \) onto \( \mathbf{b} \) is:

  \[
  \text{proj}_{\mathbf{b}} \mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|}
  \]

- **Work Done by a Force**: If a force \( \mathbf{F} \) moves an object along displacement \( \mathbf{d} \), the work done is:

  \[
  W = \mathbf{F} \cdot \mathbf{d}
  \]

---

### **6. Summary**  
- The dot product results in a **scalar**.
- Computed as \( \mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 \).
- Useful for determining angles, projections, and physical applications like work and force.






## **Left and Right Opening Parabolas**
---

### **1. Introduction to Parabolas**  
A **parabola** is a U-shaped curve that is the graph of a **quadratic equation**. 
While the most common parabolas open **upward or downward**, some parabolas open **leftward or rightward** 
when the equation is in terms of \( x \) as a function of \( y \).

---

### **2. Standard Form of Left and Right Opening Parabolas**  
The general equation of a **horizontally oriented** parabola is:

\[
(x - h) = 4p(y - k)^2
\]

or equivalently,

\[
x = a(y - k)^2 + h
\]

where:
- \( (h, k) \) is the **vertex** of the parabola.
- \( p \) is the distance from the vertex to the **focus**.
- \( a = \frac{1}{4p} \) determines the **width** and **direction** of the parabola.
- The **axis of symmetry** is **horizontal** (parallel to the x-axis).

---

### **3. Determining the Direction of Opening**  
- If **\( a > 0 \) or \( p > 0 \)** → The parabola opens **rightward**.
- If **\( a < 0 \) or \( p < 0 \)** → The parabola opens **leftward**.

---

### **4. Focus, Directrix, and Latus Rectum**  
For the equation:

\[
(x - h) = 4p(y - k)^2
\]

- **Focus:** \( (h + p, k) \)
- **Directrix:** \( x = h - p \) (a vertical line)
- **Latus Rectum Length:** \( |4p| \) (the focal width)

---

### **5. Example Equations**  
#### **Example 1: Rightward Opening Parabola**  
\[
x = \frac{1}{2} (y - 3)^2 + 2
\]
- **Vertex:** \( (2, 3) \)
- **Focus:** \( (2 + \frac{1}{4 \times \frac{1}{2}}, 3) = (2.5, 3) \)
- **Directrix:** \( x = 2 - 0.5 = 1.5 \)

#### **Example 2: Leftward Opening Parabola**  
\[
x = -\frac{1}{4} (y + 1)^2 + 5
\]
- **Vertex:** \( (5, -1) \)
- **Focus:** \( (5 - \frac{1}{4 \times \frac{1}{4}}, -1) = (4, -1) \)
- **Directrix:** \( x = 5 + 1 = 6 \)

---

### **6. Key Properties of Left and Right Opening Parabolas**
| Feature | Right-Opening Parabola | Left-Opening Parabola |
|---------|----------------------|---------------------|
| Equation | \( x = a(y - k)^2 + h \) ( \( a > 0 \) ) | \( x = a(y - k)^2 + h \) ( \( a < 0 \) ) |
| Axis of Symmetry | \( y = k \) | \( y = k \) |
| Focus | \( (h + p, k) \) | \( (h - p, k) \) |
| Directrix | \( x = h - p \) | \( x = h + p \) |
| Direction | Opens right | Opens left |

---

### **7. Applications of Left and Right Opening Parabolas**  
- **Satellite Dishes & Antennas**: Parabolas that open sideways are used in some reflector designs.
- **Projectile Motion & Physics**: Sideways-opening parabolas model horizontal cross-sections of parabolic motion.
- **Lenses & Mirrors**: Optical instruments use these shapes for focusing light.

---

### **8. Summary**  
- Left and right opening parabolas are defined by equations in the form \( x = a(y - k)^2 + h \).
- The **sign of \( a \)** determines whether the parabola opens left or right.
- The **focus, directrix, and axis of symmetry** play crucial roles in their geometric properties.
- These parabolas are widely used in engineering, physics, and optics.






## **Zero, Square, Diagonal, and Identity Matrices**

---

### **1. Zero Matrix**  
A **zero matrix** (or **null matrix**) is a matrix in which **all elements are zero**. It is denoted as \( O \).  

#### **Example: Zero Matrices of Different Sizes**  
\[
O_{2 \times 2} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}, \quad O_{3 \times 3} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}
\]

#### **Properties of the Zero Matrix**  
- **Additive Identity**: For any matrix \( A \), \( A + O = A \).
- **Multiplicative Absorption**: For any matrix \( A \) (of compatible dimensions), \( A O = O A = O \).

---

### **2. Square Matrix**  
A **square matrix** has the same number of rows and columns, i.e., an \( n \times n \) matrix.

#### **Example: Square Matrices**  
\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 & 7 \\ 8 & 9 & 10 \\ 11 & 12 & 13 \end{bmatrix}
\]
Both \( A \) and \( B \) are square matrices (\( 2 \times 2 \) and \( 3 \times 3 \), respectively).

#### **Properties of Square Matrices**  
- Can have a **determinant**.
- Can be **invertible** if \(\det(A) \neq 0\).
- Can be **diagonalizable**.

---

### **3. Diagonal Matrix**  
A **diagonal matrix** is a square matrix where all **non-diagonal elements are zero**. That is, \( A_{ij} = 0 \) for all \( i \neq j \).

#### **Example: Diagonal Matrices**  
\[
D = \begin{bmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & -2 \end{bmatrix}
\]

#### **Properties of Diagonal Matrices**  
- **Multiplication Rule**: The product of two diagonal matrices is also diagonal.
- **Inverse**: If all diagonal entries are nonzero, the inverse exists and is given by:
  \[
  D^{-1} = \begin{bmatrix} \frac{1}{d_1} & 0 & 0 \\ 0 & \frac{1}{d_2} & 0 \\ 0 & 0 & \frac{1}{d_3} \end{bmatrix}
  \]
- **Eigenvalues**: The diagonal elements are the **eigenvalues** of the matrix.

---

### **4. Identity Matrix**  
An **identity matrix** (or **unit matrix**), denoted as \( I_n \), is a **diagonal matrix with all diagonal elements equal to 1**.

#### **Example: Identity Matrices**  
\[
I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad
I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\]

#### **Properties of the Identity Matrix**  
- **Multiplicative Identity**: For any square matrix \( A \),
  \[
  A I = I A = A
  \]
- **Inverse**: \( I^{-1} = I \).
- **Eigenvalues**: Always **1**.

---

### **5. Relationships Between These Matrices**  
| Type of Matrix | Definition | Key Property |
|--------------|------------|--------------|
| Zero Matrix \( O \) | All elements are zero | \( A + O = A \), \( A O = O A = O \) |
| Square Matrix | \( n \times n \) matrix | Can have a determinant and inverse |
| Diagonal Matrix | Only diagonal elements are nonzero | \( D_1 D_2 = D_3 \) (also diagonal) |
| Identity Matrix \( I \) | Diagonal matrix with 1s on the main diagonal | \( A I = I A = A \) |

---

### **6. Applications**  
- **Zero Matrix**: Used in **null transformations** and **linear algebra proofs**.
- **Square Matrices**: Found in **system of equations**, **eigenvalue problems**, and **graph theory**.
- **Diagonal Matrices**: Common in **simplifying matrix operations** and **eigenvalue decomposition**.
- **Identity Matrix**: Essential in **matrix inversion**, **linear algebra**, and **computer graphics**.

---

### **7. Summary**  
- **Zero matrices** contain only zeros.
- **Square matrices** have equal rows and columns.
- **Diagonal matrices** have nonzero entries only on the diagonal.
- **Identity matrices** are diagonal matrices where all diagonal entries are 1.

These matrix types form the **foundation** for more advanced concepts in **linear algebra**, **computer science**, 
and **engineering**.





## **Multiplying Square Matrices**  

---

### **1. Definition of Square Matrix Multiplication**  
The **product of two square matrices** \( A \) and \( B \), both of size \( n \times n \), 
results in another square matrix \( C = AB \) of size \( n \times n \).  

Each element of \( C \) is computed as:  
\[
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
\]
where:
- \( A_{ik} \) is the element from row \( i \), column \( k \) of \( A \).
- \( B_{kj} \) is the element from row \( k \), column \( j \) of \( B \).
- The sum runs over all values of \( k \), from \( 1 \) to \( n \).

---

### **2. Example of Square Matrix Multiplication**  
#### **Given:**
\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
B = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}
\]

#### **Step-by-Step Calculation:**
\[
C_{11} = (1 \times 2) + (2 \times 1) = 2 + 2 = 4
\]
\[
C_{12} = (1 \times 0) + (2 \times 3) = 0 + 6 = 6
\]
\[
C_{21} = (3 \times 2) + (4 \times 1) = 6 + 4 = 10
\]
\[
C_{22} = (3 \times 0) + (4 \times 3) = 0 + 12 = 12
\]

Thus, the product matrix is:
\[
C = AB = \begin{bmatrix} 4 & 6 \\ 10 & 12 \end{bmatrix}
\]

---

### **3. Properties of Square Matrix Multiplication**
1. **Associative Property**:  
   \[
   (AB)C = A(BC)
   \]
   Multiplication order within parentheses does not matter.

2. **Distributive Property**:  
   \[
   A(B + C) = AB + AC
   \]

3. **Not Commutative** (in general):  
   \[
   AB \neq BA
   \]
   Unlike numbers, matrix multiplication **depends on order**.

4. **Identity Matrix Property**:  
   \[
   AI = IA = A
   \]
   Where \( I \) is the identity matrix.

5. **Zero Matrix Property**:  
   \[
   AO = O
   \]
   Where \( O \) is the zero matrix.

6. **Inverse Property** (if \( A \) is invertible):  
   \[
   A A^{-1} = A^{-1} A = I
   \]

---

### **4. Special Cases**
#### **(a) Multiplying a Matrix by Itself (Squaring a Matrix)**
If \( A \) is a square matrix:
\[
A^2 = A \times A
\]
Example:
\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
\]
\[
A^2 = A \times A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
\]

Calculating:
\[
A^2 = \begin{bmatrix} (1 \times 1 + 2 \times 3) & (1 \times 2 + 2 \times 4) \\ (3 \times 1 + 4 \times 3) & (3 \times 2 + 4 \times 4) \end{bmatrix}
\]
\[
A^2 = \begin{bmatrix} 1 + 6 & 2 + 8 \\ 3 + 12 & 6 + 16 \end{bmatrix} = \begin{bmatrix} 7 & 10 \\ 15 & 22 \end{bmatrix}
\]

#### **(b) Power of a Matrix**
For integer exponent \( n \),  
\[
A^n = A \times A \times A \times \dots \times A \quad (n \text{ times})
\]

#### **(c) Diagonal Matrices Multiplication**
If \( D \) is a diagonal matrix:
\[
D = \begin{bmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{bmatrix}, \quad E = \begin{bmatrix} e_1 & 0 & 0 \\ 0 & e_2 & 0 \\ 0 & 0 & e_3 \end{bmatrix}
\]
Then:
\[
DE = \begin{bmatrix} d_1 e_1 & 0 & 0 \\ 0 & d_2 e_2 & 0 \\ 0 & 0 & d_3 e_3 \end{bmatrix}
\]
Each diagonal entry is simply multiplied.

---

### **5. Applications of Square Matrix Multiplication**
- **Transformations in Computer Graphics**: Rotation, scaling, and reflection matrices.
- **Solving Systems of Equations**: Using **matrix inverses** and **Gaussian elimination**.
- **Markov Chains**: State transitions in probability models.
- **Quantum Mechanics**: Operators in quantum state evolution.
- **Graph Theory**: Adjacency matrices representing connectivity.

---

### **6. Summary**
- Matrix multiplication follows **row-column multiplication** rules.
- It is **not commutative** but **associative** and **distributive**.
- **Diagonal matrices** multiply element-wise on the diagonal.
- **Identity matrix** acts as a **neutral element**.
- Square matrix multiplication is **fundamental** in transformations, systems of equations, and computational models.

This concept is crucial in **linear algebra, machine learning, physics, and engineering applications**.






## **Introduction to Linear Transformations**  

#### **1. What is a Linear Transformation?**  
A **linear transformation** is a function that maps vectors from one vector space to another while preserving vector addition and scalar multiplication. 
Mathematically, a function \( T: V \to W \) is a linear transformation if for all vectors \( \mathbf{u}, \mathbf{v} \) in \( V \) and all scalars \( c \),
it satisfies:

1. **Additivity**:  
   \[
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})
   \]
2. **Homogeneity (Scaling Property)**:  
   \[
   T(c \mathbf{v}) = c T(\mathbf{v})
   \]

These two conditions ensure that the transformation behaves consistently with the structure of a vector space.

---

#### **2. Matrix Representation of Linear Transformations**  
In finite-dimensional spaces, every linear transformation can be represented by a **matrix**. If \( T: \mathbb{R}^n \to \mathbb{R}^m \) is a linear transformation, there exists an \( m \times n \) matrix \( A \) such that for any vector \( \mathbf{x} \):

\[
T(\mathbf{x}) = A \mathbf{x}
\]

where:
- \( A \) is the **transformation matrix**.
- \( \mathbf{x} \) is an \( n \)-dimensional vector.
- \( T(\mathbf{x}) \) is the transformed \( m \)-dimensional vector.

---

#### **3. Examples of Linear Transformations**
##### **a) Scaling**
\[
T(x, y) = (2x, 2y)
\]
Matrix form:
\[
A = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}
\]

##### **b) Rotation by \( \theta \)**
\[
T(x, y) = (x \cos\theta - y \sin\theta, x \sin\theta + y \cos\theta)
\]
Matrix form:
\[
A = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
\]

##### **c) Reflection Across the x-axis**
\[
T(x, y) = (x, -y)
\]
Matrix form:
\[
A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
\]

##### **d) Shear Transformation**
\[
T(x, y) = (x + ky, y)
\]
Matrix form:
\[
A = \begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}
\]

---

#### **4. Properties of Linear Transformations**
1. **Preserve the origin**: \( T(0) = 0 \).
2. **Composition of linear transformations is linear**.
3. **Invertibility**: If \( A \) is an invertible matrix, then \( T \) has an inverse transformation \( T^{-1} \).

---

#### **5. Kernel and Range**
- **Kernel (Null Space):** The set of all vectors mapped to zero:
  \[
  \ker(T) = \{ \mathbf{x} \mid T(\mathbf{x}) = 0 \}
  \]
  Determines when \( T \) is **one-to-one**.
  
- **Range (Image):** The set of all possible outputs:
  \[
  \text{Im}(T) = \{ T(\mathbf{x}) \mid \mathbf{x} \in V \}
  \]
  Determines when \( T \) is **onto**.

By the **Rank-Nullity Theorem**:
\[
\dim(\ker(T)) + \dim(\text{Im}(T)) = \dim(V)
\]

---

#### **6. Applications of Linear Transformations**
- **Computer Graphics**: Rotations, scaling, and perspective transformations.
- **Data Science & PCA**: Dimensionality reduction using eigenvectors and eigenvalues.
- **Physics & Engineering**: Modeling transformations in mechanics and electromagnetism.

Understanding linear transformations is foundational for **linear algebra, computer vision, optimization, and deep learning**.





## **The Minors of a 3×3 Matrix**  

#### **1. Understanding Minors in a Matrix**  
The **minor** of an element in a matrix is the determinant of the smaller matrix that remains after removing the row and column containing that element. 
This is useful in calculating **cofactors**, **determinants**, and **matrix inverses**.

For a **\(3 \times 3\) matrix**:
\[
A =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
\]
the **minor** of an element \( a_{ij} \) is found by deleting the \( i \)th row and \( j \)th column and computing the determinant of the resulting \( 2 \times 2 \) matrix.

---

#### **2. Computing the Minors of a \(3 \times 3\) Matrix**  
Each element \( a_{ij} \) has a minor \( M_{ij} \), which is the determinant of the \( 2 \times 2 \) submatrix formed by removing the row and column of \( a_{ij} \).

##### **Example: Compute the Minors for a 3×3 Matrix**  
Given:
\[
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\]

The minor of each element is calculated as follows:

1. **Minor of \( a_{11} = 1 \):**  
   Remove the first row and first column:
   \[
   M_{11} = \begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} = (5 \times 9 - 6 \times 8) = (45 - 48) = -3
   \]

2. **Minor of \( a_{12} = 2 \):**  
   Remove the first row and second column:
   \[
   M_{12} = \begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} = (4 \times 9 - 6 \times 7) = (36 - 42) = -6
   \]

3. **Minor of \( a_{13} = 3 \):**  
   Remove the first row and third column:
   \[
   M_{13} = \begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix} = (4 \times 8 - 5 \times 7) = (32 - 35) = -3
   \]

4. **Minor of \( a_{21} = 4 \):**  
   Remove the second row and first column:
   \[
   M_{21} = \begin{vmatrix} 2 & 3 \\ 8 & 9 \end{vmatrix} = (2 \times 9 - 3 \times 8) = (18 - 24) = -6
   \]

5. **Minor of \( a_{22} = 5 \):**  
   Remove the second row and second column:
   \[
   M_{22} = \begin{vmatrix} 1 & 3 \\ 7 & 9 \end{vmatrix} = (1 \times 9 - 3 \times 7) = (9 - 21) = -12
   \]

6. **Minor of \( a_{23} = 6 \):**  
   Remove the second row and third column:
   \[
   M_{23} = \begin{vmatrix} 1 & 2 \\ 7 & 8 \end{vmatrix} = (1 \times 8 - 2 \times 7) = (8 - 14) = -6
   \]

7. **Minor of \( a_{31} = 7 \):**  
   Remove the third row and first column:
   \[
   M_{31} = \begin{vmatrix} 2 & 3 \\ 5 & 6 \end{vmatrix} = (2 \times 6 - 3 \times 5) = (12 - 15) = -3
   \]

8. **Minor of \( a_{32} = 8 \):**  
   Remove the third row and second column:
   \[
   M_{32} = \begin{vmatrix} 1 & 3 \\ 4 & 6 \end{vmatrix} = (1 \times 6 - 3 \times 4) = (6 - 12) = -6
   \]

9. **Minor of \( a_{33} = 9 \):**  
   Remove the third row and third column:
   \[
   M_{33} = \begin{vmatrix} 1 & 2 \\ 4 & 5 \end{vmatrix} = (1 \times 5 - 2 \times 4) = (5 - 8) = -3
   \]

---

#### **3. The Matrix of Minors**
\[
M =
\begin{bmatrix}
-3 & -6 & -3 \\
-6 & -12 & -6 \\
-3 & -6 & -3
\end{bmatrix}
\]

---

#### **4. Applications of Minors**
- **Cofactors**: Used in determinant expansion and inverse calculations.
- **Adjugate Matrix**: The cofactor matrix (transposed).
- **Inverse of a Matrix**: If \( A^{-1} \) exists, it is given by:
  \[
  A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
  \]
- **Solving Systems of Equations**: Minors contribute to Cramer's Rule.

Understanding minors is essential in **linear algebra, numerical analysis, and machine learning applications involving matrix operations**.






## **Introduction to the Inverse of a Matrix**  

#### **1. What is the Inverse of a Matrix?**  
The **inverse** of a square matrix \( A \) is another matrix, denoted as \( A^{-1} \), such that:  

\[
A A^{-1} = A^{-1} A = I
\]

where \( I \) is the **identity matrix**, which satisfies:  

\[
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \quad \text{(for a 2×2 matrix)}
\]

A matrix must be **square** (\( n \times n \)) and **non-singular** (\( \det(A) \neq 0 \)) for an inverse to exist.

---

#### **2. Conditions for a Matrix to Have an Inverse**  
A matrix \( A \) has an inverse if and only if:
- \( A \) is a **square matrix** (\( n \times n \)).
- \( A \) is **non-singular**, meaning \( \det(A) \neq 0 \).  

If \( \det(A) = 0 \), \( A \) is **singular** and has **no inverse**.

---

#### **3. Finding the Inverse of a 2×2 Matrix**  
For a **2×2 matrix**:

\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\]

its inverse is given by:

\[
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
\]

where \( \det(A) = ad - bc \) (the determinant of \( A \)).  

##### **Example**  
Given:

\[
A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}
\]

1. Compute the determinant:

   \[
   \det(A) = (4 \times 6) - (7 \times 2) = 24 - 14 = 10
   \]

2. Apply the formula:

   \[
   A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix}
   \]

3. Simplify:

   \[
   A^{-1} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}
   \]

---

#### **4. Finding the Inverse of a 3×3 Matrix Using the Adjugate Method**  
For a **3×3 matrix**:

\[
A = \begin{bmatrix} 
a_{11} & a_{12} & a_{13} \\ 
a_{21} & a_{22} & a_{23} \\ 
a_{31} & a_{32} & a_{33} 
\end{bmatrix}
\]

the inverse is:

\[
A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)
\]

where **adj(A)** is the adjugate matrix, obtained by:
1. Finding the **cofactor matrix**.
2. Taking the **transpose** of the cofactor matrix.

##### **Example**  
Given:

\[
A = \begin{bmatrix} 
2 & 3 & 1 \\ 
4 & 5 & 6 \\ 
7 & 8 & 9 
\end{bmatrix}
\]

1. Compute \( \det(A) \).
2. Compute the **cofactor matrix**.
3. Compute the **adjugate matrix** (transpose of cofactor matrix).
4. Compute \( A^{-1} \) by dividing each element of the adjugate matrix by \( \det(A) \).

---

#### **5. Properties of Matrix Inverses**
1. **Uniqueness**: If \( A \) has an inverse, it is unique.
2. **Inverse of a Product**:  
   \[
   (AB)^{-1} = B^{-1} A^{-1}
   \]
3. **Inverse of a Transpose**:  
   \[
   (A^T)^{-1} = (A^{-1})^T
   \]
4. **Inverse of an Inverse**:  
   \[
   (A^{-1})^{-1} = A
   \]
5. **Determinant Relationship**:  
   \[
   \det(A^{-1}) = \frac{1}{\det(A)}
   \]

---

#### **6. Applications of Matrix Inverses**
- **Solving Linear Systems**:  
  \[
  Ax = b \quad \Rightarrow \quad x = A^{-1} b
  \]
- **Computer Graphics**: Used for geometric transformations.
- **Cryptography**: Used in encoding and decoding messages.
- **Machine Learning**: Used in optimization algorithms.

---

Understanding matrix inversion is fundamental for **linear algebra, data science, computer vision, and numerical computing**.





## **The Determinant of a 3×3 Matrix**  

#### **1. What is the Determinant of a Matrix?**  
The determinant of a matrix is a scalar value that provides important properties of the matrix, such as whether it is invertible. 
The determinant of a **3×3 matrix** is found using **cofactor expansion** (Laplace expansion).  

For a **3×3 matrix**:

\[
A = \begin{bmatrix} 
a_{11} & a_{12} & a_{13} \\ 
a_{21} & a_{22} & a_{23} \\ 
a_{31} & a_{32} & a_{33} 
\end{bmatrix}
\]

the determinant, denoted as \( \det(A) \) or \( |A| \), is calculated as:

\[
\det(A) = a_{11} \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} 
- a_{12} \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} 
+ a_{13} \begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix} 
\]

Each **2×2 determinant** (inside \( \begin{vmatrix} \cdot \end{vmatrix} \)) is called a **minor**.

---

#### **2. Expanding Along the First Row**  
The determinant of the **3×3 matrix** is:

\[
\det(A) = a_{11} M_{11} - a_{12} M_{12} + a_{13} M_{13}
\]

where each **minor determinant** is computed as:

\[
M_{11} = \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} = (a_{22} a_{33} - a_{23} a_{32})
\]

\[
M_{12} = \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} = (a_{21} a_{33} - a_{23} a_{31})
\]

\[
M_{13} = \begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix} = (a_{21} a_{32} - a_{22} a_{31})
\]

Thus,

\[
\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
\]

---

#### **3. Example Calculation**
Consider:

\[
A = \begin{bmatrix} 
1 & 2 & 3 \\ 
4 & 5 & 6 \\ 
7 & 8 & 9 
\end{bmatrix}
\]

**Step 1: Compute the 2×2 Minors**  

\[
M_{11} = \begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} = (5 \times 9 - 6 \times 8) = 45 - 48 = -3
\]

\[
M_{12} = \begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} = (4 \times 9 - 6 \times 7) = 36 - 42 = -6
\]

\[
M_{13} = \begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix} = (4 \times 8 - 5 \times 7) = 32 - 35 = -3
\]

**Step 2: Compute the Determinant**  

\[
\det(A) = 1(-3) - 2(-6) + 3(-3)
\]

\[
= -3 + 12 - 9 = 0
\]

Since \( \det(A) = 0 \), this matrix is **singular**, meaning it has no inverse.

---

#### **4. Properties of a 3×3 Determinant**
1. **Row Operations Affect the Determinant**:  
   - Swapping two rows **negates** the determinant.
   - Multiplying a row by a scalar **multiplies** the determinant by that scalar.
   - Adding a multiple of one row to another **does not** change the determinant.

2. **If Any Row or Column is All Zeros**, then \( \det(A) = 0 \).

3. **If Two Rows (or Columns) are Identical**, then \( \det(A) = 0 \).

4. **Multiplicative Property**:  
   If \( A \) and \( B \) are both \( 3 \times 3 \) matrices:

   \[
   \det(A B) = \det(A) \cdot \det(B)
   \]

5. **Inverse and Determinant**:  
   If \( A \) is invertible, then:

   \[
   \det(A^{-1}) = \frac{1}{\det(A)}
   \]

---

#### **5. Applications of the Determinant**
- **Checking for Invertibility**: If \( \det(A) \neq 0 \), \( A \) has an inverse.
- **Solving Linear Systems**: Used in **Cramer's Rule**.
- **Finding Volume of a Parallelepiped**: The determinant represents the **signed volume** of a parallelepiped formed by three vectors.
- **Computer Graphics and Physics**: Used for transformations and cross-products.

---

### **Conclusion**
The determinant of a **3×3 matrix** provides critical insights into the properties of a matrix, including whether 
it is **invertible** or **singular**. The **cofactor expansion method** is a fundamental way to compute it, 
and understanding its properties is essential in **linear algebra, engineering, and applied mathematics**.





## **The Vertex of a Parabola**  

#### **1. Understanding the Vertex of a Parabola**  
A **parabola** is a U-shaped curve defined by a quadratic equation. The **vertex** of a parabola 
is its highest or lowest point, depending on its orientation. It represents the **turning point**
and plays a key role in understanding the parabola's geometry.  

The general forms of a quadratic equation are:  

1. **Standard Form:**  
   \[
   y = ax^2 + bx + c
   \]
   The vertex is given by:
   \[
   x = -\frac{b}{2a}
   \]
   Once \( x \) is found, substitute it into the equation to find \( y \).

2. **Vertex Form:**  
   \[
   y = a(x - h)^2 + k
   \]
   The vertex is simply **\( (h, k) \)**.

---

#### **2. Finding the Vertex in Standard Form**  
For the quadratic equation:
\[
y = ax^2 + bx + c
\]

The **x-coordinate** of the vertex is:

\[
x = -\frac{b}{2a}
\]

To find the **y-coordinate**, substitute \( x \) back into the equation:

\[
y = a\left(-\frac{b}{2a}\right)^2 + b\left(-\frac{b}{2a}\right) + c
\]

Thus, the vertex is:

\[
\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)
\]

##### **Example 1: Finding the Vertex from Standard Form**
Find the vertex of:

\[
y = 2x^2 - 4x + 1
\]

1. **Compute \( x \)-coordinate:**
   \[
   x = -\frac{-4}{2(2)} = \frac{4}{4} = 1
   \]

2. **Substitute into the equation:**
   \[
   y = 2(1)^2 - 4(1) + 1 = 2 - 4 + 1 = -1
   \]

Thus, the **vertex is \( (1, -1) \)**.

---

#### **3. Finding the Vertex in Vertex Form**  
The **vertex form** of a parabola:

\[
y = a(x - h)^2 + k
\]

**Vertex:** \( (h, k) \)  

##### **Example 2: Finding the Vertex from Vertex Form**
Given:

\[
y = 3(x + 2)^2 - 5
\]

The vertex is \( (-2, -5) \).

---

#### **4. Orientation and Properties of the Vertex**
- If **\( a > 0 \)**, the parabola **opens upward**, and the vertex is the **minimum** point.
- If **\( a < 0 \)**, the parabola **opens downward**, and the vertex is the **maximum** point.

**Example Interpretation:**
- \( y = 2x^2 + 3x + 4 \) (since \( a > 0 \), vertex is a minimum)
- \( y = -5(x - 1)^2 + 3 \) (since \( a < 0 \), vertex is a maximum)

---

#### **5. Applications of the Vertex**
- **Optimization Problems**: Maximum or minimum values in physics, economics, and engineering.
- **Projectile Motion**: The vertex represents the **highest point** in projectile motion.
- **Computer Graphics**: Parabolas are used in animations and rendering.

---

### **Conclusion**
The **vertex of a parabola** is the most important point in its geometry, 
found using **\( x = -\frac{b}{2a} \)** in standard form or **directly from vertex form**.
It determines the direction, highest/lowest point, and practical applications in various fields.






## **Inverses of \(2 \times 2\) Matrices**  

#### **1. Understanding the Inverse of a Matrix**  
The inverse of a square matrix \( A \), denoted as \( A^{-1} \), is a matrix that satisfies:  

\[
A A^{-1} = A^{-1} A = I
\]

where \( I \) is the **identity matrix**:

\[
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\]

For a \( 2 \times 2 \) matrix:

\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\]

the inverse exists **only if** the determinant \( \det(A) \neq 0 \), where:

\[
\det(A) = ad - bc
\]

If \( \det(A) = 0 \), the matrix **does not have an inverse**.

---

#### **2. Formula for the Inverse of a \(2 \times 2\) Matrix**  
If \( \det(A) \neq 0 \), the inverse is given by:

\[
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
\]

This formula follows a simple pattern:
- **Swap** \( a \) and \( d \).
- **Negate** \( b \) and \( c \).
- **Divide by \( \det(A) \).**

---

#### **3. Example Calculation**  
Find the inverse of:

\[
A = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}
\]

1. **Compute the determinant**:

   \[
   \det(A) = (2)(4) - (3)(1) = 8 - 3 = 5
   \]

   Since \( \det(A) \neq 0 \), the inverse exists.

2. **Apply the inverse formula**:

   \[
   A^{-1} = \frac{1}{5} \begin{bmatrix} 4 & -3 \\ -1 & 2 \end{bmatrix}
   \]

3. **Result**:

   \[
   A^{-1} = \begin{bmatrix} \frac{4}{5} & -\frac{3}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{bmatrix}
   \]

---

#### **4. Properties of Inverses**
- \( (A^{-1})^{-1} = A \)  
- \( (AB)^{-1} = B^{-1} A^{-1} \)  
- \( (A^T)^{-1} = (A^{-1})^T \)  
- If \( \det(A) = 0 \), \( A \) is **singular** (non-invertible).

---

#### **5. Application of Matrix Inverses**
- **Solving Systems of Equations**: If \( AX = B \), then:

  \[
  X = A^{-1} B
  \]

- **Transformations in Computer Graphics**: Used in rotations, scaling, and reflections.
- **Control Systems & Physics**: State-space representations involve matrix inverses.

---

### **Conclusion**
The inverse of a \(2 \times 2\) matrix is computed using:

\[
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
\]

It exists only when \( \det(A) \neq 0 \). This concept is fundamental in linear algebra, 
computer science, and engineering applications.





## **Calculating Intercepts of Parabolas**  

A **parabola** is a quadratic function of the form:

\[
y = ax^2 + bx + c
\]

where \( a, b, c \) are constants. The intercepts of a parabola refer to **points where the curve crosses the x-axis and y-axis**.

---

### **1. Finding the Y-Intercept**
The **y-intercept** is the point where the parabola crosses the **y-axis**. This happens when \( x = 0 \).

#### **Formula for Y-Intercept:**
\[
y = c
\]

#### **Example:**
Given the quadratic function:

\[
y = 2x^2 - 3x + 5
\]

Substituting \( x = 0 \):

\[
y = 2(0)^2 - 3(0) + 5 = 5
\]

**Y-Intercept:** \( (0,5) \)

---

### **2. Finding the X-Intercept(s)**
The **x-intercepts** (also called **roots or zeros**) occur where the parabola crosses the **x-axis**, meaning \( y = 0 \).

#### **Equation for X-Intercepts:**
\[
ax^2 + bx + c = 0
\]

Solving this quadratic equation gives the x-intercepts.

#### **Methods to Find X-Intercepts:**
1. **Factoring** (if possible)
2. **Quadratic Formula** (if factoring is difficult)
3. **Completing the Square** (less common but useful)

#### **Using the Quadratic Formula:**
\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

- **If** \( b^2 - 4ac > 0 \), **two real solutions** → two x-intercepts.
- **If** \( b^2 - 4ac = 0 \), **one real solution** → one x-intercept (the vertex is on the x-axis).
- **If** \( b^2 - 4ac < 0 \), **no real solutions** → no x-intercepts (the parabola does not cross the x-axis).

---

### **3. Example Calculations**
#### **Example 1: Finding X-Intercepts**
Given:

\[
y = x^2 - 4x + 3
\]

Solve:

\[
x^2 - 4x + 3 = 0
\]

**Factoring:**
\[
(x - 3)(x - 1) = 0
\]

Setting each factor to zero:

\[
x - 3 = 0 \quad \text{or} \quad x - 1 = 0
\]

\[
x = 3, \quad x = 1
\]

**X-Intercepts:** \( (1,0) \) and \( (3,0) \)

---

#### **Example 2: Using the Quadratic Formula**
Given:

\[
y = 2x^2 - 4x + 1
\]

Solve:

\[
2x^2 - 4x + 1 = 0
\]

Using the quadratic formula:

\[
x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(2)(1)}}{2(2)}
\]

\[
x = \frac{4 \pm \sqrt{16 - 8}}{4}
\]

\[
x = \frac{4 \pm \sqrt{8}}{4}
\]

\[
x = \frac{4 \pm 2\sqrt{2}}{4} = \frac{2 \pm \sqrt{2}}{2}
\]

**X-Intercepts:** \( \left(\frac{2 + \sqrt{2}}{2}, 0\right) \) and \( \left(\frac{2 - \sqrt{2}}{2}, 0\right) \)

---

### **4. Summary**
- **Y-Intercept:** Found by setting \( x = 0 \).
- **X-Intercepts:** Found by solving \( ax^2 + bx + c = 0 \).
- **Quadratic Formula** is used when factoring is difficult.
- **Number of x-intercepts depends on the discriminant** (\( b^2 - 4ac \)).

Understanding intercepts is crucial in **graphing parabolas, physics (projectile motion), and 
engineering applications**.






## **Properties of Matrix Addition**  

Matrix addition is an essential operation in linear algebra that follows specific mathematical properties. 
Understanding these properties is fundamental when working with matrices in applications like machine learning, 
physics, and computer graphics.

---

### **1. Definition of Matrix Addition**
Matrix addition is performed by adding corresponding elements of two matrices of the **same dimensions**. 

For two matrices **A** and **B** of size \( m \times n \):

\[
A + B = \left[ a_{ij} \right] + \left[ b_{ij} \right] = \left[ a_{ij} + b_{ij} \right]
\]

Each element of the resulting matrix is obtained by:

\[
(A + B)_{ij} = A_{ij} + B_{ij}
\]

#### **Example:**
If

\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
\]

Then:

\[
A + B = \begin{bmatrix} 1+5 & 2+6 \\ 3+7 & 4+8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}
\]

---

### **2. Properties of Matrix Addition**
Matrix addition obeys the following properties:

#### **1. Commutative Property**
\[
A + B = B + A
\]
Matrix addition is **commutative**, meaning the order of addition does not affect the result.

**Example:**
\[
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} =
\begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}
\]

\[
\begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} + \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} =
\begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}
\]

Both orders produce the same matrix.

---

#### **2. Associative Property**
\[
(A + B) + C = A + (B + C)
\]
Matrix addition is **associative**, meaning the way matrices are grouped does not change the sum.

**Example:**
\[
\left( \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} \right) + \begin{bmatrix} 9 & 10 \\ 11 & 12 \end{bmatrix}
\]

First, compute \( A + B \):

\[
\begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix} + \begin{bmatrix} 9 & 10 \\ 11 & 12 \end{bmatrix} =
\begin{bmatrix} 15 & 18 \\ 21 & 24 \end{bmatrix}
\]

Now compute \( B + C \):

\[
\begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} + \begin{bmatrix} 9 & 10 \\ 11 & 12 \end{bmatrix} =
\begin{bmatrix} 14 & 16 \\ 18 & 20 \end{bmatrix}
\]

\[
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 14 & 16 \\ 18 & 20 \end{bmatrix} =
\begin{bmatrix} 15 & 18 \\ 21 & 24 \end{bmatrix}
\]

Both ways produce the same result.

---

#### **3. Existence of an Additive Identity (Zero Matrix)**
There exists a **zero matrix** \( O \), where:

\[
A + O = O + A = A
\]

For any matrix \( A \), adding a matrix of the same dimensions filled with zeros does not change \( A \).

**Example:**
\[
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} =
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
\]

---

#### **4. Existence of an Additive Inverse (Negative Matrix)**
For every matrix \( A \), there exists a matrix \( -A \) such that:

\[
A + (-A) = (-A) + A = O
\]

The negative matrix \( -A \) is obtained by multiplying each element of \( A \) by -1.

**Example:**
\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
-A = \begin{bmatrix} -1 & -2 \\ -3 & -4 \end{bmatrix}
\]

\[
A + (-A) = \begin{bmatrix} 1-1 & 2-2 \\ 3-3 & 4-4 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
\]

---

#### **5. Closure Property**
If \( A \) and \( B \) are matrices of the same size, their sum \( A + B \) is also a matrix of the same size.

For example, if \( A \) and \( B \) are both \( 2 \times 2 \) matrices, then \( A + B \) will also be a \( 2 \times 2 \) matrix.

---

### **3. Summary of Properties**
| Property | Equation | Description |
|-----------|------------|-------------|
| **Commutative** | \( A + B = B + A \) | Order does not matter. |
| **Associative** | \( (A + B) + C = A + (B + C) \) | Grouping does not matter. |
| **Additive Identity** | \( A + O = A \) | Adding a zero matrix leaves \( A \) unchanged. |
| **Additive Inverse** | \( A + (-A) = O \) | Every matrix has an opposite that sums to zero. |
| **Closure** | If \( A \) and \( B \) are \( m \times n \) matrices, then \( A + B \) is also \( m \times n \). | The sum remains within the set of matrices of the same dimension. |

---

### **4. Applications of Matrix Addition**
1. **Computer Graphics:** Adding transformation matrices to apply multiple effects.
2. **Machine Learning & Data Science:** Combining weight matrices in neural networks.
3. **Economics:** Summing matrices to analyze financial trends.
4. **Physics & Engineering:** Adding matrices in simulations and structural calculations.

Understanding these properties allows for efficient problem-solving in mathematics and its applications.






## **The Geometric Interpretation of the 2×2 Determinant**  

The determinant of a \(2 \times 2\) matrix provides a geometric interpretation related to **area, transformations, 
and orientation** in 2D space. Understanding how the determinant affects geometric shapes and transformations 
is fundamental in linear algebra, physics, and computer graphics.

---

### **1. The Determinant of a 2×2 Matrix**
For a \(2 \times 2\) matrix:

\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\]

The determinant is given by:

\[
\det(A) = ad - bc
\]

This scalar value has significant geometric meaning in terms of area scaling, transformations, and orientation.

---

### **2. Interpretation as Area Scaling**
The determinant represents the **signed area** of the parallelogram formed by the column vectors of the matrix.

#### **Case 1: Identity Matrix (\(A\) as a Basis)**
For the identity matrix:

\[
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\]

\[
\det(I) = (1)(1) - (0)(0) = 1
\]

The unit square remains unchanged.

#### **Case 2: General 2D Transformation**
If the column vectors of \( A \) are:

\[
\mathbf{v}_1 = \begin{bmatrix} a \\ c \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} b \\ d \end{bmatrix}
\]

Then the parallelogram formed by \( \mathbf{v}_1 \) and \( \mathbf{v}_2 \) has area:

\[
\text{Area} = |\det(A)|
\]

##### **Example**
Consider:

\[
A = \begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix}
\]

\[
\det(A) = (2)(4) - (1)(3) = 8 - 3 = 5
\]

The parallelogram spanned by the column vectors has an area of **5**.

---

### **3. Orientation and Signed Area**
The sign of the determinant indicates whether the transformation preserves or reverses orientation:

- **If \( \det(A) > 0 \):** The transformation **preserves** orientation.
- **If \( \det(A) < 0 \):** The transformation **flips** orientation (reflection).
- **If \( \det(A) = 0 \):** The transformation **collapses** the plane into a lower-dimensional space (line or point), meaning the vectors are **linearly dependent**.

##### **Example: Reflection**
For:

\[
A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
\]

\[
\det(A) = (0)(0) - (1)(1) = -1
\]

Since the determinant is negative, this matrix represents a reflection, flipping the orientation.

---

### **4. Determinant as a Volume Factor**
The determinant also tells us how a transformation scales areas:

\[
\text{New Area} = |\det(A)| \times \text{Original Area}
\]

For a transformation matrix \( A \):

- If \( |\det(A)| > 1 \), the transformation **expands** areas.
- If \( 0 < |\det(A)| < 1 \), the transformation **contracts** areas.
- If \( |\det(A)| = 0 \), the transformation **collapses** the shape into a lower dimension.

##### **Example: Scaling**
For:

\[
A = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}
\]

\[
\det(A) = (3)(2) - (0)(0) = 6
\]

The unit square expands by a factor of **6**.

---

### **5. Summary of Geometric Insights**
| Property | Interpretation |
|----------|---------------|
| \( \det(A) \) | Signed area of the parallelogram formed by column vectors. |
| \( \det(A) > 0 \) | Orientation is preserved. |
| \( \det(A) < 0 \) | Reflection occurs, reversing orientation. |
| \( \det(A) = 0 \) | Vectors are linearly dependent (collapse to a lower dimension). |
| \( |\det(A)| \) | The scaling factor for area. |

The determinant of a \(2 \times 2\) matrix thus serves as a **measure of transformation, area scaling, 
and orientation preservation** in 2D geometry.






## **Calculating the Inverse of a \(3 \times 3\) Matrix Using the Cofactor Method**  

The inverse of a \(3 \times 3\) matrix \(A\) exists only if its determinant is nonzero. 
One method to compute the inverse is the **cofactor method**, which involves finding the matrix of cofactors, 
forming the adjugate, and dividing by the determinant.

---

## **1. Formula for the Inverse of a 3×3 Matrix**  

Given a \(3 \times 3\) matrix:

\[
A = \begin{bmatrix} 
a & b & c \\ 
d & e & f \\ 
g & h & i 
\end{bmatrix}
\]

The inverse \( A^{-1} \) is given by:

\[
A^{-1} = \frac{1}{\det(A)} \text{Adj}(A)
\]

where:
- \( \det(A) \) is the determinant of \( A \).
- \( \text{Adj}(A) \) (the **adjugate matrix**) is the transpose of the **cofactor matrix**.

---

## **2. Step-by-Step Calculation of \( A^{-1} \)**
### **Step 1: Compute the Determinant**
The determinant of a \(3 \times 3\) matrix is given by:

\[
\det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
\]

If \( \det(A) = 0 \), the matrix is **singular** and does **not** have an inverse.

### **Step 2: Compute the Cofactor Matrix**
The **cofactor** \( C_{ij} \) of an element \( A_{ij} \) is found by deleting row \( i \) and column \( j \), then computing the determinant of the resulting \(2 \times 2\) matrix, with a sign adjustment:

\[
C_{ij} = (-1)^{i+j} \det(M_{ij})
\]

where \( M_{ij} \) is the minor of \( A_{ij} \) (the determinant of the \(2 \times 2\) submatrix obtained by removing row \( i \) and column \( j \)).

#### **Example of Cofactors**
For \( A \), the cofactors are:

\[
C_{11} = \det \begin{bmatrix} e & f \\ h & i \end{bmatrix} = ei - fh
\]

\[
C_{12} = -\det \begin{bmatrix} d & f \\ g & i \end{bmatrix} = -(di - fg)
\]

\[
C_{13} = \det \begin{bmatrix} d & e \\ g & h \end{bmatrix} = dh - eg
\]

Computing all cofactors, we get the **cofactor matrix**:

\[
C = \begin{bmatrix} 
ei - fh & -(di - fg) & dh - eg \\ 
-(bi - ch) & ai - cg & -(ah - bg) \\ 
bf - ce & -(af - cd) & ae - bd 
\end{bmatrix}
\]

### **Step 3: Compute the Adjugate Matrix**
The **adjugate matrix** \( \text{Adj}(A) \) is obtained by **transposing** the cofactor matrix:

\[
\text{Adj}(A) = C^T = \begin{bmatrix} 
ei - fh & -(bi - ch) & bf - ce \\ 
-(di - fg) & ai - cg & -(af - cd) \\ 
dh - eg & -(ah - bg) & ae - bd 
\end{bmatrix}
\]

### **Step 4: Compute \( A^{-1} \)**
Finally, divide by \( \det(A) \):

\[
A^{-1} = \frac{1}{\det(A)} \text{Adj}(A)
\]

---

## **3. Example Calculation**
Consider:

\[
A = \begin{bmatrix} 
2 & 3 & 1 \\ 
4 & 5 & 6 \\ 
7 & 8 & 9 
\end{bmatrix}
\]

### **Step 1: Compute \( \det(A) \)**
\[
\det(A) = 2(5 \times 9 - 6 \times 8) - 3(4 \times 9 - 6 \times 7) + 1(4 \times 8 - 5 \times 7)
\]

\[
= 2(45 - 48) - 3(36 - 42) + 1(32 - 35)
\]

\[
= 2(-3) - 3(-6) + 1(-3) = -6 + 18 - 3 = 9
\]

### **Step 2: Compute Cofactor Matrix**
\[
C = \begin{bmatrix} 
(5 \times 9 - 6 \times 8) & -(4 \times 9 - 6 \times 7) & (4 \times 8 - 5 \times 7) \\ 
-(3 \times 9 - 1 \times 8) & (2 \times 9 - 1 \times 7) & -(2 \times 8 - 3 \times 7) \\ 
(3 \times 6 - 1 \times 5) & -(2 \times 6 - 1 \times 4) & (2 \times 5 - 3 \times 4) 
\end{bmatrix}
\]

\[
= \begin{bmatrix} 
-3 & 6 & -3 \\ 
-19 & 11 & -5 \\ 
13 & -8 & -2 
\end{bmatrix}
\]

### **Step 3: Compute the Adjugate Matrix**
\[
\text{Adj}(A) = C^T = \begin{bmatrix} 
-3 & -19 & 13 \\ 
6 & 11 & -8 \\ 
-3 & -5 & -2 
\end{bmatrix}
\]

### **Step 4: Compute \( A^{-1} \)**
\[
A^{-1} = \frac{1}{9} \begin{bmatrix} 
-3 & -19 & 13 \\ 
6 & 11 & -8 \\ 
-3 & -5 & -2 
\end{bmatrix}
\]

---

## **4. Key Takeaways**
- The **cofactor method** involves finding **cofactors**, forming the **adjugate**, and dividing by the **determinant**.
- If \( \det(A) = 0 \), the matrix is singular and has no inverse.
- This method works for any square matrix but is computationally expensive for larger matrices.

This approach is fundamental in solving linear systems, physics simulations, and graphics transformations.





## **Multiplying a Matrix by a Column Vector**  

Matrix-vector multiplication is a fundamental operation in linear algebra, used in solving systems of 
linear equations, transformations, machine learning models, and physics simulations.

---

## **1. Definition and Formula**  
Given an \( m \times n \) matrix \( A \):

\[
A = \begin{bmatrix} 
a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{bmatrix}
\]

and an \( n \times 1 \) column vector \( x \):

\[
x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}
\]

The product \( Ax \) is an \( m \times 1 \) column vector:

\[
Ax = \begin{bmatrix} 
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n \\ 
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n \\ 
\vdots \\ 
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n 
\end{bmatrix}
\]

This operation **computes a linear combination** of the matrix’s column vectors weighted by the corresponding elements of \( x \).

---

## **2. Example Calculation**  
Consider:

\[
A = \begin{bmatrix} 
2 & -1 & 3 \\ 
4 & 0 & 1 \\ 
-2 & 5 & 6 
\end{bmatrix}
\]

and the vector:

\[
x = \begin{bmatrix} 1 \\ -2 \\ 4 \end{bmatrix}
\]

Multiplying:

\[
Ax = \begin{bmatrix} 
(2 \times 1) + (-1 \times -2) + (3 \times 4) \\ 
(4 \times 1) + (0 \times -2) + (1 \times 4) \\ 
(-2 \times 1) + (5 \times -2) + (6 \times 4) 
\end{bmatrix}
\]

\[
= \begin{bmatrix} 2 + 2 + 12 \\ 4 + 0 + 4 \\ -2 -10 + 24 \end{bmatrix} 
= \begin{bmatrix} 16 \\ 8 \\ 12 \end{bmatrix}
\]

---

## **3. Interpretation and Applications**
- **Linear Systems**: If \( A \) represents coefficients and \( x \) represents variables, \( Ax \) is the result of applying the system.
- **Transformations**: In graphics, multiplying a vector by a matrix transforms its position.
- **Machine Learning**: Neural networks compute activations using matrix-vector multiplication.

This operation is efficient and heavily optimized in computational libraries like NumPy, TensorFlow, and PyTorch.






## **Convergent and Divergent Infinite Series**  

Infinite series play a crucial role in mathematics, physics, and engineering, particularly in calculus and analysis. 
Understanding their convergence or divergence helps in determining their sum and applicability in real-world problems.

---

## **1. Definition of an Infinite Series**  
An **infinite series** is the sum of the terms of an infinite sequence:

\[
S = a_1 + a_2 + a_3 + \dots = \sum_{n=1}^{\infty} a_n
\]

where \( a_n \) represents the terms of the sequence.

The behavior of this sum as \( n \to \infty \) determines whether the series **converges** or **diverges**.

---

## **2. Convergent Series**  
An infinite series **converges** if the sequence of its partial sums approaches a finite limit.

### **Partial Sums**
The partial sum \( S_n \) of the first \( n \) terms is:

\[
S_n = \sum_{k=1}^{n} a_k
\]

If \( \lim\limits_{n \to \infty} S_n = S \) (a finite number), then the series **converges** to \( S \).

### **Example: Geometric Series**  
A geometric series:

\[
\sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ar^3 + \dots
\]

converges if \( |r| < 1 \) and its sum is:

\[
S = \frac{a}{1 - r}
\]

Example: \( \sum_{n=0}^{\infty} \frac{1}{2^n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots \)  
Since \( |r| = \frac{1}{2} < 1 \), it converges to:

\[
S = \frac{1}{1 - \frac{1}{2}} = 2
\]

---

## **3. Divergent Series**  
A series **diverges** if its partial sums tend to infinity or oscillate without approaching a finite limit.

### **Example: Harmonic Series**  
\[
\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots
\]

Although individual terms decrease, the partial sums grow without bound:

\[
\lim\limits_{n \to \infty} S_n = \infty
\]

Thus, the harmonic series **diverges**.

### **Example: Geometric Series with \( |r| \geq 1 \)**  
\[
\sum_{n=0}^{\infty} 2^n = 1 + 2 + 4 + 8 + \dots
\]

Since \( r = 2 \), the terms grow exponentially, causing the series to **diverge to infinity**.

---

## **4. Tests for Convergence or Divergence**
Several tests determine whether a series converges or diverges.

### **1. nth-Term Test for Divergence**
If \( \lim\limits_{n \to \infty} a_n \neq 0 \), the series **diverges**.

Example: \( \sum_{n=1}^{\infty} \frac{n}{n+1} \), where \( \lim\limits_{n \to \infty} \frac{n}{n+1} = 1 \neq 0 \), so it diverges.

### **2. Integral Test**  
If \( f(n) \) is positive, decreasing, and continuous, and the improper integral:

\[
\int_{1}^{\infty} f(x)dx
\]

converges, then the series \( \sum a_n \) also converges.

### **3. Comparison Test**  
If \( 0 \leq a_n \leq b_n \) and \( \sum b_n \) converges, then \( \sum a_n \) also converges.  
Conversely, if \( \sum b_n \) diverges and \( a_n \geq b_n \), then \( \sum a_n \) also diverges.

Example: Since \( \sum \frac{1}{n^2} \) (p-series with \( p > 1 \)) converges and \( \frac{1}{n^2} \leq \frac{1}{n} \), we conclude that \( \sum \frac{1}{n} \) diverges.

### **4. Ratio Test**  
For a series \( \sum a_n \), if

\[
L = \lim\limits_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|
\]

- If \( L < 1 \), the series **converges**.
- If \( L > 1 \), the series **diverges**.
- If \( L = 1 \), the test is inconclusive.

Example: The geometric series \( \sum \frac{1}{2^n} \) has:

\[
\lim\limits_{n \to \infty} \frac{1}{2^{n+1}} \div \frac{1}{2^n} = \frac{1}{2} < 1
\]

so it **converges**.

---

## **5. Summary**
| **Series Type**         | **Convergent Condition** | **Example** |
|-------------------------|-------------------------|-------------|
| **Geometric Series**    | \( |r| < 1 \)           | \( \sum \frac{1}{2^n} \) |
| **Harmonic Series**     | Always diverges         | \( \sum \frac{1}{n} \) |
| **p-Series** \( \sum \frac{1}{n^p} \) | \( p > 1 \) converges, \( p \leq 1 \) diverges | \( \sum \frac{1}{n^2} \) converges, \( \sum \frac{1}{n} \) diverges |
| **Comparison Test**     | Compare to known series | \( \sum \frac{1}{n^2} \leq \sum \frac{1}{n} \) |
| **Ratio Test**          | \( L < 1 \) converges, \( L > 1 \) diverges | \( \sum \frac{n!}{2^n} \) diverges |

Mastering these concepts is essential in calculus, physics, and machine learning, where series approximations 
and summations are frequently used.







## **Calculating the Magnitude of Cartesian Vectors in 3D**  

In three-dimensional space, a **Cartesian vector** represents a directed quantity with three components 
along the \( x \)-, \( y \)-, and \( z \)-axes. The **magnitude** (or length) of a vector measures its 
size and is computed using the Euclidean norm.

---

## **1. Definition of a 3D Cartesian Vector**  
A 3D vector is represented as:

\[
\mathbf{v} = (x, y, z)
\]

where:  
- \( x \) is the component along the **x-axis**  
- \( y \) is the component along the **y-axis**  
- \( z \) is the component along the **z-axis**

### **Example:**
\[
\mathbf{v} = (3, -4, 5)
\]

This vector has components **3** in the x-direction, **-4** in the y-direction, and **5** in the z-direction.

---

## **2. Formula for the Magnitude of a 3D Vector**  
The magnitude (or norm) of a vector **\( \mathbf{v} \)** is given by:

\[
|\mathbf{v}| = \sqrt{x^2 + y^2 + z^2}
\]

This follows from the **Pythagorean Theorem** in three dimensions.

---

## **3. Step-by-Step Calculation**  
### **Example 1:**  
Find the magnitude of the vector \( \mathbf{v} = (3, -4, 5) \).

**Step 1:** Square each component  
\[
3^2 = 9, \quad (-4)^2 = 16, \quad 5^2 = 25
\]

**Step 2:** Sum the squares  
\[
9 + 16 + 25 = 50
\]

**Step 3:** Take the square root  
\[
|\mathbf{v}| = \sqrt{50} = 5\sqrt{2} \approx 7.07
\]

Thus, the magnitude of \( \mathbf{v} \) is **\( 7.07 \)**.

### **Example 2:**  
Find the magnitude of \( \mathbf{w} = (-2, 6, -3) \).

\[
|\mathbf{w}| = \sqrt{(-2)^2 + 6^2 + (-3)^2}
\]

\[
= \sqrt{4 + 36 + 9} = \sqrt{49} = 7
\]

---

## **4. Special Cases**
### **1. Zero Vector (\( \mathbf{0} \))**
The **zero vector** \( \mathbf{0} = (0,0,0) \) has a magnitude of:

\[
|\mathbf{0}| = \sqrt{0^2 + 0^2 + 0^2} = 0
\]

### **2. Unit Vectors**
A **unit vector** has a magnitude of **1** and is often used to indicate direction. The standard unit vectors in 3D are:

\[
\mathbf{i} = (1,0,0), \quad \mathbf{j} = (0,1,0), \quad \mathbf{k} = (0,0,1)
\]

Each has a magnitude of:

\[
|\mathbf{i}| = \sqrt{1^2 + 0^2 + 0^2} = 1
\]

---

## **5. Applications of Vector Magnitude**
1. **Physics** – Computing velocity, force, and displacement magnitudes.  
2. **Engineering** – Determining resultant forces in statics and dynamics.  
3. **Computer Graphics** – Normalizing vectors for lighting and shading.  
4. **Machine Learning** – Measuring distances in high-dimensional spaces.  

The magnitude of a vector is essential for many real-world applications, including **unit vector normalization**, 
**vector projections**, and **distance computations**.






## **The Cross Product of Two Vectors**  

The **cross product** of two vectors in three-dimensional space is an operation that produces a new 
vector **perpendicular** to both input vectors. It is widely used in physics, engineering, 
and computer graphics for calculating normals, rotational effects, and force directions.

---

## **1. Definition of the Cross Product**  
For two vectors **\( \mathbf{a} \) and \( \mathbf{b} \)** in **3D space**, the **cross product** is denoted as:

\[
\mathbf{a} \times \mathbf{b}
\]

If:

\[
\mathbf{a} = (a_1, a_2, a_3), \quad \mathbf{b} = (b_1, b_2, b_3)
\]

Then, the cross product is given by:

\[
\mathbf{a} \times \mathbf{b} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
\]

Expanding the determinant:

\[
\mathbf{a} \times \mathbf{b} =
\begin{bmatrix}
a_2b_3 - a_3b_2 \\
a_3b_1 - a_1b_3 \\
a_1b_2 - a_2b_1
\end{bmatrix}
\]

This results in a **new vector** perpendicular to both **\( \mathbf{a} \)** and **\( \mathbf{b} \)**.

---

## **2. Geometric Interpretation**
- The cross product **produces a vector** that is **orthogonal (perpendicular)** to both input vectors.
- The direction follows the **right-hand rule**:
  - Point your **index finger** in the direction of \( \mathbf{a} \).
  - Point your **middle finger** in the direction of \( \mathbf{b} \).
  - Your **thumb** will point in the direction of \( \mathbf{a} \times \mathbf{b} \).

- The **magnitude** of the cross product is given by:

\[
|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}| \sin\theta
\]

where:
- \( |\mathbf{a}| \) and \( |\mathbf{b}| \) are the magnitudes of the vectors.
- \( \theta \) is the angle between them.

The result is **zero** if the vectors are **parallel** or **antiparallel** (\( \theta = 0^\circ \) or \( 180^\circ \)).

---

## **3. Example Calculations**
### **Example 1: Cross Product of Two Vectors**
Given:

\[
\mathbf{a} = (1, 2, 3), \quad \mathbf{b} = (4, 5, 6)
\]

Calculate \( \mathbf{a} \times \mathbf{b} \):

\[
\mathbf{a} \times \mathbf{b} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 2 & 3 \\
4 & 5 & 6
\end{vmatrix}
\]

Expanding along the first row:

\[
\mathbf{i} (2 \cdot 6 - 3 \cdot 5) - \mathbf{j} (1 \cdot 6 - 3 \cdot 4) + \mathbf{k} (1 \cdot 5 - 2 \cdot 4)
\]

\[
\mathbf{i} (12 - 15) - \mathbf{j} (6 - 12) + \mathbf{k} (5 - 8)
\]

\[
\mathbf{i} (-3) - \mathbf{j} (-6) + \mathbf{k} (-3)
\]

\[
(-3, 6, -3)
\]

Thus:

\[
\mathbf{a} \times \mathbf{b} = (-3, 6, -3)
\]

---

## **4. Special Cases**
### **1. Parallel Vectors**
If \( \mathbf{a} \) and \( \mathbf{b} \) are **parallel**, then:

\[
\mathbf{a} \times \mathbf{b} = \mathbf{0}
\]

because **\( \sin 0^\circ = 0 \)**.

### **2. Perpendicular Vectors**
If \( \mathbf{a} \) and \( \mathbf{b} \) are **perpendicular**, then:

\[
|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}|
\]

since **\( \sin 90^\circ = 1 \)**.

---

## **5. Applications of the Cross Product**
1. **Physics** – Used to compute **torque** \( \mathbf{\tau} = \mathbf{r} \times \mathbf{F} \), where \( \mathbf{r} \) is the position vector and \( \mathbf{F} \) is the force.
2. **Engineering** – Determines **moment of force** and rotational mechanics.
3. **Computer Graphics** – Used in shading, lighting, and normal vector calculations.
4. **Navigation** – Helps determine perpendicular directions in 3D space.
5. **Machine Learning** – Used in **vector representations** and transformations.

The cross product is a powerful tool for working with vector quantities, particularly in **3D geometry,
physics, and engineering**.







## **Circles in the Coordinate Plane**  

A **circle** is a set of all points in a plane that are equidistant from a fixed point called the **center**. 
In the **coordinate plane**, circles are represented algebraically using equations derived from the **distance formula**.

---

### **1. The Standard Equation of a Circle**
The equation of a circle with center \( (h, k) \) and radius \( r \) is given by:

\[
(x - h)^2 + (y - k)^2 = r^2
\]

where:
- \( (h, k) \) is the **center** of the circle.
- \( r \) is the **radius** of the circle.
- \( (x, y) \) represents any point on the circle.

This equation comes from the **distance formula**:

\[
\sqrt{(x - h)^2 + (y - k)^2} = r
\]

Squaring both sides gives the standard equation.

---

### **2. Equation of a Circle Centered at the Origin**
If the circle is centered at the **origin** \( (0,0) \), then the equation simplifies to:

\[
x^2 + y^2 = r^2
\]

Example:
- If a circle has a radius of **5**, its equation is:

\[
x^2 + y^2 = 25
\]

---

### **3. Finding the Equation of a Circle**
#### **Example 1: Given Center and Radius**
Find the equation of a circle with center \( (3, -2) \) and radius \( 4 \).

Using the standard equation:

\[
(x - 3)^2 + (y + 2)^2 = 4^2
\]

\[
(x - 3)^2 + (y + 2)^2 = 16
\]

---

### **4. Finding the Center and Radius from an Equation**
To determine the center and radius from an equation, rewrite it in standard form.

#### **Example 2: Given an Expanded Equation**
Consider:

\[
x^2 + y^2 - 6x + 4y - 3 = 0
\]

#### **Step 1: Group \( x \)-terms and \( y \)-terms**
\[
(x^2 - 6x) + (y^2 + 4y) = 3
\]

#### **Step 2: Complete the Square**
- For \( x^2 - 6x \), take **half** of \(-6\), square it: \( \left( \frac{-6}{2} \right)^2 = 9 \).
- For \( y^2 + 4y \), take **half** of \(4\), square it: \( \left( \frac{4}{2} \right)^2 = 4 \).

\[
(x^2 - 6x + 9) + (y^2 + 4y + 4) = 3 + 9 + 4
\]

\[
(x - 3)^2 + (y + 2)^2 = 16
\]

Thus, the **center** is \( (3, -2) \) and the **radius** is:

\[
r = \sqrt{16} = 4
\]

---

### **5. Graphing a Circle**
To graph a circle:
1. **Plot the center** \( (h, k) \).
2. **Measure the radius** \( r \) in all four directions (up, down, left, right).
3. **Sketch the circle** smoothly around these points.

Example:
For \( (x - 2)^2 + (y + 1)^2 = 9 \):
- **Center**: \( (2, -1) \)
- **Radius**: \( \sqrt{9} = 3 \)
- **Graph by plotting** points at:
  - \( (2+3, -1) = (5, -1) \)
  - \( (2-3, -1) = (-1, -1) \)
  - \( (2, -1+3) = (2, 2) \)
  - \( (2, -1-3) = (2, -4) \)

---

### **6. Tangents and Secants**
- A **tangent** to a circle **touches** the circle at exactly **one** point.
- A **secant** is a line that **intersects** the circle at **two** points.

Equation of a **tangent line** at \( (x_0, y_0) \):

\[
(x_0 - h)(x - h) + (y_0 - k)(y - k) = r^2
\]

---

### **7. Applications of Circles in the Coordinate Plane**
1. **Physics** – Motion of planets, circular orbits.
2. **Engineering** – Designing gears, wheels.
3. **Computer Graphics** – Rendering circular objects.
4. **Navigation** – GPS calculations involving circular boundaries.

Understanding how to manipulate circle equations allows for solving geometric and real-world problems effectively.






## **Defining Vector-Valued Functions, Deep Dive**  

A **vector-valued function** is a function where the input is a scalar (typically \( t \), representing 
time or a parameter) and the output is a vector. These functions are fundamental in physics, engineering, 
and computer graphics for describing motion, curves, and fields in space.

---

### **1. Definition of a Vector-Valued Function**
A **vector-valued function** is a function of the form:

\[
\mathbf{r}(t) = f(t) \mathbf{i} + g(t) \mathbf{j} + h(t) \mathbf{k}
\]

or equivalently,

\[
\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle
\]

where:
- \( f(t), g(t), h(t) \) are real-valued functions of \( t \),
- \( \mathbf{i}, \mathbf{j}, \mathbf{k} \) are unit vectors along the \( x \)-, \( y \)-, and \( z \)-axes.

For 2D cases, the function simplifies to:

\[
\mathbf{r}(t) = f(t) \mathbf{i} + g(t) \mathbf{j} = \langle f(t), g(t) \rangle
\]

where the output lies in the **plane** rather than 3D space.

---

### **2. Example of a Vector-Valued Function**
#### **Example 1: Circular Motion**
A particle moving in a circle of radius \( R \) centered at the origin can be described by:

\[
\mathbf{r}(t) = R \cos t \mathbf{i} + R \sin t \mathbf{j}
\]

where:
- \( t \) represents time or an angle,
- \( R \) is the radius of the circle.

For \( R = 5 \), this becomes:

\[
\mathbf{r}(t) = 5 \cos t \mathbf{i} + 5 \sin t \mathbf{j}
\]

which traces a **circle** of radius 5.

---

### **3. Graphical Interpretation**
- A **vector-valued function** defines a **curve** in space.
- Each point on the curve corresponds to a value of \( t \).
- The **position vector** \( \mathbf{r}(t) \) points from the origin to the curve at time \( t \).

For instance:
- \( \mathbf{r}(0) \) gives the **starting position**.
- \( \mathbf{r}(t) \) describes how the position **evolves over time**.

---

### **4. Operations on Vector-Valued Functions**
#### **Addition**
If \( \mathbf{r}_1(t) \) and \( \mathbf{r}_2(t) \) are two vector functions:

\[
\mathbf{r}(t) = \mathbf{r}_1(t) + \mathbf{r}_2(t)
\]

is defined component-wise:

\[
\langle f_1(t), g_1(t), h_1(t) \rangle + \langle f_2(t), g_2(t), h_2(t) \rangle = \langle f_1(t) + f_2(t), g_1(t) + g_2(t), h_1(t) + h_2(t) \rangle
\]

#### **Scalar Multiplication**
For a scalar \( c \),

\[
c \mathbf{r}(t) = c f(t) \mathbf{i} + c g(t) \mathbf{j} + c h(t) \mathbf{k}
\]

stretches or shrinks the function.

#### **Example 2: Scaling a Vector Function**
If:

\[
\mathbf{r}(t) = \langle 3t, t^2, 2t \rangle
\]

then multiplying by 2 gives:

\[
2 \mathbf{r}(t) = \langle 6t, 2t^2, 4t \rangle
\]

which scales the curve.

---

### **5. Differentiation and Integration of Vector-Valued Functions**
#### **Derivative**
The **derivative** of a vector function is computed component-wise:

\[
\mathbf{r}'(t) = \frac{d}{dt} \langle f(t), g(t), h(t) \rangle = \langle f'(t), g'(t), h'(t) \rangle
\]

Example:

\[
\mathbf{r}(t) = \langle t^2, \sin t, e^t \rangle
\]

\[
\mathbf{r}'(t) = \langle 2t, \cos t, e^t \rangle
\]

The derivative represents the **velocity** in motion applications.

#### **Integration**
Integration is also computed component-wise:

\[
\int \mathbf{r}(t) dt = \langle \int f(t) dt, \int g(t) dt, \int h(t) dt \rangle
\]

Example:

\[
\int \langle t, e^t, \cos t \rangle dt = \langle \frac{t^2}{2}, e^t, \sin t \rangle + \mathbf{C}
\]

where \( \mathbf{C} \) is a constant vector.

---

### **6. Applications of Vector-Valued Functions**
- **Physics:** Motion in space (position, velocity, acceleration)
- **Engineering:** Electromagnetic fields, fluid flow
- **Computer Graphics:** Animation, 3D modeling
- **Robotics:** Path planning

Understanding vector-valued functions is crucial for analyzing motion and transformations in multidimensional spaces.







## **Multiplying a Matrix by the Identity Matrix**  

### **1. Definition of the Identity Matrix**  
The **identity matrix**, denoted as \( I_n \) for an \( n \times n \) matrix, is a special square matrix with **1s on the diagonal and 0s elsewhere**:

\[
I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\]

For any square matrix, multiplying by \( I_n \) preserves the matrix itself.

---

### **2. Multiplying a Matrix by the Identity Matrix**  
Let \( A \) be an \( m \times n \) matrix and \( I_n \) the \( n \times n \) identity matrix. The multiplication rules are:

- **Right multiplication** (Post-multiplication): \( A I_n = A \)
- **Left multiplication** (Pre-multiplication): \( I_m A = A \) (only when \( A \) is \( m \times n \))

#### **Example 1: Multiplication with a \( 2 \times 2 \) Matrix**
Let:

\[
A = \begin{bmatrix} 3 & 5 \\ 7 & 2 \end{bmatrix}
\]

Multiplying by \( I_2 \):

\[
A I_2 = \begin{bmatrix} 3 & 5 \\ 7 & 2 \end{bmatrix} \times \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\]

Computing:

\[
A I_2 = \begin{bmatrix} (3 \times 1 + 5 \times 0) & (3 \times 0 + 5 \times 1) \\ (7 \times 1 + 2 \times 0) & (7 \times 0 + 2 \times 1) \end{bmatrix} = \begin{bmatrix} 3 & 5 \\ 7 & 2 \end{bmatrix}
\]

The result is \( A \), confirming the identity property.

---

### **3. Why Does This Work?**
Multiplying a matrix by the identity matrix does not alter its values because:
- Each row of \( A \) is **dot-multiplied** with each column of \( I_n \).
- Since \( I_n \) has 1s on the diagonal and 0s elsewhere, each row of \( A \) remains unchanged.

---

### **4. Identity Matrix in Non-Square Matrices**
For a **rectangular matrix** \( A \) of size \( m \times n \), the multiplication follows:

- **Right multiplication** \( A I_n = A \), preserving the shape.
- **Left multiplication** \( I_m A = A \), preserving the shape (only if \( A \) is \( m \times n \)).

#### **Example 2: \( 3 \times 2 \) Matrix**
Let:

\[
A = \begin{bmatrix} 4 & 6 \\ 1 & 9 \\ 3 & 2 \end{bmatrix}
\]

Multiply by \( I_2 \):

\[
A I_2 = \begin{bmatrix} 4 & 6 \\ 1 & 9 \\ 3 & 2 \end{bmatrix} \times \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 4 & 6 \\ 1 & 9 \\ 3 & 2 \end{bmatrix}
\]

Since \( A \) is \( 3 \times 2 \), left multiplication by \( I_3 \) is **not** possible.

---

### **5. Properties of the Identity Matrix**
1. **Neutral Element**: \( A I_n = A \) and \( I_m A = A \).
2. **Inverse Role**: The inverse of \( A \) (if it exists) satisfies \( A A^{-1} = I_n \).
3. **Eigenvalues**: The identity matrix has all eigenvalues equal to **1**.
4. **Determinant**: \( \det(I_n) = 1 \) for any \( n \).
5. **Commutativity with Inverse**: \( A^{-1} A = A A^{-1} = I_n \).

---

### **6. Applications in Linear Algebra**
- **Solving Systems of Equations**: \( A X = B \) often uses \( I_n \) in **Gaussian elimination**.
- **Transformations**: \( I_n \) represents **no change** in coordinate transformations.
- **Matrix Decomposition**: Identity matrices appear in LU, QR, and SVD decompositions.
- **Machine Learning & Data Science**: Identity matrices help in **regularization** and **covariance matrices**.

Multiplying by the identity matrix confirms that a matrix remains unchanged, making \( I_n \) fundamental in matrix operations.






## **Equations of Circles Centered at the Origin**  

### **1. Standard Equation of a Circle**
A circle is the set of all points equidistant from a fixed center. If the circle is **centered at the origin** \( (0,0) \), 
the equation follows from the **distance formula**:

\[
x^2 + y^2 = r^2
\]

where:  
- \( (x, y) \) represents any point on the circle,  
- \( r \) is the radius of the circle.

---

### **2. Derivation from the Distance Formula**
The distance formula states:

\[
\text{Distance} = \sqrt{(x - h)^2 + (y - k)^2}
\]

For a circle centered at \( (0,0) \) with radius \( r \), setting the distance equal to \( r \):

\[
\sqrt{x^2 + y^2} = r
\]

Squaring both sides:

\[
x^2 + y^2 = r^2
\]

---

### **3. Examples of Circles Centered at the Origin**
#### **Example 1: Unit Circle**
If \( r = 1 \):

\[
x^2 + y^2 = 1
\]

This represents the **unit circle**, fundamental in **trigonometry**.

#### **Example 2: Circle with Radius 5**
If \( r = 5 \):

\[
x^2 + y^2 = 25
\]

This is a circle with a **radius of 5**, centered at \( (0,0) \).

#### **Example 3: Circle with Radius \( \frac{3}{2} \)**
If \( r = \frac{3}{2} \):

\[
x^2 + y^2 = \frac{9}{4}
\]

---

### **4. Generalizing to 3D (Sphere Centered at the Origin)**
In three dimensions, the equation of a **sphere** centered at \( (0,0,0) \) with radius \( r \) is:

\[
x^2 + y^2 + z^2 = r^2
\]

This extends the concept of a circle to 3D space.

---

### **5. Applications of Circles Centered at the Origin**
- **Trigonometry**: The unit circle defines sine and cosine functions.
- **Physics**: Circular motion equations use this form.
- **Computer Graphics**: Circles centered at the origin simplify transformations.
- **Complex Numbers**: Modulus representations use this equation.

Circles centered at the origin provide the simplest and most symmetrical form, serving as the basis for many mathematical and real-world applications.






## **Conformability for Matrix Multiplication**  

### **1. Definition of Matrix Multiplication**
Matrix multiplication is defined when the number of **columns** in the first matrix matches the number of **rows** in the second matrix. This property is called **conformability** for multiplication.

If **\( A \)** is an **\( m \times n \)** matrix and **\( B \)** is an **\( p \times q \)** matrix, then matrix multiplication **\( AB \)** is only defined if:  

\[
\text{Number of columns of } A = \text{Number of rows of } B
\]

\[
n = p
\]

The resulting product **\( AB \)** will have dimensions:

\[
m \times q
\]

---

### **2. Example of Conformable Matrices**
#### **Example 1: Valid Multiplication**
Let  
\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}  \quad (3 \times 2)
\]
\[
B = \begin{bmatrix} 7 & 8 & 9 \\ 10 & 11 & 12 \end{bmatrix}  \quad (2 \times 3)
\]
Since the **number of columns of \( A \) (2)** matches the **number of rows of \( B \) (2)**, we can multiply them.  
The resulting matrix \( AB \) will have dimensions **\( 3 \times 3 \)**.

#### **Example 2: Invalid Multiplication**
Let  
\[
C = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}  \quad (2 \times 3)
\]
\[
D = \begin{bmatrix} 7 & 8 \\ 9 & 10 \end{bmatrix}  \quad (2 \times 2)
\]
Multiplication \( CD \) is **not defined** because the number of columns in \( C \) (3) does not match the number of rows in \( D \) (2).

---

### **3. Special Cases**
#### **Square Matrices (\( n \times n \))**
For a square matrix \( A \) of size \( n \times n \), multiplying with another \( n \times n \) matrix is always defined.

#### **Matrix and Vector Multiplication**
A matrix \( A \) of size \( m \times n \) can multiply a column vector \( x \) of size \( n \times 1 \):

\[
Ax = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = 
\begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \end{bmatrix}
\]

which results in an \( m \times 1 \) column vector.

#### **Identity Matrix**
The identity matrix \( I_n \) of size \( n \times n \) satisfies:

\[
AI_n = A, \quad I_n A = A
\]

wherever multiplication is conformable.

---

### **4. Applications**
- **Linear Algebra**: Solving systems of equations.
- **Machine Learning**: Transforming feature vectors.
- **Physics**: Representing transformations.
- **Computer Graphics**: Rotations and scaling.

Understanding conformability ensures correct computations and avoids undefined operations in matrix algebra.





## **Equations of Circles**  

### **1. Definition of a Circle**  
A **circle** is the set of all points \((x, y)\) in a coordinate plane that are equidistant from a 
fixed point called the **center**. This fixed distance is the **radius** \( r \).

---

### **2. Standard Equation of a Circle**  
The equation of a circle centered at **\( (h, k) \)** with radius **\( r \)** is given by:

\[
(x - h)^2 + (y - k)^2 = r^2
\]

where:  
- \( (h, k) \) is the center of the circle,  
- \( r \) is the radius,  
- \( (x, y) \) represents any point on the circle.

---

### **3. Circle Centered at the Origin**  
If the center is at the **origin** \( (0,0) \), the equation simplifies to:

\[
x^2 + y^2 = r^2
\]

For example, if \( r = 5 \), the equation is:

\[
x^2 + y^2 = 25
\]

---

### **4. Finding the Equation of a Circle**
Given:  
- Center \( (h, k) = (3, -2) \)  
- Radius \( r = 4 \)  

Using the standard form:

\[
(x - 3)^2 + (y + 2)^2 = 4^2
\]

\[
(x - 3)^2 + (y + 2)^2 = 16
\]

---

### **5. General Form of a Circle's Equation**  
Expanding the standard equation:

\[
(x - h)^2 + (y - k)^2 = r^2
\]

\[
x^2 - 2hx + h^2 + y^2 - 2ky + k^2 = r^2
\]

Rearranging:

\[
x^2 + y^2 - 2hx - 2ky + (h^2 + k^2 - r^2) = 0
\]

This is called the **general form**:

\[
x^2 + y^2 + Dx + Ey + F = 0
\]

where:
- \( D = -2h \)
- \( E = -2k \)
- \( F = h^2 + k^2 - r^2 \)

---

### **6. Converting General Form to Standard Form**  
Given a circle equation in general form:

\[
x^2 + y^2 + 6x - 4y - 3 = 0
\]

To convert it to standard form, complete the square:

#### **Step 1: Group x and y terms**
\[
(x^2 + 6x) + (y^2 - 4y) = 3
\]

#### **Step 2: Complete the square**
For \( x^2 + 6x \), take half of 6, square it:  
\( \left(\frac{6}{2}\right)^2 = 9 \)

For \( y^2 - 4y \), take half of -4, square it:  
\( \left(\frac{-4}{2}\right)^2 = 4 \)

Add these inside the equation, adjusting the right-hand side:

\[
(x^2 + 6x + 9) + (y^2 - 4y + 4) = 3 + 9 + 4
\]

\[
(x + 3)^2 + (y - 2)^2 = 16
\]

which is now in standard form with center \( (-3, 2) \) and radius \( 4 \).

---

### **7. Applications of Circle Equations**
- **Geometry**: Analyzing circles in coordinate geometry.
- **Physics**: Modeling circular motion.
- **Computer Graphics**: Rendering circular objects.
- **Engineering**: Designing mechanical parts.

Understanding circle equations allows for solving geometric problems, analyzing real-world motion, 
and working with transformations in various fields.







## **The Addition Law of Probability**  

#### **1. Introduction**  
The **Addition Law of Probability** is a fundamental rule that helps compute the probability of the 
union of two or more events. It accounts for overlapping probabilities to ensure no double counting. 
The general formula is:  

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

This formula ensures that the probability of both **A and B occurring simultaneously** (i.e., **\( P(A \cap B) \)**)
is **subtracted** to avoid double counting.

---

#### **2. Case 1: Mutually Exclusive (Disjoint) Events**  
If **events A and B are mutually exclusive**, meaning they cannot occur together (**\( P(A \cap B) = 0 \)**), 
the formula simplifies to:  

\[
P(A \cup B) = P(A) + P(B)
\]

##### **Example: Rolling a Die**  
Let \( A \) be rolling a **3** and \( B \) be rolling a **5**. These events are **mutually exclusive** 
because you cannot roll both numbers at once.

\[
P(A) = \frac{1}{6}, \quad P(B) = \frac{1}{6}
\]

\[
P(A \cup B) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}
\]

---

#### **3. Case 2: Overlapping Events (General Case)**  
If events **A and B are not mutually exclusive**, we must subtract **\( P(A \cap B) \)** to avoid overcounting.

##### **Example: Drawing a Card**  
Let:  
- \( A \) = drawing a **Heart**  
- \( B \) = drawing a **Face Card (Jack, Queen, or King)**  

There are **13 Hearts** and **12 Face Cards** in a **52-card deck**, but **3 cards are both Hearts and Face Cards**
(Jack, Queen, King of Hearts).  

\[
P(A) = \frac{13}{52}, \quad P(B) = \frac{12}{52}, \quad P(A \cap B) = \frac{3}{52}
\]

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

\[
P(A \cup B) = \frac{13}{52} + \frac{12}{52} - \frac{3}{52} = \frac{22}{52} = \frac{11}{26}
\]

---

#### **4. Extension to Three or More Events**  
For **three events \( A, B, C \)**, the general formula is:

\[
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(B \cap C) - P(A \cap C) + P(A \cap B \cap C)
\]

---

#### **5. Key Takeaways**
- **Use simple addition** for **mutually exclusive** events.
- **Subtract overlapping probabilities** for **non-mutually exclusive** events.
- **For multiple events**, apply the extended formula.

This law is widely used in probability problems, risk assessment, and real-world applications like finance, 
insurance, and AI models.







## **Polar Equations of Circles Centered at the Origin**  

#### **1. Introduction**  
In polar coordinates, a point is represented as \( (r, \theta) \), where:  
- \( r \) is the **radial distance** from the origin.
- \( \theta \) is the **angle** from the positive x-axis.  

The equation of a circle changes when expressed in polar form, particularly when it is centered at the origin.

---

#### **2. Standard Polar Equation of a Circle**
A circle centered at the origin with radius \( R \) is given by the simple equation:

\[
r = R
\]

where \( R \) is the constant radius of the circle. This means that every point on the circle is at a fixed distance \( R \) from the origin, regardless of \( \theta \).

##### **Example**:  
A circle of radius **5** centered at the origin has the equation:

\[
r = 5
\]

---

#### **3. Polar Equations of Circles in General Form**  
The general equation of a circle in polar coordinates, including shifted versions, is:

\[
r = 2 R \cos \theta \quad \text{or} \quad r = 2 R \sin \theta
\]

depending on its orientation.  

##### **Three Important Cases:**
1. **Circle Centered at the Origin**  
   \[
   r = R
   \]
   (A simple circle with radius \( R \).)

2. **Circle Tangent to the Origin (Passing Through the Origin)**  
   - When the circle is **shifted right** along the x-axis:
     \[
     r = 2 R \cos \theta
     \]
   - When the circle is **shifted upward** along the y-axis:
     \[
     r = 2 R \sin \theta
     \]

3. **General Form of a Circle in Polar Coordinates**  
   The equation for a circle with **center shifted to \( (R_0, \theta_0) \) in polar coordinates** is:

   \[
   r^2 - 2 R_0 r \cos(\theta - \theta_0) + R_0^2 = R^2
   \]

   where:
   - \( R_0 \) is the radial distance of the center from the origin.
   - \( \theta_0 \) is the angular position of the center.
   - \( R \) is the radius.

---

#### **4. Derivation from Cartesian Form**  
The Cartesian equation of a circle centered at the origin is:

\[
x^2 + y^2 = R^2
\]

Since **polar coordinates** relate to Cartesian coordinates as:

\[
x = r \cos \theta, \quad y = r \sin \theta
\]

substituting:

\[
(r \cos \theta)^2 + (r \sin \theta)^2 = R^2
\]

\[
r^2 (\cos^2 \theta + \sin^2 \theta) = R^2
\]

Since \( \cos^2 \theta + \sin^2 \theta = 1 \), we get:

\[
r^2 = R^2
\]

which simplifies to:

\[
r = R
\]

This confirms the standard polar form.

---

#### **5. Key Takeaways**
- The simplest polar equation of a circle centered at the origin is **\( r = R \)**.
- If the center is shifted, the equation can take the form **\( r = 2 R \cos \theta \)** or **\( r = 2 R \sin \theta \)**.
- More general forms exist for circles not centered at the origin.

Polar equations of circles play an important role in physics, engineering, and navigation, 
especially in **radar systems, planetary motion, and wavefront propagation**.







## **Equations of Ellipses Centered at the Origin**  

#### **1. Introduction**  
An **ellipse** is the set of all points such that the sum of their distances from two fixed points, 
called **foci**, is constant. In polar and Cartesian coordinates, ellipses have distinct forms, 
and their equations depend on the orientation and eccentricity.

---

#### **2. Standard Equation of an Ellipse (Cartesian Form)**  
For an ellipse centered at the **origin** with the **major axis along the x-axis**, the equation is:

\[
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
\]

where:
- \( a \) = **semi-major axis** (the longest radius).
- \( b \) = **semi-minor axis** (the shortest radius).
- The foci are located at \( (\pm c, 0) \), where \( c^2 = a^2 - b^2 \).

If the **major axis is along the y-axis**, the equation is:

\[
\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1
\]

---

#### **3. Relationship Between the Semi-Axes and the Eccentricity**  
The **eccentricity** of an ellipse, denoted by \( e \), measures how "stretched" it is:

\[
e = \frac{c}{a}
\]

where \( c = \sqrt{a^2 - b^2} \). The value of \( e \) satisfies \( 0 \leq e < 1 \), with \( e = 0 \) for a circle.

---

#### **4. Polar Equation of an Ellipse (Focus at the Origin)**  
When one of the **foci is at the origin** and the ellipse is oriented along the x-axis, the equation in polar coordinates is:

\[
r = \frac{a(1 - e^2)}{1 + e \cos \theta}
\]

where:
- \( r \) is the radial distance,
- \( \theta \) is the angle from the positive x-axis,
- \( e \) is the eccentricity,
- \( a \) is the semi-major axis.

For an ellipse oriented along the y-axis:

\[
r = \frac{a(1 - e^2)}{1 + e \sin \theta}
\]

---

#### **5. Derivation from the Cartesian Equation**  
Starting from the **standard Cartesian form**:

\[
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
\]

Using **polar coordinate conversions**:

\[
x = r \cos \theta, \quad y = r \sin \theta
\]

Substituting these into the equation:

\[
\frac{(r \cos \theta)^2}{a^2} + \frac{(r \sin \theta)^2}{b^2} = 1
\]

\[
r^2 \left( \frac{\cos^2 \theta}{a^2} + \frac{\sin^2 \theta}{b^2} \right) = 1
\]

Solving for \( r \):

\[
r = \frac{1}{\sqrt{\frac{\cos^2 \theta}{a^2} + \frac{\sin^2 \theta}{b^2}}}
\]

This confirms the general polar representation of an ellipse.

---

#### **6. Special Cases of Ellipses**
1. **Circle**: When \( a = b \), the ellipse becomes a **circle** with radius \( a \):

   \[
   x^2 + y^2 = a^2
   \]

   In polar form:

   \[
   r = a
   \]

2. **Highly Stretched Ellipses**: When \( e \approx 1 \), the ellipse becomes **narrow** and approaches a **parabolic shape**.

---

#### **7. Key Takeaways**
- The **Cartesian equation** of an ellipse is based on the semi-major and semi-minor axes.
- The **polar form** describes an ellipse with a focus at the **origin** and uses **eccentricity**.
- The eccentricity **\( e \)** determines how "stretched" the ellipse is.
- Special cases include **circles** (\( e = 0 \)) and **highly elongated ellipses** (\( e \approx 1 \)).

Ellipses are widely used in **orbital mechanics, planetary motion, and signal processing**, 
making their study fundamental in applied mathematics and physics.







## **Equations of Ellipses Centered at a General Point**  

#### **1. Introduction**  
An **ellipse** is the set of all points where the sum of their distances from two fixed points, 
called **foci**, is constant. When an ellipse is centered at a general point \( (h, k) \) rather than the origin,
its equation is modified accordingly.

---

#### **2. Standard Equation of an Ellipse (Centered at \( (h, k) \))**  
If an ellipse is centered at \( (h, k) \), the **standard equation** depends on whether the **major axis is horizontal or vertical**:

1. **Horizontal Major Axis** (stretched along the x-axis):

   \[
   \frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
   \]

2. **Vertical Major Axis** (stretched along the y-axis):

   \[
   \frac{(x - h)^2}{b^2} + \frac{(y - k)^2}{a^2} = 1
   \]

where:
- \( (h, k) \) is the **center** of the ellipse.
- \( a \) is the **semi-major axis** (longer radius).
- \( b \) is the **semi-minor axis** (shorter radius).
- The **foci** are located at:
  - **Horizontal ellipse:** \( (h \pm c, k) \)
  - **Vertical ellipse:** \( (h, k \pm c) \)
  - where \( c^2 = a^2 - b^2 \).

---

#### **3. Relationship Between the Axes and the Eccentricity**  
The **eccentricity** \( e \) of an ellipse measures how elongated it is:

\[
e = \frac{c}{a}
\]

where \( c = \sqrt{a^2 - b^2} \). The **closer \( e \) is to 1**, the more elongated the ellipse. The special case of \( e = 0 \) corresponds to a **circle**.

---

#### **4. Polar Equation of an Ellipse (Centered at \( (h, k) \))**  
In **polar coordinates**, the equation of an ellipse centered at \( (h, k) \) is more complex. If the **focus is at \( (h, k) \) and the major axis is along the x-axis**, the equation is:

\[
r = \frac{a(1 - e^2)}{1 + e \cos(\theta - \theta_0)}
\]

where:
- \( r \) is the radial distance from the focus,
- \( \theta \) is the angle from the positive x-axis,
- \( e \) is the eccentricity,
- \( \theta_0 \) is the angular offset from the x-axis.

For **vertical orientation**, replace \( \cos \) with \( \sin \):

\[
r = \frac{a(1 - e^2)}{1 + e \sin(\theta - \theta_0)}
\]

---

#### **5. Transforming from Centered at the Origin to a General Point**  
If the ellipse is originally centered at the **origin**, we can apply the transformation:

\[
x' = x - h, \quad y' = y - k
\]

Replacing \( x \) and \( y \) in the **standard equation**:

\[
\frac{x'^2}{a^2} + \frac{y'^2}{b^2} = 1
\]

Expanding:

\[
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
\]

This shows that shifting an ellipse simply modifies the coordinate terms.

---

#### **6. Special Cases**
1. **Circle:** If \( a = b \), the ellipse simplifies to a **circle** centered at \( (h, k) \):

   \[
   (x - h)^2 + (y - k)^2 = r^2
   \]

2. **Highly Stretched Ellipses:** When \( e \approx 1 \), the ellipse becomes **narrow** and approaches a **parabola-like shape**.

---

#### **7. Key Takeaways**
- The **equation of an ellipse centered at \( (h, k) \)** adjusts the standard form by shifting \( x \) and \( y \).
- The **foci depend on the orientation** of the major axis.
- The **polar equation** describes the ellipse with a focus at \( (h, k) \).
- **Eccentricity \( e \)** determines the **oval shape** of the ellipse, with \( e = 0 \) giving a **circle**.

Ellipses are fundamental in **orbital mechanics, physics, and engineering**, making them a key concept in 
applied mathematics.






## **Determining Circle Properties by Completing the Square**  

#### **1. Introduction**  
A **circle** in the coordinate plane is defined by the general second-degree equation:

\[
Ax^2 + Ay^2 + Dx + Ey + F = 0
\]

For a standard circle, \( A = 1 \), so the equation simplifies to:

\[
x^2 + y^2 + Dx + Ey + F = 0
\]

To determine the **center** and **radius**, we rewrite this equation into **standard form**:

\[
(x - h)^2 + (y - k)^2 = r^2
\]

where \( (h, k) \) is the **center**, and \( r \) is the **radius**. We achieve this by **completing the square**.

---

#### **2. Steps to Complete the Square**  

Given a general equation of a circle:

\[
x^2 + y^2 + Dx + Ey + F = 0
\]

1. **Group the \( x \)-terms and \( y \)-terms:**
   \[
   (x^2 + Dx) + (y^2 + Ey) = -F
   \]

2. **Complete the square for each variable:**
   - Take **half** of the coefficient of \( x \) (which is \( D \)), square it, and add it inside the parentheses.
   - Do the same for \( y \) using \( E \).
   - Ensure you **add the same values to both sides** to keep the equation balanced.

3. **Rewrite the perfect square terms:**
   \[
   (x - h)^2 + (y - k)^2 = r^2
   \]
   where:
   - \( h = -\frac{D}{2} \),  
   - \( k = -\frac{E}{2} \),  
   - \( r = \sqrt{\left( \frac{D}{2} \right)^2 + \left( \frac{E}{2} \right)^2 - F} \).

---

#### **3. Example Problem**  

**Example:** Convert the equation

\[
x^2 + y^2 - 6x + 8y + 9 = 0
\]

into standard form and determine the center and radius.

**Step 1: Group the terms**
\[
(x^2 - 6x) + (y^2 + 8y) = -9
\]

**Step 2: Complete the square**
- Take **half of \(-6\)**, square it:  
  \[
  \left( \frac{-6}{2} \right)^2 = 9
  \]
- Take **half of \( 8 \)**, square it:  
  \[
  \left( \frac{8}{2} \right)^2 = 16
  \]
- Add these to both sides:
  \[
  (x^2 - 6x + 9) + (y^2 + 8y + 16) = -9 + 9 + 16
  \]

**Step 3: Rewrite as squares**
\[
(x - 3)^2 + (y + 4)^2 = 16
\]

**Step 4: Identify circle properties**
- **Center**: \( (3, -4) \)
- **Radius**: \( \sqrt{16} = 4 \)

---

#### **4. Key Takeaways**
- **Completing the square** converts a circle's general equation into standard form.
- The **center** is \( (-D/2, -E/2) \).
- The **radius** is \( r = \sqrt{(D/2)^2 + (E/2)^2 - F} \).
- This method is essential in **geometry, physics, and engineering applications**.

By mastering this technique, circle equations become easier to interpret and manipulate.







## **Finding Intercepts of Ellipses**  

In the Cartesian plane, an **ellipse** can be represented in standard form as:  

\[
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
\]

where:  
- \( (h, k) \) is the center of the ellipse.  
- \( a \) and \( b \) are the semi-major and semi-minor axes, respectively.  

To **find the intercepts**, we determine where the ellipse intersects the x-axis and y-axis.

### **1. X-Intercepts**  
Set \( y = 0 \) in the equation:

\[
\frac{(x - h)^2}{a^2} + \frac{(0 - k)^2}{b^2} = 1
\]

\[
\frac{(x - h)^2}{a^2} + \frac{k^2}{b^2} = 1
\]

If \( \frac{k^2}{b^2} \leq 1 \), solve for \( x \):

\[
(x - h)^2 = a^2 \left(1 - \frac{k^2}{b^2}\right)
\]

Taking the square root:

\[
x - h = \pm a \sqrt{1 - \frac{k^2}{b^2}}
\]

Thus, the **x-intercepts** are:

\[
x = h \pm a \sqrt{1 - \frac{k^2}{b^2}}, \quad y = 0
\]

If \( 1 - \frac{k^2}{b^2} < 0 \), there are **no x-intercepts**.

### **2. Y-Intercepts**  
Set \( x = 0 \) in the equation:

\[
\frac{(0 - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
\]

\[
\frac{h^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
\]

If \( \frac{h^2}{a^2} \leq 1 \), solve for \( y \):

\[
(y - k)^2 = b^2 \left(1 - \frac{h^2}{a^2}\right)
\]

Taking the square root:

\[
y - k = \pm b \sqrt{1 - \frac{h^2}{a^2}}
\]

Thus, the **y-intercepts** are:

\[
x = 0, \quad y = k \pm b \sqrt{1 - \frac{h^2}{a^2}}
\]

If \( 1 - \frac{h^2}{a^2} < 0 \), there are **no y-intercepts**.

### **Key Insights**  
- If the ellipse is centered at the **origin** (\( h = 0, k = 0 \)), the x-intercepts simplify to \( (\pm a, 0) \) and the y-intercepts to \( (0, \pm b) \).  
- If the center is not at the origin, we check whether the intercepts exist based on the given values.  
- If \( h^2 > a^2 \) or \( k^2 > b^2 \), there are **no intercepts** in that direction.

This method helps in quickly determining the points where the ellipse meets the coordinate axes.








## **Calculating Circle Intercepts**  

A circle in the Cartesian plane is generally represented by the **standard equation**:  

\[
(x - h)^2 + (y - k)^2 = r^2
\]

where:  
- \( (h, k) \) is the **center** of the circle.  
- \( r \) is the **radius** of the circle.  

To find **intercepts**, we determine where the circle intersects the **x-axis** and **y-axis**.

---

### **1. X-Intercepts**  
The **x-intercepts** occur where the circle crosses the x-axis, meaning \( y = 0 \).  
Substituting \( y = 0 \) into the equation:

\[
(x - h)^2 + (0 - k)^2 = r^2
\]

\[
(x - h)^2 + k^2 = r^2
\]

Solving for \( x \):

\[
(x - h)^2 = r^2 - k^2
\]

\[
x - h = \pm \sqrt{r^2 - k^2}
\]

\[
x = h \pm \sqrt{r^2 - k^2}
\]

Thus, the **x-intercepts** are:

\[
(h + \sqrt{r^2 - k^2}, 0) \quad \text{and} \quad (h - \sqrt{r^2 - k^2}, 0)
\]

**Conditions:**  
- If \( r^2 - k^2 \geq 0 \), there are **two x-intercepts**.  
- If \( r^2 - k^2 = 0 \), there is **one x-intercept (tangent to x-axis)**.  
- If \( r^2 - k^2 < 0 \), there are **no x-intercepts**.

---

### **2. Y-Intercepts**  
The **y-intercepts** occur where the circle crosses the y-axis, meaning \( x = 0 \).  
Substituting \( x = 0 \) into the equation:

\[
(0 - h)^2 + (y - k)^2 = r^2
\]

\[
h^2 + (y - k)^2 = r^2
\]

Solving for \( y \):

\[
(y - k)^2 = r^2 - h^2
\]

\[
y - k = \pm \sqrt{r^2 - h^2}
\]

\[
y = k \pm \sqrt{r^2 - h^2}
\]

Thus, the **y-intercepts** are:

\[
(0, k + \sqrt{r^2 - h^2}) \quad \text{and} \quad (0, k - \sqrt{r^2 - h^2})
\]

**Conditions:**  
- If \( r^2 - h^2 \geq 0 \), there are **two y-intercepts**.  
- If \( r^2 - h^2 = 0 \), there is **one y-intercept (tangent to y-axis)**.  
- If \( r^2 - h^2 < 0 \), there are **no y-intercepts**.

---

### **Special Case: Circle Centered at the Origin**  
If the circle is centered at the origin (\( h = 0, k = 0 \)), the equation simplifies to:

\[
x^2 + y^2 = r^2
\]

- **X-Intercepts:** \( (\pm r, 0) \)  
- **Y-Intercepts:** \( (0, \pm r) \)  

This means the circle **always** has x- and y-intercepts unless \( r = 0 \) (a single point at the origin).

---

### **Key Takeaways**  
1. **Set \( y = 0 \) to find x-intercepts** and **set \( x = 0 \) to find y-intercepts**.  
2. **Check the square root conditions** (\( r^2 - k^2 \) and \( r^2 - h^2 \)) to determine if intercepts exist.  
3. If the circle is centered at the origin, the intercepts are simply \( (\pm r, 0) \) and \( (0, \pm r) \).  

Understanding intercepts helps in **graphing** circles efficiently and analyzing their geometric properties.







## **Multiplying Matrices**  

Matrix multiplication is a fundamental operation in linear algebra with applications in **computer graphics,
machine learning, physics, and engineering**. Unlike scalar multiplication, multiplying two matrices 
involves **dot products** between rows and columns.

---

### **1. Conformability for Matrix Multiplication**  
Matrix multiplication is only **defined** when the number of **columns in the first matrix** matches the 
number of **rows in the second matrix**.

If **\( A \)** is an **\( m \times n \)** matrix and **\( B \)** is an **\( n \times p \)** matrix, the product **\( AB \)** is an **\( m \times p \)** matrix.

\[
A_{m \times n} \times B_{n \times p} = C_{m \times p}
\]

### **2. How to Multiply Matrices**  
Each element in the resulting matrix is obtained by computing the **dot product** of the corresponding 
row from the first matrix and the column from the second matrix.

For matrices:

\[
A =
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
\]

\[
B =
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}
\]

The product **\( C = AB \)** is computed as:

\[
C =
\begin{bmatrix}
(a_{11}b_{11} + a_{12}b_{21}) & (a_{11}b_{12} + a_{12}b_{22}) \\
(a_{21}b_{11} + a_{22}b_{21}) & (a_{21}b_{12} + a_{22}b_{22})
\end{bmatrix}
\]

Each element \( c_{ij} \) is obtained as:

\[
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
\]

where \( k \) runs over the shared dimension.

---

### **3. Example Calculation**
Consider:

\[
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\]

\[
B =
\begin{bmatrix}
7 & 8 \\
9 & 10 \\
11 & 12
\end{bmatrix}
\]

Since \( A \) is **\( 2 \times 3 \)** and \( B \) is **\( 3 \times 2 \)**, their product will be a **\( 2 \times 2 \)** matrix.

\[
C = AB =
\begin{bmatrix}
(1 \cdot 7 + 2 \cdot 9 + 3 \cdot 11) & (1 \cdot 8 + 2 \cdot 10 + 3 \cdot 12) \\
(4 \cdot 7 + 5 \cdot 9 + 6 \cdot 11) & (4 \cdot 8 + 5 \cdot 10 + 6 \cdot 12)
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
(7 + 18 + 33) & (8 + 20 + 36) \\
(28 + 45 + 66) & (32 + 50 + 72)
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
58 & 64 \\
139 & 154
\end{bmatrix}
\]

---

### **4. Properties of Matrix Multiplication**
- **Not Commutative:** \( AB \neq BA \) in general.  
- **Associative:** \( (AB)C = A(BC) \).  
- **Distributive:** \( A(B + C) = AB + AC \).  
- **Identity Matrix:** \( AI = IA = A \).  
- **Zero Matrix:** \( A0 = 0A = 0 \).

---

### **5. Special Cases**
- **Multiplying by the Identity Matrix (\( I \)):** Leaves the matrix unchanged.  
- **Multiplying by a Scalar:** Each element is multiplied by the scalar.  
- **Multiplying Square Matrices:** Used in transformations and system solving.  

Matrix multiplication is widely used in **transformations, linear systems, machine learning, and quantum mechanics**. 
Understanding it is key to advanced mathematics and data science.







## **Approximating Areas with the Right Riemann Sum**
The **Right Riemann Sum** is a method for approximating the area under a curve by summing up the areas 
of **rectangles** whose heights are determined by the function values at the **right endpoints** of 
subintervals. This approach is a fundamental concept in integral calculus and numerical analysis.

---

### **1. Understanding the Right Riemann Sum**  
Given a function \( f(x) \) over an interval \([a, b]\), the **Right Riemann Sum** approximates the integral:

\[
\int_a^b f(x) \,dx
\]

by dividing the interval into \( n \) subintervals, each of equal width:

\[
\Delta x = \frac{b - a}{n}
\]

Instead of using the function values at the **left endpoints**, the heights of the rectangles are determined by evaluating \( f(x) \) at the **right endpoints** of each subinterval.

The right endpoints are:

\[
x_i = a + i\Delta x, \quad i = 1, 2, \dots, n
\]

Thus, the **Right Riemann Sum** is given by:

\[
R_n = \sum_{i=1}^{n} f(x_i) \cdot \Delta x
\]

---

### **2. Example Calculation**  
Consider approximating the area under \( f(x) = x^2 \) on the interval \([1, 3]\) using the 
Right Riemann Sum with \( n = 4 \) subintervals.

#### **Step 1: Calculate \( \Delta x \)**
\[
\Delta x = \frac{3 - 1}{4} = \frac{2}{4} = 0.5
\]

#### **Step 2: Determine Right Endpoints**
\[
x_1 = 1.5, \quad x_2 = 2.0, \quad x_3 = 2.5, \quad x_4 = 3.0
\]

#### **Step 3: Evaluate \( f(x) = x^2 \) at Right Endpoints**
\[
f(1.5) = (1.5)^2 = 2.25
\]
\[
f(2.0) = (2.0)^2 = 4.00
\]
\[
f(2.5) = (2.5)^2 = 6.25
\]
\[
f(3.0) = (3.0)^2 = 9.00
\]

#### **Step 4: Compute the Right Riemann Sum**
\[
R_4 = (2.25 + 4.00 + 6.25 + 9.00) \times 0.5
\]
\[
= 21.5 \times 0.5 = 10.75
\]

Thus, the Right Riemann Sum approximation for the integral is **10.75**.

---

### **3. Properties of the Right Riemann Sum**
- **Overestimation vs. Underestimation**:
  - If \( f(x) \) is **increasing** on \([a, b]\), the Right Riemann Sum **overestimates** the true integral.
  - If \( f(x) \) is **decreasing**, it **underestimates** the integral.
- **Improving Accuracy**: Increasing \( n \) (the number of subintervals) makes the approximation **more accurate**.

---

### **4. Connection to Definite Integrals**
As \( n \to \infty \), the Right Riemann Sum approaches the **exact integral**:

\[
\lim_{n \to \infty} R_n = \int_a^b f(x) \,dx
\]

This forms the foundation of **definite integration** in calculus.

---

### **5. Applications of Right Riemann Sums**
- **Approximating Definite Integrals** when exact integration is difficult.
- **Physics**: Estimating displacement from velocity functions.
- **Economics**: Computing approximate revenues and costs.
- **Machine Learning & Data Science**: Approximating continuous models in discrete settings.

Right Riemann Sums provide a structured way to estimate areas and integrals, 
forming a stepping stone to more advanced numerical integration techniques 
like **trapezoidal and Simpson’s rules**.






## **Left and Right Riemann Sums in Sigma Notation**  

Riemann sums approximate the area under a curve by summing up the areas of rectangles. 
The two common types are **Left Riemann Sum** and **Right Riemann Sum**, which determine 
whether the left or right endpoint of each subinterval is used to compute the height of the rectangles.

---

### **1. Left Riemann Sum**
The **Left Riemann Sum** approximates the integral using the left endpoints of subintervals as sample points. The formula in sigma notation is:

\[
L_n = \sum_{i=0}^{n-1} f(x_i) \Delta x
\]

where:
- \( x_i = a + i \Delta x \) (left endpoints of subintervals),
- \( \Delta x = \frac{b-a}{n} \) (width of each subinterval),
- \( n \) is the number of subintervals.

The approximation underestimates the integral for increasing functions and overestimates for decreasing functions.

---

### **2. Right Riemann Sum**
The **Right Riemann Sum** uses the right endpoints of subintervals as sample points:

\[
R_n = \sum_{i=1}^{n} f(x_i) \Delta x
\]

where:
- \( x_i = a + i \Delta x \) (right endpoints of subintervals),
- \( \Delta x = \frac{b-a}{n} \).

This sum overestimates the integral for increasing functions and underestimates for decreasing functions.

---

### **Comparison and Limit as \( n \to \infty \)**
- As \( n \to \infty \), both sums converge to the **definite integral**:

\[
\int_a^b f(x) \,dx = \lim_{n \to \infty} L_n = \lim_{n \to \infty} R_n.
\]

- The **Midpoint Riemann Sum** provides a better approximation than both left and right sums.
- The **Trapezoidal Rule** and **Simpson’s Rule** offer further refinements for numerical integration.

---

Understanding these sums provides insight into **numerical integration**, a key 
concept in calculus and applications like physics, machine learning, and engineering.







## **Defining Definite Integrals Using Left and Right Riemann Sums**  

The **definite integral** of a function over an interval \([a, b]\) represents the exact area under the curve. 
This area is approximated using **Riemann sums**, specifically **Left Riemann Sum** and **Right Riemann Sum**, 
which take the function's values at the left and right endpoints of sub-intervals, respectively.

---

### **1. Definite Integral as a Limit of Riemann Sums**  
The definite integral of \( f(x) \) over \( [a, b] \) is defined as:

\[
\int_a^b f(x) \,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x
\]

where:
- \( \Delta x = \frac{b-a}{n} \) is the width of each subinterval,
- \( x_i^* \) is a sample point in each subinterval,
- The limit ensures the sum approximates the exact integral as \( n \to \infty \).

---

### **2. Left Riemann Sum Approximation**  
The **Left Riemann Sum** uses the **left endpoints** of each subinterval:

\[
L_n = \sum_{i=0}^{n-1} f(x_i) \Delta x
\]

where \( x_i = a + i \Delta x \).  
- It **underestimates** the integral when \( f(x) \) is increasing.  
- It **overestimates** when \( f(x) \) is decreasing.

---

### **3. Right Riemann Sum Approximation**  
The **Right Riemann Sum** uses the **right endpoints**:

\[
R_n = \sum_{i=1}^{n} f(x_i) \Delta x
\]

where \( x_i = a + i \Delta x \).  
- It **overestimates** the integral when \( f(x) \) is increasing.  
- It **underestimates** when \( f(x) \) is decreasing.

---

### **4. Convergence to the Definite Integral**  
- As \( n \to \infty \), both left and right Riemann sums approach the exact integral:

\[
\int_a^b f(x) \,dx = \lim_{n \to \infty} L_n = \lim_{n \to \infty} R_n.
\]

- The **Midpoint Rule**, **Trapezoidal Rule**, and **Simpson’s Rule** provide more accurate numerical integration methods.

---

Understanding definite integrals through Riemann sums is fundamental in calculus, forming the basis for 
applications in **physics, economics, and machine learning (e.g., continuous probability distributions 
and optimization algorithms).**







## **Graphing the Inverse Sine Function**  

The **inverse sine function**, denoted as \( y = \sin^{-1}(x) \) or \( y = \arcsin(x) \), 
is the inverse of the sine function when restricted to its **principal domain**. 
Understanding its graph requires analyzing its **domain, range, symmetry, and key points**.

---

### **1. Definition and Domain-Range**  
The inverse sine function is defined as:

\[
y = \sin^{-1}(x) \quad \text{if and only if} \quad \sin(y) = x
\]

with the following properties:
- **Domain**: \( -1 \leq x \leq 1 \) (since sine values range between -1 and 1)
- **Range**: \( -\frac{\pi}{2} \leq y \leq \frac{\pi}{2} \) (chosen for a one-to-one function)

---

### **2. Key Points on the Graph**  
To construct the graph, consider key points:
\[
\begin{aligned}
\sin^{-1}(-1) &= -\frac{\pi}{2} \\
\sin^{-1}(-\frac{\sqrt{3}}{2}) &= -\frac{\pi}{3} \\
\sin^{-1}(-\frac{1}{2}) &= -\frac{\pi}{6} \\
\sin^{-1}(0) &= 0 \\
\sin^{-1}(\frac{1}{2}) &= \frac{\pi}{6} \\
\sin^{-1}(\frac{\sqrt{3}}{2}) &= \frac{\pi}{3} \\
\sin^{-1}(1) &= \frac{\pi}{2}
\end{aligned}
\]

---

### **3. Symmetry and Shape**  
- The graph is **increasing** throughout its domain.
- It is **symmetric about the origin** because the function is **odd**:  
  \[
  \sin^{-1}(-x) = -\sin^{-1}(x)
  \]
- The curve passes through **(0,0)** and is **bounded** by \( (-1, -\frac{\pi}{2}) \) and \( (1, \frac{\pi}{2}) \).

---

### **4. Sketching the Graph**  
1. **Plot the key points** listed above.
2. The function starts at \( (-1, -\frac{\pi}{2}) \), smoothly increases, and ends at \( (1, \frac{\pi}{2}) \).
3. The curve is **steepest at \( x=0 \)** and flattens towards the endpoints.

---

### **5. Relationship with \( y = \sin(x) \)**
- The graph of \( y = \sin^{-1}(x) \) is the **reflection** of \( y = \sin(x) \) (restricted to \( -\frac{\pi}{2} \leq x \leq \frac{\pi}{2} \)) across the line \( y = x \).
- This highlights the **inverse function property**.

---

### **6. Applications**  
- **Trigonometry & Geometry**: Used in angle measurements.
- **Physics & Engineering**: Describes wave behavior and oscillations.
- **Machine Learning**: Applied in activation functions and signal processing.

---

By mastering the graph of \( y = \sin^{-1}(x) \), inverse trigonometric transformations become intuitive, 
aiding deeper mathematical understanding.







## **Solving Elementary Quadratic Inequalities**  

Quadratic inequalities involve expressions of the form:  

\[
ax^2 + bx + c \; \text{(inequality sign)} \; 0
\]

where the inequality sign can be \( <, \leq, >, \geq \). The solution represents the range of 
\( x \)-values that satisfy the inequality.

---

### **1. General Steps for Solving Quadratic Inequalities**
To solve a quadratic inequality, follow these steps:

#### **Step 1: Rewrite in Standard Form**
Ensure the inequality is in standard form:

\[
ax^2 + bx + c \; \text{(inequality sign)} \; 0
\]

Example: Solve \( x^2 - 5x + 6 > 0 \).

#### **Step 2: Solve the Corresponding Quadratic Equation**
Find the roots of the quadratic equation by setting:

\[
ax^2 + bx + c = 0
\]

Using factoring, completing the square, or the quadratic formula:

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

For \( x^2 - 5x + 6 = 0 \):

\[
(x - 2)(x - 3) = 0 \quad \Rightarrow \quad x = 2, 3
\]

#### **Step 3: Determine the Sign of Each Interval**
The roots divide the number line into intervals. Test a value in each interval to determine if the inequality holds.

For \( x^2 - 5x + 6 > 0 \), consider:
- **Interval 1**: \( (-\infty, 2) \) → Choose \( x = 0 \), \( (0 - 2)(0 - 3) = ( -2)( -3) = 6 \) (Positive ✅)
- **Interval 2**: \( (2, 3) \) → Choose \( x = 2.5 \), \( (2.5 - 2)(2.5 - 3) = (0.5)(-0.5) = -0.25 \) (Negative ❌)
- **Interval 3**: \( (3, \infty) \) → Choose \( x = 4 \), \( (4 - 2)(4 - 3) = (2)(1) = 2 \) (Positive ✅)

#### **Step 4: Write the Solution in Interval Notation**
Since the inequality is **strictly greater** than zero, the solution includes intervals where the expression is **positive**:

\[
(-\infty, 2) \cup (3, \infty)
\]

For **\( \leq \) or \( \geq \) inequalities**, include the roots as solutions.

---

### **2. Special Cases**
1. **No Real Solutions**: If the quadratic has no real roots (i.e., \( b^2 - 4ac < 0 \)), the parabola does not cross the \( x \)-axis. The entire function is either positive or negative.
2. **Perfect Square Cases**: If the quadratic factors into \( (x - r)^2 \), the sign does not change around \( r \), affecting the solution set.

---

### **3. Graphical Interpretation**
A quadratic function represents a **parabola**:
- If **\( a > 0 \)**: Opens **up**.
- If **\( a < 0 \)**: Opens **down**.

- \( ax^2 + bx + c > 0 \) means **above** the x-axis.
- \( ax^2 + bx + c < 0 \) means **below** the x-axis.

---

### **4. Application**
Quadratic inequalities appear in:
- **Physics** (projectile motion, motion constraints).
- **Economics** (profit/loss functions).
- **Machine Learning** (support vector machine boundaries).

By mastering these steps, quadratic inequalities become intuitive, making advanced problem-solving easier.









## **Simplifying Expressions Using the Secant-Tangent Identity**  

The **secant-tangent identity** is a fundamental trigonometric identity that establishes a direct 
relationship between the secant and tangent functions. It is given by:

\[
\sec^2\theta = 1 + \tan^2\theta
\]

This identity is derived from the Pythagorean identity:

\[
\sin^2\theta + \cos^2\theta = 1
\]

by dividing every term by \( \cos^2\theta \):

\[
\frac{\sin^2\theta}{\cos^2\theta} + \frac{\cos^2\theta}{\cos^2\theta} = \frac{1}{\cos^2\theta}
\]

which simplifies to:

\[
\tan^2\theta + 1 = \sec^2\theta
\]

---

### **1. Using the Secant-Tangent Identity for Simplification**
This identity is useful for simplifying trigonometric expressions that involve \( \sec^2\theta \) or \( \tan^2\theta \). Let's look at some examples.

#### **Example 1: Simplifying an Expression**
Simplify the expression:

\[
\sec^2\theta - \tan^2\theta
\]

Using the identity:

\[
\sec^2\theta = 1 + \tan^2\theta
\]

Substituting:

\[
(1 + \tan^2\theta) - \tan^2\theta = 1
\]

Thus, the given expression simplifies to:

\[
1
\]

---

#### **Example 2: Expressing in Terms of \( \tan\theta \)**
Simplify:

\[
\frac{\sec^2\theta}{\sec^2\theta - 1}
\]

Using the identity \( \sec^2\theta - 1 = \tan^2\theta \), we rewrite:

\[
\frac{\sec^2\theta}{\tan^2\theta}
\]

Using \( \sec^2\theta = 1 + \tan^2\theta \):

\[
\frac{1 + \tan^2\theta}{\tan^2\theta} = 1 + \frac{1}{\tan^2\theta}
\]

which can be rewritten using cotangent:

\[
1 + \cot^2\theta
\]

---

#### **Example 3: Converting Between Secant and Tangent**
Simplify:

\[
\frac{1}{\sec^2\theta - 1}
\]

Using \( \sec^2\theta - 1 = \tan^2\theta \), we get:

\[
\frac{1}{\tan^2\theta}
\]

which simplifies to:

\[
\cot^2\theta
\]

---

### **2. Application of the Secant-Tangent Identity**
This identity appears in:
- **Trigonometric Integrals**: Used in calculus for integral evaluations.
- **Physics**: Wave motion and optics.
- **Engineering**: Signal processing and AC circuit analysis.

By recognizing the secant-tangent identity, trigonometric expressions become easier to manipulate, 
making calculations more efficient.






## **Simplifying Trigonometric Expressions Using the Cotangent-Cosecant Identity**  

### **1. Understanding the Cotangent-Cosecant Identity**  
The cotangent (\(\cot x\)) and cosecant (\(\csc x\)) functions are defined as:  
\[
\cot x = \frac{\cos x}{\sin x}, \quad \csc x = \frac{1}{\sin x}
\]  
A key identity involving these functions is:  
\[
1 + \cot^2 x = \csc^2 x
\]  
This identity is derived from the Pythagorean identity \( \sin^2 x + \cos^2 x = 1 \).  

---

### **2. Techniques for Simplification**  
When simplifying expressions involving \(\cot x\) and \(\csc x\), common strategies include:  
- **Rewriting in terms of sine and cosine:** Express cotangent and cosecant in terms of sine and cosine to identify common factors.  
- **Factoring identities:** Use the identity \( 1 + \cot^2 x = \csc^2 x \) to factor and simplify expressions.  
- **Rationalizing denominators:** If an expression contains a fraction with trigonometric functions, rationalizing may simplify it.  

---

### **3. Examples of Simplification**  

#### **Example 1: Simplify**  
\[
\frac{1}{\cot x - \csc x}
\]  
**Solution:**  
Rewriting in terms of sine and cosine:  
\[
\cot x - \csc x = \frac{\cos x}{\sin x} - \frac{1}{\sin x} = \frac{\cos x - 1}{\sin x}
\]  
So the given expression becomes:  
\[
\frac{1}{\frac{\cos x - 1}{\sin x}} = \frac{\sin x}{\cos x - 1}
\]  

#### **Example 2: Simplify**  
\[
\frac{\cot^2 x}{\csc^2 x}
\]  
Using the identity \( 1 + \cot^2 x = \csc^2 x \), we rewrite:  
\[
\frac{\cot^2 x}{\csc^2 x} = \frac{\csc^2 x - 1}{\csc^2 x} = 1 - \frac{1}{\csc^2 x}
\]  
Since \( \frac{1}{\csc^2 x} = \sin^2 x \), the expression simplifies to:  
\[
1 - \sin^2 x = \cos^2 x
\]  

---

### **4. Application in Problem Solving**  
These simplifications are useful in calculus, solving integrals, and proving trigonometric identities. 
Mastering them makes solving trigonometric equations more intuitive and efficient.  





## **Solving Quadratic Inequalities Using the Sign Table Method**  

### **Understanding Quadratic Inequalities**  
A quadratic inequality takes the form:  
\[
ax^2 + bx + c \ \{>, <, \geq, \leq\} \ 0
\]  
where \(a, b, c\) are real numbers and \(a \neq 0\). The goal is to determine the values of \(x\)
that satisfy the inequality.  

### **Step 1: Solve the Corresponding Quadratic Equation**  
Set the quadratic expression equal to zero and solve for \(x\):  
\[
ax^2 + bx + c = 0
\]  
The solutions (roots) partition the number line into intervals.

### **Step 2: Create a Sign Table**  
1. **Plot the roots** on the number line, dividing it into intervals.  
2. **Choose a test point** from each interval and substitute it into the quadratic expression to determine its sign (positive or negative).  
3. **Analyze the sign pattern** based on the parabola's orientation:  
   - If \(a > 0\), the parabola opens upward (\(\cup\)).  
   - If \(a < 0\), the parabola opens downward (\(\cap\)).  

### **Step 3: Determine the Solution Set**  
- For inequalities like \(ax^2 + bx + c > 0\), select intervals where the quadratic expression is **positive**.  
- For \(ax^2 + bx + c < 0\), select intervals where the expression is **negative**.  
- Include or exclude boundary points based on **strict (\(<,>\)) or inclusive (\(\leq, \geq\)) inequalities**.  

### **Example**  
Solve:  
\[
x^2 - 5x + 6 \leq 0
\]  
1. **Solve \(x^2 - 5x + 6 = 0\)**  
   Factor: \((x-2)(x-3) = 0\)  
   Roots: \(x = 2, 3\)  
2. **Sign Table Analysis**  
   - Intervals: \( (-\infty, 2), (2,3), (3, \infty) \)  
   - Choose test points: \(x = 0, 2.5, 4\)  
   - Evaluate sign of \((x-2)(x-3)\) in each interval.  
   - The expression is **negative** in \((2,3)\), **positive** otherwise.  
3. **Conclusion**  
   - Since the inequality is \(\leq 0\), include the roots:  
   \[
   x \in [2,3]
   \]  

This method provides a structured way to solve quadratic inequalities graphically and analytically.






## **Solving Quadratic Inequalities from Graphs**  

### **Understanding Quadratic Inequalities**  
A quadratic inequality is an expression of the form:  
\[
ax^2 + bx + c \ \{>, <, \geq, \leq\} \ 0
\]  
where \( a, b, c \) are real numbers and \( a \neq 0 \). The goal is to find the values of \( x \) 
that satisfy the inequality by analyzing the graph of the quadratic function.  

### **Step 1: Graph the Quadratic Function**  
- Convert the inequality into an equation:  
  \[
  y = ax^2 + bx + c
  \]  
- Graph \( y = ax^2 + bx + c \), which is a **parabola**.  
  - If \( a > 0 \), the parabola **opens upward** (\(\cup\)).  
  - If \( a < 0 \), the parabola **opens downward** (\(\cap\)).  

### **Step 2: Identify the x-Intercepts (Roots)**  
- Solve \( ax^2 + bx + c = 0 \) to find the points where the graph intersects the x-axis.  
- These roots **divide the x-axis into intervals** where the function is either positive or negative.  

### **Step 3: Determine Solution Regions Based on the Inequality**  
- **For \( ax^2 + bx + c > 0 \)** → Find intervals where the graph is **above** the x-axis.  
- **For \( ax^2 + bx + c < 0 \)** → Find intervals where the graph is **below** the x-axis.  
- **For \( ax^2 + bx + c \geq 0 \) or \( \leq 0 \)** → Include the roots (where \( y = 0 \)) in the solution set.  

### **Example**  
Solve:  
\[
x^2 - 4x + 3 \leq 0
\]  
1. **Graph the function \( y = x^2 - 4x + 3 \)**  
   - Factor: \( (x-1)(x-3) = 0 \)  
   - Roots: \( x = 1, 3 \)  
   - Parabola opens **upward** since \( a = 1 > 0 \).  

2. **Analyze the Graph**  
   - The parabola is **below the x-axis** between \( x = 1 \) and \( x = 3 \).  
   - The function is **nonpositive** in this interval.  

3. **Write the Solution**  
   - Since the inequality is \( \leq 0 \), include the roots:  
   \[
   x \in [1,3]
   \]  

### **Key Takeaways**  
- Graphing helps visualize where the quadratic expression is positive or negative.  
- The roots **partition the number line**, allowing easy identification of solution intervals.  
- **Include or exclude** boundary points based on the inequality sign (\(<\) vs. \( \leq \)).






## **Calculating $`\frac{dy}{dx}`$ Using $`\frac{dx}{dy}`$, Deep Dive**  

When given \( \frac{dx}{dy} \), we can find \( \frac{dy}{dx} \) using the reciprocal relationship:

\[
\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}, \quad \text{provided } \frac{dx}{dy} \neq 0.
\]

This approach is particularly useful in cases where it is easier to differentiate \( x \) with respect to \( y \) rather than differentiating \( y \) with respect to \( x \), such as:  

1. **Implicit Differentiation**: When an equation is given in terms of \( x \) and \( y \), sometimes differentiating \( x \) with respect to \( y \) is more straightforward.  
2. **Parametric Equations**: If a function is given parametrically as \( x = f(t) \) and \( y = g(t) \), then:

   \[
   \frac{dx}{dt}, \quad \frac{dy}{dt} \quad \Rightarrow \quad \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}.
   \]

3. **Inverse Functions**: If \( y = f^{-1}(x) \) is the inverse of \( x = f(y) \), then:

   \[
   \frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}.
   \]

#### **Example: Inverse Function Approach**
Suppose \( x = y^3 + 2y \). To find \( \frac{dy}{dx} \):

1. Differentiate both sides with respect to \( y \):

   \[
   \frac{dx}{dy} = 3y^2 + 2.
   \]

2. Take the reciprocal:

   \[
   \frac{dy}{dx} = \frac{1}{3y^2 + 2}.
   \]

This method provides a simple way to compute derivatives when \( x \) is given explicitly in terms of \( y \).







## **The Fundamental Theorem of Algebra for Quadratic Equations with Real or Imaginary Roots**  

#### **The Fundamental Theorem of Algebra (FTA)**  
The **Fundamental Theorem of Algebra** states that every polynomial equation of degree \( n \) with complex coefficients has exactly \( n \) 
complex roots (counting multiplicities).  

For a **quadratic equation** of the form:  

\[
ax^2 + bx + c = 0, \quad a \neq 0
\]

this means there are always **two roots** in the set of complex numbers \( \mathbb{C} \). These roots can be either:  
1. **Both real**, or  
2. **A pair of complex conjugates (imaginary roots)**.  

#### **The Discriminant and Root Types**  
The nature of the roots depends on the **discriminant** \( \Delta \), given by:

\[
\Delta = b^2 - 4ac.
\]

- **If \( \Delta > 0 \):** Two distinct **real roots**.  
- **If \( \Delta = 0 \):** One repeated **real root**.  
- **If \( \Delta < 0 \):** Two **complex conjugate roots** (imaginary).  

### **1. Quadratic Equations with Real Roots**
For real roots, the discriminant must be **non-negative** (\( \Delta \geq 0 \)).  

#### **Case 1: Two Distinct Real Roots (\( \Delta > 0 \))**
Example: Solve \( x^2 - 5x + 6 = 0 \).  
- Coefficients: \( a = 1 \), \( b = -5 \), \( c = 6 \).  
- Compute the discriminant:

\[
\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1 > 0.
\]

- Roots:

\[
x = \frac{-(-5) \pm \sqrt{1}}{2(1)} = \frac{5 \pm 1}{2}.
\]

\[
x = 3, \quad x = 2.
\]

#### **Case 2: One Repeated Real Root (\( \Delta = 0 \))**
Example: Solve \( x^2 - 4x + 4 = 0 \).  
- Coefficients: \( a = 1 \), \( b = -4 \), \( c = 4 \).  
- Compute the discriminant:

\[
\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0.
\]

- Root:

\[
x = \frac{4 \pm 0}{2(1)} = \frac{4}{2} = 2.
\]

This means \( x = 2 \) is a **double root**.

---

### **2. Quadratic Equations with Imaginary (Complex) Roots**
If the discriminant is **negative** (\( \Delta < 0 \)), the roots involve the **imaginary unit \( i \)**, where:

\[
i = \sqrt{-1}.
\]

#### **Case 3: Two Complex Conjugate Roots (\( \Delta < 0 \))**
Example: Solve \( x^2 + x + 1 = 0 \).  
- Coefficients: \( a = 1 \), \( b = 1 \), \( c = 1 \).  
- Compute the discriminant:

\[
\Delta = (1)^2 - 4(1)(1) = 1 - 4 = -3 < 0.
\]

- Roots:

\[
x = \frac{-1 \pm \sqrt{-3}}{2(1)} = \frac{-1 \pm i\sqrt{3}}{2}.
\]

Since \( \sqrt{-3} = i\sqrt{3} \), the roots are:

\[
x = \frac{-1 + i\sqrt{3}}{2}, \quad x = \frac{-1 - i\sqrt{3}}{2}.
\]

These are **complex conjugates**.

---

### **Conclusion**
By the **Fundamental Theorem of Algebra**, every quadratic equation has exactly **two roots** in \( \mathbb{C} \),
whether real or complex. The **discriminant \( \Delta \)** determines whether the roots are:  
- **Real (distinct or repeated) if \( \Delta \geq 0 \)**.  
- **Complex conjugates (imaginary) if \( \Delta < 0 \)**.  

Thus, quadratic equations are always **solvable** in \( \mathbb{C} \), even if their roots are not in \( \mathbb{R} \).






## 

















































