
#### Structure of Directories & Files
```
databaseUpdater/
├── GenomeDB/                       # Genome data import module (GFF -> DB)
│   ├── GenomeDBDiff.py
│   ├── GenomeDBUpdater.py
│   ├── GenomeDBUtil.py
│   ├── GFFRewriter.py
│   └── hamap_families.dat
├── RecentPicturePruning/           # Make a history of the top 20 images by each user
│   └── RecentPicturePruning.py
├── util/
│   ├── CronJobReport.py
│   └── SubProcess.py
└── databaseUpdaterCronJob.sh       # For automatic update of genome database
```

`databaseUpdater` directory has modules for Import Genome Database, 
Recent viewed images handling module, and Cron job scripts. 
Please note that MaizeDIG uses genome data from MaizeGDB and 
it is not required to use `GenomeDB` module and `Cron` job scripts.
Please see [BioDIG](https://github.com/idoerg/BioDIG) Git Hub page for details. 

