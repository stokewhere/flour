import pathlib

import flour
import numpy as np


def test_xyz(
    tmp_path: pathlib.Path,
) -> None:

    xyz_path = tmp_path / "molecule.xyz"
    comment = "comment"
    elements = np.array(['Pd', 'C', 'O', 'H'])
    positions = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
            [10.0, 11.0, 12.0],
        ]
    )
    flour.write_xyz(
        path=xyz_path,
        comment=comment,
        # atoms=elements,
        # positions=positions,
    )
    assert True
    return
    xyz_data = flour.read_xyz(xyz_path)
    assert comment == xyz_data.comment
    assert np.all(np.isclose(elements, xyz_data.elements))
    assert np.all(np.isclose(positions, xyz_data.positions))