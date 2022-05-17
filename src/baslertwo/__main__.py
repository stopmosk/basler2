"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """BaslerTwo."""


if __name__ == "__main__":
    main(prog_name="basler2")  # pragma: no cover
