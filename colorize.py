#!/usr/bin/env python3

import argparse

import warnings

# Silenciar warnings no críticos
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

from pathlib import Path
from deoldify.visualize import get_image_colorizer

def main():
    parser = argparse.ArgumentParser(description="Colorizador DeOldify CLI")
    parser.add_argument("image", type=Path, help="Imagen en blanco y negro")
    parser.add_argument("--render-factor", type=int, default=35)
    parser.add_argument("--artistic", action="store_true")
    parser.add_argument("--compare", action="store_true")
    parser.add_argument("--no-watermark", action="store_true")

    args = parser.parse_args()

    colorizer = get_image_colorizer(artistic=args.artistic)

    colorizer.plot_transformed_image(
        path=args.image,
        render_factor=args.render_factor,
        compare=args.compare,
        watermarked=not args.no_watermark
    )

if __name__ == "__main__":
    main()