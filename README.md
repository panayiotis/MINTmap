# MINTmap

If you just want to download the latest version for basic usage, please visit
[cm.jefferson.edu/MINTmap](https://cm.jefferson.edu/MINTmap).

MINTmap generates tRF (tRNA fragment) profiles from a trimmed short RNA-Seq dataset.
It is available under the open source GNU GPL v3.0 license.

Note: Color-space reads are not supported in this tool.
For information on methods and color-space, please see
[this paper](http://www.nature.com/articles/srep41184).

MINTmap is developed and maintained by
[Computational Medicine Center](https://cm.jefferson.edu),
Thomas Jefferson University.
You can contact us at:
[cm.jefferson.edu/contact-us](https://cm.jefferson.edu/contact-us)

## Publications

* Loher, P, Telonis, AG, Rigoutsos, I. MINTmap: fast and exhaustive profiling of
nuclear and mitochondrial tRNA fragments from short RNA-seq data.
Sci Rep. 2017;7 :41184.
doi: [10.1038/srep41184](http://dx.doi.org/10.1038/srep41184).
PubMed [PMID:28220888](http://www.ncbi.nlm.nih.gov/pubmed/28220888).
PubMed Central [PMC5318995](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC5318995).

* Pliatsika, V, Loher, P, Telonis, AG, Rigoutsos, I. MINTbase: a framework for
the interactive exploration of mitochondrial and nuclear tRNA fragments.
Bioinformatics. 2016;32 (16):2481-9. doi: 
[10.1093/bioinformatics/btw194](http://dx.doi.org/10.1093/bioinformatics/btw194).
PubMed [PMID:27153631](http://www.ncbi.nlm.nih.gov/pubmed/27153631).
PubMed Central [PMC4978933](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978933).

## Installation

To use MINTmap you need to have python3 installed.
To install MINTmap, run:
```sh
pip3 --user install TODO
```

## Usage

After installing MINTmap, to generate tRF profiles from a fastq file, run:
```sh
MINTmap /.../path_to_trimmed_input_file.fastq
```

### Example

To run the tRF profiles of the trimmed fastq file that resides in the directory
`ExampleRun` do the following:

* open a terminal and `cd` to the directory of this README file.
e.g. `cd Downloads/TODO/`
* then cd to the directory of the `ExampleRun` by running: `cd ExampleRun`
* finally generate the tRF profiles of the trimmed fastq file in the current
directory by running: `MINTmap exampleInput.trimmed.fastq.gz
* run `ls` to list the output files in the current directory

## Program Arguments

```
usage: MINTmap [-h] [-c CUSTOM_RPM] [-m MAPPING_BUNDLE_PATH] [-p PREFIX]
               [--log-level {debug,info,warning}]
               input_file_path

MINTmap generates tRF (tRNA fragment) profiles from a trimmed short RNA-Seq dataset.

positional arguments:
  input_file_path       The input_file_path contains the sequenced reads to be
                        analyzed. Any trimming (e.g. quality and adapter trimming)
                        must be done prior to running this tool. If
                        input_file_path ends in .gz it will be treated as a
                        gzipped FASTQ file. The FASTQ file contains four lines per
                        read (more info here:
                        https://en.wikipedia.org/wiki/FASTQ_format). Color-space
                        reads are not supported. This is a required argument.

optional arguments:
  -h, --help            show this help message and exit
  -c CUSTOM_RPM, --custom-rpm CUSTOM_RPM
                        The value CUSTOM_RPM is meant to be used as alternative
                        denominator when computing the rpm abundance of an isomir.
                        When this parameter is defined by the user, an additional
                        column in the output files will be populated with rpm
                        values that have been calculated using this value in the
                        denominator - i.e. these values will be equal to raw
                        reads/<customrpm>*1,000,000, a common value to use here is
                        the original number of sequenced reads prior to quality
                        and adaptor-trimming.
  -m MAPPING_BUNDLE_PATH, --mapping-bundle MAPPING_BUNDLE_PATH
                        This is the relative or absolute path to the mapping
                        bundle that will be used. If not specified, the default
                        mapping bundle will be used.
  -p PREFIX, --prefix PREFIX
                        Naming prefix for the generated files. If not specified,
                        OUTPUT_PREFIX will be set to "output" and all output files
                        will be generated in the current working directory.
  --log-level {debug,info,warning}
                        Set the logging level. The default is info.
```
