# A template repository of creating a REMARK that works with nbreproduce

To create a `nbreproduce` compatible project the project needs a bash file, something like `reproduce.sh`, which contains all the required steps to rebuild(execute) the particular project.

These bash script can contain any number of sequential steps, like running a python script, building latex files.


It's possible to have multiple bash scripts too. A script like `reproduce_min.sh` which rebuilds a subset of the project in case the whole rebuild takes a lot of time.
