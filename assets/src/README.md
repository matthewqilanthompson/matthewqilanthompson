# Profile art sources

All pixel art on this profile is drawn in code (no image model, no drawing app).

| File | Makes |
| ---- | ----- |
| `scene_recipe.py` | the header scene (`../header.gif`, `../header-still.png`) as a grid recipe JSON |
| `hopper_sprite.py` | the grasshopper sprite and its standing / jumping poses, used by the scene |
| `icons2.py` | section icons (`../icons/`) and project icons (`../projects/`) |

Regenerate the header: `python3 scene_recipe.py scene.json`, then render the recipe to PNG/GIF at 4x
(frame 0 is the still). Icons: `python3 icons2.py out/` writes PNGs at 2x. Requires Python 3 and Pillow.
