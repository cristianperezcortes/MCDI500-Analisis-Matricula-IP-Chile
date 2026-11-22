"""La figura de contraste puede reconstruirse a partir de los CSV públicos."""
from pathlib import Path
from scripts.generar_figura2_publicacion import crear_figura


def test_figura_de_puntos_f4_desde_clon(tmp_path):
    destino = crear_figura(tmp_path / "figura2.png")
    assert destino.exists()
    assert destino.stat().st_size > 10000
    assert destino.read_bytes()[:8] == bytes.fromhex("89504e470d0a1a0a")
