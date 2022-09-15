# Repo Tools

## Usage
`python repo-tool/batch-clone.py`
```
Usage: batch-clone.py [OPTIONS]

Options:
  -f, --account-list TEXT    csv file containing list of github accounts
                             [required]
  --account-col TEXT         name of column containing account names
                             [default: username]
  -p, --project-prefix TEXT  prefix for project names (ie. lab01-)'
                             [required]
  -s, --source TEXT          base url for source  [default:
                             https://github.com/CSCI4100U]
  -o, --output-dir TEXT      directory for clones  [default: .]
  -v, --verbose
  --help                     Show this message and exit.
```
