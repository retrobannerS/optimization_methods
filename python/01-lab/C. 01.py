import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)
plt.rc(
    "text.latex",
    preamble=r"""
\usepackage[english, russian]{babel}
\usepackage[utf8]{inputenc}
""",
)
plt.style.use("seaborn-v0_8")


def find_intersection(a1, b1, a2, b2):
    x_1 = (b2 - b1) / (a1 - a2)
    x_2 = a1 * x_1 + b1 if a1 != float("inf") else a2 * x_1 + b2
    return x_1, x_2


a1, b1 = 1, 11
a2, b2 = 1/4, -2
a3, b3 = float("inf"), 0
a4, b4 = 0, 0
g1, g2 = 3, 1
a = [a1, a2, a3, a4]
b = [b1, b2, b3, b4]


X = np.linspace(-20, 100, 1000)
line1 = a1 * X + b1
line2 = a2 * X + b2
line3 = a3 * X + b3
line3 = np.zeros(1000)
line4 = a4 * X + b4

fix, ax = plt.subplots()
plt.quiver(
    0,
    0,
    g1,
    g2,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="black",
    label=r"$\overrightarrow{grad}\ F(x_1,x_2)$",
)


ax.plot(X, line1, label=r"$x_2 = x_1 + 11$")
ax.plot(X, line2, label=r"$x_2 = \frac{1}{4}x_1 - 2$")
ax.plot(line3, X, label=r"$x_1 = 0$")
ax.plot(X, line4, label=r"$x_2 = 0$")
ax.fill_between(
    X, line1, 50, color="blue", alpha=0.2, label=r"Область $x_2 \geq x_1 + 11$"
)
ax.fill_between(
    X,
    line2,
    -20,
    color="red",
    alpha=0.2,
    label=r"Область $x_2 \leq \frac{1}{4}x_1 - 2$",
)

intersections = []
for i in range(len(a)):
    for j in range(len(a)):
        if i < j:
            intersections += [find_intersection(a[i], b[i], a[j], b[j])]

intersections = [(x_1, x_2) for (x_1, x_2) in intersections if x_1 >= 0 and x_2 >= 0]

for i, (x_1, x_2) in enumerate(intersections, start=1):
    plt.plot(x_1, x_2, "ko")
    plt.annotate(
        f"{i}: ({x_1:.2f}, {x_2:.2f})",
        xy=(x_1, x_2),
        xytext=(x_1 + 0.3, x_2 + 0.4),
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )

ax.set_xlim(-0.01, 30)
ax.set_ylim(-0.01, 30)
ax.set_xlabel(r"$\mathbf{x_1}$", fontsize=12)
ax.set_ylabel(r"$\mathbf{x_2}$", fontsize=12)
ax.legend(loc="upper right", fontsize=12, ncol=2)
plt.gca().set_aspect("equal")
plt.show()


def F(x_1, x_2):
    return g1 * x_1 + g2 * x_2


for i, (x_1, x_2) in enumerate(intersections, start=1):
    if i == 1 or i == 3:
        print(f"Значение F в точке {i} равно {F(x_1, x_2):.2f}")
