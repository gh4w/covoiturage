from setuptools import find_packages, setup

setup(
    name='tuto',
    version='1.0.0',
    # quels répertoires de paquets inclure:
    packages=find_packages(),
    # MANIFEST.in doit détailler où trouver ces données.
    # TODO: lire la doc pour se passer du fichier MANIFEST.in
    # et utiliser un setup.cfg à la place.
    # Permettra au setup de générer soit le tuto, soit l'appli, 
    # suivant le fichier de config.
    include_package_data=True,
    zip_safe=False,
    install_requires=[ 'flask' ]
)


