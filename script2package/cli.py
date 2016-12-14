from script2package import util
import argparse
import os.path

def main():
    """
    `script2package` will correctly treat any `setup.cfg` files which it comes
    across.

    If it will simply use the default setup settings with the package using
    the name of the script as the name of the package. The filename will be
    automatically sanitized.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('script')
    parser.add_argument('--base', action='store', default='package')
    args = parser.parse_args()

    if args.script is None or not os.path.isfile(args.script):
        print("Please enter a valid python script!")
        raise

    try:
        from config import config
    except:
        config = {}

    setup_cfg = "setup.cfg" if os.path.isfile("setup.cfg") else None

    util.generate_skeleton(args.script, base=args.base, config=config, setup_cfg=setup_cfg)
