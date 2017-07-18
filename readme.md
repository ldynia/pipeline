# Luigi

Links:
* [docs](https://luigi.readthedocs.io/en/latest/index.html)
* [github](https://github.com/spotify/luigi)

```
$ cd /app/luigi

PYTHONPATH='.' luigi --module tasks.run_all RunAllTask --local-scheduler
```

# NextFlow

Links:
* [docs](https://www.nextflow.io/docs/latest/index.html)
* [github](https://github.com/nextflow-io/nextflow)

```
$ cd /app/next_flow
$ nextflow pipeline.nf
```

# Snakemake

Links:
* [docs](https://snakemake.readthedocs.io/en/stable/)
* [bitbucket](https://bitbucket.org/snakemake/snakemake/src)

```
$ cd /app/snakemake
$ snakemake $(snakemake -l)
```

# Slurm

Links:
* [github](https://github.com/acorg/slurm-pipeline)

```
$ cd /app/slurm-pipeline
$ slurm-pipeline.py -s pipeline.json > status.json
```
