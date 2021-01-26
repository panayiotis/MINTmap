# MINTmap

To download the MINTmap tool, please visit
[cm.jefferson.edu/MINTmap](https://cm.jefferson.edu/MINTmap).

MINTmap generates tRF (tRNA fragment) profiles from a trimmed short RNA-Seq
dataset.  
Note: Color-space reads are not supported in this tool.
For information on methods and color-space, please see
[this paper](http://www.nature.com/articles/srep41184).

MINTmap is developed and maintained by the
[Computational Medicine Center](https://cm.jefferson.edu),
Thomas Jefferson University.

To cite MINTmap use: *Loher, P. et al. MINTmap: fast and exhaustive profiling of
nuclear and mitochondrial tRNA fragments from short RNA-seq data.
Sci. Rep. 7, 41184; doi: 10.1038/srep41184 (2017).*

You can contact us at
[cm.jefferson.edu/contact-us](https://cm.jefferson.edu/contact-us)


## License

MINTmap is available under the open source GNU GPL v3.0 license
(https://www.gnu.org/licenses/gpl-3.0.en.html).  
Included MINTplates library uses a different license, for more information see:
https://github.com/TJU-CMC-Org/LicensePlates/blob/master/README_TermsOfUse_MINTplates.txt


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

To use MINTmap, you need to have [python3](https://www.python.org/downloads/)
installed.

Download the latest MINTmap from
[cm.jefferson.edu/MINTmap](https://cm.jefferson.edu/MINTmap)
and then uncompress the contents.

Open a terminal and move to the directory that contains the uncompressed
contents.

To install MINTmap run:

    pip3 install MINTmap-3.0.0-py3-none-any.whl


## Usage

After installing MINTmap, to generate tRF profiles from a fastq file, run:

    MINTmap .../path_to_trimmed_input_file.fastq

### Example Run

To run the tRF profiles of the trimmed fastq file that resides in the directory
`ExampleRun` do the following:

Open a terminal and `cd` to the directory of this README file. eg:

    cd Downloads/MINTmap/

Then, `cd` to the directory of the `ExampleRun` by running:

    cd ExampleRun

To generate the tRF profiles of the trimmed fastq file in the current
directory run:

    MINTmap exampleInput.trimmed.fastq.gz

Finaly, run `ls` to list the output files in the current directory:

    ls


## Output Files

* Plain text and HTML file pairs for exclusive tRFs profiles
(\*.exclusive-tRFs.expression.\*).  
RPM and annotation information included.  
HTML file also links to verbose MINTbase records.
* Plain text and HTML file pairs for non-exclusive tRFs profiles
(\*.ambiguous-tRFs.expression.\*).  
RPM and annotation information included.  
HTML file also links to verbose MINTbase records.
* High level mapping stats are also generated seperately for exclusive and
non-exclusive tRFs (\*.countsmeta.txt)
