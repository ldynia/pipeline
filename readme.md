# Luigi

Links:
* [docs](https://luigi.readthedocs.io/en/latest/index.html)
* [github](https://github.com/spotify/luigi)

```
$ cd /app/luigi

PYTHONPATH='' luigi --module tasks.run_all RunAllTask --local-scheduler
```

# NextFlow

Links:
* [docs](https://www.nextflow.io/docs/latest/index.html)
* [github](https://github.com/nextflow-io/nextflow)

```
$ nextflow /app/next_flow/pipeline.nf
```

# Snakemake

Links:
* [docs](https://snakemake.readthedocs.io/en/stable/)
* [bitbucket](https://bitbucket.org/snakemake/snakemake/src)

```
$ cd /app/snakemake
$ snakemake $(snakemake -l)
```
