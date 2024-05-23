# mfjet

`mfjet` is a Python package that provides tools for computing Minkowski functionals useful for encoding geometric features of jets appearing in high energy particle colliders.


 * [Neural Network-based Top Tagger with Two-Point Energy Correlations and Geometry of Soft Emissions](https://doi.org/10.1007/JHEP07%282020%29111), <br />
    Amit Chakraborty, Sung Hak Lim, Mihoko M. Nojiri, and Michihisa Takeuchi, <br />
    JHEP 07 (2020) 111, arXiv:2003.11787
 * [Morphology for Jet Classification](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.105.014004), <br />
    Sung Hak Lim, and Mihoko M. Nojiri, <br />
    Phys. Rev. D 105, 014004, arXiv:2010.13469
 * [Jet Classification Using High-Level Features from Anatomy of Top Jets](https://arxiv.org/abs/2312.11760), <br />
    Amon Furuichi, Sung Hak Lim, and Mihoko M. Nojiri, <br />
    arXiv:2312.11760

Installation
------------

### Development version
```
pip install git+https://github.com/sunghak-lim/mfjet.git
```

### Dependency
 * numpy, scipy, shapely

Examples
-------
 * [Example code for computing MFs in Eucildean geometry](examples/Tutorial_MF_Euclidean.ipynb),
 * [Example code for computing MFs in Manhattan geometry](examples/Tutorial_MF_Manhattan.ipynb)
 * [Example code for computing MFs of pixellated image](examples/Tutorial_MF_Pixel.ipynb)

API Documentations
------------------
 * [Module documentations](https://mfjet.readthedocs.io/en/latest/py-modindex.html)

Citing mfjet
------------
Please use this bibtex: (Details to be updated.)
```bibtex
@article{Furuichi:2023vdx,
    author = "Furuichi, Amon and Lim, Sung Hak and Nojiri, Mihoko M.",
    title = "{Jet Classification Using High-Level Features from Anatomy of Top Jets}",
    eprint = "2312.11760",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    month = "12",
    year = "2023"
}
```

References
----------
 * Steiner-type formulas
   * (Euclidean geometry) (https://arxiv.org/abs/1012.5881)
   * (Manhattan geometry) (https://arxiv.org/abs/1207.7276)
