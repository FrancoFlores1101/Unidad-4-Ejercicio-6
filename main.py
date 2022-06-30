from claseRepositorioProvincias import RepositorioProvincias
from claseControlador import ControladorProvincias
from claseVistaPrincipal import VistaPrincipal
from claseObjectEncoder import ObjectEncoder


def main():
    conn = ObjectEncoder("provincias.json")
    repo = RepositorioProvincias(conn)
    vista = VistaPrincipal()
    ctrl = ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()