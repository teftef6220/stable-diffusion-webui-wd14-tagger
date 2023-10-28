from pathlib import Path
from argparse import ArgumentParser

import argparse
import os

modules_path = os.path.dirname(os.path.realpath(__file__))

parser_pre = argparse.ArgumentParser(add_help=False)
parser_pre.add_argument("--data-dir", type=str, default=os.path.dirname(modules_path), help="base path where all user data is stored", )
cmd_opts_pre = parser_pre.parse_known_args()[0]
data_path = cmd_opts_pre.data_dir

models_path = os.path.join(data_path, "models")


default_ddp_path = Path(models_path, 'deepdanbooru')


def preload(parser: ArgumentParser):
    # default deepdanbooru use different paths:
    # models/deepbooru and models/torch_deepdanbooru
    # https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/c81d440d876dfd2ab3560410f37442ef56fc6632

    parser.add_argument(
        '--deepdanbooru-projects-path',
        type=str,
        help='Path to directory with DeepDanbooru project(s).',
        default=default_ddp_path
    )
