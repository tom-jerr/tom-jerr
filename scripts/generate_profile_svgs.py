#!/usr/bin/env python3
"""Deterministic SVG generator for tom-jerr's GitHub profile visuals.

Generates light and dark theme pairs for:
  1. assets/banner-{light,dark}.svg        (900 x 176)
  2. assets/systems-stack-{light,dark}.svg (900 x 406)

Usage:
  python scripts/generate_profile_svgs.py [output_dir]
"""

from __future__ import annotations

import html
import sys
from pathlib import Path

SANS_FONT = '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif'
MONO_FONT = 'ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace'

THEMES = {
    "light": {
        "canvas": "#FFFFFF",
        "card_bg": "#F6F8FA",
        "card_border": "#D0D7DE",
        "sub_bg": "#FFFFFF",
        "sub_border": "#D8DEE4",
        "text_primary": "#1F2328",
        "text_secondary": "#57606A",
        "text_muted": "#6E7781",
        "blue_bg": "#DDF4FF",
        "blue_border": "#54AEFF",
        "blue_text": "#0969DA",
        "teal_bg": "#DAFBE1",
        "teal_border": "#4AC26B",
        "teal_text": "#1A7F37",
        "amber_bg": "#FFF8C5",
        "amber_border": "#D4A72C",
        "amber_text": "#9A6700",
        "slate_bg": "#F0F3F6",
        "slate_border": "#B8C1CC",
        "slate_text": "#424A53",
        "tile_idle": "#EAEEF2",
        "tile_mid": "#B6E3FF",
        "tile_hot": "#0969DA",
        "tile_accent": "#1A7F37",
        "arrow": "#57606A",
        "arrow_feedback": "#0969DA",
    },
    "dark": {
        "canvas": "#0D1117",
        "card_bg": "#161B22",
        "card_border": "#30363D",
        "sub_bg": "#0D1117",
        "sub_border": "#30363D",
        "text_primary": "#E6EDF3",
        "text_secondary": "#9198A1",
        "text_muted": "#7D8590",
        "blue_bg": "#12263F",
        "blue_border": "#388BFD",
        "blue_text": "#79C0FF",
        "teal_bg": "#122A1E",
        "teal_border": "#2EA043",
        "teal_text": "#56D364",
        "amber_bg": "#2B2111",
        "amber_border": "#D29922",
        "amber_text": "#E3B341",
        "slate_bg": "#1C2128",
        "slate_border": "#444C56",
        "slate_text": "#ADB7C1",
        "tile_idle": "#21262D",
        "tile_mid": "#1F4B85",
        "tile_hot": "#58A6FF",
        "tile_accent": "#3FB950",
        "arrow": "#8B949E",
        "arrow_feedback": "#58A6FF",
    },
}


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def svg_text(
    x: float,
    y: float,
    text: str,
    *,
    size: float = 13,
    weight: str = "400",
    fill: str,
    family: str = SANS_FONT,
    anchor: str = "start",
    letter_spacing: str | None = None,
) -> str:
    extra = f' letter-spacing="{letter_spacing}"' if letter_spacing else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family=\'{family}\' '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}"{extra}>{esc(text)}</text>'
    )


def svg_rect(
    x: float,
    y: float,
    w: float,
    h: float,
    *,
    fill: str,
    stroke: str = "none",
    stroke_width: float = 1.0,
    rx: float = 8,
) -> str:
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
    )


def render_banner(theme_name: str) -> str:
    t = THEMES[theme_name]
    w, h = 900, 176
    lines: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Zhiyi Liu GitHub Profile Banner">',
        f'  <title>Zhiyi Liu (@tom-jerr) — LLM Inference &amp; Agent Serving Systems</title>',
        "  <!-- Outer card -->",
        f'  {svg_rect(2, 2, w - 4, h - 4, fill=t["card_bg"], stroke=t["card_border"], stroke_width=1.2, rx=14)}',
    ]

    # Left content column
    lx = 36
    # Eyebrow tag
    lines.append(
        f'  {svg_text(lx, 36, "M.S. CS @ UESTC  ·  CLASS OF 2027", size=11.5, weight="600", fill=t["blue_text"], family=MONO_FONT, letter_spacing="0.6")}'
    )
    # Name + handle
    lines.append(
        f'  {svg_text(lx, 76, "Zhiyi Liu", size=34, weight="700", fill=t["text_primary"])}'
    )
    lines.append(
        f'  {svg_text(lx + 148, 75, "@tom-jerr", size=17, weight="500", fill=t["text_muted"], family=MONO_FONT)}'
    )
    # Tagline
    lines.append(
        f'  {svg_text(lx, 105, "LLM Inference Systems  ·  Agent Serving  ·  CUDA Kernel Optimization", size=14.5, weight="400", fill=t["text_secondary"])}'
    )

    # Focus chips
    chips = [
        ("Agent Serving", t["blue_bg"], t["blue_border"], t["blue_text"], 114),
        ("LLM Engine", t["teal_bg"], t["teal_border"], t["teal_text"], 98),
        ("CUDA / Tensor Core", t["amber_bg"], t["amber_border"], t["amber_text"], 148),
        ("Systems Engineering", t["slate_bg"], t["slate_border"], t["slate_text"], 146),
    ]
    cx = lx
    cy = 124
    for label, bg, border, fg, cw in chips:
        lines.append(f'  {svg_rect(cx, cy, cw, 28, fill=bg, stroke=border, stroke_width=1.0, rx=7)}')
        lines.append(
            f'  {svg_text(cx + cw / 2, cy + 18.5, label, size=11.5, weight="600", fill=fg, anchor="middle")}'
        )
        cx += cw + 10

    # Right side geometric GPU / Tensor Tile motif (4x4 grid inside a clean frame)
    gx, gy = 696, 26
    gw, gh = 168, 124
    lines.append("  <!-- GPU / Tensor Core tile schematic -->")
    lines.append(
        f'  {svg_rect(gx, gy, gw, gh, fill=t["sub_bg"], stroke=t["sub_border"], stroke_width=1.0, rx=10)}'
    )
    lines.append(
        f'  {svg_text(gx + 12, gy + 19, "SM / TENSOR TILE", size=9.5, weight="600", fill=t["text_muted"], family=MONO_FONT, letter_spacing="0.5")}'
    )

    pattern = [
        [2, 1, 1, 0, 1, 3],
        [1, 2, 1, 0, 3, 1],
        [1, 1, 2, 1, 1, 0],
        [0, 1, 1, 2, 0, 1],
    ]
    color_map = {
        0: t["tile_idle"],
        1: t["tile_mid"],
        2: t["tile_hot"],
        3: t["tile_accent"],
    }
    tile_w, tile_h, gap = 20, 16, 4
    start_tx = gx + 14
    start_ty = gy + 30
    for r, row in enumerate(pattern):
        for c, val in enumerate(row):
            tx = start_tx + c * (tile_w + gap)
            ty = start_ty + r * (tile_h + gap)
            lines.append(f'  {svg_rect(tx, ty, tile_w, tile_h, fill=color_map[val], rx=3)}')

    lines.append(
        f'  {svg_text(gx + gw - 12, gy + gh - 9, "KV · GEMM · SCHED", size=9, weight="500", fill=t["text_muted"], family=MONO_FONT, anchor="end")}'
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_systems_stack(theme_name: str) -> str:
    t = THEMES[theme_name]
    w, h = 900, 406

    lines: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Full-Stack LLM Inference and Systems Architecture">',
        "  <title>Full-Stack AI &amp; Systems Focus</title>",
        "  <defs>",
        f'    <marker id="arrow-down" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">',
        f'      <path d="M 1 1 L 9 5 L 1 9 z" fill="{t["arrow"]}"/>',
        "    </marker>",
        f'    <marker id="arrow-up" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">',
        f'      <path d="M 1 1 L 9 5 L 1 9 z" fill="{t["arrow_feedback"]}"/>',
        "    </marker>",
        f'    <marker id="arrow-right" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
        f'      <path d="M 1 1 L 9 5 L 1 9 z" fill="{t["arrow"]}"/>',
        "    </marker>",
        "  </defs>",
        "  <!-- Background -->",
        f'  {svg_rect(2, 2, w - 4, h - 4, fill=t["card_bg"], stroke=t["card_border"], stroke_width=1.2, rx=14)}',
        "  <!-- Header -->",
        f'  {svg_text(24, 33, "Full-Stack AI & Systems Focus", size=16, weight="700", fill=t["text_primary"])}',
        f'  {svg_text(w - 24, 32, "Agent Serving  ·  Inference Engine  ·  CUDA Kernels  ·  Systems Foundation", size=11.5, weight="500", fill=t["text_muted"], anchor="end")}',
    ]

    # Four horizontal tiers on the left
    tiers = [
        {
            "title": "Agent Layer",
            "sub": "Current Research",
            "bg": t["blue_bg"],
            "border": t["blue_border"],
            "accent": t["blue_text"],
            "blocks": [
                ("Agent for LLM Acceleration", "Kernel & Config Auto-Tuning"),
                ("Agent Serving Systems", "Multi-Step Scheduling & KV Cache"),
            ],
        },
        {
            "title": "Inference Engine",
            "sub": "MiniInfer · SGLang",
            "bg": t["teal_bg"],
            "border": t["teal_border"],
            "accent": t["teal_text"],
            "blocks": [
                ("KV & Prefix Cache", "Paged · Radix Cache"),
                ("Batch Scheduler", "Chunked · Overlap"),
                ("Model Execution", "CUDA Graph · MoE · TP/EP"),
            ],
        },
        {
            "title": "GPU & Kernels",
            "sub": "cuda-learn",
            "bg": t["amber_bg"],
            "border": t["amber_border"],
            "accent": t["amber_text"],
            "blocks": [
                ("GEMM & MMA", "SGEMM · BF16 Tensor Core"),
                ("Attention & Ops", "FlashAttn · Fused RMSNorm"),
                ("Bindings & IPC", "TVM FFI · PyTorch · Graph"),
            ],
        },
        {
            "title": "Systems Base",
            "sub": "C++ · Go · OS",
            "bg": t["slate_bg"],
            "border": t["slate_border"],
            "accent": t["slate_text"],
            "blocks": [
                ("Distributed & ANN", "Nebula · TinyKV · 6.824"),
                ("Storage & SQL", "BusTub · MiniLSM · miniob"),
                ("OS & Networking", "MIT 6.S081 · epoll Relay"),
            ],
        },
    ]

    stack_x = 24
    stack_w = 656
    tier_h = 72
    tier_gap = 14
    start_y = 52
    label_w = 152

    tier_centers_y: list[float] = []

    lines.append("  <!-- Layered horizontal stack -->")
    for idx, tier in enumerate(tiers):
        ty = start_y + idx * (tier_h + tier_gap)
        tier_centers_y.append(ty + tier_h / 2)

        # Tier outer container
        lines.append(
            f'  {svg_rect(stack_x, ty, stack_w, tier_h, fill=tier["bg"], stroke=tier["border"], stroke_width=1.1, rx=10)}'
        )
        # Tier title (left column)
        lines.append(
            f'  {svg_text(stack_x + 16, ty + 31, tier["title"], size=13.5, weight="700", fill=tier["accent"])}'
        )
        lines.append(
            f'  {svg_text(stack_x + 16, ty + 50, tier["sub"], size=11, weight="500", fill=t["text_secondary"], family=MONO_FONT)}'
        )

        # Peer sub-blocks on common grid
        blocks = tier["blocks"]
        inner_x = stack_x + label_w
        inner_w = stack_w - label_w - 14
        block_gap = 10
        n = len(blocks)
        bw = (inner_w - block_gap * (n - 1)) / n
        bh = 48
        by = ty + (tier_h - bh) / 2

        for b_idx, (b_title, b_sub) in enumerate(blocks):
            bx = inner_x + b_idx * (bw + block_gap)
            lines.append(
                f'  {svg_rect(bx, by, bw, bh, fill=t["sub_bg"], stroke=t["sub_border"], stroke_width=1.0, rx=7)}'
            )
            lines.append(
                f'  {svg_text(bx + bw / 2, by + 20.5, b_title, size=12, weight="600", fill=t["text_primary"], anchor="middle")}'
            )
            lines.append(
                f'  {svg_text(bx + bw / 2, by + 37.5, b_sub, size=10.5, weight="400", fill=t["text_secondary"], anchor="middle")}'
            )

    # Right vertical channel cards (Execution Down / Feedback Up)
    chan_y = start_y
    chan_h = 4 * tier_h + 3 * tier_gap  # 330px, aligned exactly with top and bottom tiers
    chan1_x = 708
    chan_w = 78
    chan2_x = 798

    lines.append("  <!-- Right vertical channel cards -->")
    # Channel 1: Top-Down Execution
    lines.append(
        f'  {svg_rect(chan1_x, chan_y, chan_w, chan_h, fill=t["sub_bg"], stroke=t["sub_border"], stroke_width=1.1, rx=10)}'
    )
    lines.append(
        f'  {svg_text(chan1_x + chan_w / 2, chan_y + 22, "Top-Down", size=11, weight="700", fill=t["text_primary"], anchor="middle")}'
    )
    lines.append(
        f'  {svg_text(chan1_x + chan_w / 2, chan_y + 37, "Execution", size=10.5, weight="500", fill=t["text_secondary"], anchor="middle")}'
    )
    # Channel 2: Bottom-Up Telemetry & Agent Feedback
    lines.append(
        f'  {svg_rect(chan2_x, chan_y, chan_w, chan_h, fill=t["sub_bg"], stroke=t["blue_border"], stroke_width=1.1, rx=10)}'
    )
    lines.append(
        f'  {svg_text(chan2_x + chan_w / 2, chan_y + 22, "Bottom-Up", size=11, weight="700", fill=t["blue_text"], anchor="middle")}'
    )
    lines.append(
        f'  {svg_text(chan2_x + chan_w / 2, chan_y + 37, "Feedback", size=10.5, weight="500", fill=t["text_secondary"], anchor="middle")}'
    )

    # Connectors layer (above containers, zero box-crossing)
    lines.append("  <!-- Connectors -->")
    # Horizontal stubs from stack right edge to Channel 1
    for cy in tier_centers_y:
        lines.append(
            f'  <line x1="{stack_x + stack_w:.1f}" y1="{cy:.1f}" x2="{chan1_x - 3:.1f}" y2="{cy:.1f}" '
            f'stroke="{t["arrow"]}" stroke-width="1.3" marker-end="url(#arrow-right)"/>'
        )

    # Vertical solid arrow inside Channel 1 (top-down)
    c1_mid = chan1_x + chan_w / 2
    lines.append(
        f'  <line x1="{c1_mid:.1f}" y1="{chan_y + 52:.1f}" x2="{c1_mid:.1f}" y2="{chan_y + chan_h - 18:.1f}" '
        f'stroke="{t["arrow"]}" stroke-width="1.8" marker-end="url(#arrow-down)"/>'
    )
    # Channel 1 step pills (centered cleanly over white/dark pill background so line never obscures text)
    down_labels = ["Prompts", "Batches", "Kernels", "Hardware"]
    for label, cy in zip(down_labels, tier_centers_y):
        py = max(cy, chan_y + 72) if label == "Prompts" else cy
        lines.append(
            f'  {svg_rect(chan1_x + 8, py - 11, chan_w - 16, 22, fill=t["card_bg"], stroke=t["sub_border"], stroke_width=0.9, rx=5)}'
        )
        lines.append(
            f'  {svg_text(c1_mid, py + 3.8, label, size=10, weight="600", fill=t["text_secondary"], anchor="middle")}'
        )

    # Vertical dashed arrow inside Channel 2 (bottom-up feedback)
    c2_mid = chan2_x + chan_w / 2
    lines.append(
        f'  <line x1="{c2_mid:.1f}" y1="{chan_y + chan_h - 18:.1f}" x2="{c2_mid:.1f}" y2="{chan_y + 52:.1f}" '
        f'stroke="{t["arrow_feedback"]}" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrow-up)"/>'
    )
    up_labels = ["Agent Opt", "Scheduling", "Profiles", "Latency"]
    for label, cy in zip(up_labels, tier_centers_y):
        py = max(cy, chan_y + 72) if label == "Agent Opt" else cy
        lines.append(
            f'  {svg_rect(chan2_x + 6, py - 11, chan_w - 12, 22, fill=t["blue_bg"], stroke=t["blue_border"], stroke_width=0.9, rx=5)}'
        )
        lines.append(
            f'  {svg_text(c2_mid, py + 3.8, label, size=10, weight="600", fill=t["blue_text"], anchor="middle")}'
        )

    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def generate_all(output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = [
        (output_dir / "banner-light.svg", render_banner("light")),
        (output_dir / "banner-dark.svg", render_banner("dark")),
        (output_dir / "systems-stack-light.svg", render_systems_stack("light")),
        (output_dir / "systems-stack-dark.svg", render_systems_stack("dark")),
    ]
    written: list[Path] = []
    for path, content in outputs:
        path.write_text(content, encoding="utf-8", newline="\n")
        written.append(path)
    return written


def main() -> int:
    default_out = Path(__file__).resolve().parent.parent / "assets"
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else default_out
    written = generate_all(out_dir)
    for path in written:
        print(f"Generated: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
