#!/usr/bin/env python3
"""Generate all figures for the mechanics exercise book."""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon, Rectangle
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

OUT = os.path.dirname(os.path.abspath(__file__))

INK = "#1f2937"
BLUE = "#1f4e79"
RED = "#b23a48"
GREEN = "#2f6b4f"
ORANGE = "#c25b2a"
PURPLE = "#6b4c9a"
GRAY = "#6b7280"
LIGHT = "#dfe7ef"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "font.size": 11,
    "axes.linewidth": 0.9,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "text.color": INK,
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


def arrow(ax, start, vec, color=INK, lw=1.8, ls="-", label=None,
          label_off=(0.06, 0.06), label_color=None, fontsize=12, zorder=5,
          arrowstyle="-|>", mutation=12):
    start = np.asarray(start, dtype=float)
    vec = np.asarray(vec, dtype=float)
    end = start + vec
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle=arrowstyle, color=color, lw=lw,
                                linestyle=ls, shrinkA=0, shrinkB=0,
                                mutation_scale=mutation),
                zorder=zorder)
    if label:
        ax.text(end[0] + label_off[0], end[1] + label_off[1], label,
                color=label_color or color, fontsize=fontsize, zorder=zorder + 1)
    return end


def clean_axes(ax, equal=True):
    ax.set_aspect("equal" if equal else "auto")
    ax.axis("off")


# ---------------------------------------------------------------------------
# 1. Vector addition and subtraction
# ---------------------------------------------------------------------------
def fig_vector_addition():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.1))
    for ax in axes:
        clean_axes(ax)
        ax.set_xlim(-0.6, 5.6)
        ax.set_ylim(-2.2, 4.2)

    ax = axes[0]
    a = np.array([3.1, 0.7])
    b = np.array([1.4, 2.5])
    O = np.array([0.3, 0.2])
    A = O + a
    B = A + b
    arrow(ax, O, a, BLUE, label=r"$\vec{a}$", label_off=(-0.25, 0.12))
    arrow(ax, A, b, RED, label=r"$\vec{b}$", label_off=(0.06, 0.06))
    arrow(ax, O, a + b, GREEN, lw=2.3, label=r"$\vec{a}+\vec{b}$",
          label_off=(0.05, -0.32))
    ax.text(O[0] - 0.18, O[1] - 0.28, r"$O$", fontsize=12)
    ax.text(A[0] - 0.05, A[1] - 0.3, r"$A$", fontsize=12)
    ax.text(B[0] + 0.02, B[1] + 0.08, r"$B$", fontsize=12)
    ax.set_title("Triangle rule", fontsize=12, color=INK)

    ax = axes[1]
    a = np.array([3.1, 0.7])
    b = np.array([1.4, 2.5])
    O = np.array([0.3, 0.2])
    A = O + a
    B = O + b
    S = O + a + b
    arrow(ax, O, a, BLUE, label=r"$\vec{a}$", label_off=(-0.05, -0.32))
    arrow(ax, O, b, RED, label=r"$\vec{b}$", label_off=(-0.25, 0.12))
    arrow(ax, O, a + b, GREEN, lw=2.3, label=r"$\vec{a}+\vec{b}$",
          label_off=(0.05, 0.08))
    arrow(ax, B, a, BLUE, lw=1.1, ls="--")
    arrow(ax, A, b, RED, lw=1.1, ls="--")
    arrow(ax, A, b - a, PURPLE, lw=1.7, label=r"$\vec{b}-\vec{a}$",
          label_off=(0.05, -0.35))
    ax.text(O[0] - 0.18, O[1] - 0.28, r"$O$", fontsize=12)
    ax.set_title("Parallelogram rule", fontsize=12, color=INK)
    save(fig, "01_vector_addition.pdf")


# ---------------------------------------------------------------------------
# 2. Cartesian coordinates in 3D
# ---------------------------------------------------------------------------
def fig_cartesian_3d():
    fig = plt.figure(figsize=(6.2, 4.6))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_box_aspect((1.15, 1, 0.95))
    ax.set_axis_off()
    L = 3.2
    ax.quiver(0, 0, 0, L, 0, 0, color=INK, lw=1.2, arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, L, 0, color=INK, lw=1.2, arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 0, L, color=INK, lw=1.2, arrow_length_ratio=0.08)
    ax.text(L + 0.15, 0, 0, r"$x$", fontsize=12)
    ax.text(0, L + 0.15, 0, r"$y$", fontsize=12)
    ax.text(0, 0, L + 0.15, r"$z$", fontsize=12)

    P = np.array([2.2, 2.4, 1.9])
    ax.quiver(0, 0, 0, *P, color=RED, lw=2.2, arrow_length_ratio=0.06)
    ax.text(P[0] + 0.08, P[1] + 0.05, P[2] + 0.12, r"$M$", color=RED, fontsize=12)
    # dashed projections
    ax.plot([P[0], P[0]], [P[1], P[1]], [0, P[2]], color=GRAY, lw=0.9, ls="--")
    ax.plot([P[0], P[0]], [0, P[1]], [0, 0], color=GRAY, lw=0.9, ls="--")
    ax.plot([0, P[0]], [P[1], P[1]], [0, 0], color=GRAY, lw=0.9, ls="--")
    ax.plot([P[0], P[0]], [P[1], P[1]], [0, 0], color=GRAY, lw=0.9, ls=":")
    ax.plot([P[0], 0], [P[1], P[1]], [0, 0], color=GRAY, lw=0.9, ls="--")
    ax.scatter([P[0]], [P[1]], [0], color=GRAY, s=12)
    ax.text(P[0] + 0.05, P[1] + 0.12, -0.22, r"$x$", color=GRAY, fontsize=10)
    ax.text(P[0] + 0.12, P[1] + 0.12, P[2] / 2, r"$z$", color=GRAY, fontsize=10)
    ax.text(P[0] + 0.12, P[1] / 2, 0.05, r"$y$", color=GRAY, fontsize=10)
    ax.text(0.08, -0.28, -0.25, r"$O$", fontsize=12)
    ax.set_xlim(-0.3, L)
    ax.set_ylim(-0.3, L)
    ax.set_zlim(-0.3, L)
    save(fig, "02_cartesian_3d.pdf")


# ---------------------------------------------------------------------------
# 3. Dot product and cross product
# ---------------------------------------------------------------------------
def fig_dot_cross():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.2))
    for ax in axes:
        clean_axes(ax)
        ax.set_xlim(-0.7, 5.2)
        ax.set_ylim(-1.0, 4.4)

    ax = axes[0]
    O = np.array([0.2, 0.2])
    a = np.array([4.2, 0.0])
    b = np.array([2.2, 2.8])
    arrow(ax, O, a, BLUE, label=r"$\vec{a}$", label_off=(0.06, -0.38))
    arrow(ax, O, b, RED, label=r"$\vec{b}$", label_off=(0.05, 0.08))
    proj = np.dot(b, a) / np.dot(a, a) * a
    P = O + proj
    ax.plot([O[0] + b[0], P[0]], [O[1] + b[1], P[1]], color=GRAY, lw=0.9, ls="--")
    arrow(ax, O, proj, GREEN, lw=2.0, label=r"$b\cos\theta$",
          label_off=(-0.15, -0.45))
    ax.add_patch(Arc(O, 1.35, 1.35, theta1=0, theta2=np.degrees(np.arctan2(b[1], b[0])),
                     color=INK, lw=0.9))
    ax.text(O[0] + 1.55, O[1] + 0.52, r"$\theta$", fontsize=12)
    ax.text(2.1, 1.75, r"$\vec{a}\cdot\vec{b}=ab\cos\theta$", fontsize=11, color=GREEN)
    ax.set_title("Scalar (dot) product", fontsize=12)

    ax = axes[1]
    O = np.array([0.3, 0.3])
    a = np.array([3.8, 0.0])
    b = np.array([2.0, 2.4])
    arrow(ax, O, a, BLUE, label=r"$\vec{a}$", label_off=(0.06, -0.38))
    arrow(ax, O, b, RED, label=r"$\vec{b}$", label_off=(0.05, 0.08))
    ax.add_patch(Arc(O, 1.2, 1.2, theta1=0, theta2=np.degrees(np.arctan2(b[1], b[0])),
                     color=INK, lw=0.9))
    ax.text(O[0] + 1.38, O[1] + 0.46, r"$\theta$", fontsize=12)
    C = np.array([2.6, 3.55])
    ax.scatter([C[0]], [C[1]], s=190, facecolor="white", edgecolor=PURPLE, lw=1.6, zorder=6)
    ax.scatter([C[0]], [C[1]], s=22, color=PURPLE, zorder=7)
    ax.text(C[0] + 0.22, C[1] - 0.05, r"$\vec{c}=\vec{a}\times\vec{b}$", color=PURPLE, fontsize=12)
    ax.text(C[0] - 0.18, C[1] - 0.55, r"(out of page)", color=PURPLE, fontsize=9)
    ax.text(2.2, 1.35, r"$|\vec{c}|=ab\sin\theta$", fontsize=11, color=PURPLE)
    ax.set_title("Vector (cross) product", fontsize=12)
    save(fig, "03_dot_cross.pdf")


# ---------------------------------------------------------------------------
# 4. Trajectory frame
# ---------------------------------------------------------------------------
def fig_trajectory_frame():
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    clean_axes(ax)
    ax.set_xlim(-0.5, 7.2)
    ax.set_ylim(-0.6, 4.6)
    t = np.linspace(0, 1, 200)
    x = 0.6 + 6.0 * t
    y = 0.5 + 2.6 * np.sin(np.pi * t) + 0.8 * t
    ax.plot(x, y, color=INK, lw=1.8)
    ax.text(x[-1] + 0.08, y[-1], "trajectory", fontsize=10, color=INK)

    i = 125
    M = np.array([x[i], y[i]])
    dx = x[i + 1] - x[i - 1]
    dy = y[i + 1] - y[i - 1]
    tang = np.array([dx, dy])
    tang = tang / np.linalg.norm(tang)
    norm = np.array([-tang[1], tang[0]])
    if norm[1] < 0:
        norm = -norm

    O = np.array([0.2, 0.2])
    arrow(ax, O, M - O, GRAY, lw=1.4, label=r"$\vec{r}$", label_off=(-0.3, 0.2))
    ax.scatter([M[0]], [M[1]], color=RED, s=28, zorder=6)
    ax.text(M[0] + 0.05, M[1] + 0.18, r"$M$", color=RED, fontsize=12)
    arrow(ax, M, 1.5 * tang, BLUE, lw=2.0, label=r"$\vec{v}$", label_off=(0.06, 0.1))
    arrow(ax, M, 1.05 * norm, GREEN, lw=1.8, label=r"$\vec{u}_n$", label_off=(0.05, 0.12))
    arrow(ax, M, 1.25 * tang, PURPLE, lw=1.6, label=r"$\vec{u}_t$", label_off=(-0.35, -0.42))
    arrow(ax, M, 0.55 * tang + 0.9 * norm, ORANGE, lw=2.2,
          label=r"$\vec{a}$", label_off=(0.08, 0.08))
    arrow(ax, M, 0.55 * tang, ORANGE, lw=1.0, ls="--")
    ax.text(4.2, 0.15, r"$\vec{a}=a_t\vec{u}_t+a_n\vec{u}_n$", fontsize=11, color=ORANGE)
    ax.text(0.02, 0.02, r"$O$", fontsize=12)
    save(fig, "04_trajectory_frame.pdf")


# ---------------------------------------------------------------------------
# 5. Motion graphs
# ---------------------------------------------------------------------------
def fig_motion_graphs():
    t = np.linspace(0, 5, 300)
    a = 1.5
    v0 = 2.0
    x0 = 0.5
    v = v0 + a * t
    x = x0 + v0 * t + 0.5 * a * t ** 2

    fig, axes = plt.subplots(3, 1, figsize=(6.6, 6.6), sharex=True)
    axes[0].plot(t, x, color=BLUE, lw=2)
    axes[0].set_ylabel(r"$x\,(\mathrm{m})$")
    axes[0].set_title("Uniformly accelerated motion: position, velocity, acceleration", fontsize=11)
    axes[1].plot(t, v, color=GREEN, lw=2)
    axes[1].set_ylabel(r"$v\,(\mathrm{m\,s^{-1}})$")
    axes[2].plot(t, np.full_like(t, a), color=RED, lw=2)
    axes[2].set_ylabel(r"$a\,(\mathrm{m\,s^{-2}})$")
    axes[2].set_xlabel(r"$t\,(\mathrm{s})$")
    for ax in axes:
        ax.grid(True, color=LIGHT, lw=0.7)
        ax.set_xlim(0, 5)
        for s in ["top", "right"]:
            ax.spines[s].set_visible(False)
    axes[1].fill_between(t, 0, v, color=GREEN, alpha=0.10)
    axes[2].fill_between(t, 0, a, color=RED, alpha=0.10)
    fig.tight_layout()
    save(fig, "05_motion_graphs.pdf")


# ---------------------------------------------------------------------------
# 6. Projectile motion
# ---------------------------------------------------------------------------
def fig_projectile():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    clean_axes(ax)
    v0, alpha, g = 20.0, np.radians(50), 9.81
    tmax = 2 * v0 * np.sin(alpha) / g
    t = np.linspace(0, tmax, 300)
    x = v0 * np.cos(alpha) * t
    y = v0 * np.sin(alpha) * t - 0.5 * g * t ** 2
    ax.plot(x, y, color=BLUE, lw=2.2)
    ax.axhline(0, color=INK, lw=1.0)
    ax.set_xlim(-1, x.max() + 4)
    ax.set_ylim(-1, y.max() + 3)
    ax.set_aspect("equal")

    arrow(ax, (0, 0), (2.3 * np.cos(alpha), 2.3 * np.sin(alpha)), RED, lw=2,
          label=r"$\vec{v}_0$", label_off=(0.12, 0.1))
    ax.add_patch(Arc((0, 0), 2.2, 2.2, theta1=0, theta2=np.degrees(alpha), color=INK, lw=0.9))
    ax.text(1.25, 0.42, r"$\alpha$", fontsize=12)

    xh = x.max() / 2
    yh = y.max()
    ax.plot([xh, xh], [0, yh], color=GRAY, lw=0.9, ls="--")
    ax.annotate(r"$y_{\max}=\dfrac{v_0^2\sin^2\alpha}{2g}$",
                xy=(xh, yh), xytext=(xh + 1.2, yh + 0.9), fontsize=10,
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    ax.annotate(r"$x_{\max}=\dfrac{v_0^2\sin 2\alpha}{g}$",
                xy=(x.max(), 0), xytext=(x.max() - 9.5, 2.2), fontsize=10,
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    ax.plot([0, x.max()], [0, 0], color=GREEN, lw=1.4, alpha=0.5)
    save(fig, "06_projectile.pdf")


# ---------------------------------------------------------------------------
# 7. Circular motion
# ---------------------------------------------------------------------------
def fig_circular_motion():
    fig, ax = plt.subplots(figsize=(5.8, 5.4))
    clean_axes(ax)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    R = 1.2
    ax.add_patch(Circle((0, 0), R, fill=False, color=INK, lw=1.4, ls="--"))
    th = np.radians(48)
    M = np.array([R * np.cos(th), R * np.sin(th)])
    ax.plot([0, M[0]], [0, M[1]], color=GRAY, lw=1.1)
    ax.scatter([M[0]], [M[1]], color=RED, s=30, zorder=6)
    ax.text(M[0] + 0.08, M[1] + 0.1, r"$M$", color=RED, fontsize=12)
    ut = np.array([-np.sin(th), np.cos(th)])
    ur = np.array([np.cos(th), np.sin(th)])
    arrow(ax, M, 0.85 * ut, BLUE, lw=2, label=r"$\vec{v}=v\vec{u}_t$", label_off=(0.05, 0.08))
    arrow(ax, M, -0.72 * ur, GREEN, lw=1.8, label=r"$\vec{a}_n$", label_off=(-0.55, -0.28))
    arrow(ax, M, 0.55 * ut, PURPLE, lw=1.5, label=r"$\vec{u}_t$", label_off=(0.05, -0.3))
    arrow(ax, M, 0.55 * ur, ORANGE, lw=1.5, label=r"$\vec{u}_r$", label_off=(0.08, 0.05))
    ax.add_patch(Arc((0, 0), 0.55, 0.55, theta1=0, theta2=np.degrees(th), color=INK, lw=0.8))
    ax.text(0.30, 0.14, r"$\theta$", fontsize=11)
    ax.text(0.02, -0.1, r"$O$", fontsize=12)
    ax.text(-1.05, -1.62, r"$a_t=\dot v,\qquad a_n=\dfrac{v^2}{R}$", fontsize=11)
    save(fig, "07_circular_motion.pdf")


# ---------------------------------------------------------------------------
# 8. Polar basis
# ---------------------------------------------------------------------------
def fig_polar_basis():
    fig, ax = plt.subplots(figsize=(5.8, 5.0))
    clean_axes(ax)
    ax.set_xlim(-0.8, 4.6)
    ax.set_ylim(-0.8, 4.2)
    ax.annotate("", xy=(4.2, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0))
    ax.annotate("", xy=(0, 3.8), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0))
    ax.text(4.3, -0.1, r"$x$", fontsize=12)
    ax.text(-0.05, 3.95, r"$y$", fontsize=12)
    th = np.radians(38)
    r = 3.0
    M = np.array([r * np.cos(th), r * np.sin(th)])
    arrow(ax, (0, 0), M, RED, lw=2, label=r"$\vec{r}=r\,\vec{u}_r$", label_off=(0.08, 0.1))
    ur = np.array([np.cos(th), np.sin(th)])
    ut = np.array([-np.sin(th), np.cos(th)])
    arrow(ax, M, 1.0 * ur, ORANGE, lw=1.8, label=r"$\vec{u}_r$", label_off=(0.1, 0.05))
    arrow(ax, M, 1.0 * ut, BLUE, lw=1.8, label=r"$\vec{u}_\theta$", label_off=(0.06, 0.1))
    ax.add_patch(Arc((0, 0), 1.05, 1.05, theta1=0, theta2=np.degrees(th), color=INK, lw=0.8))
    ax.text(0.62, 0.26, r"$\theta$", fontsize=12)
    ax.text(-0.18, -0.3, r"$O$", fontsize=12)
    ax.text(M[0] + 0.08, M[1] + 0.15, r"$M$", color=RED, fontsize=12)
    ax.text(0.9, -0.6, r"$\vec{v}=\dot r\,\vec{u}_r+r\dot\theta\,\vec{u}_\theta$", fontsize=10.5)
    save(fig, "08_polar_basis.pdf")


# ---------------------------------------------------------------------------
# 9. Cylindrical and spherical coordinates
# ---------------------------------------------------------------------------
def fig_cyl_spherical():
    fig = plt.figure(figsize=(9.6, 4.6))
    for k, kind in enumerate(["cyl", "sph"]):
        ax = fig.add_subplot(1, 2, k + 1, projection="3d")
        ax.set_box_aspect((1, 1, 1))
        ax.set_axis_off()
        L = 2.8
        ax.quiver(0, 0, 0, L, 0, 0, color=INK, lw=1.0, arrow_length_ratio=0.08)
        ax.quiver(0, 0, 0, 0, L, 0, color=INK, lw=1.0, arrow_length_ratio=0.08)
        ax.quiver(0, 0, 0, 0, 0, L, color=INK, lw=1.0, arrow_length_ratio=0.08)
        ax.text(L + 0.1, 0, 0, r"$x$", fontsize=10)
        ax.text(0, L + 0.1, 0, r"$y$", fontsize=10)
        ax.text(0, 0, L + 0.1, r"$z$", fontsize=10)

        if kind == "cyl":
            rho, th, z = 2.0, np.radians(40), 1.7
            P = np.array([rho * np.cos(th), rho * np.sin(th), z])
            ax.quiver(0, 0, 0, *P, color=RED, lw=1.9, arrow_length_ratio=0.06)
            ax.plot([P[0], P[0]], [P[1], P[1]], [0, P[2]], color=GRAY, lw=0.9, ls="--")
            ax.plot([P[0], P[0]], [0, P[1]], [0, 0], color=GRAY, lw=0.9, ls="--")
            ax.plot([0, P[0]], [P[1], P[1]], [0, 0], color=GRAY, lw=0.9, ls="--")
            ax.plot([0, P[0]], [0, P[1]], [0, 0], color=BLUE, lw=1.3)
            ax.text(P[0] + 0.06, P[1] + 0.05, P[2] + 0.1, r"$M$", color=RED, fontsize=10)
            ax.text(P[0] / 2 - 0.05, P[1] / 2, -0.28, r"$\rho$", color=BLUE, fontsize=11)
            ax.text(0.05, 0.05, P[2] / 2, r"$z$", color=GRAY, fontsize=11)
            ax.text(0.55, 0.16, 0.1, r"$\theta$", fontsize=10)
            ax.set_title("Cylindrical $(\\rho,\\theta,z)$", fontsize=11)
        else:
            r, th, ph = 2.4, np.radians(52), np.radians(35)
            P = np.array([r * np.sin(th) * np.cos(ph), r * np.sin(th) * np.sin(ph), r * np.cos(th)])
            ax.quiver(0, 0, 0, *P, color=RED, lw=1.9, arrow_length_ratio=0.06)
            ax.plot([P[0], P[0]], [P[1], P[1]], [0, P[2]], color=GRAY, lw=0.9, ls="--")
            ax.plot([P[0], P[0]], [0, P[1]], [0, 0], color=GRAY, lw=0.9, ls="--")
            ax.plot([0, P[0]], [P[1], P[1]], [0, 0], color=GRAY, lw=0.9, ls="--")
            ax.plot([0, P[0]], [0, P[1]], [0, 0], color=BLUE, lw=1.2)
            ax.plot([0, P[0]], [0, P[1]], [0, P[2]], color=GRAY, lw=0.7, ls=":")
            ax.text(P[0] + 0.05, P[1] + 0.05, P[2] + 0.12, r"$M$", color=RED, fontsize=10)
            ax.text(P[0] / 2 - 0.2, P[1] / 2 - 0.1, P[2] / 2 + 0.1, r"$r$", color=RED, fontsize=11)
            ax.text(0.35, 0.12, 0.25, r"$\theta$", fontsize=10)
            ax.text(P[0] / 2, P[1] / 2 - 0.15, -0.25, r"$\phi$", color=BLUE, fontsize=10)
            ax.set_title("Spherical $(r,\\theta,\\phi)$", fontsize=11)
        ax.set_xlim(-0.2, L)
        ax.set_ylim(-0.2, L)
        ax.set_zlim(-0.2, L)
    fig.tight_layout()
    save(fig, "09_cyl_spherical.pdf")


# ---------------------------------------------------------------------------
# 10. Rotating frame and Coriolis
# ---------------------------------------------------------------------------
def fig_rotating_frame():
    fig, ax = plt.subplots(figsize=(6.2, 5.6))
    clean_axes(ax)
    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(-2.4, 2.4)
    ax.add_patch(Circle((0, 0), 1.75, fill=False, color=INK, lw=1.2, ls="--"))
    ax.add_patch(Arc((0, 0), 2.4, 2.4, theta1=35, theta2=95, color=ORANGE, lw=1.8))
    ax.annotate("", xy=(-0.55, 1.15), xytext=(-0.85, 0.85),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.8))
    ax.text(-1.25, 1.12, r"$\vec{\Omega}$", color=ORANGE, fontsize=13)

    th = np.radians(30)
    M = np.array([1.35 * np.cos(th), 1.35 * np.sin(th)])
    ax.scatter([M[0]], [M[1]], color=RED, s=30, zorder=6)
    ax.text(M[0] + 0.08, M[1] + 0.08, r"$M$", color=RED, fontsize=12)
    ax.plot([0, M[0]], [0, M[1]], color=GRAY, lw=0.9, ls=":")
    vr = np.array([-np.sin(th), np.cos(th)]) * 0.9
    arrow(ax, M, vr, BLUE, lw=2, label=r"$\vec{v}_r$", label_off=(0.06, 0.08))
    ac = 2 * np.cross([0, 0, 1.0], [vr[0], vr[1], 0])[:2]
    ac = ac / np.linalg.norm(ac) * 0.85
    arrow(ax, M, ac, GREEN, lw=1.8, label=r"$\vec{a}_c=2\vec{\Omega}\times\vec{v}_r$",
          label_off=(0.05, 0.12))
    ax.text(-2.3, -2.25, "rotating frame $R'$ (angular velocity $\\vec{\\Omega}$)",
            fontsize=10, color=INK)
    save(fig, "10_rotating_frame.pdf")


# ---------------------------------------------------------------------------
# 11. Inclined plane free-body diagram
# ---------------------------------------------------------------------------
def fig_incline_fbd():
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    clean_axes(ax)
    ax.set_xlim(-0.8, 6.8)
    ax.set_ylim(-0.8, 4.4)
    ang = np.radians(30)
    base = np.array([0.2, 0.2])
    L = 6.0
    A = base
    B = base + np.array([L * np.cos(ang), 0])
    C = base + np.array([L * np.cos(ang), L * np.sin(ang)])
    ax.add_patch(Polygon([A, B, C], closed=True, facecolor="#eef2f6", edgecolor=INK, lw=1.4))
    ax.plot([A[0], B[0]], [A[1], B[1]], color=INK, lw=1.6)

    s = 0.62
    P = A + s * np.array([L * np.cos(ang), L * np.sin(ang)]) + np.array([-0.35 * np.sin(ang), 0.35 * np.cos(ang)])
    size = 0.55
    corners = [P + size * np.array([np.cos(ang), np.sin(ang)]),
               P + size * np.array([np.cos(ang), np.sin(ang)]) + size * np.array([-np.sin(ang), np.cos(ang)]),
               P + size * np.array([-np.sin(ang), np.cos(ang)])]
    block = Polygon([corners[0] - size * np.array([np.cos(ang), np.sin(ang)]),
                     corners[0], corners[1], corners[2]], closed=True,
                    facecolor="#c9d6e3", edgecolor=INK, lw=1.2)
    ax.add_patch(block)
    center = P + 0.28 * np.array([np.cos(ang), np.sin(ang)]) + 0.28 * np.array([-np.sin(ang), np.cos(ang)])

    arrow(ax, center, (0, -1.25), RED, lw=2, label=r"$m\vec{g}$", label_off=(-0.55, -0.1))
    arrow(ax, center, 1.25 * np.array([-np.sin(ang), np.cos(ang)]), BLUE, lw=2,
          label=r"$\vec{N}$", label_off=(0.1, 0.05))
    arrow(ax, center, 1.0 * np.array([-np.cos(ang), -np.sin(ang)]), GREEN, lw=2,
          label=r"$\vec{f}$", label_off=(-0.55, -0.28))
    ax.plot([center[0], center[0] - 1.2 * np.sin(ang)],
            [center[1], center[1] - 1.2 * np.cos(ang)], color=GRAY, lw=0.8, ls="--")
    ax.plot([center[0], center[0] + 1.1 * np.cos(ang)],
            [center[1], center[1] + 1.1 * np.sin(ang)], color=GRAY, lw=0.8, ls="--")
    ax.add_patch(Arc(A, 1.5, 1.5, theta1=0, theta2=30, color=INK, lw=1.0))
    ax.text(A[0] + 0.78, A[1] + 0.16, r"$\alpha$", fontsize=12)
    ax.text(center[0] + 0.55, center[1] + 0.55, r"$mg\sin\alpha$", fontsize=9, color=GRAY)
    ax.text(center[0] - 0.15, center[1] - 1.55, r"$mg\cos\alpha$", fontsize=9, color=GRAY)
    save(fig, "11_incline_fbd.pdf")


# ---------------------------------------------------------------------------
# 12. Atwood machine
# ---------------------------------------------------------------------------
def fig_atwood():
    fig, ax = plt.subplots(figsize=(5.4, 5.2))
    clean_axes(ax)
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-0.4, 4.6)
    ax.plot([-1.7, 1.7], [4.1, 4.1], color=INK, lw=2)
    ax.add_patch(Circle((0, 3.85), 0.28, fill=False, color=INK, lw=1.6))
    ax.plot([-0.28, -0.28], [3.85, 2.0], color=INK, lw=1.2)
    ax.plot([0.28, 0.28], [3.85, 2.6], color=INK, lw=1.2)

    def block(x, y, w, h, label, color):
        ax.add_patch(Rectangle((x - w / 2, y - h), w, h, facecolor=color,
                               edgecolor=INK, lw=1.3))
        ax.text(x, y - h / 2, label, ha="center", va="center", fontsize=13)

    block(-0.28, 2.0, 0.9, 0.7, r"$m_1$", "#c9d6e3")
    block(0.28, 2.6, 0.9, 0.7, r"$m_2$", "#e3cdc9")
    arrow(ax, (-0.28, 1.0), (0, -0.75), RED, lw=1.6, label=r"$m_1\vec{g}$", label_off=(-0.9, 0.1))
    arrow(ax, (0.28, 1.6), (0, -0.75), RED, lw=1.6, label=r"$m_2\vec{g}$", label_off=(0.12, 0.1))
    ax.text(0.42, 3.9, r"$T$", fontsize=11)
    ax.text(-0.55, 3.9, r"$T$", fontsize=11)
    ax.text(0, -0.3, r"$a=\dfrac{(m_1-m_2)g}{m_1+m_2}$", fontsize=11, ha="center")
    save(fig, "12_atwood.pdf")


# ---------------------------------------------------------------------------
# 13. Friction law
# ---------------------------------------------------------------------------
def fig_friction():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    F = np.linspace(0, 10, 400)
    mus, muk, N = 0.6, 0.4, 10
    fs = np.minimum(F, mus * N)
    fk = np.where(F >= mus * N, muk * N, np.nan)
    ax.plot(F, fs, color=BLUE, lw=2.2, label="actual friction")
    ax.plot(F, fk, color=RED, lw=2.2, ls="--", label="kinetic friction $f_k=\\mu_k N$")
    ax.axvline(mus * N, color=GRAY, lw=0.9, ls=":")
    ax.axhline(mus * N, color=GRAY, lw=0.9, ls=":")
    ax.axhline(muk * N, color=GRAY, lw=0.9, ls=":")
    ax.text(mus * N + 0.15, mus * N + 0.12, r"$f_s^{\max}=\mu_s N$", fontsize=10, color=BLUE)
    ax.text(mus * N + 0.15, muk * N - 0.45, r"$f_k=\mu_k N$", fontsize=10, color=RED)
    ax.text(mus * N - 0.5, -0.7, r"$\mu_s N$", fontsize=10, color=GRAY)
    ax.set_xlabel(r"applied force $F$")
    ax.set_ylabel(r"friction force $f$")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.grid(True, color=LIGHT, lw=0.7)
    ax.legend(frameon=False, loc="lower right", fontsize=9)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    save(fig, "13_friction.pdf")


# ---------------------------------------------------------------------------
# 14. Spring-mass system
# ---------------------------------------------------------------------------
def fig_spring_mass():
    fig, ax = plt.subplots(figsize=(7.6, 2.9))
    clean_axes(ax)
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-1.2, 1.6)
    ax.plot([0.2, 0.2], [-0.8, 0.8], color=INK, lw=3)
    x0, x1 = 0.25, 3.2
    xs = np.linspace(x0, x1, 200)
    ys = 0.0 + 0.28 * np.sin(np.linspace(0, 22 * np.pi, 200))
    ax.plot(xs, ys, color=BLUE, lw=1.5)
    ax.add_patch(Rectangle((x1, -0.5), 1.2, 1.0, facecolor="#c9d6e3", edgecolor=INK, lw=1.3))
    ax.text(x1 + 0.6, 0.0, r"$m$", ha="center", va="center", fontsize=14)
    ax.plot([x1 + 1.2, 8.2], [0, 0], color=INK, lw=1.4)
    ax.annotate("", xy=(8.0, -0.75), xytext=(x1 + 1.2, -0.75),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.0))
    ax.text((x1 + 1.2 + 8.0) / 2, -1.05, r"$x$", fontsize=12, ha="center")
    ax.plot([x1 + 1.2, x1 + 1.2], [-0.55, 0.55], color=GRAY, lw=1.0, ls=":")
    ax.text(x1 + 1.15, 0.65, r"$x=0$", fontsize=10, ha="center")
    arrow(ax, (x1 + 0.6, 0.0), (-1.3, 0), RED, lw=1.8, label=r"$F=-kx$",
          label_off=(-0.2, 0.18))
    save(fig, "14_spring_mass.pdf")


# ---------------------------------------------------------------------------
# 15. Potential energy well
# ---------------------------------------------------------------------------
def fig_energy_well():
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    x = np.linspace(-1.9, 1.9, 500)
    U = x ** 4 - 2 * x ** 2 + 0.4
    ax.plot(x, U, color=BLUE, lw=2.2)
    for x0 in [-1, 1]:
        ax.scatter([x0], [x0 ** 4 - 2 * x0 ** 2 + 0.4], color=GREEN, s=45, zorder=6)
        ax.text(x0 + 0.07, x0 ** 4 - 2 * x0 ** 2 + 0.42, "stable", fontsize=9, color=GREEN)
    ax.scatter([0], [0.4], color=RED, s=45, zorder=6)
    ax.text(0.07, 0.45, "unstable", fontsize=9, color=RED)
    ax.axhline(0.4, color=GRAY, lw=0.8, ls=":")
    ax.axhline(1.4, color=ORANGE, lw=1.0, ls="--")
    ax.text(1.2, 1.48, r"$E_T$", color=ORANGE, fontsize=11)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$E_p(x)$")
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(0, 3.2)
    ax.grid(True, color=LIGHT, lw=0.7)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    save(fig, "15_energy_well.pdf")


# ---------------------------------------------------------------------------
# 16. Damped oscillations
# ---------------------------------------------------------------------------
def fig_damped():
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    t = np.linspace(0, 10, 700)
    w0 = 2.0
    ax.plot(t, np.exp(-0.25 * t) * np.cos(w0 * t), color=BLUE, lw=1.8,
            label="underdamped")
    ax.plot(t, np.exp(-w0 * t) * (1 + w0 * t), color=GREEN, lw=1.8,
            label="critically damped")
    ax.plot(t, 0.5 * (np.exp(-0.6 * t) + np.exp(-2.8 * t)), color=ORANGE, lw=1.8,
            label="overdamped")
    ax.axhline(0, color=INK, lw=0.8)
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$x(t)$")
    ax.set_xlim(0, 10)
    ax.grid(True, color=LIGHT, lw=0.7)
    ax.legend(frameon=False, fontsize=9)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    save(fig, "16_damped_oscillations.pdf")


# ---------------------------------------------------------------------------
# 17. Kepler orbit
# ---------------------------------------------------------------------------
def fig_kepler():
    fig, ax = plt.subplots(figsize=(6.6, 4.8))
    a, b = 2.4, 1.6
    c = np.sqrt(a ** 2 - b ** 2)
    th = np.linspace(0, 2 * np.pi, 400)
    x = a * np.cos(th) - c
    y = b * np.sin(th)
    ax.plot(x, y, color=BLUE, lw=2.0)
    ax.scatter([-c], [0], color=ORANGE, s=110, zorder=6)
    ax.text(-c + 0.12, 0.12, "Sun", color=ORANGE, fontsize=10)
    ax.scatter([0], [0], color=GRAY, s=12)
    i = 70
    M = np.array([x[i], y[i]])
    ax.plot([-c, M[0]], [-0, M[1]], color=RED, lw=1.3)
    ax.text((M[0] - c) / 2 - 0.15, M[1] / 2 + 0.12, r"$r$", color=RED, fontsize=11)
    ax.text(-c + 0.35, 0.35, r"$\theta$", fontsize=11)
    ax.annotate("", xy=(a - c, 0), xytext=(-c, 0),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=0.9))
    ax.text((a - c - c) / 2, -0.35, r"$a$", color=GRAY, fontsize=11)
    ax.plot([-c, -c], [-b, b], color=GRAY, lw=0.7, ls=":")
    ax.text(-c - 0.55, 0.0, r"$b$", color=GRAY, fontsize=11)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-a - c - 0.6, a - c + 0.6)
    ax.set_ylim(-b - 0.6, b + 0.6)
    ax.text(-3.0, -2.4, r"$\dfrac{T^2}{a^3}=\dfrac{4\pi^2}{GM}$", fontsize=11)
    save(fig, "17_kepler.pdf")


# ---------------------------------------------------------------------------
# 18. Work along a curved path
# ---------------------------------------------------------------------------
def fig_work_path():
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    clean_axes(ax)
    ax.set_xlim(-0.4, 7.0)
    ax.set_ylim(-0.4, 4.4)
    t = np.linspace(0, 1, 200)
    x = 0.4 + 5.8 * t
    y = 0.5 + 2.0 * t + 1.0 * np.sin(np.pi * t)
    ax.plot(x, y, color=INK, lw=1.8)
    A = np.array([x[0], y[0]])
    B = np.array([x[-1], y[-1]])
    ax.scatter([A[0], B[0]], [A[1], B[1]], color=RED, s=28, zorder=6)
    ax.text(A[0] - 0.25, A[1] - 0.1, r"$A$", fontsize=12)
    ax.text(B[0] + 0.05, B[1] + 0.05, r"$B$", fontsize=12)
    i = 115
    M = np.array([x[i], y[i]])
    dx, dy = x[i + 1] - x[i - 1], y[i + 1] - y[i - 1]
    tang = np.array([dx, dy])
    tang = tang / np.linalg.norm(tang)
    arrow(ax, M, 0.75 * tang, PURPLE, lw=1.8, label=r"$d\vec{\ell}$",
          label_off=(0.05, 0.1))
    arrow(ax, M, 1.25 * np.array([0.75, 0.66]), ORANGE, lw=2.0,
          label=r"$\vec{F}$", label_off=(0.08, 0.08))
    ax.add_patch(Arc(M, 1.1, 1.1,
                     theta1=np.degrees(np.arctan2(tang[1], tang[0])),
                     theta2=np.degrees(np.arctan2(0.66, 0.75)), color=GRAY, lw=0.8))
    ax.text(M[0] + 0.42, M[1] + 0.28, r"$\theta$", fontsize=10, color=GRAY)
    ax.text(2.0, 0.25, r"$W_{A\to B}=\int_A^B \vec{F}\cdot d\vec{\ell}$",
            fontsize=11)
    save(fig, "18_work_path.pdf")


# ---------------------------------------------------------------------------
# 19. Terminal velocity
# ---------------------------------------------------------------------------
def fig_terminal_velocity():
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    t = np.linspace(0, 5, 400)
    tau = 0.9
    v = 2.5 * (1 - np.exp(-t / tau))
    ax.plot(t, v, color=BLUE, lw=2.2)
    ax.axhline(2.5, color=GRAY, lw=0.9, ls="--")
    ax.text(2.6, 2.58, r"$v_L=\dfrac{mg}{k}$", fontsize=11, color=GRAY)
    ax.annotate(r"$v(t)=v_L\left(1-e^{-t/\tau}\right)$", xy=(1.2, v[96]),
                xytext=(2.0, 1.2), fontsize=11,
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$v$")
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 3.0)
    ax.grid(True, color=LIGHT, lw=0.7)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    save(fig, "19_terminal_velocity.pdf")


# ---------------------------------------------------------------------------
# 20. Simple pendulum
# ---------------------------------------------------------------------------
def fig_pendulum():
    fig, ax = plt.subplots(figsize=(5.2, 4.8))
    clean_axes(ax)
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.4, 1.2)
    ax.plot([-1.2, 1.2], [0.85, 0.85], color=INK, lw=2.5)
    th = np.radians(35)
    L = 2.3
    M = np.array([L * np.sin(th), 0.85 - L * np.cos(th)])
    ax.plot([0, M[0]], [0.85, M[1]], color=INK, lw=1.3)
    ax.scatter([M[0]], [M[1]], color=RED, s=180, zorder=6)
    arrow(ax, M, (0, -0.95), RED, lw=1.8, label=r"$m\vec{g}$", label_off=(-0.45, -0.15))
    arrow(ax, M, (-0.85 * np.sin(th), 0.85 * np.cos(th)), BLUE, lw=1.8,
          label=r"$\vec{T}$", label_off=(-0.3, 0.1))
    ax.plot([M[0], M[0]], [M[1], M[1] + 0.7], color=GRAY, lw=0.8, ls="--")
    ax.plot([M[0], M[0] - 0.6 * np.cos(th)], [M[1], M[1] + 0.6 * np.sin(th)],
            color=GRAY, lw=0.8, ls="--")
    ax.text(0.12, 0.55, r"$\theta$", fontsize=12)
    ax.add_patch(Arc((0, 0.85), 0.7, 0.7, theta1=270, theta2=270 + np.degrees(th),
                     color=INK, lw=0.8))
    ax.text(0.0, -2.3, r"$\ddot\theta+\dfrac{g}{L}\sin\theta=0$", fontsize=11)
    save(fig, "20_pendulum.pdf")


# ---------------------------------------------------------------------------
# 21. Collision
# ---------------------------------------------------------------------------
def fig_collision():
    fig, axes = plt.subplots(2, 1, figsize=(7.0, 3.8))
    for ax in axes:
        clean_axes(ax)
        ax.set_xlim(-0.5, 8.5)
        ax.set_ylim(-0.9, 1.1)
    for ax, ttl in zip(axes, ["before", "after"]):
        ax.axhline(0, color=INK, lw=1.2)
        ax.set_title(ttl, fontsize=10, loc="left")
    # before
    axes[0].add_patch(Circle((2.0, 0.3), 0.28, facecolor="#c9d6e3", edgecolor=INK))
    axes[0].add_patch(Circle((5.6, 0.3), 0.28, facecolor="#e3cdc9", edgecolor=INK))
    axes[0].text(2.0, 0.3, r"$m_1$", ha="center", va="center", fontsize=9)
    axes[0].text(5.6, 0.3, r"$m_2$", ha="center", va="center", fontsize=9)
    arrow(axes[0], (2.4, 0.3), (0.95, 0), BLUE, lw=1.8, label=r"$v_1$", label_off=(0.0, 0.12))
    arrow(axes[0], (5.9, 0.3), (0.7, 0), GREEN, lw=1.8, label=r"$v_2$", label_off=(0.0, 0.12))
    # after
    axes[1].add_patch(Circle((3.2, 0.3), 0.28, facecolor="#c9d6e3", edgecolor=INK))
    axes[1].add_patch(Circle((5.2, 0.3), 0.28, facecolor="#e3cdc9", edgecolor=INK))
    axes[1].text(3.2, 0.3, r"$m_1$", ha="center", va="center", fontsize=9)
    axes[1].text(5.2, 0.3, r"$m_2$", ha="center", va="center", fontsize=9)
    arrow(axes[1], (2.8, 0.3), (-0.7, 0), BLUE, lw=1.8, label=r"$v_1'$", label_off=(-0.5, 0.12))
    arrow(axes[1], (5.6, 0.3), (0.85, 0), GREEN, lw=1.8, label=r"$v_2'$", label_off=(0.0, 0.12))
    fig.tight_layout()
    save(fig, "21_collision.pdf")


# ---------------------------------------------------------------------------
# 22. Angular momentum
# ---------------------------------------------------------------------------
def fig_angular_momentum():
    fig, ax = plt.subplots(figsize=(5.8, 4.6))
    clean_axes(ax)
    ax.set_xlim(-0.6, 6.0)
    ax.set_ylim(-1.0, 4.6)
    O = np.array([0.2, 0.2])
    M = np.array([4.2, 2.6])
    ax.scatter([M[0]], [M[1]], color=RED, s=28, zorder=6)
    ax.text(M[0] + 0.08, M[1] + 0.1, r"$M$", color=RED, fontsize=12)
    arrow(ax, O, M - O, GRAY, lw=1.5, label=r"$\vec{r}$", label_off=(-0.2, 0.15))
    arrow(ax, M, (1.2, 0.8), BLUE, lw=2, label=r"$\vec{p}=m\vec{v}$",
          label_off=(0.05, 0.1))
    C = np.array([4.9, 3.9])
    ax.scatter([C[0]], [C[1]], s=190, facecolor="white", edgecolor=PURPLE, lw=1.6, zorder=6)
    ax.scatter([C[0]], [C[1]], s=22, color=PURPLE, zorder=7)
    ax.text(C[0] + 0.2, C[1] - 0.05, r"$\vec{L}_O=\vec{r}\times\vec{p}$",
            color=PURPLE, fontsize=12)
    ax.text(C[0] - 0.1, C[1] - 0.5, "(out of page)", color=PURPLE, fontsize=9)
    ax.text(0.0, 0.0, r"$O$", fontsize=12)
    save(fig, "22_angular_momentum.pdf")


if __name__ == "__main__":
    funcs = [
        fig_vector_addition, fig_cartesian_3d, fig_dot_cross,
        fig_trajectory_frame, fig_motion_graphs, fig_projectile,
        fig_circular_motion, fig_polar_basis, fig_cyl_spherical,
        fig_rotating_frame, fig_incline_fbd, fig_atwood, fig_friction,
        fig_spring_mass, fig_energy_well, fig_damped, fig_kepler,
        fig_work_path, fig_terminal_velocity, fig_pendulum,
        fig_collision, fig_angular_momentum,
    ]
    for f in funcs:
        f()
        print("ok", f.__name__)
    print("All figures written to", OUT)
