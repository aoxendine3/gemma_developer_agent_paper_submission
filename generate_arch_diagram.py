import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dark style
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Color palette
c_blue = '#00d2ff'
c_purple = '#9d4edd'
c_green = '#00f5d4'
c_orange = '#ff9e00'
c_pink = '#ff0054'
c_box_bg = '#161b22'
c_border = '#30363d'

def draw_box(ax, x, y, w, h, title, subtitle, color, icon_text=""):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", facecolor=c_box_bg, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h*0.65, title, ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    ax.text(x + w/2, y + h*0.3, subtitle, ha='center', va='center', fontsize=9, color='#8b949e')

# Title Header
ax.text(50, 94, "HEXCELL HYPERBOLIC MEMORY SWARM ARCHITECTURE", ha='center', va='center', fontsize=16, fontweight='bold', color='white')
ax.text(50, 90, "Google Gemma 4 (31B-IT QAT W4A16-CT) Zero-Copy Agent Execution Pipeline", ha='center', va='center', fontsize=11, color=c_blue)

# Layer 1: Gemma 4 Host Agent & ADK Runner
draw_box(ax, 5, 65, 40, 18, "Gemma 4 Developer Agent", "gemma-4-31b-it-qat-w4a16-ct\nGoogle ADK Agent (agent.yaml)", c_purple)

# Layer 2: 24-Head Fractal Manifold
draw_box(ax, 55, 65, 40, 18, "24-Head Fractal Manifold", "24 Heads × 768 Dimensions\nTotal Vector Space: 18,432-D", c_blue)

# Arrow 1 -> 2
ax.annotate("", xy=(55, 74), xytext=(45, 74), arrowprops=dict(arrowstyle="->", color=c_purple, lw=2.5))
ax.text(50, 77, "Cognitive Vector Stream", ha='center', va='center', fontsize=8, color='white')

# Layer 3: Poincaré Hyperbolic Metric Engine
draw_box(ax, 5, 30, 40, 20, "Poincaré Metric Engine (B¹⁸⁴³²)", "Geodesic Metric: d_B(u, v)\nMöbius Addition: u ⊕_B v\nProjection Gate: π_≤0.85", c_pink)

# Arrow 2 -> 3
ax.annotate("", xy=(25, 50), xytext=(75, 65), arrowprops=dict(arrowstyle="->", color=c_blue, lw=2, connectionstyle="arc3,rad=-0.2"))

# Layer 4: Rust FFI Bare-Metal Bridge
draw_box(ax, 55, 30, 40, 20, "Rust FFI Bare-Metal Bridge", "libcontext_bridge.dylib\nC-ABI Export Handlers\nZero-Allocation Strides", c_orange)

# Arrow 3 -> 4
ax.annotate("", xy=(55, 40), xytext=(45, 40), arrowprops=dict(arrowstyle="->", color=c_pink, lw=2.5))
ax.text(50, 43, "52 μs Möbius Ops", ha='center', va='center', fontsize=8, color='white')

# Layer 5: 6-Fold HexCell Lock-Free Memory Lattice
draw_box(ax, 20, 3, 60, 18, "6-Fold HexCell Lock-Free Memory Lattice", "POSIX Shared Memory (0x3000) | Atomic Double-Buffering (14.2M Reads/sec)\nZero State Pollution | Hardware Taint Lattice (0xBEAF)", c_green)

# Arrow 4 -> 5 & 3 -> 5
ax.annotate("", xy=(50, 21), xytext=(25, 30), arrowprops=dict(arrowstyle="->", color=c_green, lw=2, connectionstyle="arc3,rad=0.2"))
ax.annotate("", xy=(50, 21), xytext=(75, 30), arrowprops=dict(arrowstyle="->", color=c_green, lw=2, connectionstyle="arc3,rad=-0.2"))

plt.tight_layout()
plt.savefig('barn/gemma_paper_sub/docs/images/architecture_diagram.png', bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
print("Successfully generated architecture_diagram.png")
