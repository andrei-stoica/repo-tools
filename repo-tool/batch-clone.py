from email.policy import default
import click
from git import Repo, exc
import csv
from os import path
import logging


def parse_csv(filename: str) -> list[dict]:
    with open(filename) as f:
        data = []
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[header[i]] = value
            data.append(row_dict)
        return data


@click.command()
@click.option(
    "--account-list",
    "-f",
    required=True,
    help="csv file containing list of github accounts",
)
@click.option(
    "--account-col",
    default="username",
    show_default=True,
    help="name of column containing account names",
)
@click.option(
    "--project-prefix",
    "-p",
    required=True,
    help="prefix for project names (ie. lab01-)'",
)
@click.option(
    "--source",
    "-s",
    default="https://github.com/CSCI4100U",
    show_default=True,
    help="base url for source",
)
@click.option(
    "--output-dir", "-o", default=".", show_default=True, help="directory for clones"
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    default=False,
)
def batch_clone(account_list, account_col, project_prefix, source, output_dir, verbose):
    print(verbose)
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)
    accounts = [i[account_col] for i in parse_csv(account_list)]
    for account in accounts:
        source_url = f"{source}/{project_prefix}{account}"
        dest = path.join(output_dir, f"{project_prefix}{account}")
        try:
            Repo.clone_from(
                source_url,
                dest,
            )
            logging.info(f"Cloned {source_url} into {dest}")
        except exc.GitCommandError as e:
            logging.info(f"Failed to clone {source_url}")
            logging.debug(e.stderr.strip())


if __name__ == "__main__":
    batch_clone()
