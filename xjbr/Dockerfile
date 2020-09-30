FROM jupyter/minimal-notebook

# container is too big ..
# RUN conda update -n base conda 

RUN conda install --quiet -y numpy pandas && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN mkdir /home/jovyan/data && \
    cd /home/jovyan/data && \
    wget https://bit.ly/c1_xenopus_s10 -O s10.zip && \
    unzip s10.zip && \
    wget https://bit.ly/c1_xenopus_s11 -O s11.zip && \
    unzip s11.zip && \
    wget https://bit.ly/c1_xenopus_s12 -O s12.zip && \
    unzip s12.zip && \
    wget https://bit.ly/c1_xenopus_s14 -O s14.zip && \
    unzip s14.zip && \
    wget https://bit.ly/c1_xenopus_s20 -O s20.zip && \
    unzip s20.zip && \
    rm -f *.zip

VOLUME ["/home/$NB_USER/.jupyter"]
