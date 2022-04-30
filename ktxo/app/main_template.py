"""
@@Application Template@@
"""

import argparse
import json
import logging
import logging.config
import os
import sys

import ktxo.app._about as about





#---------------------------------------------------------------------------
# Global vars
#---------------------------------------------------------------------------

_log = logging.getLogger("ktxo.app") # loggers

# Application config
CONFIG={}

#---------------------------------------------------------------------------
#   Versions helper
#---------------------------------------------------------------------------
def get_version():
    """Get version: python, current script and other needed"""
    python_version=sys.version.replace('\n','')

    return [f'{about.__name__} v{about.__version__} ({about.__date__}) by {about.__author__}',
            about.__version__,
            f"Python version {python_version}",
            f"Other version n.n.n" # Add any other version that you need to show
            ]

def show_version():
    """Print version"""
    print(get_version()[0])
    print(get_version()[2])
    print(get_version()[3])  ## Add


#---------------------------------------------------------------------------
#   Command args
#---------------------------------------------------------------------------
description_message = about.__description_message__
example_usage = f'''
Examples:
- Usage sample 1
{about.__name__} option1 option2

- Usage sample 2
{about.__name__} option3


'''
#---------------------------------------------------------------------------
def check_options(val):
    """Example of custom validation args"""
    if not val.islower():
        raise argparse.ArgumentTypeError(f'{str(val)} must be lowercase')
    return val


def parse_args():
    """Command arg parse"""
    parser = argparse.ArgumentParser(prog=about.__name__,
                                     description=about.__description_message__,
                                     epilog=example_usage,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-i", "--int_val",
                        help="Some int value",
                        type=int,
                        default=-1)

    parser.add_argument("-b", "--bool_val",
                        help="Some boolean value",
                        action='store_true')

    parser.add_argument("-s", "--string_val",
                        help="Some string val with custom validation function",
                        type=check_options)

    parser.add_argument("-c", "--config",
                        help="Application configuration file")

    parser.add_argument("-l", "--log",
                        help="Logging configuration file")

    parser.add_argument("-L", "--log_level",
                        help="Log level. Valid options: I(info), D(debug), W(warning), E(error)",
                        choices=['I','D','W','E'],
                        default='I')

    parser.add_argument("-v", "--version",
                        help="Show script version",
                        action='store_true')

    args = parser.parse_args()
    if args.version:
        show_version()
        sys.exit(0)

    # No arguments received
    if len(sys.argv) == 1:
        print("Ops, missing arguments")
        parser.print_usage()
        #parser.print_help()
        sys.exit(1)
    return args


LOG_LEVELS={'I':logging.INFO,'D':logging.DEBUG,'W':logging.WARNING,'E':logging.ERROR}
def init_log(args):
    if args.log:
        with open(args.log, 'r', encoding="utf-8") as fd:
            logging.config.dictConfig(json.load(fd))
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    # Set root level
    # For specific logger: _log.setLevel(LOG_LEVELS.get(args.log_level,logging.INFO))
    logging.getLogger().setLevel(LOG_LEVELS.get(args.log_level,logging.INFO))


def init_cfg(args):
    global CONFIG
    if args.config:
        with open(args.config, 'r', encoding="utf-8") as fd:
            CONFIG = json.load(fd)
    # Override some option

    if args.int_val: CONFIG['int_val']= args.int_val

#---------------------------------------------------------------------------
#   Main
#---------------------------------------------------------------------------
def main():

    args = parse_args()
    init_log(args)
    init_cfg(args)

    _log.info(get_version()[0])
    _log.info(get_version()[2])
    _log.info(get_version()[3])

    _log.info(f"Starting pid={os.getpid()}")
    _log.info(f"Using args {args}")
    _log.debug(f'Using configuratin file {args.config}: CONFIG={CONFIG}')
    # ---------------------------------------------------------------------------
    #   Application code
    # ---------------------------------------------------------------------------

    _log.info(f"Aplication end, pid={os.getpid()}")

if __name__ == '__main__':
    main()
    sys.exit(0)