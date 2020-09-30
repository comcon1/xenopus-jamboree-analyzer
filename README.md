# Xenopus Jamboree Analysis

## ABOUT

Here, you'll find the docker container which downloads *Xenopus laevis* single cell RNA-seq data and its clustering information.

## INSTALL

First, build docker image `xjbr`:

    cd xjbr
    docker build -t comcon1/xjbr .

Then run container (don't forget to set PORT and USER before):

    ./container-start.sh

The last command from the script will give you the token. Use it to authorize.

Alternatively, one can use sample `docker-compose.yml.example` for run with `docker-compose`. In this case, you can put jupyter configuration file into the config volume defining enterance password and SSL certificates.

*Note: fix ownership & permissions for `work` folder if you want ipynb files to be writable.*

## USAGE

Open notebook `example-usage.ipynb` and follow the instructions. 

## CITE

You **MUST** cite the following paper:

Briggs, J. A., Weinreb, C., Wagner, D. E., Megason, S., Peshkin, L., Kirschner, M. W., & Klein, A. M. (2018). The dynamics of gene expression in vertebrate embryogenesis at single-cell resolution. *Science*, **360**(6392), eaar5780. doi:[10.1126/science.aar5780](https://doi.org/10.1126/science.aar5780).
 

All the data in the container were obtained from [the public repository of Klein's lab](https://kleintools.hms.harvard.edu/tools/currentDatasetsList_xenopus_v2.html).

