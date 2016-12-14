from script2package import util
import argparse
import yaml

def main():
    """
    The CLI will parse a valid yaml config file.

    ```
    config={
        ...
    }
    ```

    Which `setup` will then parse as `setup(**config)`

    If it will simply use the default setup settings with the package using
    the name of the script as the name of the package. The filename will be
    automatically sanitized.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('script')
    parser.add_argument('--config', action="store", type=str,
                        help="destination of the config diction, should target a python file")
    parser.add_argument('--base', action='store', default='package')
    args = parser.parse_args()

    if args.script is None:
        print("Please enter a script!")
        raise

    if args.config is not None:
        f = open(args.config)
        config = yaml.load(f)
    else:
        config = {}

    util.generate_skeleton(args.script, base=args.base, config=config)
