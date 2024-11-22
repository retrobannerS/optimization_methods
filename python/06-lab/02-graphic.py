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

plt.figure(figsize=(7, 4.5))

a1, b1 = -1 / 2, 7
a2, b2 = 5 / 3, 5
a3, b3 = 2 / 3, -4
a4, b4 = float("inf"), 0
a5, b5 = 0, 0
g1, g2 = 1, 1

a = [a1, a2, a3, a4, a5]
b = [b1, b2, b3, b4, b5]

X = np.linspace(-20, 100, 1000)
line1 = a1 * X + b1
line2 = a2 * X + b2
line3 = a3 * X + b3
line4 = np.zeros(1000)
line5 = a5 * X + b5
line6 = np.ones(1000) * 9

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

plt.plot(X, line1, label=r"$x_2 = -\frac{1}{2}x_1 + 7$")
plt.plot(X, line2, label=r"$x_2 = \frac{5}{3}x_1 + 5$")
plt.plot(X, line3, label=r"$x_2 = \frac{2}{3}x_1 - 4$")
plt.plot(line4, X, label=r"$x_1 = 0$", lw=5)
plt.plot(X, line5, label=r"$x_2 = 0$", lw=5)
plt.plot(line6, X, label=r"$x_1 = 9$")

plt.fill_between(
    X, line1, -1, color="cyan", alpha=0.2, label=r"Область $x_2 \leq -\frac{1}{2}x_1 + 7$"
)
plt.fill_between(
    X, line2, -1, color="green", alpha=0.2, label=r"Область $x_2 \leq \frac{5}{3}x_1 + 5$"
)
plt.fill_between(
    X, line3, 15, color="purple", alpha=0.2, label=r"Область $x_2 \leq \frac{2}{3}x_1 - 4$"
)
plt.axvspan(0, 9, color='red', alpha=0.2, label=r"Область $x_1 \leq 9$")

intersections = []
for i in range(len(a)):
    for j in range(len(a)):
        if i < j:
            intersections += [find_intersection(a[i], b[i], a[j], b[j])]

intersections += [(9, 0), (9, 2.5), (9, 2)]

intersections = [(x_1, x_2) for (x_1, x_2) in intersections if 0 <= x_1 <= 9 and x_2 >= 0]

for i, (x_1, x_2) in enumerate(intersections, start=1):
    plt.plot(x_1, x_2, 'ko')
    plt.annotate(f'\\textbf {i}: ({x_1:.2f}, {x_2:.2f})', xy=(x_1, x_2), xytext=(x_1 + 0.3, x_2 + 0.4),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))


plt.xlabel(r"$x_1$", fontsize=14)
plt.ylabel(r"$x_2$", fontsize=14)

plt.xlim(-0.01, 15)
plt.ylim(-0.01, 10)
plt.legend(ncol=2)
plt.gca().set_aspect("equal")
plt.show()

def F(x_1, x_2):
    return g1 * x_1 + g2 * x_2

for i, (x_1, x_2) in enumerate(intersections, start=1):
    if i not in [2, 6]:
        print(f"Значение F в точке {i} равно {F(x_1, x_2):.2f}")