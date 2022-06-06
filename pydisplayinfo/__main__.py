from argparse import ArgumentParser, Namespace

from pydisplayinfo.display_info import DisplayInfo


def create_arg_parser() -> Namespace:
    parser = ArgumentParser(
        description="Get information from the current display",
        allow_abbrev=False,
        argument_default=False,
        add_help=True,
    )
    action = "store_true"

    di = DisplayInfo
    parser.add_argument("--show", action=action, help=di.all.__doc__)
    parser.add_argument("--res", action=action, help=di.resolution.__doc__)
    parser.add_argument("--offset-x", action=action, help=di.offset_x.__doc__)
    parser.add_argument("--offset-y", action=action, help=di.offset_y.__doc__)
    parser.add_argument("--width", action=action, help=di.width.__doc__)
    parser.add_argument("--height", action=action, help=di.height.__doc__)

    return parser


def parse_args() -> Namespace:
    parser = create_arg_parser()
    args: Namespace = parser.parse_args()
    if not any(vars(args).values()):
        args = parser.parse_args(["--help"])
    return args


def main(args: Namespace = None):
    if not args:
        args: Namespace = parse_args()

    display_info = DisplayInfo()

    if args.show:
        raise NotImplementedError
        # print("Display info (values only):\n")
        # print(*all_props, sep="\n", file=sys.stdout)
    elif args.res:
        output = "{}x{}".format(*display_info.resolution)
    else:
        for key, value in vars(args).items():
            if value:
                output = getattr(display_info, key)
    return output


if __name__ == "__main__":
    main()
