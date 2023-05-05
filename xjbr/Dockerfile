FROM jupyter/minimal-notebook

# container is too big ..
# RUN conda update -n base conda 

RUN conda install --quiet -y numpy pandas && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN mkdir /home/jovyan/data && \
    cd /home/jovyan/data && \
    wget http://erg.biophys.msu.ru/~comcon1/s10-to-22.zip -O alls.zip && \
    unzip alls.zip && \
    rm -f *.zip

VOLUME ["/home/$NB_USER/.jupyter"]
