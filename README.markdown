# Installation

This depends on two Python libraries:

```
pip install requests
pip install panoptes-client
```

# Usage

```
./upload_to_caesar.py <path-to-csv-file>
```

The uploader remembers state in between runs, such that it doesn't need to send
subjects whose data hasn't changed since the last run. This state is preserved
in the `last_run.pickle` file. Simply remove it if you run into any problems.
