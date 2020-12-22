import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
)


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "jpn_name"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text/name"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(30, 31),
)

perspective_transform = NormPerspectiveTransformCfg(20, 20, 1.5)

training_jpn_family_name_data = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "jpn_family_names.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "name_chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

training_kanji_data = GeneratorCfg(
    num_image=150000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
            RandCorpusCfg(
                length=(2, 8),
                chars_file=TEXT_DIR / "jpn_name_char.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

training_hiragana_data = GeneratorCfg(
    num_image=10000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
            RandCorpusCfg(
                length=(3, 8),
                chars_file=TEXT_DIR / "jpn_hiragana_char.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

training_katakana_data = GeneratorCfg(
    num_image=10000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
            RandCorpusCfg(
                length=(3, 8),
                chars_file=TEXT_DIR / "jpn_katakana_char.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_jpn_family_name_data = GeneratorCfg(
    num_image=20000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "jpn_family_names.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "name_chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_kanji_data = GeneratorCfg(
    num_image=10000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
            RandCorpusCfg(
                length=(2, 8),
                chars_file=TEXT_DIR / "jpn_name_char.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_hiragana_data = GeneratorCfg(
    num_image=1000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
            RandCorpusCfg(
                length=(3, 8),
                chars_file=TEXT_DIR / "jpn_hiragana_char.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_katakana_data = GeneratorCfg(
    num_image=1000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
            RandCorpusCfg(
                length=(3, 8),
                chars_file=TEXT_DIR / "jpn_katakana_char.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

# fmt: off
configs = [
    training_jpn_family_name_data,
    training_kanji_data,
    training_hiragana_data,
    training_katakana_data,
    evaluation_jpn_family_name_data,
    evaluation_kanji_data,
    evaluation_hiragana_data,
    evaluation_katakana_data,
]
# fmt: on
